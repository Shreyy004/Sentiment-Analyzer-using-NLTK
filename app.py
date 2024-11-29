from flask import Flask,render_template,request
from Sentiment_analyzer import SentimentAnalyzer

app=Flask(__name__)
analyzer=SentimentAnalyzer()
@app.route('/')

def home():
    return render_template('index.html')

@app.route('/analyze',methods=['POST'])

def analyze():
    text=request.form['text']
    sentiment=analyzer.analyze_sentiment(text)
    return f'The sentiment of your text is: {sentiment}'

if __name__=='__main__':
    app.run()
