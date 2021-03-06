'''doc'''

# End of Sentence, and Padding
START_TOKEN = '\t'
END_TOKEN = '\n'
PAD_TOKEN = '<pad>'

#
# Reference to https://pytorch.org/tutorials/beginner/chatbot_tutorial.html#run-model
#
EMBEDDING_DIM = 512
RNN_UNIT_NUM = 512
DROPOUT_RATE = 0.2

BATCH_SIZE = 64
LEARNING_RATE = 3e-3

# max words per sentence
MAX_LEN = 10
