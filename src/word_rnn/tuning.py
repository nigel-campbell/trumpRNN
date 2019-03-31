import subprocess


data = './data/trump'
models = ['LSTM', 'GRU']
em_sizes = [50, 100, 200]  # Word embedding
hidden_layers = [50, 100, 500]
n_layers = [2, 5, 10]
epochs = [6, 40, 100]
dropout = [0.0, 0.2]

count = 0
for model in models:
    for em_size in em_sizes:
        for nhidden in hidden_layers:
            for layer_count in n_layers:
                for epoch_count in epochs:
                    for dropout_count in dropout:
                        output_file = '{}_{}_{}.pt'.format(model, \
                                em_size, n_hidden, layer_count, \
                                epoch_count, dropout_count)
                        subprocess.call(['python', 'main.py',
                                         '--data', 'data/trump/',
                                         '--models', model,
                                         '--emsize', str(em_size),
                                         '--nhid', str(nhidden),
                                         '--nlayers', str(layer_count),
                                         '--epochs', str(epoch_count),
                                         '--dropout', str(dropout_count),
                                         '--save', output_file,
                                         '--cuda' ])
