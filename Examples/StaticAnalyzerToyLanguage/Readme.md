# Usage
There three different type of data encodings used, byte code, ascii arrays and sequence embedding. For each type of encoding a preprocess script is used to preprocess the data into a usable format.

## Byte code

The script preprocess_data.py is used to convert the training samples into byte code. The script receivers as parameter two directories which contain the valid and non valid samples and an output file name that will contain the encoded data. The output file can be fed to the script train.py or train_keras.py on the data. Note that all three scripts contain a variable max_length which needs to be the same in all scripts. max_length must bigger then the size of the biggest training sample in encoded form.

## Ascii arrays

The script preprocess_data_string.py is used to convert the training samples into ascii arrays. The script receivers as parameter two directories which contain the valid and non valid samples and an output file name that will contain the encoded data. The output file can be fed to the script train.py or train_keras.py to train on the data. Note that all three scripts contain a variable max_length which needs to be the same in all scripts. max_length must bigger then the size of the biggest training sample in encoded form.

## Sequence embedding

The script preprocess_data_seq_embed.py is used to convert the training samples into sequences. The script receivers as parameter two directories which contain the valid and non valid samples and an output file name that will contain the encoded data. The output file can be fed to the script train_seq_embed. Note that both scripts contain a variable max_length which needs to be the same in all scripts. max_length must bigger then the size of the biggest training sample in encoded form.