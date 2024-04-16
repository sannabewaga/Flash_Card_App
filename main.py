from tkinter import *
import pandas
import random

scheduled_event_id=None

##-----------------------------------------new words---------------------------------------#

data=pandas.read_csv("data/french_words.csv")

French_words= data["French"].to_list()
English_words = data["English"].to_list()



def change_word():

    canvas.itemconfig(main_image,image=center_image)
    global random_index
    random_index= random.randint(0,len(French_words)-1)

    canvas.itemconfig(word_text,text=French_words[random_index])
    canvas.itemconfig(upper_text,text="French")



def flip_card():
    window.after(3000, lambda: canvas.itemconfig(word_text, text=English_words[random_index]))
    window.after(3000, lambda: canvas.itemconfig(main_image, image=reverse_image))
    window.after(3000, lambda: canvas.itemconfig(upper_text, text="English"))


def right_button_click():
    global scheduled_event_id  # Use the global scheduled_event_id
    change_word()
    if scheduled_event_id:
        window.after_cancel(scheduled_event_id)  # Cancel the previous scheduled event
    scheduled_event_id = window.after(3000, flip_card)


def left_button_click():
    canvas.itemconfig(word_text, text=English_words[random_index])
    canvas.itemconfig(main_image, image=reverse_image)
    canvas.itemconfig(upper_text, text="English")
    change_word()
    flip_card()





#---------------------------------------ui-------------------------------------------------------#

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.minsize(height=800,width=1000)
window.config(bg=BACKGROUND_COLOR,padx=100,pady=50)


#canvas thing


canvas= Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
center_image = PhotoImage(file="card_front.png")
reverse_image = PhotoImage(file="card_back.png")
main_image =canvas.create_image(400, 270, image=center_image)
upper_text=canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"), fill="black")
word_text =canvas.create_text(400,300,text="word",font=("Ariel", 60, "bold"), fill="black")

canvas.grid(row=0,column=0,columnspan=2)

### cross and tick button

right_button_image = PhotoImage(file="right.png")
right_button = Button(image=right_button_image,borderwidth=1, highlightthickness=0, relief="groove",command=right_button_click)
right_button.grid(row= 2 , column = 0,pady=50)


wrong_button_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_button_image,borderwidth=1, highlightthickness=0, relief="groove",command=left_button_click)
wrong_button.grid(row = 2 ,column = 1,pady=50)











change_word()
flip_card()







window.mainloop()




