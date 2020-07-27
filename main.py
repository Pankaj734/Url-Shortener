import urlDB
import algo

original_url = input("Enter original url : ")

short_url = ""

check = urlDB.check(original_url)

if(check == 0):
	print("Your short url : ")
	print("http://MyUrlShortner/"+urlDB.fetchShortOf(original_url))

else:
	id = urlDB.insertOriginal(original_url)
	short_url = short_url + algo.short(id)
	urlDB.insert(original_url,short_url)
	print("")
	print("http://MyUrlShortner/"+urlDB.fetchShortOf(original_url))





