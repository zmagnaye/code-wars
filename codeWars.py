# Solution for Even or Odd:
def even_or_odd(number):
    return "Even" if (number % 2 == 0) else "Odd"

# Solution for Convert a Number to a String
def number_to_string(num):
    return str(num)

# Solution for Remove String Spaces
def no_space(x):
    final_string = "".join(x.split())
    return final_string

# Solution for Vowel Count
def get_count(sentence):
    vowels = "aeiou"
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count