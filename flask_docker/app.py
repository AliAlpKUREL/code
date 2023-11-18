from flask import Flask, jsonify, render_template, request
import requests
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/get_movie_data', methods=['POST'])
def get_movie_data():
    # Get the city from the form data
    searchText = request.form.get('searchText')

    # Replace 'your_api_key' with your actual OpenWeatherMap API key
    api_key = 'your_api_key'
    api_url = f'https://api.themoviedb.org/3/search/movie?api_key=ab166ff82684910ae3565621aea04d62&language=en-US&query=${searchText}&page=1&include_adult=false'
    response = requests.get(api_url)

    # Return JSON response
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)