from bs4 import BeautifulSoup 
import requests 
import csv


listOfJojos =  [
'https://jojo.fandom.com/wiki/Jonathan_Joestar',
'https://jojo.fandom.com/wiki/Will_Anthonio_Zeppeli',
'https://jojo.fandom.com/wiki/Robert_E._O._Speedwagon',
'https://jojo.fandom.com/wiki/Erina_Pendleton',
'https://jojo.fandom.com/wiki/Poco',
'https://jojo.fandom.com/wiki/George_Joestar_I',
'https://jojo.fandom.com/wiki/Tonpetty',
'https://jojo.fandom.com/wiki/Straizo',
'https://jojo.fandom.com/wiki/Dire',
'https://jojo.fandom.com/wiki/Dio_Brando',
'https://jojo.fandom.com/wiki/Wang_Chan',
'https://jojo.fandom.com/wiki/Jack_the_Ripper',
'https://jojo.fandom.com/wiki/Tarkus',
'https://jojo.fandom.com/wiki/Bruford',
'https://jojo.fandom.com/wiki/Dario_Brando',
'https://jojo.fandom.com/wiki/Joseph_Joestar',
'https://jojo.fandom.com/wiki/Caesar_Anthonio_Zeppeli',
'https://jojo.fandom.com/wiki/Lisa_Lisa',
'https://jojo.fandom.com/wiki/Rudol_von_Stroheim',
'https://jojo.fandom.com/wiki/Messina',
'https://jojo.fandom.com/wiki/Loggins',
'https://jojo.fandom.com/wiki/Smokey_Brown',
'https://jojo.fandom.com/wiki/Suzi_Q',
'https://jojo.fandom.com/wiki/Kars',
'https://jojo.fandom.com/wiki/Esidisi',
'https://jojo.fandom.com/wiki/Wamuu',
'https://jojo.fandom.com/wiki/Santana',
'https://jojo.fandom.com/wiki/Straizo',
'https://jojo.fandom.com/wiki/Donovan',
'https://jojo.fandom.com/wiki/Wired_Beck',
'https://jojo.fandom.com/wiki/Mark',
'https://jojo.fandom.com/wiki/Mario_Zeppeli',
'https://jojo.fandom.com/wiki/George_Joestar_II',
'https://jojo.fandom.com/wiki/Jotaro_Kujo',
'https://jojo.fandom.com/wiki/Muhammad_Avdol',
'https://jojo.fandom.com/wiki/Noriaki_Kakyoin',
'https://jojo.fandom.com/wiki/Jean_Pierre_Polnareff',
'https://jojo.fandom.com/wiki/Iggy',
'https://jojo.fandom.com/wiki/Holy_Kujo',
'https://jojo.fandom.com/wiki/Anne',
'https://jojo.fandom.com/wiki/Roses',
'https://jojo.fandom.com/wiki/Enya_the_Hag',
'https://jojo.fandom.com/wiki/Vanilla_Ice',
'https://jojo.fandom.com/wiki/Hol_Horse',
'https://jojo.fandom.com/wiki/Nukesaku',
'https://jojo.fandom.com/wiki/Pet_Shop',
'https://jojo.fandom.com/wiki/Mariah',
'https://jojo.fandom.com/wiki/Alessi',
'https://jojo.fandom.com/wiki/Oingo',
'https://jojo.fandom.com/wiki/Boingo',
'https://jojo.fandom.com/wiki/Anubis',
'https://jojo.fandom.com/wiki/Kenny_G.',
'https://jojo.fandom.com/wiki/Gray_Fly',
'https://jojo.fandom.com/wiki/Impostor_Captain_Tennille',
'https://jojo.fandom.com/wiki/Forever',
'https://jojo.fandom.com/wiki/Devo',
'https://jojo.fandom.com/wiki/Rubber_Soul',
'https://jojo.fandom.com/wiki/J._Geil',
'https://jojo.fandom.com/wiki/Nena',
'https://jojo.fandom.com/wiki/ZZ',
'https://jojo.fandom.com/wiki/Steely_Dan',
'https://jojo.fandom.com/wiki/Arabia_Fats',
'https://jojo.fandom.com/wiki/Mannish_Boy',
'https://jojo.fandom.com/wiki/Cameo',
'https://jojo.fandom.com/wiki/Midler',
'https://jojo.fandom.com/wiki/Chaka',
'https://jojo.fandom.com/wiki/Khan',
'https://jojo.fandom.com/wiki/Josuke_Higashikata',
'https://jojo.fandom.com/wiki/Okuyasu_Nijimura',
'https://jojo.fandom.com/wiki/Koichi_Hirose',
'https://jojo.fandom.com/wiki/Rohan_Kishibe',
'https://jojo.fandom.com/wiki/Hayato_Kawajiri',
'https://jojo.fandom.com/wiki/Reimi_Sugimoto',
'https://jojo.fandom.com/wiki/Shigekiyo_Yangu',
'https://jojo.fandom.com/wiki/Mikitaka_Hazekura',
'https://jojo.fandom.com/wiki/Yukako_Yamagishi',
'https://jojo.fandom.com/wiki/Yuya_Fungami',
'https://jojo.fandom.com/wiki/Tamami_Kobayashi',
'https://jojo.fandom.com/wiki/Toshikazu_Hazamada',
'https://jojo.fandom.com/wiki/Tonio_Trussardi',
'https://jojo.fandom.com/wiki/Aya_Tsuji',
'https://jojo.fandom.com/wiki/Tomoko_Higashikata',
'https://jojo.fandom.com/wiki/Ryohei_Higashikata',
'https://jojo.fandom.com/wiki/Shinobu_Kawajiri',
'https://jojo.fandom.com/wiki/Yoshikage_Kira',
'https://jojo.fandom.com/wiki/Yoshihiro_Kira',
'https://jojo.fandom.com/wiki/Keicho_Nijimura',
'https://jojo.fandom.com/wiki/Akira_Otoishi',
'https://jojo.fandom.com/wiki/Anjuro_Katagiri',
'https://jojo.fandom.com/wiki/Ken_Oyanagi',
'https://jojo.fandom.com/wiki/Toyohiro_Kanedaichi',
'https://jojo.fandom.com/wiki/Terunosuke_Miyamoto',
'https://jojo.fandom.com/wiki/Masazo_Kinoto',
'https://jojo.fandom.com/wiki/Giorno_Giovanna',
'https://jojo.fandom.com/wiki/Bruno_Bucciarati',
'https://jojo.fandom.com/wiki/Leone_Abbacchio',
'https://jojo.fandom.com/wiki/Guido_Mista',
'https://jojo.fandom.com/wiki/Narancia_Ghirga',
'https://jojo.fandom.com/wiki/Pannacotta_Fugo',
'https://jojo.fandom.com/wiki/Trish_Una',
'https://jojo.fandom.com/wiki/Coco_Jumbo',
'https://jojo.fandom.com/wiki/Pericolo',
'https://jojo.fandom.com/wiki/Diavolo',
'https://jojo.fandom.com/wiki/Vinegar_Doppio',
'https://jojo.fandom.com/wiki/Squalo_and_Tiziano',
'https://jojo.fandom.com/wiki/Carne',
'https://jojo.fandom.com/wiki/Cioccolata',
'https://jojo.fandom.com/wiki/Secco',
'https://jojo.fandom.com/wiki/Polpo',
'https://jojo.fandom.com/wiki/Mario_Zucchero',
'https://jojo.fandom.com/wiki/Sale',
'https://jojo.fandom.com/wiki/Risotto_Nero',
'https://jojo.fandom.com/wiki/Formaggio',
'https://jojo.fandom.com/wiki/Illuso',
'https://jojo.fandom.com/wiki/Prosciutto',
'https://jojo.fandom.com/wiki/Pesci',
'https://jojo.fandom.com/wiki/Melone',
'https://jojo.fandom.com/wiki/Ghiaccio',
'https://jojo.fandom.com/wiki/Scolippi',
'https://jojo.fandom.com/wiki/Jolyne_Cujoh',
'https://jojo.fandom.com/wiki/Ermes_Costello',
'https://jojo.fandom.com/wiki/Foo_Fighters',
'https://jojo.fandom.com/wiki/Narciso_Anasui',
'https://jojo.fandom.com/wiki/Weather_Report',
'https://jojo.fandom.com/wiki/Gwess',
'https://jojo.fandom.com/wiki/Irene',
'https://jojo.fandom.com/wiki/Annakiss',
'https://jojo.fandom.com/wiki/Enrico_Pucci',
'https://jojo.fandom.com/wiki/Donatello_Versus',
'https://jojo.fandom.com/wiki/Rikiel',
'https://jojo.fandom.com/wiki/Ungalo',
'https://jojo.fandom.com/wiki/The_Green_Baby',
'https://jojo.fandom.com/wiki/Johngalli_A',
'https://jojo.fandom.com/wiki/Sports_Maxx',
'https://jojo.fandom.com/wiki/Miuccia_Miuller',
'https://jojo.fandom.com/wiki/Miraschon',
'https://jojo.fandom.com/wiki/Lang_Rangler',
'https://jojo.fandom.com/wiki/Kenzou',
'https://jojo.fandom.com/wiki/D_an_G',
'https://jojo.fandom.com/wiki/Guccio',
'https://jojo.fandom.com/wiki/Viviano_Westwood',
'https://jojo.fandom.com/wiki/Thunder_McQueen',
'https://jojo.fandom.com/wiki/Romeo_Jisso',
'https://jojo.fandom.com/wiki/Perla_Pucci',
'https://jojo.fandom.com/wiki/Loccobarocco',
'https://jojo.fandom.com/wiki/Johnny_Joestar',
'https://jojo.fandom.com/wiki/Gyro_Zeppeli',
'https://jojo.fandom.com/wiki/Lucy_Steel',
'https://jojo.fandom.com/wiki/Steven_Steel',
'https://jojo.fandom.com/wiki/Hot_Pants',
'https://jojo.fandom.com/wiki/Mountain_Tim',
'https://jojo.fandom.com/wiki/Diego_Brando',
'https://jojo.fandom.com/wiki/Wekapipo',
'https://jojo.fandom.com/wiki/Pocoloco',
'https://jojo.fandom.com/wiki/Norisuke_Higashikata_I',
'https://jojo.fandom.com/wiki/Funny_Valentine',
'https://jojo.fandom.com/wiki/Blackmore',
'https://jojo.fandom.com/wiki/Mike_O.',
'https://jojo.fandom.com/wiki/Ringo_Roadagain',
'https://jojo.fandom.com/wiki/Axl_RO',
'https://jojo.fandom.com/wiki/Magenta_Magenta',
'https://jojo.fandom.com/wiki/Dr._Ferdinand',
'https://jojo.fandom.com/wiki/D-I-S-C-O',
'https://jojo.fandom.com/wiki/Eleven_Men',
'https://jojo.fandom.com/wiki/Pork_Pie_Hat_Kid',
'https://jojo.fandom.com/wiki/Diego_Brando_From_Another_World',
'https://jojo.fandom.com/wiki/Sandman',
'https://jojo.fandom.com/wiki/Benjamin_Boom_Boom',
'https://jojo.fandom.com/wiki/Andre_Boom_Boom',
'https://jojo.fandom.com/wiki/L._A._Boom_Boom',
'https://jojo.fandom.com/wiki/Mrs._Robinson',
'https://jojo.fandom.com/wiki/Oyecomova',
'https://jojo.fandom.com/wiki/Sugar_Mountain',
'https://jojo.fandom.com/wiki/Scarlet_Valentine',
'https://jojo.fandom.com/wiki/Jesus',
'https://jojo.fandom.com/wiki/Gregorio_Zeppeli',
'https://jojo.fandom.com/wiki/George_Joestar_I_(Steel_Ball_Run)',
'https://jojo.fandom.com/wiki/Nicholas_Joestar',
'https://jojo.fandom.com/wiki/Marco',
'https://jojo.fandom.com/wiki/Josuke_Higashikata_(JoJolion)',
'https://jojo.fandom.com/wiki/Yasuho_Hirose',
'https://jojo.fandom.com/wiki/Rai_Mamezuku',
'https://jojo.fandom.com/wiki/Joshu_Higashikata',
'https://jojo.fandom.com/wiki/Tsurugi_Higashikata',
'https://jojo.fandom.com/wiki/Norisuke_Higashikata_IV',
'https://jojo.fandom.com/wiki/Daiya_Higashikata',
'https://jojo.fandom.com/wiki/Hato_Higashikata',
'https://jojo.fandom.com/wiki/Jobin_Higashikata',
'https://jojo.fandom.com/wiki/Mitsuba_Higashikata',
'https://jojo.fandom.com/wiki/Kaato_Higashikata',
'https://jojo.fandom.com/wiki/Kyo_Nijimura',
'https://jojo.fandom.com/wiki/Yoshikage_Kira_(JoJolion)',
'https://jojo.fandom.com/wiki/Josefumi_Kujo',
'https://jojo.fandom.com/wiki/Karera_Sakunami',
'https://jojo.fandom.com/wiki/Holy_Joestar-Kira',
'https://jojo.fandom.com/wiki/Tamaki_Damo',
'https://jojo.fandom.com/wiki/Yotsuyu_Yagiyama',
'https://jojo.fandom.com/wiki/Aisho_Dainenjiyama',
'https://jojo.fandom.com/wiki/A._Phex_Brothers',
'https://jojo.fandom.com/wiki/Dolomite',
'https://jojo.fandom.com/wiki/Urban_Guerrilla',
'https://jojo.fandom.com/wiki/Doremifasolati_Do',
'https://jojo.fandom.com/wiki/Poor_Tom',
'https://jojo.fandom.com/wiki/Wu_Tomoki',
'https://jojo.fandom.com/wiki/Satoru_Akefu',
'https://jojo.fandom.com/wiki/Tooru',
'https://jojo.fandom.com/wiki/Ojiro_Sasame',
'https://jojo.fandom.com/wiki/Suzuyo_Hirose',

]


csv_file = open('jojobigtest.csv','w')

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