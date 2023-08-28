"""ALX python web framework task 6"""

# Import Flask and render_template
from flask import Flask, render_template

# Create a Flask app instance
app = Flask(__name__)

# Define routes and corresponding functions


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' when the root route is accessed."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB' when the /hbnb route is accessed."""
    return 'HBNB'

# ... (previous routes omitted for brevity)

# Define a route and its corresponding function for the /number_odd_or_even/<n> URL


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even_route(n):
    """Display an HTML page with the number and whether it's even or odd."""
    odd_or_even = 'odd' if n % 2 != 0 else 'even'
    return render_template('6-number_odd_or_even.html', n=n, odd_or_even=odd_or_even)


# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
