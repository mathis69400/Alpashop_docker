from flask import Flask, render_template, g
import templates, sqlite3, db
from datetime import date



app = Flask(__name__)


@app.route("/")
def home():
    d = date.today().isoformat()
    return render_template("home.html", la_date = d, lamas = db.findAll("*"))

@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route("/produits")
def produits():
    return render_template("produits/index.html", lamas = db.findLama("*")) 

if __name__ == "__main__":
    app.run(debug=True)