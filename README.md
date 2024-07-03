# End-to-End Anime Recommender System

### Content-Based Filtering
The content-based recommender system is created using two separate neural networks, each with three hidden dense layers. One network processes user data, while the other processes anime data. These two networks are then combined using a dot product, followed by an additional dense layer to predict the ratings. This approach analyzes textual descriptions and attributes of anime to suggest similar series based on their features, providing tailored suggestions that align with users' interests.

### Collaborative Filtering
Collaborative filtering generates user parameter vectors and anime feature vectors from existing ratings stored in a matrix 𝑌, where each element 𝑦(𝑖,𝑗) represents the rating given by user j to anime i, with unrated entries as 0. An indicator matrix 𝐑, where 𝑟(𝑖,𝑗) is 1 if user j has rated anime i, supports this. The system learns user parameter vectors (𝐰(𝑗)) and anime feature vectors (𝐱(𝑖)) using these ratings. Predictions are made by computing the dot product of 𝐰(𝑗) and 𝐱(𝑖), plus a bias term 𝑏(𝑗), enabling personalized anime recommendations. This learning process is optimized using TensorFlow, involving a cost function and gradient descent to minimize prediction errors.

### Combined Recommender System
The combined recommender system integrates both the collaborative and content-based approaches. This hybrid method leverages the strengths of both systems to provide even more accurate and relevant recommendations for anime fans.

With these three recommenders in place, anime fans can discover new and exciting series, whether they're seeking action-packed adventures, heartwarming dramas, or fantastical escapades. Our end-to-end recommender system aims to inspire and assist anime fans in finding their next favorite series. Start your exploration today with our personalized anime recommendations!

## How to Use the API

1. Clone this repository
2. Run this command:
   ```bash
   pip install -r requirements.txt
3. Run this command:
   ```bash
   python app.py

