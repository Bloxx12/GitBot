from flask import Flask, render_template, request

app = Flask(__name__)

#@app.route('/')
#def hello() -> str:
#    return 'Hello World!'

@app.route('/temp', methods=['GET'])
def hello3() -> 'html':
    return render_template('template2.html')

@app.route('/', methods=['GET'])
def inputfunc() -> 'html':
    return render_template('template1.html')

@app.route('/test', methods=['POST'])
def results() -> 'html':
    return render_template('results.html',
                            inputeins = request.form['eingabeeins'],
                            inputzwei = request.form['eingabezwei'])
app.run()