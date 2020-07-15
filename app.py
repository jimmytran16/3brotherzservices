from flask import Flask, render_template, request, redirect, url_for,jsonify
from dotenv import load_dotenv,find_dotenv
import smtplib, ssl, csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from datetime import datetime, timedelta
import os


app = Flask(__name__)
load_dotenv(dotenv_path='.env') # get the path of the .env with conf variables
#Secure connection redirection
# @app.before_request
# def before_request():
#     if not request.is_secure and app.env != "development":
#         url = request.url.replace("http://", "https://", 1)
#         code = 301
#         return redirect(url, code=code)

@app.route('/') 
def landing():
    return render_template('main/index.html')

@app.route('/get-your-quote/') #routing to get your quotes form 
def get_your_quote():
    return render_template('main/get-quote.html')

@app.route('/submit-quote/',methods=['POST']) #get the data from the form and send out the email
def submit_your_quote():
    if request.method == "POST":
        #data from the form
        print(request.form)
        _firstname = request.form['first_name']
        _lastname = request.form['last_name']
        _email = request.form['email']
        _phone = request.form['phone']
        _message = request.form['message_info']
        #concat name
        _name = '{} , {}'.format(_firstname,_lastname)
        #email crudentials for smtp
        sender_email = os.environ.get('SENDER')
        company_email = os.environ.get('RECIEPIENT')
        password = os.environ.get('PASSWORD')  
        try: #pass the clients crudentials into the func send_out_email()          
            send_out_mail(sender_email,password,company_email,_name,_email,_phone,_message)
            success = 'Successfully Sent!  We will give you a phone call!'
        except Exception as error:
            fail = 'Error sending the message!'
            print(error)
            return render_template('main/get-quote.html',fail=fail)
        return render_template('main/get-quote.html',success=success)
    elif request.method == "GET":
        return jsonify({"Error":"GET method not allowed!"})



def send_out_mail(sender_email,password,company_email,_name,_email,_phone,_message):
    sender_email = sender_email
    company_email = company_email
    password = password
    today_date = (datetime.today() - timedelta(days=1)).strftime('%m-%d-%y')
    subject_field = "QUOTE request {}".format(today_date)
    #str that contains all of the body
    body = "<br>{}<br>{}<br>{}<br>{}<br>".format(_name,_email,_phone,_message)
    # body = _message
    print(body)
    # Create the plain-text and HTML version of your message
    text = """\
    This is a test email!!
    """
    html = """\
    Hello, we have request for quote:
    """+body+"""
    """

    print(html)

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    print(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        try:
            message = MIMEMultipart("alternative")
            message["Subject"] = subject_field
            message["From"] = sender_email
            message["To"] = company_email

            # Add HTML/plain-text parts to MIMEMultipart message
            # The email client will try to render the last part first
            message.attach(part1)
            message.attach(part2)
            server.sendmail( #send the email
                sender_email, company_email, message.as_string()
            )
            # print(f'Success send email to {company_email}')
        except Exception as error:
            print(error)
            # print(f'Fail to send email to {company_email}')

if __name__ == '__main__':
    app.run(debug=True)