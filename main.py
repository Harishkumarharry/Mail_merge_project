with open("Input/Names/invited_names.txt", 'r') as names:
    list_of_names = names.readlines()

with open("Input/Letters/starting_letter.txt", 'r') as letters:
    letter = letters.read()

for list_of_name in range(len(list_of_names)):
    final_letter = letter.replace("[name]", list_of_names[list_of_name].strip())
    letter_name = "Output/ReadyToSend/letter_for_" + list_of_names[list_of_name].strip()
    with open(f"{letter_name}", 'w') as ready_to_send:
        ready_to_send.write(final_letter)
