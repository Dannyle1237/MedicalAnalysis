from flask import Flask, request, render_template, request, jsonify
import json
#this is the file to handle backend stuff of the webpage
from python_database import database_func as dbf

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True



def algorithm(arr):
    #Only run algorithm if array is not empty
    if(len(user_arr) != 0):
        #reset diseases array
        confirmed_diseases = []
        #pulls row
        for i in range (len(combinations)):     
            count = 0
            #pulls symptom list
            for symptom in user_arr:            
                #checks for symptoms in combinations[rows][column]     
                if symptom in combinations[i][1]: 
                    count += 1
            if count == (len(user_arr)):
                #print(combinations[i])
                if combinations[i][0] not in confirmed_diseases:
                    confirmed_diseases.append(combinations[i][0])       
        #print("Confirmed diseases " + str(confirmed_diseases))
    else:
        confirmed_diseases = []
    return confirmed_diseases

#Global variables
#All available symptoms and diseases in database
symptoms = dbf.storeQueryToVar('''SELECT * FROM Symptom''')
diseases = dbf.storeQueryToVar('''SELECT * FROM Disease''')
#Because everything in a database is stored as a tuple(array), you can 
#grab the first value of each item
for idx, item in enumerate(symptoms):
    symptoms[idx] = item[0]
#clean the symptoms list for dropdown menu so its better for user to read
dropdown_symptoms = []
for symptom in symptoms:
    cleaned_s = formatToRead(symptom)
    dropdown_symptoms.append(cleaned_s)
#print(dropdown_symptoms)

#Combinations of all possible diseases and symptoms (Disease, list of symptoms separated by space as one string)
combinations = dbf.storeQueryToVar('''SELECT * FROM Combination''')
#Array to store diseases received from algorithm
confirmed_diseases= []
#Array of user inputted symptoms
user_arr = []
#Readable user arr
read_arr = []



@app.route("/")
def home():
    global symptoms, confirmed_diseases, user_arr, combinations, dropdown_symptoms, read_arr
    #When page reloads reset the array and confirmed diseases
    confirmed_diseases = []
    user_arr = []
    read_arr = []

    return render_template("home.html", symptomList = dropdown_symptoms, confirmedDiseases = confirmed_diseases, userList = read_arr)

@app.route('/', methods=['POST'])
@app.route('/list', methods=['POST'])
def my_form_post():
    global symptoms, confirmed_diseases, user_arr, combinations, dropdown_symptoms, read_arr

    user_input = request.form['symptom_input']
    #Clean user input to match data format
    user_input = user_input.replace(' ', '_')
    user_input = user_input.lower()

    #Check for valid input
    if(user_input not in user_arr and user_input in symptoms):
        read_arr.append(formatToRead(user_input))
        user_arr.append(user_input)
        print(f"Symptom({user_input}) user inputted into array")
    else:
        print(f"Symptom({user_input}) not inputted cause it is invalid")
    
    confirmed_diseases = algorithm(user_arr)

    return render_template("home.html", symptomList = dropdown_symptoms, confirmedDiseases = confirmed_diseases, userList = read_arr)

@app.route('/delete-symptom', methods=['POST'])
def delete_note():
    global user_arr, read_arr, confirmed_diseases
    id = json.loads(request.data)
    read_arr.pop(int(id['idx']))
    user_arr.pop(int(id['idx']))
    confirmed_diseases = algorithm(user_arr)

    return jsonify({})

@app.route('/list')
def list():
    global symptoms, confirmed_diseases, user_arr, combinations, dropdown_symptoms, read_arr
    return render_template("home.html", symptomList = dropdown_symptoms, confirmedDiseases = confirmed_diseases, userList = read_arr)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

#Below runs webapp
if __name__=='__main__':
    app.run(debug=True)