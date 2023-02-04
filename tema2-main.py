from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "!!Hola Mundo!! adios hhdh"

@app.route("/hola")
def hola():
    return "<h1> saludo desde hola</h1>"

@app.route("/nueva")
def nueva():
    return "<h1> saludo desde nueva</h1>"

if __name__=="__main__":
    app.run(debug=True)