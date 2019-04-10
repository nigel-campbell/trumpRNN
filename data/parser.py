tweets = ['2013.txt', '2014.txt', '2015.txt', '2016.txt', '2017.txt', '2018.txt', '2019.txt']

data = []
for txt in tweets:
	with open(txt, 'r') as f:
		data.append(f.readlines())

for txt in data:
	for i, line in enumerate(txt):
		http_index = line.find('http')
		if http_index == 0:
			txt[i] = ''
		elif http_index != -1:
			txt[i] = line[:http_index - 1]

#pointless
repeated = 1

with open('fulldata.txt', 'w') as f:
	for _ in range(repeated):
		for txt in data:
			for tweet in txt:
				f.write(tweet.replace('\n', ' ').replace('  ', ' '))
