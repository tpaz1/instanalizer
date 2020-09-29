from instanalyzer import instanalyzer
from flask import Flask, request
""" Here we are importing the Flask module and creating a Flask web server from the Flask module."""

bot = instanalyzer()
"""creats an instance of our class"""

app = Flask(__name__)
"""This current file will represent my web application."""

@app.route("/login")
"""representing our /login web page using request sub-library that let us login with our credentials
 from the url"""

def login():
    username = request.args.get('username')
    password = request.args.get('password')
    ## login?username=username&password=p@ssw0rd
    bot.login(username, password)
    return "success"

@app.route("/unfollow")
"""representing our /unfollow web page"""
def unfollow_users():
    return 'Unfollowing @' + bot.unfollow_users()

if __name__ == "__main__":
    """this will run the application"""
    app.run(debug=True)