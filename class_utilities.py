from class_note import Note

from datetime import date
from time import sleep

#Utilities Class: Used for providing methods required for performing few operations 
#                 required by User Interface class.
class Utilities:
    def __init__(self):
        pass
    #Method helps to validate if given note id is a valid idor not.
    def validate_id():
        if(len(Note.note_id_list)==0) :
            print("No Notes present in My Notes Library!")
        else :
            while True:
                print("List of existing Note Id's:\n", Note.note_id_list)
                try:
                    read_id = int(input('Enter Note Id: '))
                    index = Note.note_id_list.index(read_id)
                    break
                except:
                    print("Sorry! Entered Note Id does not exist")
            return index
    
    #Method provides a menu if you wish to update all fields or required fields only
    def validate_update_option():
        while True:
            try:
                print("\nSelect an option from below menu.\n"\
                      "1. Update all details in a note\n"\
                      "2. Update Creation date of the note\n"\
                      "3. Update Title of the note\n"\
                      "4. Update Text in the note\n"\
                      "5. Update Completion status of note\n"\
                      "6. Update Completion date of the note")
                option = int(input("Enter your Option:"))
                if option in [1,2,3,4,5,6]:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Oops! You have entered invalid option")
        return option
    
    #Method helps to update create date and completion date and validate
    #user input and check its format.
    def validate_date():
        while True:
            ind = input("Select an option from below.\n"\
                        "1. Today's date.\n"\
                        "2. Specify desired date.\n"\
                        "Enter your option [1/2]: ")
            if ind == '1':
                return date.today()
            elif ind == '2':
                dt = input('Please enter date in YYYY-MM-DD format:')
                while True:
                    try:
                        year,month,day = map(int,dt.split('-'))
                        dt = date(year,month,day)
                        if dt > date.today():
                            raise ValueError
                        else:
                            break
                    except ValueError:
                        print("Given Date should not be beyond today's date")
                        sleep(1)
                        dt = input('Please enter a valid date in YYYY-MM-DD format:')
                    except:
                        print('Oops! You have entered an invalid date value.')
                        sleep(1)
                        dt = input('Please enter a valid date in YYYY-MM-DD format:')
                return dt
            else:
                print('Opps! You have given an invalid input.')
            sleep(1)

    #Method converts sring date to date datatype while reading from file.
    def convert_to_date(dt):
        year,month,day = map(int,dt.split('-'))
        dt = date(year,month,day)
        return dt

    #Method used for updating values of fields stored in a note using the set methods
    def update_note_info(obj,opt):
        def update_title():
            return input('Enter new title to the note: ')
        
        def update_text():
            return input("Enter text to be stored in the note: ")
        
        def update_dt():
            return Utilities.validate_date()
        
        def update_completion_status():
            while True:
                try:
                    val = input("Is the note Complete? [Yes/No] : ").lower()
                    if val in ['yes','no']:
                        break
                    else:
                        raise Exception
                except:
                    print("Please enter only Yes or No")
            return True if(val == 'yes') else False
        
        def validate_completion_dt(obj):
            if Note.get_completed(obj):
                return 'Invalid' if \
                    Note.get_date_created(obj) > Note.get_date_completed(obj)\
                        else 'Valid'
                
         
        if opt == 2:
            Note.set_date_created(obj, update_dt())
            if validate_completion_dt(obj) == 'Invalid':
                print("You have updated creation date of the note.\n"\
    "Please update its completion date as current completion date is older than latest creation date.")
                Utilities.update_note_info(obj,6)
        elif opt == 3:
            Note.set_title(obj, update_title())
        elif opt == 4:
            Note.set_text(obj, update_text())
        elif opt == 5:
            status = update_completion_status()
            Note.set_completed(obj, status)
            if status:
                print("You have updated that note is completed.\n"\
                      "Please also update its completion date")
                Utilities.update_note_info(obj,6)
        elif opt == 6:
            if Note.get_completed(obj):
                while True:
                    try:
                        dt = update_dt()
                        if dt >= Note.get_date_created(obj):
                            Note.set_date_completed(obj, dt)
                            break
                        else:
                            raise Exception
                    except:
                        print("Completion Date should not not be a date before creation date")
            else:
                Note.set_date_completed(obj, False)
                print("This note is not yet complete.\n"\
                      "Please update Note Completion Status to update completion date")
        else:
            print("Update Create date of note")
            Note.set_date_created(obj, update_dt())
            Note.set_title(obj, update_title())
            Note.set_text(obj, update_text())
            Note.set_completed(obj, update_completion_status()) 
            if Note.get_completed(obj):
                print("\nYou have updated that note is completed.\n"\
                      "Please also update its completion date")
                while True:
                    try:
                        dt = update_dt()
                        if dt >= Note.get_date_created(obj):
                            Note.set_date_completed(obj, dt)
                            break
                        else:
                            raise Exception
                    except:
                        print("Completion Date should not not be a date before creation date")
            else:
                Note.set_date_completed(obj, False)
            
        if validate_completion_dt(obj) == 'Invalid':
                Utilities.update_note_info(obj,6)