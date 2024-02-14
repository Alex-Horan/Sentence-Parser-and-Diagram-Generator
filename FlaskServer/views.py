from flask import (
    Blueprint, redirect, request, session, jsonify, render_template
)
from . import sentParsing
import os
import os.path

bp = Blueprint('graph', __name__, url_prefix='/') #helps separate views from the init file

@bp.route('/', methods=('POST')) #routing the default page
def index():
    if (request.method == 'POST') and request.is_json:
        
        print("received post request")
        response = request.get_json()
        print(response)
        result = sentParsing.graphGen(response)
        if result:
            return result
        else:
            return jsonify("<h1>Error creating dependency tree</h1>")