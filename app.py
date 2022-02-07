from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:vitauautomation@localhost/Vitau'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db = SQLAlchemy(app)

class Medicoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, unique=True, nullable=False)
    timestamp = db.Column(db.DateTime(timezone=False), nullable=False)

    def __init__(self, valor, timestamp):
        self.valor = valor
        self.timestamp = timestamp

@app.route('/')
def home():
    return '<a href="/addValue"><button> Click here </button></a>'


@app.route("/addValue")
def addValue():
    return render_template("index.html")


@app.route("/sendValue", methods=['POST'])
def sendValue():
    valor = request.form["valor"]
    timestamp = request.form["timestamp"]
    entry = Medicoes(valor, timestamp)
    db.session.add(entry)
    db.session.commit()

    return render_template("index.html")

if __name__ == '__main__':
    db.create_all()
    app.run()