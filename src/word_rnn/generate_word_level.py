import subprocess

from os import listdir
from os.path import isfile, join


path = 'models/'
output_path = 'results/'
files = [f for f in listdir(path) if isfile(join(path, f))]
print("Generating samples for {} models".format(len(files)))
for fname in files:
    output =  output_path + fname.replace('.pt', 'txt')
    print("Generating output for {}. Saving to {}".format(fname, output))
    subprocess.call(['python', 'generate.py', 
                     '--data', 'data/trump',
                     '--outf', output,
                     '--checkpoint', path + fname,
                     '--cuda'])
