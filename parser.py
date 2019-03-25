tweets = ['2013.txt', '2014.txt', '2015.txt', '2016.txt', '2017.txt', '2018.txt']

data = []
for txt in tweets:
	with open(txt, 'r') as f:
		data.append(f.readlines())

for txt in data:
	for i, line in enumerate(txt):
		http_index = line.find('http')
		if http_index != -1:
			txt[i] = line[:http_index - 1]

with open('fulldata.txt', 'w') as f:
	for txt in data:
		f.writelines(txt)



# 		with open('2020.txt', 'w') as g:
# 			for line in f:
# 				http_index = line.find('http')
# 				if http_index != -1:
# 					line = line[:http_index - 1] + '\n'
# 				g.write(line)

# with open('2020.txt', 'r+') as f:
# 	for line in f:
# 		print(line)
# 		http_index = line.find('http')
# 		if http_index != -1:
# 			line = line[:http_index - 1] + '\n'
# 		f.write(line)
# 	