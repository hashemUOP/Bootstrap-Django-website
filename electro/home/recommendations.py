import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from products.models import UserReview, ProductModel

def generate_user_similarity():
    # This function calculates the similarity between users based on their product ratings

    reviews = UserReview.objects.all()  # Fetches all user reviews from the database using Django

    # Extracts unique user and product IDs from the reviews, which will be used as the rows and columns of the user-item matrix
    user_ids = reviews.values_list('user__id', flat=True).distinct()  # Use 'user__id' to get the user ID from the ForeignKey
    product_ids = reviews.values_list('product_id', flat=True).distinct()  # Get product IDs

    # Creates a pandas DataFrame where: Rows represent users user_ids. Columns represent products product_ids. all initial values are set to 0
    user_item_matrix = pd.DataFrame(0, index=user_ids, columns=product_ids)

    for review in reviews:  # بتلف ع كل review
        # Updates the user_item_matrix with the user's rating (star_reviews) for the corresponding product
        user_item_matrix.at[review.user.id, review.product_id] = review.star_reviews  # Use review.user.id to access the user ID via ForeignKey

    # Calculates the cosine similarity between all rows (users)
    similarity_matrix = cosine_similarity(user_item_matrix.fillna(0))  # Cosine similarity calculation

    # Returns the similarity matrix and the list of user IDs (matrix index)
    return similarity_matrix, user_item_matrix.index


def recommend_products(user_id, num_recommendations=5):
    similarity_matrix, user_ids = generate_user_similarity()  # Generates the similarity matrix

    user_index = list(user_ids).index(user_id)  # Finds the index of the target user (user_id) in the list of user IDs

    # Extracts similarity scores for the target user
    similar_users = list(enumerate(similarity_matrix[user_index]))
    # Sorts users by similarity in descending order, excluding the target user (self-comparison)
    similar_users = sorted(similar_users, key=lambda x: x[1], reverse=True)[1:]

    product_scores = {}  # Creates an empty dictionary to store scores for products
    for index, similarity_score in similar_users:  # Iterates through similar users and fetches their product reviews
        other_user_reviews = UserReview.objects.filter(user__id=user_ids[index])  # Fetch reviews of similar users

        for review in other_user_reviews:  # Ensures the target user hasn’t already rated the product
            # If the target user has not rated the product yet
            if not UserReview.objects.filter(user__id=user_id, product_id=review.product_id).exists():
                # Calculates weighted scores for products based on the similar user’s rating and similarity score
                if review.product_id not in product_scores:
                    # Accumulates scores if multiple similar users rated the same product
                    product_scores[review.product_id] = review.star_reviews * similarity_score
                else:
                    product_scores[review.product_id] += review.star_reviews * similarity_score

    # Sorts products by their scores in descending order and selects the top num_recommendations
    recommended_product_ids = sorted(product_scores, key=product_scores.get, reverse=True)[:num_recommendations]

    # Queries the ProductModel to get details (e.g., name, price) for the recommended products
    recommended_products = ProductModel.objects.filter(ID__in=recommended_product_ids)

    return recommended_products  # Returns the final list of recommended products
