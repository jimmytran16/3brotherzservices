from main import app
from flask import render_template, request, redirect, url_for,jsonify
from dotenv import load_dotenv,find_dotenv
from main.emailutil.sendemail import send_out_mail
import os

load_dotenv(load_dotenv()) # get the path of the .env with conf variables
#Secure connection redirection
# @app.before_request
# def before_request():
#     if not request.is_secure and app.env != "development":
#         url = request.url.replace("http://", "https://", 1)
#         code = 301
#         return redirect(url, code=code)

@app.route('/')
@app.route('/home/')
def landing_page():
    return render_template('main/index.html')

@app.route('/get-your-quote/') #routing to get your quotes form
def get_your_quote():
    return render_template('main/contact.html',quote=True)

@app.route('/services/') #route to go to Services
def go_to_services():
    return render_template("main/services.html")

@app.route('/contact/') #route to go to contacts page
def go_to_contacts():
    return render_template("main/contact.html",success=request.args.get('success'),fail=request.args.get('fail'))

@app.route('/aboutus/') #route to go to contacts page
def go_to_about_us():
    return render_template("main/about.html")

@app.route('/more-work/') #route to go to contacts page
def go_to_more_works():
    return render_template("main/moreworks.html")

@app.route('/our-works/') #route to go to contacts page
def go_to_our_work():
    return render_template("main/works.html")

@app.route('/submit-contact-form/',methods=['POST']) #submit contact's form handler
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
        print('LOG {} {} {} '.format(sender_email,company_email,password))
        try:
            send_out_mail(sender_email,password,company_email,_name,_email,_phone,_message,version=2)
        except Exception as error:
            print(error);return redirect(url_for('go_to_contacts',fail='Failed to send message! Please contact us by calling (781)-539-7511'))
        # return render_template('main/contact.html',success="Successfully sent! We will get back to you soon!")
        return redirect(url_for('go_to_contacts',success='Successfully sent! We will get back to you soon!'))
    elif request.method == 'GET':
        return jsonify({"Error":"GET method not allowed!"})

@app.route('/submit-quote/',methods=['POST']) #submit quote's handler
def submit_your_quote():#get the data from the form and send out the email
    if request.method == "POST":
        #data from the form
        print(request.form)
        _firstname = request.form['first_name']
        _lastname = request.form['last_name']
        _email = request.form['email']
        _phone = request.form['phone']
        _message = request.form['message']
        _location = request.form['city_state']
        #concat name
        _name = '{} {}'.format(_firstname,_lastname)
        #email crudentials for smtp
        sender_email = os.environ.get('SENDER')
        company_email = os.environ.get('RECIEPIENT')
        password = os.environ.get('PASSWORD')
        try: #pass the clients crudentials into the func send_out_email()
            send_out_mail(sender_email,password,company_email,_name,_email,_phone,_message,version=1,_location=_location)
            success = 'Successfully Sent!  We will give you a phone call!'
        except Exception as error:
            fail = 'Error sending the message!'
            print(error)
            return redirect(url_for('go_to_contacts',fail='Failed to submit! Please contact us by calling (781)-539-7511'))
        return redirect(url_for('go_to_contacts',success='Successfully sent! We will get back to you soon!'))
    elif request.method == "GET":
        return jsonify({"Error":"GET method not allowed!"})
