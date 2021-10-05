import requests

localBaseAddress = '/Users/Shu/Desktop/pokemon_images/'
baseUrl = 'https://assets.pokemon.com/assets/cms2/img/pokedex/full//'

for x in xrange(1,152):
	filename = ''
	if x<10 :
		filename = '00'+str(x)+'.png'
	if x>=10 and x<100:
		filename = '0'+str(x)+'.png'
	if x>=100:
		filename = str(x)+'.png'

		
	url = baseUrl+filename
	fileAddress = localBaseAddress+str(x)+'.png'
	r = requests.get(url, allow_redirects=True)
	open(fileAddress, 'wb').write(r.content)
	
