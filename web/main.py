from flask import Flask, render_template, url_for

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/modeling')
def modeling():
    return render_template('modeling.html')

@app.route('/api')
def api():
    return render_template('api.html')

@app.route('/graph')
def graph():
    return render_template('graph.html')

app.run
