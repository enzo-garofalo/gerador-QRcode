from flask import Flask, render_template, request, url_for
from flask_qrcode import QRcode

app = Flask(__name__)
QRcode(app)

@app.route('/')
def index():
    return render_template('index.html', page_title="Digite a Frase")

@app.route('/converter', methods=['POST',])
def converter():
    frase = request.form['frase']
    print(frase)
    return render_template('resultado.html', page_title="Frase em QR-Code", frase=frase)


if __name__ == '__main__':
    app.run(debug=True)