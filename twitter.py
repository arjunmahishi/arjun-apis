import tweepy

class Twitter:
	def __init__(self):
		API_key = "2MEzKtwmVjJuLGrvonvkYiLnO"
		API_secret = "ZxbpjSxVFqvkINgxeYDJ4TEMMQNqtOuHDMN3IykONNnoD69SOy"

		access_token = "131552332-rb1aazGz6DUulHEFAUDeTDmZ3Sv8s4dlFMfPOfwJ"
		access_token_secret = "aDI1v3AAlKCyLLQ7GvZ9LEFYqjDPaCI2rkWZDtML1jnHJ"

		auth = tweepy.OAuthHandler(API_key, API_secret)
		auth.set_access_token(access_token, access_token_secret)

		self.api = tweepy.API(auth)

	def getTweets(self, tag):
		return self.api.search(tag)

if __name__ == "__main__":
	twitter = Twitter()
	print len(twitter.getTweets("Modi"))