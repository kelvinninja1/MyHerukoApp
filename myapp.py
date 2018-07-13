from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/test/')
def testpage():
    return '<button>This is button</button>'

@app.route('/python/version')
def versionpage():
    return "The python version is: " + sys.version

# 0.0.0.0 means listening on all network interfaces
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
