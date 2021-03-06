#!/usr/bin/env python3

import sys
import flask
import json

app = flask.Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def get_main():
    global api_port
    return flask.render_template('main.html', api_port=api_port)


@app.route('/candidate')
def get_candidate():
    global api_port
    id = flask.request.args.get('id')
    return flask.render_template('candidate.html', api_port=api_port, id=id)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: {0} host port api-port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    api_port = sys.argv[3]
    app.run(host=host, port=int(port), debug=True)