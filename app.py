from flask import Flask, render_template, request
from fuzzywuzzy import fuzz
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def find_similar_anime(user_input, anime_data):
    best_match = None
    best_score = 0
    for anime_title in anime_data:
        score = fuzz.ratio(user_input, anime_title.lower())
        if score > best_score:
            best_score = score
            best_match = anime_title
    return best_match

def recommender(name,genre_tf,anime_filtered):
    cos_array = pd.DataFrame(cosine_similarity(genre_tf),columns=anime_filtered['name'],index=anime_filtered['name'])
    recommendation = (cos_array.loc[name].sort_values(ascending=False).index).tolist()
    recommendation.remove(name)
    return recommendation[:5]
    
@app.route('/predict',methods=['POST'])
def predict():
    if request.method == "POST":
        # Get the user's input from the form
        anime_title = request.form.get("anime_title")
        if anime_title:
            # Process
            anime_filtered = pd.read_csv('anime_filtered.csv')
            genre_tf = pd.read_csv('genre_tf.csv')
            genre_tf.set_index('name',inplace=True)
            anime_data = genre_tf.index
            user_input = anime_title.strip().lower()

            best_match = find_similar_anime(user_input, anime_data)
            recommendation = recommender(best_match, genre_tf, anime_filtered)
            
            # Render the template with the recommendations
            return render_template("index.html", prediction_text=recommendation,lol=best_match)
    # Default return statement
    return render_template("index.html", prediction_text=[])

if __name__ == "__main__":
    app.run(debug=True)



