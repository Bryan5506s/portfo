from flask import Flask, render_template, url_for, request
import csv
app = Flask(__name__)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email= data['email']
        message = data['message']
        name= data['name']
        file= database.write(f'\n{email},{message},{name}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        email= data['email']
        message = data['message']
        name= data['name']
        csv_writer= csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
        if(request.method=='POST'):
            data = request.form.to_dict()
            write_to_csv(data)
            return render_template('index.html')
        else:
            return 'Something went wrong...'