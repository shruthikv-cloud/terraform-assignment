from flask import Flask

app = Flask(__name__)

@app.route('/')
def my_app():
    return "My app for terraform Assignment"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

#
