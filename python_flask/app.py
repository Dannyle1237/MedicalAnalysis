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
    if arr[0] in combinations[0][1]: #if "dischromic_patches" in dischromic_patches itching nodal_skin_eruptions skin_rash
        if arr[1] in combinations[0][1]:
            print("Is found")
    print(combinations[0])
    #Because everything in a database is stored as a tuple(array), you can 
    #grab the first value of each item
    for idx, item in enumerate(symptoms):
        symptoms[idx] = item[0]
    #print(symptoms)


    return render_template("home.html", symptomList = symptoms)

#Below runs webapp
if __name__=='__main__':
    app.run(debug=True)