"""ALX python web framework task 2"""

# Import Flask
from flask import Flask
from urllib.parse import unquote

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


# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
