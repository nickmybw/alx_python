"""ALX python web frames tsk 0"""
# Import Flask
from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define a route and its corresponding function


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' when the root route is accessed."""
    return 'Hello HBNB!'


# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
