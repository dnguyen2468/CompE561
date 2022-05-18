from distutils import debug
from email.message import EmailMessage

from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)

########################################################################
#Working database code

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'our_db'

mysql = MySQL(app)

@app.route('/form')
def Form():
    return render_template('Form.html')

#cursor = mysql.connection.cursor()

@app.route('/test', methods = ['POST', 'GET'])
def test():
    if request.method == 'GET':
        return "Login via the login Form"

    if request.method == 'POST':
        UserID = request.form['UserID']
        AddressID = request.form['AddressID']
        Email = request.form['Email']
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        PW = request.form['PW']
        Phone = request.form['Phone']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO userindex VALUES(%s,%s,%s,%s,%s,%s,%s)''',(UserID,AddressID,Email,FirstName,LastName,PW,Phone))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"

########################################################################
#Connector
#Mysql-connector-python


#Generic Home Page
@app.route('/')
def Home():
    return render_template("starterHome.html")

@app.route('/Home.html')
def Home2():
    return render_template("Home.html")

#About Page
@app.route('/contact.html')
def AboutUs():
    return render_template('AboutUs.html')

#Profile Page
@app.route('/Profile.html')
def ProfilePage():
    return render_template('ProfilePage.html')

#Cart Page
@app.route('/Cart.html')
def Cart():
    return render_template('Cart.html')

#Payment Page
@app.route('/payment.html')
def Payment():
    return render_template('payment.html')
@app.route('/paymentDB', methods = ['POST', 'GET'])
def PaymentDB():
    if request.method == 'POST':
        Fullname = request.form['fullname']
        Email = request.form['email']
        Street = request.form['street']
        City = request.form['city']
        State = request.form['state']
        Zipcode = request.form['zipcode']
        Cardname = request.form['cardname']
        Cardnum = request.form['cardnumber']
        Expdate = request.form['expdate']
        CVV = request.form['cvv']
        cursor = mysql.connection.cursor()
        OrderID = cursor.execute('''SELECT OrderID FROM userorder''')
        UserID = cursor.execute('''SELECT UserID FROM userindex''')
        AddressID = cursor.execute('''SELECT AddressID FROM address''')
        cursor.execute(''' INSERT INTO billing VALUES('',%s,%s,%s,%s,%s,%s,%s)''',(OrderID,UserID,AddressID,Cardname,Cardnum,Expdate,CVV))
        mysql.connection.commit()
        cursor.close()
        return render_template('Home.html')

#Index Page
@app.route('/index')
def Index():
    return render_template('Index.html')

@app.route('/Signup.html')
def SignUp():
    return render_template('signup.html')

@app.route('/signupDB', methods = ['POST', 'GET'])
def signupDB():
     if request.method == 'GET':
        return "Sign up via the sign up form"
     if request.method == 'POST':     		
        FirstName = request.form['fname']
        LastName = request.form['lname']
        Email = request.form['email']
        PW = request.form['pass']
        #CPW = request.form['compass'] 
        #if PW != CPW:
            #return "Password not match"
        Street = request.form['street']
        City = request.form['city']
        State = request.form['state']
        Country = request.form['country']
        Zipcode = request.form['zipcode']
        Phone = request.form['telephone']    
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO address VALUES('',%s,%s,%s,%s,%s)''',(Street,City,State,Country,Zipcode))
        AddressID = cursor.execute('''SELECT AddressID FROM address''')
        cursor.execute(''' INSERT INTO userindex VALUES('',%s,%s,%s,%s,%s,%s)''',(AddressID,Email,FirstName,LastName,PW,Phone))
        mysql.connection.commit()
        cursor.close()
        return render_template("Home.html")

@app.route('/Signin.html')
def SignIn():
    return render_template('signin.html')
@app.route('/signinDB',  methods = ['POST', 'GET'])
def signinDB():
    if request.method == 'GET':
        return "Sign In"
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['psw']
        cursor = mysql.connection.cursor()
        cursor.execute('''SELECT * FROM userindex WHERE Email = %s''',(username,))
        pwCheck = cursor.fetchone()
        if pwCheck:
            return render_template ('/Home.html')
        else:
            return render_template ('/Home.html')

@app.route('/address.html')
def address():
    return render_template('address.html')

@app.route('/unamepass')
def UnamePass():
    return render_template('UnamePass.html')

########################################################################
#Front Page button routes

@app.route('/P.html')
def P():
    return render_template('P.html')

@app.route('/P1.html')
def P1():
    return render_template("P1.html")

@app.route('/P2.html')
def P2():
    return render_template("P2.html")

@app.route('/P3.html')
def P3():
    return render_template("P3.html")

@app.route('/P4.html')
def P4():
    return render_template("P4.html")

@app.route('/P5.html')
def P5():
    return render_template("P5.html")

@app.route('/P6.html')
def P6():
    return render_template("P6.html")

