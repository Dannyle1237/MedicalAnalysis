from flask import Flask, render_template
#this is the file to handle backend stuff of the webpage
from python_database import database_func as dbf

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
@app.route("/home")
def home():
    #Store column Disease in DB to variable
    diseases = dbf.storeQueryToVar('''SELECT * FROM Disease''')
    #Because everything in a database is stored as a tuple(array), you can 
    #grab the first value of each item
    for idx, item in enumerate(diseases):
        diseases[idx] = item[0]
    print(diseases)


    return render_template("home.html", diseaseList = diseases)

#Below runs webapp
if __name__=='__main__':
    app.run(debug=True)