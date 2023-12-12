from flask import Flask, render_template, url_for, request, redirect
import csv

'''Paste this:
 flask --app server run --debug
into the terminal to run the server'''

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def any_page(page_name):
    return render_template(page_name)


def write_to_database(data):
    with open('database.txt', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'email:{email}, subject: {subject}, message: {message}')


def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        print(data)
        return redirect('thankyou.html')
    else:
        return 'Something went wrong'

# @app.route("/favicon.ico")
# def fav():
#     return render_template('icon')
