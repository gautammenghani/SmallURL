from flask import Flask
from flask import render_template,request
from helperFunctions import isURLValid, hashURL

app = Flask(__name__)

urls = dict()

@app.route('/')
def hello_world():
    return render_template('form.html')

@app.route('/shortenURL', methods=['POST'])
def shortenURL():
    global urls
    url = request.form['url']
    if(not isURLValid(url)):
        return 'URL is invalid'
    else:
        #strip trailing slashes from URL
        url = url.rstrip('/')

        #check if url is already hashed
        if url in urls:
            return urls[url]
        else:
            hashedURL = "https://short.en/" + hashURL(url)
            urls[url] = hashedURL
            return hashedURL
