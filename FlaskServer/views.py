from flask import (
    Blueprint, redirect, request, session, jsonify, render_template
)
from . import sentParsing
import os
import os.path

bp = Blueprint('graph', __name__, url_prefix='/')

@bp.route('/', methods=('GET', 'POST'))
def index():
    if (request.method == 'GET'):
        return render_template('base.html', type=request.args.get('q'))

    if (request.method == 'POST') and request.is_json:
        
        print("received post request")
        response = request.get_json()
        
        result = sentParsing.graphGen(response['body'])
        if result:
            return render_template('base.html')
        else:
            return jsonify("<h1>Error creating dependency tree</h1>")