from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello():
    return render_template('layout.html')

if __name__ == ('__main__'):
    app.run(port=8000, host='0.0.0.0', debug=True)
