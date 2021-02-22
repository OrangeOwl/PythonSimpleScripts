import random

messages = ['yes', 'no', 'never', 'ask again later', 'big oof']
# Print the Messages variable, with a random integer range from 0 to the length of messages -1 (since lists start at 0)
print(messages[random.randint(0, len(messages)-1)])


