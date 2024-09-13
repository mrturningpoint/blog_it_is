from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<h1>Hey there, welcome!</h1>"

@app.route('/about')
def about():
    return "this is the info page"

if __name__ == "__main__":
    app.run(debug=True)
