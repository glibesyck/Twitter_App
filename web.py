from flask import Flask, render_template, request
from data import get_information, geocoding, generating_map

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/gen_map", methods=["POST"])
def gen_map():
    username = request.form.get('username')
    if not username:
        return render_template('failure.html')
    generating_map(geocoding(get_information(username)))
    return render_template('friends.html')

if __name__=='__main__':
    app.run(debug=False)