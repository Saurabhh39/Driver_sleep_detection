from tkinter import *
from PIL import Image,ImageTk
from detector import *

root=Tk()
root.title("Driver Sleepiness Detector")
root.minsize(width=500,height=500)
root.geometry("600x500")

background_image =Image.open("bg-img.jpg")
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)      
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \nSleepiness Detection System", bg='red', fg='black', font=('Gotham',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Sleepiness Detection",bg='blue', fg='black', command=sleep_detector)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

btn2 = Button(root,text="Show Landmarks",bg='green', fg='black', command=landmarks_show)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

root.mainloop()