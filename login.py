from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///login.db"
db = SQLAlchemy(app)

#class for making profile object
class profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    

@app.route("/")
def login():
    return render_template("login.html")


##creating DB and running app
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)