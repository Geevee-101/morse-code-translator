from art import logo

morse_code_dict = {
    "A": "._",
    "B": "_...",
    "C": "_._.",
    "D": "_..",
    "E": ".",
    "F": ".._.",
    "G": "__.",
    "H": "....",
    "I": "..",
    "J": ".___",
    "K": "_._",
    "L": "._..",
    "M": "__",
    "N": "_.",
    "O": "___",
    "P": ".__.",
    "Q": "__._",
    "R": "._.",
    "S": "...",
    "T": "_",
    "U": ".._",
    "V": "..._",
    "W": ".__",
    "X": "_.._",
    "Y": "_.__",
    "Z": "__..",
    "1": ".____",
    "2": "..___",
    "3": "...__",
    "4": "...._",
    "5": ".....",
    "6": "_....",
    "7": "__...",
    "8": "___..",
    "9": "____.",
    "0": "_____"
}


def verify_menu_number(choice):
    number_valid = False
    number_is_number = False

    while not number_valid:
        while not number_is_number:
            try:
                choice = int(choice)
            except ValueError:
                choice = input("That was not a number. Please try again: ")
            else:
                number_is_number = True

        if choice < 1 or choice > 2:
            choice = input("Only option 1 or 2 is available. Please try again: ")
            number_is_number = False
        else:
            number_valid = True
    return choice


def verify_input(input_txt):
    input_txt_valid = False

    while not input_txt_valid:
        while not input_txt or input_txt.isspace():
            print("Input empty. Only letters and positive integers are accepted.")
            input_txt = input("Please try again: ")

        input_txt_valid = True
        input_txt_check = input_txt.replace(" ", "").upper()
        for letter in input_txt_check:
            if letter not in morse_code_dict:
                input_txt_valid = False
                print("Invalid input. Only letters and positive integers are accepted.")
                input_txt = input("Please try again: ")
                break

    return input_txt


# Ask for input to convert message
def text_to_morse_code(input_word):
    input_word = input_word.upper()
    translated_input = []
    for i in input_word:
        for key in morse_code_dict:
            if i == key:
                translated_input.append(morse_code_dict[key])
    return translated_input


def morse_code_translator():
    print("\nNote: Only letters and positive integers are accepted. Sentences are also accepted.")
    input_text = input("Text to translate into morse code: ")

    input_text = verify_input(input_text)
    input_text = input_text.split()

    for text in input_text:
        translated_text = text_to_morse_code(text)
        print(f"\nThe text '{text}' in morse code is:")
        list_length = len(translated_text)
        for letter in translated_text:
            list_length = list_length - 1
            if list_length == 0:
                print(f"{letter}")
            else:
                print(f"{letter}", end=" / ")


# main
print(logo)
print("\nA morse code translator program by Aidi Khalid")
repeat = True
while repeat:
    morse_code_translator()
    menu_3 = "\n1. Translate another text\n2. Exit"
    print(menu_3)
    run_again = input("Select 1 or 2: ")
    run_again = verify_menu_number(run_again)
    if run_again == 1:
        continue
    else:
        repeat = False
