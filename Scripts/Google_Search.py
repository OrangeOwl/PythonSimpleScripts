# Will require the python libraries google + googlesearch
import google
import googlesearch
from googlesearch import search
# to search 
query = input("Search Google! >>")

def search_item(): 
	global query 
	for results in search(query, tld="co.in", num=2, stop=2, pause=2): 
		print("::TOP SEARCH RESULT::")
		print(results)
		
		
search_item()		 
