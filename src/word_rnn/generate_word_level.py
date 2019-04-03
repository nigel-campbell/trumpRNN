import subprocess

from os import listdir
from os.path import isfile, join


path = 'models/'
files = [f for f in listdir(path) if isfile(join(path, f))]
print("Generating samples for {} models".format(len(files)))
for fname in files:
    outf = fname[:len(files)-2]
    print("Generating output for {}. Saving to {}".format(fname, outf))
    subprocess.call(['python', 'generate.py', 
                     '--data', 'data/trump',
                     '--outf', outf,
                     '--checkpoint', path + fname,
                     '--cuda'])
