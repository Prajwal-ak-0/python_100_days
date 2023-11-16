with open("./Input/Names/invited_names.txt", "r") as file:
    names = file.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as file:
    content_template = file.read()

for name in names:
    content = content_template.replace("[name]", name.strip())
    file_path = f"./Output/ReadyToSend/{name.strip()}.txt"
    with open(file_path, 'w') as output_file:
        output_file.write(content)
