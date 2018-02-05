from bs4 import BeautifulSoup
import requests

def get_post(post_id):
	url_link = "http://safetyzone.iogp.org/FatalIncidents/detail.asp?inc_id="
	link_end_string = str(post_id)
	url_link = url_link + link_end_string
	r  = requests.get(url_link)
	data = r.text
	soup = BeautifulSoup(data)
	content = [] 
	
	#lazy programming--take a look to change this, shouldn't be using a break
	for link in soup.find_all('p'):
		content.append(link)
		break
	
	string = ""
	
	for i in content:
		str_add = str(i)
		string = string + str_add
		
#	string = str(post_id) + " - " + string

	if len(string) > 50:
		return string

	return "invalid id"
