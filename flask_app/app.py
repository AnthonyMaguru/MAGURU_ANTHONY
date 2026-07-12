# import flask
from flask import Flask render_templates

# create an instance of a flask class
# "__name__" is a special variable that tells Flask where to look for resources

app = Flask(__name__)

# Decorator: / : Maps the URL '/'

@app.route('/')

# Define a function to display text welcome to Flask
def home():
    # Write the text that can be displayed on your browser
    return '<h1> Welcome to Flask Framework </h1>'

# Route: /about : Maps the URL '/about'

@app.route('/about')
def about():
    return '<h1> About Flask </h1>'

# Dynamic Route: /mystory/<story>
# Maps the URL '/mystory' followed by any text

@app.route('/mystory/<story>')
def mystory(story):
    return f'<h1>My Story: {story}</h1>'

# profile Create Dynamic Route: /profile/<username>
@app.route('/profile/<username>')

def profile(username,user_id):
    # Data passed  from python function to HTML template
    return render_template('profile.html', username=username, user_id= user_id)

# Template inheritance: base.html


# To ensure your server runs only if this script is executed directly

if __name__ == '__main__':
    app.run(debug=True)