from flask import Flask, render_template,url_for
app= Flask(__name__)
posts=[
    {
        'name':'ankit kumar',
        'job':'ceo',
        'salary':'1.8 cr'
    },
    {
        'name':'swastik ',
        'job':'web 3.0 developer',
        'salary':'2 cr'        
    },
    {
        'name':'jeewan',
        'job':'startup owner ',
        'salary':'unlimited'        
    }
      ]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home3.html',posts=posts)


@app.route("/about")
def about():
    return render_template('about3.html',title='herorkp')
@app.route("/test")
def test():
    return "Test page is working!"


if __name__ == '__main__':
    app.run(debug= True,port=5001)