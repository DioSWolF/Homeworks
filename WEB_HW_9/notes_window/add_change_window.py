from datetime import datetime
from tkinter import *
from .class_notes import TextNote, KeyWords, Article, Notes, NotesSave, DateNote

#********************************** Window config ****************************    


def article_field(notes_form, read_flag = None, new_notes_flag=None):
    global ent_article
    if read_flag == None:
        ent_article = Entry(master=notes_form, width=47)
        ent_article.insert(0, notes_save[find_article].article.value) 
        ent_article.configure(state='disabled')
    elif new_notes_flag=="":
        ent_article = Entry(master=notes_form, width=47)

        btn_article_insert = Button(master=notes_form, width=11, text="Save", command=getArticleInput)
        btn_article_insert.grid(row=0, column=2)
        btn_articlet_delete = Button(master=notes_form, width=11, text="Clean text", command=delete_article)
        btn_articlet_delete.grid(row=0, column=4)


    else:   
        ent_article = Entry(master=notes_form, width=47)

        btn_article_recover = Button(master=notes_form, width=11, text="Restore", command=artical_return_text)
        btn_article_insert = Button(master=notes_form, width=11, text="Save", command=getArticleInput)
             
        btn_article_insert.grid(row=0, column=2)
        btn_article_recover.grid(row=0, column=3)
   
    lbl_article = Label(master=notes_form, text="Article:")

    try:
        ent_article.insert(0, notes_save[find_article].article.value) 
    except KeyError:
        pass

    lbl_article.grid(row=0, column=0, sticky="e")
    ent_article.grid(row=0, column=1)


def text_fiel(notes_form, read_flag = None,  new_notes_flag=None):
    global text_form
    if read_flag == None:
        text_form = Text(master=notes_form, width=35, height=15)
        text_form.insert("1.0", notes_save[find_article].text_note.value) 
        text_form.configure(state='disabled')
    elif new_notes_flag == "":

        btn_text_insert = Button(master=notes_form, width=11, text="Save", command=getArticleInput)
        btn_text_delete = Button(master=notes_form, width=11, text="Clean text", command=delete_text)
        btn_text_insert.grid(row=2, column=2)
        btn_text_delete.grid(row=2, column=4)

    else:   
        btn_text_recover = Button(master=notes_form, width=11, text="Restore", command=text_return_text)
        btn_text_insert = Button(master=notes_form, width=11, text="Save", command=getTextInput)
        btn_text_delete = Button(master=notes_form, width=11, text="Clean text", command=delete_text)
        btn_text_insert.grid(row=2, column=2)
        btn_text_recover.grid(row=2, column=3)
        btn_text_delete.grid(row=2, column=4)

    text_form = Text(master=notes_form, width=35, height=15)

    text_lbl = Label(master=notes_form, text="Notes:")
    
    try:
        text_form.insert("1.0", notes_save[find_article].text_note.value) 
    except:
        pass

    text_lbl.grid(row=2, column=0, sticky="e")
    text_form.grid(row=2, column=1)

def keywords_field(notes_form, read_flag = None, new_notes_flag=None):
    global ent_tags
    if read_flag == None:
        ent_tags = Entry(master=notes_form, width=47)
        ent_tags.insert(0, notes_save[find_article].key_words.value) 
        ent_tags.configure(state='disabled')

    elif new_notes_flag == "":

        btn_tags_insert = Button(master=notes_form, width=11, text="Save", command=getArticleInput)
        btn_tags_delete = Button(master=notes_form, width=11, text="Clean text", command=delete_tags)
        btn_tags_insert.grid(row=3, column=2)
        btn_tags_delete.grid(row=3, column=4) 

    else:   

        btn_tags_recover = Button(master=notes_form, width=11, text="Restore", command=tags_return_text)
        btn_tags_insert = Button(master=notes_form, width=11, text="Save", command=getKeywordsInput)
        btn_tags_delete = Button(master=notes_form, width=11, text="Clean text", command=delete_tags)

        btn_tags_recover.grid(row=3, column=3)
        btn_tags_insert.grid(row=3, column=2)
        btn_tags_delete.grid(row=3, column=4)    
    ent_tags = Entry(master=notes_form, width=47)
    lbl_tags = Label(master=notes_form, text="Tags:")

    try:
        ent_tags.insert(0, notes_save[find_article].key_words.value) 
    except:
        pass
    # ent_article.insert(1, "dioswolf")   ****************    ввод текста в поле тегов(для восстановления)

    lbl_tags.grid(row=3, column=0, sticky="e")
    ent_tags.grid(row=3, column=1)

