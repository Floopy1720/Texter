@app.route('/sentiment/chart')
def sentiment_img():
	text = request.args.get('text')
	text = TextBlob(text)
	text = text.correct()
	analysis = analyzer.polarity_scores(text)
	pie_sentiment(analysis['neg'], analysis['neu'], analysis['pos'],text)
	return render_template('image.html')
	pass

@app.route('/sentiment/chart_correctionFalse')
def sentiment_img_non():
	text = request.args.get('text')
	analysis = analyzer.polarity_scores(text)
	pie_sentiment(analysis['neg'], analysis['neu'], analysis['pos'])
	return render_template('image.html')
	pass