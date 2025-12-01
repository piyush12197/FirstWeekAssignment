def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s


# Example usage
print(reverse_string("hello"))  # "olleh"
