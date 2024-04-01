from flask import Flask, request, render_template
import pyshorteners

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    if 'long_url' in request.args:
        url = request.args['long_url']
        shorter = pyshorteners.Shortener()
        short_url = shorter.tinyurl.short(url)
        return short_url
    app=Flask(__name__,template_folder='templates')
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)