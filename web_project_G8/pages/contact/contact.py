from flask import Blueprint, render_template

# catalog blueprint definition
contact = Blueprint('contact', __name__, static_folder='static', static_url_path='/contact', template_folder='templates')


# Routes
@catalog.route('/contact')
def index():
    return render_template('contact.html')