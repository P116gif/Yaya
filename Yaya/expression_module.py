from textblob import TextBlob
from vtube_module import send_parameter_to_vts
import time

# Function to analyze sentiment
def analyze_sentiment(text):

    blob = TextBlob(text)

    polarity = blob.sentiment.polarity

    print(blob.sentiment)

    if polarity > 0.5:
        return "1"
    elif polarity > 0.0:
        return "2"
    elif polarity < -0.5:
        return "6"
    elif polarity < 0.0:
        return "6"
    else:
        return "Neutral"

# Function to trigger an expression
def trigger_expression(expression):
    send_parameter_to_vts(expression, 1.0)  # Activate the expression
    time.sleep(2)  # Keep the expression active for 2 seconds
    send_parameter_to_vts(expression, 0.0)  # Deactivate the expression