@app.route('/P7.html')
def P7():
    return render_template("P7.html")

@app.route('/P8.html')
def P8():
    return render_template("P8.html")

@app.route('/P9.html')
def P9():
    return render_template("P9.html")

@app.route('/P10.html')
def P10():
    return render_template("P10.html")

@app.route('/C.html')
def C():
    return render_template("C.html")

@app.route('/C1.html')
def C1():
    return render_template("C1.html")

@app.route('/C2.html')
def C2():
    return render_template("C2.html")

@app.route('/C3.html')
def C3():
    return render_template("C3.html")

@app.route('/C4.html')
def C4():
    return render_template("C4.html")

@app.route('/C5.html')
def C5():
    return render_template("C5.html")

@app.route('/C6.html')
def C6():
    return render_template("C6.html")

@app.route('/C7.html')
def C7():
    return render_template("C7.html")

@app.route('/C8.html')
def C8():
    return render_template("C8.html")

@app.route('/C9.html')
def C9():
    return render_template("C9.html")

@app.route('/C10.html')
def C10():
    return render_template("C10.html")

@app.route('/L.html')
def L():
    return render_template("L.html")

@app.route('/L1.html')
def L1():
    return render_template("L1.html")

@app.route('/L2.html')
def L2():
    return render_template("L2.html")

@app.route('/L3.html')
def L3():
    return render_template("L3.html")

@app.route('/L4.html')
def L4():
    return render_template("L4.html")

@app.route('/L5.html')
def L5():
    return render_template("L5.html")

@app.route('/L6.html')
def L6():
    return render_template("L6.html")

@app.route('/L7.html')
def L7():
    return render_template("L7.html")

@app.route('/L8.html')
def L8():
    return render_template("L8.html")

@app.route('/L9.html')
def L9():
    return render_template("L9.html")

@app.route('/L10.html')
def L10():
    return render_template("L10.html")

@app.route('/WC.html')
def WC():
    return render_template("WC.html")

@app.route('/WC1.html')
def WC1():
    return render_template("WC1.html")

@app.route('/WC2.html')
def WC2():
    return render_template("WC2.html")

@app.route('/WC3.html')
def WC3():
    return render_template("WC3.html")

@app.route('/WC4.html')
def WC4():
    return render_template("WC4.html")

@app.route('/WC5.html')
def WC5():
    return render_template("WC5.html")

@app.route('/WC6.html')
def WC6():
    return render_template("WC6.html")

@app.route('/WC7.html')
def WC7():
    return render_template("WC7.html")

@app.route('/WC8.html')
def WC8():
    return render_template("WC8.html")

@app.route('/WC9.html')
def WC9():
    return render_template("WC9.html")

@app.route('/WC10.html')
def WC10():
    return render_template("WC10.html")

@app.route('/MW.html')
def MW():
    return render_template("MW.html")

@app.route('/MW1.html')
def MW1():
    return render_template("MW1.html")

@app.route('/MW2.html')
def MW2():
    return render_template("MW2.html")

@app.route('/MW3.html')
def MW3():
    return render_template("MW3.html")

@app.route('/MW4.html')
def MW4():
    return render_template("MW4.html")

@app.route('/MW5.html')
def MW5():
    return render_template("MW5.html")

@app.route('/MW6.html')
def MW6():
    return render_template("MW6.html")

@app.route('/MW7.html')
def MW7():
    return render_template("MW7.html")

@app.route('/MW8.html')
def MW8():
    return render_template("MW8.html")

@app.route('/MW9.html')
def MW9():
    return render_template("MW9.html")

@app.route('/MW10.html')
def MW10():
    return render_template("MW10.html")

@app.route('/GB.html')
def GB():
    return render_template("GB.html")

@app.route('/GB1.html')
def GB1():
    return render_template("GB1.html")

@app.route('/GB2.html')
def GB2():
    return render_template("GB2.html")

@app.route('/GB3.html')
def GB3():
    return render_template("GB3.html")

@app.route('/GB4.html')
def GB4():
    return render_template("GB4.html")

@app.route('/GB5.html')
def GB5():
    return render_template("GB5.html")

@app.route('/GB6.html')
def GB6():
    return render_template("GB6.html")

@app.route('/GB7.html')
def GB7():
    return render_template("GB7.html")

@app.route('/GB8.html')
def GB8():
    return render_template("GB8.html")

@app.route('/GB9.html')
def GB9():
    return render_template("GB9.html")

@app.route('/GB10.html')
def GB10():
    return render_template("GB10.html")

########################################################################

@app.route('/debug')
def Debug():
    return render_template('debug.html')    

#turns on debug mode, allows for refreshing page for updates
if __name__ == "__main__":
    app.run(debug=True)

#app.run(host='localhost', port=5000)

#Trying to install Flask Excel
