"""ALX python web framework task 5"""


# Import Flask and render_template
from flask import Flask, render_template

# Create a Flask app instance
app = Flask(__name__)

# Define a route and its corresponding function for the root URL


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' when the root route is accessed."""
    return 'Hello HBNB!'

# Define a route and its corresponding function for the /hbnb URL


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB' when the /hbnb route is accessed."""
    return 'HBNB'

# Define a route and its corresponding function for the /c/<text> URL


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Display 'C <text>' when the /c/<text> route is accessed."""
    decoded_text = unquote(text).replace('_', ' ')
    return 'C ' + decoded_text

# Define a route and its corresponding function for the /python/(<text>) URL


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Display 'Python <text>' when the /python/(<text>) route is accessed."""
    decoded_text = unquote(text).replace('_', ' ')
    return 'Python ' + decoded_text

# Define a route and its corresponding function for the /number/<n> URL


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Display '<n> is a number' when the /number/<n> route is accessed."""
    return '{} is a number'.format(n)

# Define a route and its corresponding function for the /number_template/<n> URL


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """Display an HTML page with the number 'n' inside an H1 tag."""
    return render_template('5-number.html', n=n)


# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
