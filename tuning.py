import subprocess

n_epochs = [500, 1000, 2000, 3000]
hidden_size = [128, 256, 512, 1028]
learning_rate = [0.0001, 0.001, 0.01, 0.1]
chunk_len = [50, 100, 150]
batch_size = [50, 100, 150, 200]

for epoch in n_epochs:
    for hidden in hidden_size:
    	for lr in learning_rate:
    	    for chunk in chunk_len:
		for batch in batch_size:
		    subprocess.call(['python', 'src/char_rnn/train.py', 
						'data/full_dataset.txt', 
						'--n_epochs', str(epoch),
						'--hidden_size', str(hidden), 
						'--learning_rate', str(lr), 
						'--chunk_len', str(chunk), 
						'--batch_size', str(batch),
						'--cuda'])