#********************************** Return text Function **********************
def artical_return_text():
    ent_article.delete(0, END)
    ent_article.insert(1, old_name)

def text_return_text():
    text_form.delete("0.1", END)
    text_form.insert("1.0", notes_save[old_name].text_note.value)

def tags_return_text():
    ent_tags.delete(0, END)
    ent_tags.insert(1, notes_save[old_name].key_words.value)

#********************************** Delete functions ****************************    
def delete_article():
    ent_article.delete(0, END)

def delete_text():

    text_form.delete("0.1", END)

def delete_tags():

    ent_tags.delete(0, END)



#********************************** Added functions ****************************   


def add_new_note(result_artilce: str):
    global old_name

    for keys, item in notes_save.items():
        if result_artilce == item.article.value:
            return error_wind
    
    article = Article(result_artilce)
    
    text_note = TextNote(text_form.get(1.0, END+"-1c"))
    key_words = KeyWords(ent_tags.get())
    time_add = DateNote(datetime.now())

    note = Notes(article, text_note, key_words, time_add)
    try:
        del notes_save[old_name]
    except KeyError:
        pass
    old_name = result_artilce
    return save_info(notes_save, note)

def save_info(notes_save: NotesSave, note : Notes):   
    notes_save.add_record(note)
    notes_save.save_data()


#********************************** Write functions ****************************   

def write_text_notes_field(result_text):

    key_note = ent_article.get()

    text_note = TextNote(result_text)
    try:
        notes_save[key_note].text_note = text_note
        time_add = DateNote(datetime.now())
        notes_save[key_note].date_note = time_add
    except KeyError:
        error_wind()
    notes_save.save_data()
    return 

def write_key_words_field(result_keys):
    
    key_note = ent_article.get()

    key_words = KeyWords(result_keys)
    try:
        notes_save[key_note].key_words = key_words
        time_add = DateNote(datetime.now())
        notes_save[key_note].date_note = time_add
    except KeyError:
        error_wind()    
    notes_save.save_data()
    return 


#********************************** GET TEXT functions ********************************


def getArticleInput():
    global old_name
    result_artilce = ent_article.get()
    return add_new_note(result_artilce)

def getTextInput():
    result_text= text_form.get(1.0, END+"-1c")
    return write_text_notes_field(result_text)


def getKeywordsInput():
    result_keys = ent_tags.get()
    return write_key_words_field(result_keys)

#********************************** ERROR and EXIT functions ****************************   

def exit():
    newWindow.destroy()


def btn_exit(notes_form):
    pass_lbl = Label(master=notes_form, text="", height=2)
    pass_lbl.grid(row=4, rowspan=2, column=2)
    btn_exit = Button(master=notes_form, text="Exit", width=20, height=3, command=exit)
    btn_exit.grid(row=6, rowspan=4, column=3, columnspan=3)


def error_wind(*_):
    global error_glob
    error_glob = Toplevel()
    error_glob.geometry("+1000+500") 
    btn_submit = Button(master=error_glob, text="Wrong article name", width=20, height=3,command=exit_menu)
    btn_submit.pack(padx=10, ipadx=10)
    error_glob.mainloop()

def exit_menu():
    notes_save.save_data()
    error_glob.destroy()


#********************************** START functions ******************************** 


def start_window_notes(_, new_notes_flag):
    global newWindow
    read_flag = ""
    newWindow = _
    newWindow.geometry("+800+320")  
    article_field(newWindow, read_flag, new_notes_flag)
    text_fiel(newWindow, read_flag, new_notes_flag)
    keywords_field(newWindow, read_flag, new_notes_flag)
    btn_exit(newWindow)
    newWindow.mainloop()

def createNewWindow(notes_data, article=None, new_notes_flag=None):
    global find_article
    global old_name
    old_name = article
    find_article = article
    global notes_save
    notes_save = notes_data
    notes_save.load_data()
    global newWindow
    newWindow = Toplevel()
    start_window_notes(newWindow, new_notes_flag)

def read(newWindow):
    newWindow.geometry("+800+320")  
    # text_form.configure(state='disabled')
    # ent_tags.configure(state='disabled')
    article_field(newWindow)
    text_fiel(newWindow)
    keywords_field(newWindow)
    btn_exit(newWindow)
    newWindow.mainloop()

def start_read_notes(notes_data, article=None):
    global find_article
    global old_name
    old_name = article
    find_article = article
    global notes_save
    notes_save = notes_data
    notes_save.load_data()
    global newWindow
    newWindow = Toplevel()
    read(newWindow)
