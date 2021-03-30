from flask import flask

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1> Hello</h1>"

@app.route('/predict')
def predict():
    return '<h2>PRedict</h2>'
    
if __main__ == '__main__':
    app.run(debug=True)