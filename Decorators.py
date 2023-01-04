#You are given code that takes input and prints it as a simple row of text.

#Add the uppercase_decorator to make the text uppercase.
#The upper() method can be used on strings to make them uppercase.

text = input()


def uppercase_decorator(func):
    def wrapper(text):
        return func(text).upper()

    return wrapper


@uppercase_decorator
def display_text(text):
    return (text)


print(display_text(text))