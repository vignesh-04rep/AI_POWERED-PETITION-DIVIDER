import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.classify import NaiveBayesClassifier
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

# Sample dataset for grievances and complaints (In real scenarios, you need a much larger dataset)
data = {
    'complaint_text': [
        "The water supply in our neighborhood is irregular and needs to be fixed urgently.",
        "The public transportation service is overcrowded and unreliable. Immediate action is needed.",
        "There is no proper sanitation in our area, making it unsafe for residents.",
        "I am being unfairly treated by my supervisor and demand immediate intervention.",
        "Our local hospital lacks medical supplies and staff. Patients are suffering.",
        "The roads are filled with potholes, causing damage to vehicles and accidents."
    ],
    'category': ['Infrastructure', 'Public Safety', 'Health', 'Human Resources', 'Health', 'Infrastructure'],
    'department': ['Public Works', 'Public Safety Department', 'Health Department', 'Human Resources', 'Health Department', 'Public Works']
}

# Convert dataset to a pandas DataFrame
df = pd.DataFrame(data)

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

# Prepare training data for the Naive Bayes classifier for category prediction
train_data_category = [(extract_features(complaint['complaint_text']), complaint['category']) for _, complaint in df.iterrows()]
train_data_department = [(extract_features(complaint['complaint_text']), complaint['department']) for _, complaint in df.iterrows()]

# Train Naive Bayes classifiers for category and department
category_classifier = NaiveBayesClassifier.train(train_data_category)
department_classifier = NaiveBayesClassifier.train(train_data_department)

# Function to predict category and department using the trained classifiers
def predict_category_and_department(complaint_text):
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

# Predict category, department, and urgency for a new complaint or grievance
new_grievance = "I have been denied medical benefits despite meeting all the requirements."

# Predict category and department
predicted_category, predicted_department = predict_category_and_department(new_grievance)

# Analyze sentiment for urgency
new_sentiment_score = sia.polarity_scores(new_grievance)['compound']
predicted_urgency = categorize_urgency(new_sentiment_score)

# Output the results
print(f"Predicted Category: {predicted_category}")
print(f"Predicted Department: {predicted_department}")
print(f"Predicted Urgency: {predicted_urgency}")
