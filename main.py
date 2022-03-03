from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello World!'

@app.route('/index.html')
def inputting() -> 'html':
    return render_template('template1.html')
app.run()

@app.route('/test')
def hello() -> str:
    return 'Hello World!'