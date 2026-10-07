# Task 1
def hello():
    return "Hello!"
# Task 2
def greet(name):
    return f"Hello, {name}!"
# Task 3
def calc(val1, val2, operation="multiply"):
    try:
        if operation == "add":
            return val1 + val2
        elif operation == "subtract":
            return val1 - val2
        elif operation == "multiply":
            return val1 * val2
        elif operation == "divide":
            return val1 / val2
        elif operation == "modulo":
            return val1 % val2
        elif operation == "power":
            return val1 ** val2
        elif operation == "int_divide":
            return val1 // val2

    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

# Task 4
def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)

    except ValueError:
        return f"You can't convert {value} into a {data_type}."

    # Task 5
def grade(*args):
        try:
            average = sum(args) / len(args)

            if average >= 90:
                return "A"
            elif average >= 80:
                return "B"
            elif average >= 70:
                return "C"
            elif average >= 60:
                return "D"
            else:
                return "F"

        except TypeError:
            return "Invalid data was provided."


def repeat(str, count):
    result = ""

    for _ in range(count):
        result += str
    return result

# Task 7
def student_scores(operation, **kwargs):
    if operation == "mean":
        return sum(kwargs.values()) / len(kwargs)
    elif operation == "best":
        return max(kwargs, key=kwargs.get)
# Task 8 
def titleize(string):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = string.split()
    result = []

    for index, word in enumerate(words):
        if index == 0 or index == len(words) - 1:
            result.append(word.capitalize())
        elif word in little_words:
            result.append(word.lower())
        else:
            result.append(word.capitalize())

    return " ".join(result)

# Task 9

def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"

    return result

# Task 10

def pig_latin(string):
    vowels = "aeiou"
    words = string.lower().split()
    result = []

    for word in words:
        if word[0] in vowels:
            new_word = word + "ay"
        else:
            index = 0

            while index < len(word) and word[index] not in vowels:
                if word[index:index + 2] == "qu":
                    index += 2
                    break
                index += 1

            new_word = word[index:] + word[:index] + "ay"
        result.append(new_word)
    return" ".join(result)