#sample python flask app to disply hello world
# In return statement give the  cool html page with hello world
from flask import Flask  # type: ignore

app = Flask(__name__)

@app.route('/')

def hello_world():
    return '<h1>Hello World! I am a Successful DevOps/AI Engineer</h1>'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)