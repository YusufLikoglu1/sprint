from datetime import datetime
from flask import Flask, render_template, redirect, request
from . import app
import smtplib
from email.mime.text import MIMEText
import random


@app.route("/")
def home():
    return render_template("login.html")

@app.route('/send_mail', methods=['POST','GET'])
def send_mail():
    
    subject = "Email Verification"
    global body
    body = str(random.randint(1,1000))
    sender = "demoatschool@gmail.com"
    recipients = ["sanic2fst@gmail.com"]
    password = "gafjnrjzlszvgseq"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()
    print(request.form["userid"])
    #return "Hello"
    
    return render_template("success.html")

@app.route("/about", methods=['POST','GET'])
def about():

    if request.form["Number"] == body:
        return render_template("quote.html")
    else:
        return "wrong code"    
   #return render_template("dsuccess.html")

#@app.route("/contact/")
#def contact():
#    return render_template("contact.html")

#@app.route("/hello/")
#@app.route("/hello/<name>")
#def hello_there(name = None):
#    return render_template(
#        "hello_there.html",
#        name=name,
#        date=datetime.now()
#    )

#@app.route("/api/data")
#def get_data():
#    return app.send_static_file("data.json")

