# commands for running in Windows
# $env:FLASK_APP = "rps"
# $env:FLASK_ENV = "development"
# python -m flask run

from flask import Flask
from flask import render_template
from flask import request
import random 

from flask import Flask, url_for, request
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/',methods = ['POST', 'GET'])
def index():
  # if there is form data and there is a choice variable then we can see who won the game
  if request.method == 'POST' and request.form.get("choice") != "":
    choices = ["rock", "paper", "scissors"]
    user = request.form.get("choice")
    computer = choices[random.randint(0,2)]

    # if user and computer make the same choice
    if user == computer:
      # it's a draw
      return render_template('draw.html', user=user, computer=computer)

    # if user choice beats computer
    if user == "rock" and computer == "scissors"  or user == "paper" and computer == "rock" or user == "scissors" and computer == "paper":
      # it's a win
      return render_template('win.html', user=user, computer=computer)

    # if not a draw and user did not win
    # it is a loss
    return render_template('lose.html', user=user, computer=computer)

  # if no form data then we show the index page
  else:
    return render_template('index.html')

