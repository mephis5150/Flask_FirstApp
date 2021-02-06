from flask import Flask, render_template
from backend import create, read, database

app = Flask(__name__)
app.secret_key = "&#73;[HEX.20]&#83;AS.99AS.114B.01100101B.01100001AS.109"

#Login form
@app.route("/login")
def login():
    return render_template('Signin.html')

#Signup form
@app.route("/signup")
def signup():
    return render_template('Signup.html')

#Check connect to database already
@app.route("/connectdb")
def conndb():
    return str(database.connection())

#call method insert data to MySQL
@app.route("/create", methods=['GET', 'POST'])
def create_data():
    return create.create()

#call method query data from MySQL
@app.route("/read", methods=['GET', 'POST'])
def read_data():
    return read.read()

if __name__ == "__main__":
    app.run(debug=True)