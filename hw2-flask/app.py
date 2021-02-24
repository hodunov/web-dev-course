from flask import Flask, render_template, request
import requests
from faker import Faker

app = Flask(__name__)


@app.route('/')
def main():
    """
    Home page with invitation
    """
    return render_template("main.html")


@app.route('/requirements')
def requirements():
    """
    Display the contents of the requirements.txt
    """
    with open('requirements.txt', 'r') as req:
        return render_template("req.html", **{
            'text': req.read().split(),
        })


@app.route("/generate-users/")
def generate_users():
    """
    Display randomly generated users (first name + mail) by default 100
    """
    # Define query string parameter
    user_count = int(request.args.get('user_count')) if request.args.get('user_count') else 100
    # Collect the generated data into a tuple list
    user_data = [(Faker().unique.first_name(), Faker().unique.email()) for _ in range(user_count)]
    return render_template("users.html", **{
        'user_data': user_data,
    })


@app.route("/space/")
def space():
    """
    Display the current number of astronauts
    """
    req = requests.get('http://api.open-notify.org/astros.json')
    return render_template("space.html", **{
        'req': req.json()['people'],
    })


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True
    )
