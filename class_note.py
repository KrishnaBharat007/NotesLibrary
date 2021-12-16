#Note Class : Used for creating note instances based on the schema defined in note class
class Note:
    cntr = 0
    note_id_list = []
    
    #Constructor method used to define required attributes
    def __init__(self, dt_created, title, text, completion_status, dt_completed = ''):
        self.__date_created = dt_created
        self.__title = title
        self.__text = text
        self.__completed = completion_status
        self.__date_completed = dt_completed
        self.__id = Note.cntr + 1
        Note.note_id_list.append(self.__id)
        Note.set_cntr()

    #Method used for incremental operation of the counter value used for generating ID
    def set_cntr():
        Note.cntr +=1

    #Method enables user to update note creation date
    def set_date_created(self, dt_created):
        self.__date_created = dt_created

    #Method enables user to fetch note creation date
    def get_date_created(self):
        return self.__date_created

    #Method enables user to update note title
    def set_title(self, title):
        self.__title = title

    #Method enables user to fetch note title
    def get_title(self):
        return self.__title

    #Method enables user to update note text
    def set_text(self, text):
        self.__text = text

    #Method enables user to fetch note text
    def get_text(self):
        return self.__text

    #Method enables user to update note completion status
    def set_completed(self, completion_status):
        self.__completed = completion_status

    #Method enables user to fetch note completion status
    def get_completed(self):
        return self.__completed

    #Method enables user to update note completion date
    def set_date_completed(self, dt_completed):
        self.__date_completed = dt_completed

    #Method enables user to fetch note completion date
    def get_date_completed(self):
        return self.__date_completed

    #Method enables user to fetch note id
    def get_id(self):
        return self.__id
    
    #Method enables user to assign note id (Used only for loading notes from file)
    def set_id(self, note_id):
        self.__id = note_id
    
    #Method enables user to fetch combined details of note
    def get_note_info(self):
        note_data = (str(self.__id) + ',' + str(self.__date_created) + ',' + \
            self.__title + ',' + self.__text + ',' + str(self.__completed) + \
            ',' + str(self.__date_completed))
        return note_data

    #Method enables user to fetch note information for user display.
    def __str__(self):
        note_info =  "Note Id \t\t\t:"+ str(self.__id) +\
                    "\nNote Created on \t\t:" + str(self.__date_created) +\
                    "\nTitle of Note \t\t\t:" + self.__title +\
                    "\nText of Note \t\t\t:" + self.__text +\
                    "\nNote Completion Status \t\t:" + \
                    (('Complete' +\
                      '\nNote Completed on \t\t:'+str(self.__date_completed)) \
                            if self.__completed else 'Incomplete')
        return note_info
