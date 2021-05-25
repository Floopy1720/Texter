from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
outup_sent_scorce = "None"

def sent_scorce(inp):
	global outup_sent_scorce
	analysis = analyzer.polarity_scores(inp)
	outup_sent_scorce = analysis
	pass