import requests


cities = ['london', 'svo', 'Череповец'] 
url_template = 'https://wttr.in/{}'
payload = {"mMnTqu": "", "lang":"ru"}


def main:
	for city in cities:
		url = url_template.format(city)	
		response = requests.get(url, params=payload)
		response.raise_for_status()
		print(response.text) 


if __name__ == '__main__'
	main()