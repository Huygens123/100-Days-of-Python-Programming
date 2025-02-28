# TODO: Create a letter using starting_letter.txt for each name in invited_names.txt

with open("input/Letters/starting_letter.txt", 'r') as file:
    letter = file.read()

with open("input/Names/invited_names.txt", 'r') as file:
    invited_names = file.readlines()
    names_cleaned = []
    for name in invited_names:
        names_cleaned.append(name.strip('\n'))

print(names_cleaned)

for name in names_cleaned:
    ready_to_send = (letter.replace('[name]', name))
    with open(f"./Output/ReadyToSend/letter_to_{name}", 'w') as file:
        file.write(ready_to_send)
        print(ready_to_send)
