from flask import Flask

app = Flask(__name__)

@app.route('/foo')
def get_foo():
    return 'VAMO LAAAAAAAAAAAAAAAAAAAAooooooo'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)