import os

def write_on_specific_line(file_path, line_number, new_content):

    lines = []
    # Lire toutes les lignes du fichier
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    
    # Modifier la ligne souhaitée
    if line_number < len(lines):
        lines[line_number] = new_content + '\n'
    
    # Réécrire le fichier avec les modifications
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def run() -> None:
    PATH = ''
    print('start converting')
    for filename in os.listdir(PATH):
        f = os.path.join(PATH, filename)
        print(f)
        # checking if it is a file
        if os.path.isfile(f):
            write_on_specific_line(f, 575, "chat.type.announcement=§cYou cannot use this interaction !	#")
            write_on_specific_line(f, 1092, "commands.message.display.incoming=#")
            write_on_specific_line(f, 1093, "commands.message.display.outgoing=§cYou cannot use this interaction !	#")

# Appeler la fonction run pour démarrer le processus
run()
