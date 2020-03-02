from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import pickle
import sqlite3
import os
import numpy as np
import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn import linear_model
from sklearn import preprocessing

app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.permanent_session_lifetime = timedelta(minutes=5)

pickle_in= open("symptoms\pkl_objects\model.pkl", "rb")
model = pickle.load(pickle_in)

names = ("Diabetes", "High Blood Pressures", "Pregnancy")
result = None
db = SQLAlchemy(app)

class symptoms(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    Symptom1 = db.Column(db.String(100))
    Symptom2 = db.Column(db.String(100))
    Symptom3 = db.Column(db.String(100))
    Symptom4 = db.Column(db.String(100))
    Symptom5 = db.Column(db.String(100))
    Symptom6 = db.Column(db.String(100))

    def __init__(self, Symptom1, Symptom2, Symptom3, Symptom4, Symptom5, Symptom6):
        self.Symptom1 = Symptom1
        self.Symptom2 = Symptom2
        self.Symptom3 = Symptom3
        self.Symptom4 = Symptom4
        self.Symptom5 = Symptom5
        self.Symptom6 = Symptom6

def symchecker(UserSymptoms):
    USerSymptoms = UserSymptoms
    checker = model.predict([USerSymptoms])
    names = ("Diabetes", "High Blood Pressure", "Pregnancy")
    predicted = (names[int(checker)])
    
    return predicted

    
   

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template("index.html")
    

@app.route("/view")
def view():
    return render_template("view.html", values = symptoms.query.all()) 


@app.route("/page2", methods=["POST","GET"])
def page2():
    if request.method == "POST":
        session.permanent = True
        Symptom1=None
        Symptom2=None
        Symptom3=None
        Symptom4=None
        Symptom5=None
        Symptom6=None
        Symptom1 = request.form["s1a"]
        Symptom2 = request.form["s2a"]
        Symptom3 = request.form["s3a"]
        Symptom4 = request.form["s4a"]
        Symptom5 = request.form["s5a"]
        Symptom6 = request.form["s6a"]
        session["s1s"]=Symptom1
        session["s2s"]=Symptom2
        session["s3s"]=Symptom3
        session["s4s"]=Symptom4
        session["s5s"]=Symptom5
        session["s6s"]=Symptom6
       
        sym = symptoms(Symptom1, Symptom2, Symptom3, Symptom4, Symptom5, Symptom6)
        db.session.add(sym)
        db.session.commit()

        if "s1s" in session:
            
            return redirect(url_for("checker"))
                 
       
        return render_template("page2.html", content="Testing")
        
           
    else:
        return render_template("page2.html", content="Testing")
        flash("Request Not Completed")
    
   
@app.route("/checker")
def checker():
    
    UserSymptoms=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    Symptom1 = session["s1s"]
    Symptom2 = session["s2s"]
    Symptom3 = session["s3s"]
    Symptom4 = session["s4s"]
    Symptom5 = session["s5s"]
    Symptom6 = session["s6s"]

    
    if Symptom1 == "0_Excessive Thirst":
            UserSymptoms[0]=1
    if Symptom2 == "0_Excessive Thirst":
            UserSymptoms[0]=1
    if Symptom3 == "0_Excessive Thirst":
            UserSymptoms[0]=1
    if Symptom4 == "0_Excessive Thirst":
            UserSymptoms[0]=1
    if Symptom5 == "0_Excessive Thirst":
            UserSymptoms[0]=1
    if Symptom6 == "0_Excessive Thirst":
            UserSymptoms[0]=1
         
    if Symptom1 == "1_Frequent Urination":
            UserSymptoms[1]=1
    if Symptom2 == "1_Frequent Urination":
            UserSymptoms[1]=1
    if Symptom3 == "1_Frequent Urination":
            UserSymptoms[1]=1
    if Symptom4 == "1_Frequent Urination":
            UserSymptoms[1]=1
    if Symptom5 == "1_Frequent Urination":
            UserSymptoms[1]=1
    if Symptom6 == "1_Frequent Urination":
            UserSymptoms[1]=1

    if Symptom1 == "2_Fatigue":
            UserSymptoms[2]=1
    if Symptom2 == "2_Fatigue":
            UserSymptoms[2]=1
    if Symptom3 == "2_Fatigue":
            UserSymptoms[2]=1
    if Symptom4 == "2_Fatigue":
            UserSymptoms[2]=1
    if Symptom5 == "2_Fatigue":
            UserSymptoms[2]=1
    if Symptom6 == "2_Fatigue":
            UserSymptoms[2]=1

    if Symptom1 == "3_Tingling Hands":
            UserSymptoms[3]=1
    if Symptom2 == "3_Tingling Hands":
            UserSymptoms[3]=1
    if Symptom3 == "3_Tingling Hands":
            UserSymptoms[3]=1
    if Symptom4 == "3_Tingling Hands":
            UserSymptoms[3]=1
    if Symptom5 == "3_Tingling Hands":
            UserSymptoms[3]=1
    if Symptom6 == "3_Tingling Hands":
            UserSymptoms[3]=1

    if Symptom1 == "4_Tingling Feet":
            UserSymptoms[4]=1
    if Symptom2 == "4_Tingling Feet":
            UserSymptoms[4]=1
    if Symptom3 == "4_Tingling Feet":
            UserSymptoms[4]=1
    if Symptom4 == "4_Tingling Feet":
            UserSymptoms[4]=1
    if Symptom5 == "4_Tingling Feet":
            UserSymptoms[4]=1
    if Symptom6 == "4_Tingling Feet":
            UserSymptoms[4]=1

    if Symptom1 == "5_Headache":
            UserSymptoms[5]=1
    if Symptom2 == "5_Headache":
            UserSymptoms[5]=1
    if Symptom3 == "5_Headache":
            UserSymptoms[5]=1
    if Symptom4 == "5_Headache":
            UserSymptoms[5]=1
    if Symptom5 == "5_Headache":
            UserSymptoms[5]=1
    if Symptom6 == "5_Headache":
            UserSymptoms[5]=1

    if Symptom1 == "6_Chest Pain":
            UserSymptoms[6]=1
    if Symptom2 == "6_Chest Pain":
            UserSymptoms[6]=1
    if Symptom3 == "6_Chest Pain":
            UserSymptoms[6]=1
    if Symptom4 == "6_Chest Pain":
            UserSymptoms[6]=1
    if Symptom5 == "6_Chest Pain":
            UserSymptoms[6]=1
    if Symptom6 == "6_Chest Pain":
            UserSymptoms[6]=1

    if Symptom1 == "7_Difficulty Breathing":
            UserSymptoms[7]=1
    if Symptom2 == "7_Difficulty Breathing":
            UserSymptoms[7]=1
    if Symptom3 == "7_Difficulty Breathing":
            UserSymptoms[7]=1
    if Symptom4 == "7_Difficulty Breathing":
            UserSymptoms[7]=1
    if Symptom5 == "7_Difficulty Breathing":
            UserSymptoms[7]=1
    if Symptom6 == "7_Difficulty Breathing":
            UserSymptoms[7]=1

    if Symptom1 == "8_Irregular Heartbeat":
            UserSymptoms[8]=1
    if Symptom2 == "8_Irregular Heartbeat":
            UserSymptoms[8]=1
    if Symptom3 == "8_Irregular Heartbeat":
            UserSymptoms[8]=1
    if Symptom4 == "8_Irregular Heartbeat":
            UserSymptoms[8]=1
    if Symptom5 == "8_Irregular Heartbeat":
            UserSymptoms[8]=1
    if Symptom6 == "8_Irregular Heartbeat":
            UserSymptoms[8]=1

    if Symptom1 == "9_Pounding Chest":
            UserSymptoms[9]=1
    if Symptom2 == "9_Pounding Chest":
            UserSymptoms[9]=1
    if Symptom3 == "9_Pounding Chest":
            UserSymptoms[9]=1
    if Symptom4 == "9_Pounding Chest":
            UserSymptoms[9]=1
    if Symptom5 == "9_Pounding Chest":
            UserSymptoms[9]=1
    if Symptom6 == "9_Pounding Chest":
            UserSymptoms[9]=1

    if Symptom1 == "10_Pounding Neck":
            UserSymptoms[10]=1
    if Symptom2 == "10_Pounding Neck":
            UserSymptoms[10]=1
    if Symptom3 == "10_Pounding Neck":
            UserSymptoms[10]=1
    if Symptom4 == "10_Pounding Neck":
            UserSymptoms[10]=1
    if Symptom5 == "10_Pounding Neck":
            UserSymptoms[10]=1
    if Symptom6 == "10_Pounding Neck":
            UserSymptoms[10]=1

    if Symptom1 == "11_Pounding Ears":
            UserSymptoms[11]=1
    if Symptom2 == "11_Pounding Ears":
            UserSymptoms[11]=1
    if Symptom3 == "11_Pounding Ears":
            UserSymptoms[11]=1
    if Symptom4 == "11_Pounding Ears":
            UserSymptoms[11]=1
    if Symptom5 == "11_Pounding Ears":
            UserSymptoms[11]=1
    if Symptom6 == "11_Pounding Ears":
            UserSymptoms[11]=1

    if Symptom1 == "12_Missed Period":
            UserSymptoms[12]=1
    if Symptom2 == "12_Missed Period":
            UserSymptoms[12]=1
    if Symptom3 == "12_Missed Period":
            UserSymptoms[12]=1
    if Symptom4 == "12_Missed Period":
            UserSymptoms[12]=1
    if Symptom5 == "12_Missed Period":
            UserSymptoms[12]=1
    if Symptom6 == "12_Missed Period":
            UserSymptoms[12]=1

    if Symptom1 == "13_Diarrheau":
            UserSymptoms[13]=1
    if Symptom2 == "13_Diarrheau":
            UserSymptoms[13]=1
    if Symptom3 == "13_Diarrheau":
            UserSymptoms[13]=1
    if Symptom4 == "13_Diarrheau":
            UserSymptoms[13]=1
    if Symptom5 == "13_Diarrheau":
            UserSymptoms[13]=1
    if Symptom6 == "13_Diarrheau":
            UserSymptoms[13]=1



    predicted1 = symchecker(UserSymptoms)
    return render_template("checker.html", predicted1 = predicted1, Symptom2=Symptom2, UserSymptoms=UserSymptoms) 
    
  


@app.route("/logout")
def logout():
    session.pop("s1s",None)
    session.pop("s2s",None)
    session.pop("s3s",None)
    session.pop("s4s",None)
    session.pop("s5s",None)
    session.pop("s6s",None)



 
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
