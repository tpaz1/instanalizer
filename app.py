from instanalyzer import instanalyzer
from flask import Flask, request 
from flask import render_template

""" Here we are importing the Flask module and creating a Flask web server from the Flask module."""

bot = instanalyzer()
"""creats an instance of our class"""

app = Flask(__name__)
"""This current file will represent my web application."""

@app.route("/home")
# representing our homepage

def home():
    return render_template('home.html')

@app.route("/login", methods=['GET', 'POST'])
# representing our /login web page using request sub-library that let us login with our credentials from the url

def login():
    if request.method == 'POST':
      result = request.form
      username = result['Username']
      password = result['Password']

    bot.login(username, password)
    # return "Successfuly logged with user " + username
    return render_template('unfollow.html')

@app.route("/unfollow", methods=['GET', 'POST'])
# representing our /unfollow web page

def unfollow_users():
    if request.method == 'POST':
      return bot.unfollow_users()

if __name__ == "__main__":
    app.run(debug=True)