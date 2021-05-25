from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


inp = input()
analysis = analyzer.polarity_scores(inp)
print(analysis)
analysis = analysis['compound']

if analysis >= 0.05:
	print('Pos')
	pass
elif analysis  > -0.05 and analysis < 0.05: 
	print('neu')
	pass
elif analysis <= -0.05:
	print('neg')
	pass
else:
	print("err")