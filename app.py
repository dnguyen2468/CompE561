from distutils import debug
#import pandas as pd
#request is for excel Flask 
#render template for HTML files
from flask import Flask, render_template #, request
from flaskext.mysql import MySQL
app = Flask(__name__)

#yes you do need code in python to run this database
#PHPmyAdmin may use different code
mysql = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

#Connector
#Mysql-connector-python

#Generic Home Page
@app.route('/')
def Home():
    return "This is home!"

#About Page
@app.route('/about')
def AboutUs():
    return render_template('AboutUs.html')

#Profile Page
@app.route('/profile')
def ProfilePage():
    return render_template('ProfilePage.html')

#Cart Page
@app.route('/cart')
def Cart():
    return render_template('Cart.html')

#Payment Page
@app.route('/payment')
def Payment():
    return render_template('Payment.html')

#Index Page
@app.route('/index')
def Index():
    return render_template('Index.html')

#turns on debug mode, allows for refreshing page for updates
if __name__ == "__main__":
    app.run(debug=True)

#Trying to install Flask Excel
