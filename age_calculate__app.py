from flask import Flask,render_template,request,flash,redirect,url_for,session,make_response
from datetime import date
app=Flask(__name__)
@app.route('/')
def home():
    return render_template("Age_calculator.html")
@app.route("/calculate", methods=["POST","GET"])
def calculate():
    if request.method=="POST" :

        din=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        D=request.form.get("date")
        y1=int(D.split("-")[0])
        m1=int(D.split("-")[1])
        d1=int(D.split('-')[2])
        d=date.today()
        d2=d.day
        m2=d.month
        y2=d.year
        if (m2 >= m1):
            year=y2-y1
            if (d2 < d1):
                day=din[m2-1]-d1+d2
                month=m2-m1-1
            else :
                month=m2-m1
                day=d2-d1
        elif (m1 > m2):
            year=y2-y1-1
            if (d2 < d1):
                day=din[m2-1]-d1+d2
                month=12-m1+m2-1
            else :
                month=12-m1+m2
                day=d2-d1
        # flash(year,"Years",month,"Months",day,"Days")
    return render_template("Age_calculator.html",year=year,var1=" Years ",month=month,var2=" Months ",var3=" Days ",day=day)
if __name__ == '__main__':
    app.run(debug=True)
