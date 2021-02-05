from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello Updated World! = this is for test1"

if __name__ == '__main__':
    app.run()
