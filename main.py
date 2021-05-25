from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from flask import Flask, render_template, request
# from mat import pie_sentiment
from textblob import TextBlob

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

@app.route('/')
def home():
	return render_template('home.html')
	pass

@app.route('/sentiment/values')
def sentiment_main():
	text = request.args.get('text')
	analysis = analyzer.polarity_scores(text)
	return analysis
	pass

@app.route('/sentiment')
def sentiment_val():
	text = request.args.get('text')
	analysis = analyzer.polarity_scores(text)
	analysis = analysis['compound']

	if analysis >= 0.05:
		return "Positive"
		pass
	elif analysis  > -0.05 and analysis < 0.05: 
		return "Neutral"
		pass
	elif analysis <= -0.05:
		return 'Negative'
		pass
	else:
		return "An error occured please try again"

@app.route('/text_correct')
def text_correct():
	text = request.args.get('text')
	text = TextBlob(text)
	text = text.correct()
	text = f'{text}'
	return text
	pass

@app.route('/text_tokenize')
def text_tokenize():
	text = request.args.get('text')
	text_blob = TextBlob(text)
	text_blob = f"{text_blob.words}"
	return text_blob
	pass

if __name__ == '__main__':
	app.run()