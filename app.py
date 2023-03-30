from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/new-blogs")
def new_blogs():
    return render_template("new-blogs.html")

@app.route("/archive")
def archive():
    return render_template("archive.html")

@app.route("/about-us")
def about():
    return render_template("about.html")

@app.route("/contact-us")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
