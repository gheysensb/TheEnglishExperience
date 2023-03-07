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

# Création du connecteur à la base de données database.db



@app.route('/')
def main():
        return render_template("acceuilnotlogin.html")


@app.route('/login')
def login():
    if "user" in session:
        return redirect("/")
    else:
        return render_template("Login.html")

@app.route('/login', methods=['POST'])
def login_post():
    name = request.form.get('name')
    password = request.form.get('password')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT username from userinfo WHERE username = ? """, (name, ))
    liste = cursor.fetchall()
    if len(liste) == 0:
        flash("Ce pseudo n'est pas enregistré")
        return redirect("/login")
    elif len(name) > 20  or len(password) > 90:
        flash("L'adresse email , le mot de passe ou le nom est trop long !")
        return redirect("/login")
    cursor.execute("""SELECT password from userinfo WHERE username = ? """, (name, ))
    liste = cursor.fetchall()
    if liste[0][0] != password:
        flash("Mot de passe incorrect")
        return redirect("/login")
    session['user'] = name
    cursor.close()
    conn.commit()
    conn.close()
    return redirect("/")

@app.route('/signup')
def signin():

        if "user" in session:
            return redirect("/")
        return render_template("Signup.html")

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect("/")

@app.route('/signup', methods=['POST'])
def signup_post():
    name = request.form.get('name')
    password = request.form.get('password')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT username from userinfo WHERE username = ? """, (name, ))
    liste = cursor.fetchall()
    if len(liste) != 0:
        flash("Ce pseudo est déjà enregistré pour un autre soldat")
        return redirect("/signup")
    elif len(name) > 20  or len(password) > 90:
        flash("L'adresse email , le mot de passe ou le nom est trop long !")
        return redirect("/signup")
    requete = """INSERT INTO userinfo (username,password)VALUES(?,?)"""
    values = ( name,password,)
    cursor.execute(requete, values)
    session['user'] = name
    cursor.close()
    conn.commit()
    conn.close()
    return redirect("/")

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

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/add')
def add():
    return render_template("ajout.html")

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


