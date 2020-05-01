import downloads

STATE_MENU = 0
STATE_DOWNLOADCHAR = 1
appstate = STATE_MENU

while True:
    if appstate == STATE_MENU:
        print("=== MAIN MENU ===\nSelect an option:\n\n1 - Download a character\n2 - Exit")
    elif appstate == STATE_DOWNLOADCHAR:
        print("=== DOWNLOAD A CHARACTER ===\nEnter the name of the AO character you wish to download.\nTo download multiple characters, separate them by commas: \"Klavier, Phoenix, Apollo\"\nEnter \"back\" to return to the main menu.")
    
    choice = input("> ")
    
    if appstate == STATE_MENU:
        if choice == "1":
            appstate = STATE_DOWNLOADCHAR
        elif choice == "2":
            break
        else:
            continue

    elif appstate == STATE_DOWNLOADCHAR:
        if choice.lower() == "back":
            appstate = STATE_MENU
        else:
            chars = choice.split(", ")
            for char in chars: downloads.downloadChar(char)
