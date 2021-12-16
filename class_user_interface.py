from class_note import Note
from class_utilities import Utilities
from datetime import date

#UserInterface Class: Used to perform key operations like adding, updating,
#                     removing valus in note and enables user interaction with program.
class UserInterface:
    note_list = []
    
    def __init__(self):
        pass
    #Method is used to create new note instance and adds it to list storing note objects.
    def create_note():
        dt_created = date.today()
        title = input("Let's give a title to our new note.\n")
        text = input("Please input the content of this note:\n")
        completion_status = UserInterface.note_status()
        dt_completed = dt_created if completion_status else ''
        note = Note(dt_created,title,text,completion_status,dt_completed)
        UserInterface.note_list.append(note)
        print('Hurray! Note is created and added to My Notes Library')
        
    #Method checks if any notes are existing and lets the user view information
    #stored in the note based on note id
    def read_note():
        index = Utilities.validate_id()
        if index != None:
            print(UserInterface.note_list[index].__str__())
        
    #Method checks if any notes are existing and lets the user update values 
    #stored in the note based on note id
    def update_note():
        index = Utilities.validate_id()
        if index != None:
            note_obj = UserInterface.note_list[index]
            option = Utilities.validate_update_option()
            Utilities.update_note_info(note_obj,option)

    #Method checks if any notes are existing and lets the user delete notes  
    #based on note id also updates note id list in of note class and object list in UI
    def delete_note():
        index = Utilities.validate_id()
        if index != None:
            note_obj = UserInterface.note_list[index]
            Note.note_id_list.remove(Note.get_id(note_obj))
            UserInterface.note_list.remove(note_obj)
        
    #Exits completely from the program
    def exit_ui():
        while True:
            print("\nSelect an option to exit\n",
              "1. Save & Exit\n",
              "2. Exit without saving.")
            opt = input("Enter your option: ")
            if opt == '1' :
                UserInterface.save_to_file()
                break
            elif opt == '2' :
                break
            else :
                print('Invalid option')
        print("Thanks for using My Notes Library!")
        return 'exit'
            
    #Method helps to display number of notes created, percentage of notes incomeplete
    #Also displays all notes based on users request.
    def note_details():
        if(len(Note.note_id_list)==0) :
            print("No Notes present in My Notes Library!")
        else :
            print("Number of notes created:",len(Note.note_id_list))
            print("Percentage of notes which are Incomplete:",\
                  100 - UserInterface.percentage_completion(),'%' )
            while True:
                try:
                    flag = input("View all existing notes? [Yes/No] :").lower()
                    if flag in ['yes','no']:
                        break
                    else:
                        raise Exception
                except:
                    print("Please enter only Yes or No")
            if flag =='yes':
                for i in UserInterface.note_list:
                    print(i.__str__(),'\n')
            
    #Method helps to define completion status of note
    def note_status():
        while True:
            status = input("Select option to define completion status of note.\n"\
                           "1. Incomplete.\n"\
                           "2. Complete.\n"\
                           "Enter your desired option: ")
            if status not in ['1','2']:
                print('Opps! You have given an invalid input.\n')
            else:
                return True if status == '2' else False

    #Method helps to calculate how much percentage of notes are note yet complete.
    def percentage_completion():
        val = 0
        for note in UserInterface.note_list:
            if Note.get_completed(note):
                val += 1
        percentage = round((val*100)/len(UserInterface.note_list),2)
        return percentage

    #Method helps to allow user to update note completion date from user menu options.
    def add_completion_date():
        index = Utilities.validate_id()
        if index != None:
            note_obj = UserInterface.note_list[index]
            Utilities.update_note_info(note_obj,6)

    #Method helps to calculate number of days taken to finish the note.
    def note_completion_time():
        index = Utilities.validate_id()
        if index != None:
            note_obj = UserInterface.note_list[index]
            if Note.get_completed(note_obj):
                num = Note.get_date_completed(note_obj) - Note.get_date_created(note_obj)
                print("Number of days taken to complete note: ", num.days +1)
            else:
                print("Sorry! This note is not yet complete.")

    #Method helps to save all the notes created into a file.
    def save_to_file():
        if len(UserInterface.note_list) != 0 :
            file = open("MyNotesLibrary.txt","w")
            for note in UserInterface.note_list:
                note_info = Note.get_note_info(note)
                file.write(note_info + '\n')
            print("All notes saved successfully!")
        else:
            print("No Notes present in My Notes Library!")
        
    #Method helps to load all the notes created earlier from file into memory.
    def load_from_file():
        id_list = []
        try:
            file = open("MyNotesLibrary.txt","r")
        except:
            print("Oops! File not present.")
            return None
        for note_obj in file:
            note_obj = note_obj.replace('\n','')
            note = note_obj.split(',')
            note_id = int(note[0])
            id_list.append(note_id)
            dt_created = Utilities.convert_to_date(note[1])
            if len(note[5]) == 10:
                dt_completed = Utilities.convert_to_date(note[5])
            else:
                dt_completed = ''
            status = True if note[4] =='True' else False
            obj = Note(dt_created, note[2], note[3], status, dt_completed)
            Note.set_id(obj, note_id)
            UserInterface.note_list.append(obj)
        Note.note_id_list = id_list
        Note.cntr = max(Note.note_id_list)