def display_in_a_box(word):
    dash = 4 + (len(word))
    print("-" * dash)
    print(f"| {word} |")
    print("-" * dash)

def display_lower_case(word):
    return word.lower()

def display_upper_case(word):
    return word.upper()

def reverse_word(word):
    reverse = word[::-1] #to reverse a string
    sentence = f"{word} | {reverse}"
    return sentence

def repeat(word):
    num = int(input("How many times do you want to display this word?"))
    if num % 2 == 0:
        print({display_upper_case(word ) * num})
    else:
        print(display_lower_case(word) * num)


repeat("umbrella")