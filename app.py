import datetime
from base64 import b64decode
from datetime import timedelta
from flask import Flask, request, render_template, redirect, flash, session, jsonify, make_response, url_for, json
import random
import os
import hmac
import hashlib
import sqlite3
import pickle
import logging
from pyChatGPT import ChatGPT
app = Flask(__name__)
app.secret_key = 'laclé'
app.config["SESSION_TYPE"]="filesystem"
@app.route('/')
def main():
        return render_template("acceuilnotlogin.html")


@app.route('/connexion')
def login():
    return render_template("Login.html")

@app.route('/inscription')
def signup():
    return render_template("Signup.html")

@app.route('/apropos')
def apropos():
    return render_template("about.html")

@app.route('/cgu')
def cgu():
    return render_template("cgu.html")

@app.route('/profil')
def profil():
    return render_template("profil.html")

@app.route('/apprentissage')
def apprentissage():
    return render_template("apprentissage.html")


@app.route('/challenge')
def challenge():
    return render_template('challenge.html')

@app.route('/scoreboard')
def scoreboard():
    return render_template('scoreboard.html')

@app.route('/coursparticulier')
def coursparticulier():
    return render_template('coursparticulier.html')


@app.route('/leçon')
def lecon():
    return render_template('leçon.html')

if __name__ == '__main__':
    app.run()


