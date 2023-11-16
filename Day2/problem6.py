import re


def is_pangram(my_str):
    return all(re.search(letter, my_str) for letter in 'abcdefghijklmnopqrstuvwxyz')


my_str = "The quick brown fox jumps over the lazy dog"
# my_str = "this Is a sample text"
result = is_pangram(my_str)
print(result)
if result:
    print(f"{my_str} is a pangram.")
else:
    print(f"{my_str} is not a pangram.")
