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
from apscheduler.schedulers.background import BackgroundScheduler
import logging
from pyChatGPT import ChatGPT
app = Flask(__name__)
app.secret_key = 'laclé'
app.config["SESSION_TYPE"]="filesystem"
@app.route('/')
def main():
        return render_template("acceuilnotlogin.html")







if __name__ == '__main__':
    app.run()


