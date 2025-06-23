from flask import Flask,request
import pathlib
import careerbot

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def get_interests():
    if request.method=="POST":
        name=request.form.getlist("name")[0]
        interests=request.form.getlist("interests")[0]
        print(name,interests)
        print(careerbot.output(name,interests))
    dir=str(pathlib.Path(__file__).parent.resolve())+"/static/"
    return open(dir+"index.html").read(),200