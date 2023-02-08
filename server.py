from flask import Flask, render_template, send_from_directory, request, redirect, send_file
import csv
import os
from pathlib import Path

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    try:
        return render_template(page_name)
    except:
        return render_template('/404.html')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            store_contacts(data)
            write_to_csv(data)
            return redirect('/thank_you.html')
        except:
            return 'cannot save to database'
    else:
    	return 'something went wrong'
    

@app.route('/download_cv')
def dowloadCv ():
    path =  os.path.join(Path(__file__).resolve().parent.parent, 'portfoo','media', 'Resume-Yury-Lobkov.pdf')
    try:
        return send_file(path, as_attachment=True)
    except:
        return render_template('/404.html')


def store_contacts(data_input):
    with open('database.txt','a') as database:
        database.write(str(data_input)+'\n')

def write_to_csv(data_input):
    with open('database.csv',newline='',mode='a') as database_csv:
        username = data_input['Username']
        mail = data_input['mail']
        comment = data_input['comment']        
        csv_writer = csv.writer(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([username,mail,comment])

