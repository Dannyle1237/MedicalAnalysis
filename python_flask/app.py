from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

#Below runs webapp
if __name__=='__main__':
    app.run(debug=True)