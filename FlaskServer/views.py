from flask import (
    Blueprint, redirect, request, session, jsonify
)
from . import sentParsing
import os
import os.path

bp = Blueprint('graph', __name__, url_prefix='/')

@bp.route('/', methods=('GET', 'POST'))
def index():
    # if request.method == 'GET':
    #     absPath = os.path.abspath(os.getcwd())
    #     nwPath = absPath.replace("Flask_Files", f"Flutter_Project\\assets\\con.png")
    #     if os.path.isfile(nwPath):
    #         os.remove('con.png')
    if (request.method == 'POST') and request.is_json:
        
        print("received dart post request")
        response = request.get_json()
        
        result = sentParsing.treeDeterminer(response['type'], response['body']) #function that determines whether to make dependency or constituent tree
        if result:
            return result
        else:
            return jsonify("<h1>Error creating dependency tree</h1>")