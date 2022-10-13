from flask import Flask
app = Flask(__name__)
@app.route("/home")
@app.route("/index")
@app.route("/", methods=["GET", "POST"])
def home():
     return "<p>Hello, World!</p>"
     
app.run(debug=True)