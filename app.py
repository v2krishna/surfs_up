from flask import Flask

app  = Flask(__name__)

@app.route('/')
def hello_ds():
    return 'Hello DS'

# @app.route('/')
# def hello_world():
#     return 'Hello World'

