import os

from flask import Flask, Response, abort

app = Flask(__name__)
DEFAULT_PATH = 'index.html'
MIMES = {
    'css': 'text/css',
    'html': 'text/html',
    'jpg': 'image/jpeg',
    'js': 'application/javascript',
    'json': 'application/json',
    'png': 'image/png',
}


@app.route('/')
@app.route('/<path:path>')
def serve(path=DEFAULT_PATH):
    """ Petit flask-based test server for angular-phonecat app """

    if not os.path.exists(path):
        abort(404)

    content = file(path, 'r').read()
    mimetype = MIMES[path[path.rindex('.') + 1:]]

    return Response(content, status=200, mimetype=mimetype)

if __name__ == '__main__':
    app.run('0.0.0.0', port=9001, debug=True)
