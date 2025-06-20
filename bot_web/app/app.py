from flask import Flask,request
import pathlib

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def get_interests():
    if request.method=="POST":
        print(request.form.to_dict())
    dir=str(pathlib.Path(__file__).parent.resolve())+"/static/"
    return open(dir+"index.html").read(),200