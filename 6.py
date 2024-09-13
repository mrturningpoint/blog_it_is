from flask import Flask, render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
app= Flask(__name__)
app.config['SECRET_KEY']='a3dcb4d229de6fde0bce87ee8b0d2e96'
posts=[
    {
        'name':'ankit kumar',
        'job':'ceo',
        'salary':'1.8 lpa'
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
    return render_template('home4.html',posts=posts)


@app.route("/about")
def about():
    return render_template('about3.html',title='herorkp')
@app.route("/test")
def test():
    return "Test page is working!"
@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'account created for{form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='register',form=form)
 
@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'ab@gmail.com' and form.password.data == 'password':
            flash('you have been logged in','success')
            return redirect(url_for('home'))
        else:
            flash('login failed','danger')
    return render_template('login.html',title='login',form=form)
 
if __name__ == '__main__':
    app.run(debug= True,port=5001)