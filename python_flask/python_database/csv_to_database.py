import sqlite3
import csv
import os



#Create Table for database
data_conn = sqlite3.connect('Diseases.db')
c = data_conn.cursor()
c.execute(''' CREATE TABLE Disease( 
                Disease varchar(50),
                PRIMARY KEY(Disease)
                ); ''')
c.execute(''' CREATE TABLE Symptom( 
                Symptom varchar(50),
                PRIMARY KEY(Symptom)
                ); ''')
c.execute(''' CREATE TABLE Combination( 
                Disease varchar(50),
                Symptoms varchar(850),
                ID int,
                PRIMARY KEY(ID)
                ); ''')

#We need to clean the data from the dataset
#I am doing this by simply combining all of the symptoms in a row
#into one string and storing it
#I am also putting them strings in alphabetical order
file = open('./data/dataset.csv', 'r')
data = csv.reader(file, delimiter=',')
next(data)

diseases = []
symptoms = []
#enumerate allows us to add an index for the current row we're on
for idx, row in enumerate(data):
    #Data cleaning
    #Some Symptom cells have an extra space in word
    #All Symptom cells should be lowercased
    for i in range(1,17):
        value = row[i]
        clean_value = value.replace(' ', '')
        clean_value = clean_value.lower()
        row[i] = clean_value
    
    #Now we can store the values into variables
    row_symptoms = []
    disease = row[0]
    if disease not in diseases:
        diseases.append(disease)
        c.execute("INSERT INTO Disease VALUES(?)", (disease,))
    for i in range(1,17):
        #If symptom value isnt empty then store it
        if(row[i]):
            row_symptoms.append(row[i])
            if(row[i] not in symptoms):
                symptoms.append(row[i])
                c.execute("INSERT INTO Symptom VALUES(?)", (row[i],))
    
    #Also sort these symptoms into abc order
    row_symptoms = sorted(row_symptoms)
    symptoms_string = ' '.join(row_symptoms)
    c.execute("INSERT INTO Combination VALUES(?, ?, ?)", (row[0], symptoms_string, idx))
data_conn.commit()
data_conn.close()

