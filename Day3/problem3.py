'''
List of all words starting with A.
'''
sample_string = "Apples are always a favorite among adventurous anteaters."
sample_string_sliced = sample_string.split(" ")
for x in sample_string_sliced:
    if x.startswith("a"):
        print(x)
