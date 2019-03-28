import subprocess
import glob
import re

list_of_models = glob.glob("../models/*")

#per model, generate n lines of output
lines = 50
tweet_length = 140

for model in list_of_models:
	output = re.search('models/(.+?).pt', model).group(1) + '.out'
	subprocess.call(['python', '../src/char_rnn/generate.py', 
					model, 
					'--predict_len', str(tweet_length),
					'--num', str(lines),
					'--output', output,
					'--cuda'])

