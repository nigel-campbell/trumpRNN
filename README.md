# trumpRNN

The current, 45th president of the United States Donald J. Trump is known to be a frqeuent tweeter. He also tweets with mistakes/misspellings (e.g. hamberders), and with a colloquial tone that's iconic and rather unique. 

Given the wealth of data and prominent position as the president of USA, it'd be fun to use Deep Learning to create "fake Trump". 

We will use archived version of Trump's tweets from 2013-2019 as the input data. 
We will use RNN (LSTM/GRU) as the basis of the model. 

Finally, for evaluation, we will use a similairty index to compare how close our "fake tweets" are to the actual tweets. 

Trains model:

```
usage:
python train.py shakespeare.txt

Usage: train.py [filename] [options]

Options:
--model            Whether to use LSTM or GRU units    gru
--n_epochs         Number of epochs to train           2000
--print_every      Log learning rate at this interval  100
--hidden_size      Hidden size of GRU                  50
--n_layers         Number of GRU layers                2
--learning_rate    Learning rate                       0.01
--chunk_len        Length of training chunks           200
--batch_size       Number of examples per batch        100
--cuda             Use CUDA
```

Generates tweets:

```
python generate.py shakespeare.pt --prime_str "Where"

Usage: generate.py [filename] [options]

Options:
-p, --prime_str      String to prime generation with
-l, --predict_len    Length of prediction
-t, --temperature    Temperature (higher is more chaotic)
--cuda               Use CUDA
```

Similarity measure:

```
python similarity.py \
--text "Sir Walter Elliot, of Kellynch Hall, in Somersetshire, was a man who, for his own amusement, never took up any book but the Baronetage; there he found occupation for an idle hour" \
--checkpoint checkpoints/austen_checkpoint.cp \
--charfile data/austen_chars.pkl 
```

