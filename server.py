import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def ser():
    # return "<p>Hello, World! wassup</p>"
    return render_template('index.html')


# @app.route("/index.html")
# def index():
#     return render_template('index.html')


# @app.route("/works.html")
# def works():
#     return render_template('works.html')


# @app.route("/work.html")
# def work():
#     return render_template('work.html')


# @app.route("/about.html")
# def about():
#     return render_template('about.html')


# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')


# @app.route("/components.html")
# def components():
#     return render_template('components.html')

def saveData(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        msg = data['message']
        writer_csv = csv.writer(database, delimiter=',', quotechar=':',
                                quoting=csv.QUOTE_MINIMAL)
        writer_csv.writerow([email, subject, msg])


@app.route("/<page_name>")
def page(page_name):
    return render_template(page_name)


@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        saveData(data)
        return redirect('thankyou.html')
    else:
        return 'something went wrong'
