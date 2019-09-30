from flask import Flask

app = Flask(__name__)

@app.route('/hello')

def index():
    return 'This is the homepage'

if __name__ == "__main__":
    app.run(debug=True)
    