from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
        return 'Hello, Tazkia!'

@app.route('/menu')
def menu():
        return 'Menu 1, Menu 2, Menu 3'

@app.route('/contact')
def menu():
        return 'Contact Me!'

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5099)

