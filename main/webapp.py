from flask import Blueprint
from flask import redirect

server_bp = Blueprint('main', __name__)

@server_bp.route('/')
def index():
    return redirect("/dashboard-1")
