from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello World!'

@app.route('/index.html', methods=['GET'])
def inputting() -> 'html':
    return render_template('template1.html')

@app.route('/test', methods=['POST'])
def hello2() -> 'html':
        eingabeeins = request.form['eingabeeins']
    return render_template('results.html', 
                            inputeins = eingabeeins,
                            )
app.run()