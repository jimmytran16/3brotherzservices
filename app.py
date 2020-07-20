from flask import Flask, render_template, request, redirect, url_for,jsonify
# from dotenv import load_dotenv,find_dotenv
from emailutil.sendemail import send_out_mail
import os


app = Flask(__name__)
# load_dotenv(dotenv_path='.env') # get the path of the .env with conf variables
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


if __name__ == '__main__':
    app.run(debug=True)
