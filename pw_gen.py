from string import ascii_letters, digits, punctuation
from random import sample
params = ascii_letters + digits + punctuation

def GeneratePassword(len = 5):
    return "".join(sample(params, len))