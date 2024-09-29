from flask import Blueprint, render_template

account_bp = Blueprint('account', __name__)

@account_bp.route('/signin')
def signin():
    return render_template('sign-in.html')

@account_bp.route('/signup')
def signup():
    return render_template('sign-up.html')
    
