import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the Vader lexicon
nltk.download('vader_lexicon') #pre trained sentiment analysis model

class SentimentAnalyzer:
    def __init__(self):
        # Initialize the sentiment analyzer
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        # Analyze the sentiment of the given text
        scores = self.analyzer.polarity_scores(text)
        if scores['compound'] > 0.05:
            return "Positive"
        elif scores['compound'] < -0.05:
            return "Negative"
        else:
            return "Neutral"

# Initialize the analyzer
analyzer = SentimentAnalyzer()

# Take user input
user_input = input("Enter a sentence to analyze its sentiment: ")

# Analyze the sentiment
result = analyzer.analyze_sentiment(user_input)

# Print the result
print(f"The sentiment of the entered text is: {result}")
