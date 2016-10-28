from bs4 import BeautifulSoup as bs
import requests
import re

class SearchObj:
	def __init__(self, rating, link):
		self.rating = rating
		self.link = link


def getContents(URL):
	html_code = requests.get(URL).text

	soup = bs(html_code, 'html.parser')

	contents = soup.find_all("pre", class_="js-tab-content")
	return contents[0].text

def getBestLink(query):

	URL = "https://www.ultimate-guitar.com/search.php?search_type=title&value="
	query = query.strip().replace(" ", '+')
	URL = URL + query

	html_code = requests.get(URL).text
	soup = bs(html_code, 'html.parser')

	searches = []
	best_rating = 0

	table = soup.find_all("table", class_="tresults")[0]

	for row in table.find_all('tr')[2:]:
		if len(row.find_all("b", class_="ratdig")) > 0:
			rating = int(row.find_all("b", class_="ratdig")[0].text)
		else:
			rating = 0
		link = row.find_all("td")[1].find_all("a")[0].get('href')
		searches.append(SearchObj(rating, link))

	best_search = searches[0]
	for e in searches:
		if e.rating > best_rating:
			best_rating = e.rating
			best_search = e

	return best_search.link


if __name__ == "__main__":
	MAIN_URL = "https://www.ultimate-guitar.com/search.php?search_type=title&value="
	query = raw_input("Song name : ")
	# query = "21 guns"
	query = query.strip().replace(" ", '+')
	MAIN_URL = MAIN_URL + query



	# print getContents(URL)
	URL = getBestLink(MAIN_URL)
	print getContents(URL)