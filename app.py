from flask import Flask, redirect, render_template, request
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/upload', methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        # Submit file to database
        redirect('/')
    else:
        return render_template('upload.html')