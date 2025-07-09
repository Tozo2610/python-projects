from flask import Flask,request,redirect
import pathlib
import careerbot
import functions

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def get_interests():
    dir=str(pathlib.Path(__file__).parent.resolve())+"/static/"
    if request.method=="POST":
        name=request.form.getlist("name")[0]
        interests=request.form.getlist("interests")[0]
        print(name,interests)
        print(careerbot.output(name,interests))
        return redirect("/results")
    else:
        return open(dir+"index.html").read(),200
    
@app.route("/results")
def show():
    dir=str(pathlib.Path(__file__).parent.resolve())+"/static/"
    functions.display_careers("<h1 class=\"theme_change\">Hello, world!</h1>")
    return open(dir+"results.html").read(),200