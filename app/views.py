#from app import app
from flask import render_template
from app import app
@app.route("/")
def home():
    return render_template('index.html', name=name)

@app.route("/about/")
def about(name=None):
    return render_template('about.html', name=name)

if __name__=="__main__":
    app.run(debug=True)