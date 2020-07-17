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
def landing_page():
    return render_template('main/index.html')

@app.route('/get-your-quote/') #routing to get your quotes form
def get_your_quote():
    return render_template('main/get-quote.html')
    

@app.route('/services/') #route to go to Services
def go_to_services():
    return render_template("main/services.html")

@app.route('/contact/') #route to go to contacts page
def go_to_contacts():
    return render_template("main/contact.html")

@app.route('/aboutus/') #route to go to contacts page
def go_to_about_us():
    return render_template("main/about.html")

@app.route('/our-works/') #route to go to contacts page
def go_to_our_work():
    return render_template("main/works.html")



@app.route('/submit-contact-form/',methods=['POST'])
def submit_contact_form():
    if request.method == 'POST':
        #get data from the form's field
        _name = "{} {}".format(request.form['first_name'], request.form['last_name'])
        _email = request.form['email']
        _phone = request.form['phone']
        _message = request.form['message']
        sender_email = os.environ.get('SENDER')
        company_email = os.environ.get('RECIEPIENT')
        password = os.environ.get('PASSWORD')
        try:
            send_out_mail(sender_email,password,company_email,_name,_email,_phone,_message,version=2)
        except Exception as error:
            print(error);return render_template('main/contact.html',fail="Failed to send message! Please contact us by calling (781)-539-7511")
        return render_template('main/contact.html',success="Successfully sent! We will get back to you soon!")
    elif request.method == 'GET':
        return jsonify({"Error":"GET method not allowed!"})

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
        _name = '{} {}'.format(_firstname,_lastname)
        #email crudentials for smtp
        sender_email = os.environ.get('SENDER')
        company_email = os.environ.get('RECIEPIENT')
        password = os.environ.get('PASSWORD')
        try: #pass the clients crudentials into the func send_out_email()
            send_out_mail(sender_email,password,company_email,_name,_email,_phone,_message,version=1)
            success = 'Successfully Sent!  We will give you a phone call!'
        except Exception as error:
            fail = 'Error sending the message!'
            print(error)
            return render_template('main/get-quote.html',fail=fail)
        return render_template('main/get-quote.html',success=success)
    elif request.method == "GET":
        return jsonify({"Error":"GET method not allowed!"})



def send_out_mail(sender_email,password,company_email,_name,_email,_phone,_message,version):
    sender_email = sender_email
    company_email = company_email
    password = password
    today_date = datetime.today().strftime('%m-%d-%y')
    #check for contact type (either quote or contact) --
    if version == 1:
    #str that contains all of the body
        subject_field = "QUOTE REQUESTED {}".format(today_date)
    else:
        subject_field = "CONTACT FORM {}".format(today_date)
    body = "<tr><td><p>Name:</p></td><td><p>{}</p></td></tr><tr><td><p>Email:</p></td><td><p>{}</p></td></tr><tr><td><p>Phone:</p></td><td><p>{}</p></td></tr><tr><td><p>Message:</p></td><td><p>{}</p></td></tr>".format(_name,_email,_phone,_message)    
    # body = _message
    print(body)
    # Create the plain-text and HTML version of your message
    text = """\
    This is a test email!!
    """
    html = """\
    <table>
    """+body+"""
    </table>"""

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
