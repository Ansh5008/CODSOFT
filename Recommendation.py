import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie dataset (can be replaced with a CSV)
data = {
    'title': [
        'The Matrix', 'Inception', 'Interstellar', 'The Prestige',
        'The Dark Knight', 'Tenet', 'Memento', 'Blade Runner'
    ],
    'description': [
        'A computer hacker learns about the true nature of reality and his role in the war against its controllers.',
        'A thief who steals corporate secrets through dream-sharing technology is given a task to plant an idea.',
        'A team of explorers travel through a wormhole in space in an attempt to ensure humanity’s survival.',
        'Two stage magicians engage in a battle to create the ultimate illusion while sacrificing everything.',
        'Batman sets out to dismantle the remaining criminal organizations in Gotham.',
        'A secret agent is tasked with preventing World War III through time manipulation.',
        'A man with short-term memory loss attempts to track down his wife’s murderer.',
        'A blade runner must pursue and terminate four replicants who stole a ship in space.'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Function to recommend movies based on title
def recommend_movies(title, df, top_n=5):
    # Vectorize the descriptions using TF-IDF
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['description'])

    # Compute cosine similarity matrix
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Get index of the movie that matches the title
    idx = df[df['title'].str.lower() == title.lower()].index

    if len(idx) == 0:
        return f"No movie found with title: {title}"

    idx = idx[0]

    # Get pairwise similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top_n most similar movies (excluding the queried one)
    sim_scores = sim_scores[1:top_n+1]
    movie_indices = [i[0] for i in sim_scores]

    return df['title'].iloc[movie_indices].tolist()

# Main function to interact
def run_recommender():
    print("🎬 Welcome to the Movie Recommender System!")
    print("Available Movies:")
    for i, movie in enumerate(df['title']):
        print(f"{i+1}. {movie}")

    while True:
        title = input("\nEnter a movie title (or type 'exit' to quit): ").strip()
        if title.lower() == 'exit':
            print("Thank you for using the recommender. Goodbye!")
            break

        recommendations = recommend_movies(title, df)
        if isinstance(recommendations, str):
            print(recommendations)
        else:
            print(f"\nBecause you watched '{title}', you might also like:")
            for rec in recommendations:
                print(f"• {rec}")

# Run the system
if __name__ == "__main__":
    run_recommender()
    