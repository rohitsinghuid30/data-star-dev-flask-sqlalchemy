from flask import Flask, render_template, request, redirect
import threading
import json
from datetime import datetime

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
