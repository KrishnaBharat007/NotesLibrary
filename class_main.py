from class_user_interface import UserInterface as UI
from time import sleep

#Main Class: Used to awaken the program and provides user menu to interact with other classes.
class Main:
    #Invokes program to interact with UserInterface class and perform desired operations.
    def main():
        print("Welcome to My Notes Library!")
        while True:
            print("\n",\
        "Select an option from below menu.\n",\
        " 1. Create or add a new Note.\n",\
        " 2. Read existing Note.\n",\
        " 3. Update existing Note.\n",\
        " 4. Delete existing Note.\n",\
        " 5. Show existing Note Details.\n",\
        " 6. Add Note Completion Date. \n",\
        " 7. Note Completion Time. \n",\
        " 8. Save notes to file. \n",\
        " 9. Load notes from file. \n",\
        " 0. Exit",sep = '')
            sleep(0.5)
            action = input('Enter your option: ')
            if action not in ['1','2','3','4','5','6','7','8','9','0']:
                print('Oops! You have entered an invalid option')
                continue
            UI.create_note() if action == '1' else \
            UI.read_note() if action == '2' else \
            UI.update_note() if action == '3' else \
            UI.delete_note() if action == '4' else \
            UI.note_details() if action =='5' else \
            UI.add_completion_date() if action == '6' else \
            UI.note_completion_time() if action =='7' else \
            UI.save_to_file() if action =='8' else \
            UI.load_from_file() if action =='9' else ''
            if action == '0':
                exit_check = UI.exit_ui()
                if exit_check == 'exit':
                    break

Main.main()