# from flask import Flask, render_template
# #this is the file to handle backend stuff of the webpage
# from python_database import database_func as dbf

# app = Flask(__name__)
# app.config['TEMPLATES_AUTO_RELOAD'] = True

# @app.route("/")
# @app.route("/home")
# def home():
#     #Store column Disease in DB to variable
#     diseases = dbf.storeQueryToVar('''SELECT * FROM Disease''')
#     #Because everything in a database is stored as a tuple(array), you can 
#     #grab the first value of each item
#     for idx, item in enumerate(diseases):
#         diseases[idx] = item[0]
#     print(diseases)


#     return render_template("home.html", diseaseList = diseases)



from flask import Flask, render_template
#this is the file to handle backend stuff of the webpage
from python_database import database_func as dbf

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
@app.route("/home")
def home():
    #Store column Disease in DB to variable
    symptoms = dbf.storeQueryToVar('''SELECT * FROM Symptom''')
    combinations = dbf.storeQueryToVar('''SELECT * FROM Combination''')
    arr = ["dischromic_patches", "itching"]
    confirmed_diseases = []
    for i in range (len(combinations)):     #pulls row
        count = 0
        for symptom in arr:                 #pulls symptom list
            if symptom in combinations[i][1]: #checks for symptoms in combinations[rows][column]\
                count += 1
        if count == (len(arr)):
            print(combinations[i])
            if combinations[i][0] not in confirmed_diseases:
                confirmed_diseases.append(combinations[i][0]) 
                    
    print("Confirmed diseases " + str(confirmed_diseases))




    #Because everything in a database is stored as a tuple(array), you can 
    #grab the first value of each item
    for idx, item in enumerate(symptoms):
        symptoms[idx] = item[0]
    #print(symptoms)

    print("Symptoms:" + str(symptoms))
    return render_template("home.html", symptomList = symptoms, confirmed_diseases = confirmed_diseases)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
    

#Below runs webapp
if __name__=='__main__':
    app.run(debug=True)


#Below runs webapp
if __name__=='__main__':
    app.run(debug=True)