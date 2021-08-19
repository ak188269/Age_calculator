# from logging import debug
from flask import Flask,render_template,flash,url_for,request
from flask.globals import request
app=Flask(__name__)
@app.route("/",methods=['[POST','GET'])
def age():
    return render_template("index.html")
@app.route("/age",methods=['POST','GET'])
def fun():
    if request.method=='POST':
        date=request.form.get("date")
        y1=date.split("-")[0]
        m1=date.split("-")[1]
        d1=date.split('-')[2]
        
        return render_template("index.html",date=date)
if __name__=="__main__":
    app.run(debug=True)