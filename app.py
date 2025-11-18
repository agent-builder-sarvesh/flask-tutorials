from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/product')
def product():
    return 'this is product page'
if __name__ == '__main__':
    app.run(debug=True, port=5100)