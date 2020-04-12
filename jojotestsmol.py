from bs4 import BeautifulSoup 
import requests 
import csv


listOfJojos =  [
'https://jojo.fandom.com/wiki/Jonathan_Joestar',
]


csv_file = open('jojocsvtest.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name','age','stand','debut','departure'])


for i in listOfJojos:
	jojoName = i

	source = requests.get(jojoName).text
	soup = BeautifulSoup(source, 'lxml')

	#print(soup.prettify())

	name = soup.find('div', class_='page-header__main').h1.text
	# We originally had issues within the Jojo Dataset THe HTML was in a weird way where it was super encapusulated. Using the command below you can access the data you need.
	try:
		age = soup.find('div', class_='pi-item pi-data pi-item-spacing pi-border-color', attrs={'data-source': 'age'}).text
	except Exception as e:
		age = 'Age not Confirmed'



	try:
		stand = soup.find('div', class_='pi-item pi-data pi-item-spacing pi-border-color', attrs={'data-source': 'stand'}).text
	except Exception as e:
		stand = 'No Stand'



	try:
		debut = soup.find('div',class_= 'pi-item pi-data pi-item-spacing pi-border-color', attrs={'data-source': 'mangadebut'}).text
	except Exception as e:
		debut = 'No stated Manga debut'




	try:
		departure = soup.find('div',class_= 'pi-item pi-data pi-item-spacing pi-border-color', attrs={'data-source': 'mangafinal'}).text
	except Exception as e:
		debut = 'No stated Manga departure'

	print(name)
	print(age)
	print(stand)
	print(debut)
	print(departure)

	csv_writer.writerow([name,age,stand,debut,departure])

csv_file.close()

