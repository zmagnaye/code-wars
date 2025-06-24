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