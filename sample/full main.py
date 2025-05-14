import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.classify import NaiveBayesClassifier
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
nltk.download('maxent_ne_chunker')
nltk.download('words')


# Read complaints from CSV file
def load_complaints_from_csv(file_path):
    return pd.read_csv(file_path)


# Preprocess text: Tokenize and remove stopwords
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    words = [w.lower() for w in words if w.isalpha() and w.lower() not in stop_words]
    return words


# Feature extraction for classification
def extract_features(text):
    words = preprocess_text(text)
    return {word: True for word in words}


# Train classifiers for category and department based on existing complaints
def train_classifiers(df):
    train_data_category = [(extract_features(complaint['complaint_text']), complaint['category']) for _, complaint in
                           df.iterrows()]
    train_data_department = [(extract_features(complaint['complaint_text']), complaint['department']) for _, complaint
                             in df.iterrows()]

    category_classifier = NaiveBayesClassifier.train(train_data_category)
    department_classifier = NaiveBayesClassifier.train(train_data_department)

    return category_classifier, department_classifier


# Predict category and department using the trained classifiers
def predict_category_and_department(complaint_text, category_classifier, department_classifier):
    features = extract_features(complaint_text)
    predicted_category = category_classifier.classify(features)
    predicted_department = department_classifier.classify(features)
    return predicted_category, predicted_department


# Function for analyzing sentiment using NLTK's SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


# Function to categorize urgency based on sentiment scores
def categorize_urgency(sentiment_score):
    if sentiment_score <= -0.3:
        return 'High Urgency'
    elif sentiment_score <= 0:
        return 'Medium Urgency'
    else:
        return 'Low Urgency'


# Named Entity Recognition (NER) to extract named entities from text
def extract_named_entities(text):
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    tree = ne_chunk(tagged)

    named_entities = []
    for subtree in tree:
        if isinstance(subtree, Tree):  # It's a named entity
            entity = " ".join([word for word, tag in subtree])
            named_entities.append(entity)
    return named_entities


# Function to predict category, department, and urgency for a new complaint
def predict_for_user_input(df, user_complaint):
    category_classifier, department_classifier = train_classifiers(df)

    # Predict category and department
    predicted_category, predicted_department = predict_category_and_department(user_complaint, category_classifier,
                                                                               department_classifier)

    # Analyze sentiment for urgency
    sentiment_score = sia.polarity_scores(user_complaint)['compound']
    predicted_urgency = categorize_urgency(sentiment_score)

    # Extract named entities
    named_entities = extract_named_entities(user_complaint)

    return predicted_category, predicted_department, predicted_urgency, sentiment_score, named_entities


# Function to save analysis result to CSV file
def save_analysis_to_csv(df, user_complaint, predicted_category, predicted_department, predicted_urgency, output_file):
    result = {
        'complaint_text': user_complaint,
        'predicted_category': predicted_category,
        'predicted_department': predicted_department,
        'predicted_urgency': predicted_urgency
    }
    result_df = pd.DataFrame([result])

    # Append the result to the CSV file (or create a new one if not exist)
    result_df.to_csv(output_file, mode='a', header=not pd.io.common.file_exists(output_file), index=False)


# Main function to interact with the user
def main():
    # Load complaints data from CSV file (replace 'complaints.csv' with your file)
    input_csv = 'combined_file.csv'
    df = load_complaints_from_csv(input_csv)

    # Get user input (complaint text)
    user_complaint = input("Please enter your complaint: ")

    # Get predictions
    predicted_category, predicted_department, predicted_urgency, sentiment_score, named_entities = predict_for_user_input(df, user_complaint)

    # Output the results
    print("\nAnalysis for User Petition:")
    print(f"User Petition: {user_complaint}")
    print(f"Predicted Category: {predicted_category}")
    print(f"Predicted Department: {predicted_department}")
    print(f"Sentiment Score: {sentiment_score}")
    print(f"Urgency: {predicted_urgency}")
    print(f"Named Entities: {named_entities}")

    # Save the results back to a CSV file
    output_csv = 'processed_complaints.csv'  # Change this to your desired output file
    save_analysis_to_csv(df, user_complaint, predicted_category, predicted_department, predicted_urgency, output_csv)
    print(f"Results saved to {output_csv}")


if __name__ == "__main__":
    main()
