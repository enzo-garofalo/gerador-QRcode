from flask import Flask, render_template
from flask_qrcode import QRcode

app = Flask(__name__)
QRcode(app)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)