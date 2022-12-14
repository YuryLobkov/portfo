from flask import Flask, render_template, send_from_directory, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

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

