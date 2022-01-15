from flask import Flask
from flask import render_template,request
from helperFunctions import isURLValid, hashURL

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('form.html')

@app.route('/shortenURL', methods=['POST'])
def shortenURL():
    url = request.form['url']
    if(not isURLValid(url)):
        return 'URL is invalid'
    else:
        #strip trailing slashes from URL
        url = url.rstrip('/')
        hashedURL = "https://short.en/" + hashURL(url)
        return hashedURL
