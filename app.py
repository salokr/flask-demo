from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello from Flask! 🎉</h1>"

@app.route("/demo")
def demo():
    return "<h2>This is your /demo route!</h2>"

if __name__ == "__main__":
    app.run()
