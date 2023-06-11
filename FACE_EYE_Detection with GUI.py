import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import cv2
import numpy as np

win=tk.Tk()
win.geometry('1430x700')
win.title("REAL TIME FACE AND EYE DETECTION")
win.resizable(False,False)
win.config(bg='#bdb2f9')


# created border for photos
label_1 = Label( width=32, height=17 ,borderwidth=2,relief='solid')
label_1.place(x=88,y=430)


label_2 = Label( width=33, height=17,borderwidth=2,relief='solid')
label_2.place(x=440,y=430)

label_3 = Label( width=33, height=17,borderwidth=2,relief='solid')
label_3.place(x=790,y=430)


#Create a Frame for border
border_color = Frame(win, background="black")

# Label Widget inside the Frame
label_3 = Label(border_color, width=32, height=17, bd=0 )

# Place the widgets with border Frame
label_3.pack(padx=2,pady=2)
border_color.place(x=1140,y=430)


# Define a global variable for resized image
resized_image = None

def open_image():
        global resized_image

        filepath = filedialog.askopenfilename(title="select image", filetypes=(
                ("JPG File", "*.jpg"), ("PNG File", "*.png"), ("ALL Files", "*.*")))
        img = Image.open(filepath)

        new_width = 220
        new_height = 235
        resize_img = img.resize((new_width, new_height), Image.ANTIALIAS)

        resized_image = resize_img  # set the value of the global variable

        img = ImageTk.PhotoImage(resize_img)

        lbl2.configure(image=img)
        lbl2.image = img
        return resize_img
# Define the function to detect faces in the image
def detect_face():
    global resized_image

    # Check if an image has been opened before detecting faces
    if resized_image is None:
        return

    # Load cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Convert PIL image to cv2 image
    cv_img = cv2.cvtColor(np.array(resized_image), cv2.COLOR_RGB2BGR)

    # Convert into grayscale
    gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(cv_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Convert cv2 image back to PIL image
    pil_img = Image.fromarray(cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB))

    # Display the image with detected faces
    img = ImageTk.PhotoImage(pil_img)

    lbl3.configure(image=img)
    lbl3.image = img

def detect_eye():
    global resized_image

    # Check if an image has been opened before detecting faces
    if resized_image is None:
        return

    # Load cascade
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    # Convert PIL image to cv2 image
    cv_img = cv2.cvtColor(np.array(resized_image), cv2.COLOR_RGB2BGR)

    # Convert into grayscale
    gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)

    # Detect eyes
    eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in eyes:
        cv2.rectangle(cv_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Convert cv2 image back to PIL image
    pil_img = Image.fromarray(cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB))

    # Display the image with detected faces
    img = ImageTk.PhotoImage(pil_img)

    lbl4.configure(image=img)
    lbl4.image = img
def face_eye():
        global resized_image

        # Check if an image has been opened before detecting faces
        if resized_image is None:
                return

        # Load cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # Load cascade
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

        # Convert PIL image to cv2 image
        cv_img = cv2.cvtColor(np.array(resized_image), cv2.COLOR_RGB2BGR)

        # Convert into grayscale
        gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
                cv2.rectangle(cv_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Detect eyes
        eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in eyes:
                cv2.rectangle(cv_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Convert cv2 image back to PIL image
        pil_img = Image.fromarray(cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB))

        # Display the image with detected faces
        img = ImageTk.PhotoImage(pil_img)

        lbl5.configure(image=img)
        lbl5.image = img

def go_live():
        # to capture video by webcam
        cap = cv2.VideoCapture(0)
        while True:
                # read the frame
                _, img = cap.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                # show the image
                cv2.imshow('image', img)

                # stop if escape key is pressed
                k = cv2.waitKey(30) & 0xff
                if k == 27:
                        break

        # release the video capture
        cap.waitkey()




def live_face_eye():
        # Real Time EYE FACE detecton

        import cv2

        # load cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


        # to capture video by webcam
        cap = cv2.VideoCapture(0)

        while True:
                # read the frame
                _, img = cap.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                # detect faces
                faces = face_cascade.detectMultiScale(gray, 1.1, 4)
                eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)


                # draw rectangle around faces
                for (x, y, w, h) in faces:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

                # draw rectangle around eyes
                for (x, y, w, h) in eyes:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # show the image
                cv2.imshow('image', img)

                # stop if escape key is pressed
                k = cv2.waitKey(30) & 0xff
                if k == 27:
                        break

        # release the video capture
        cap.waitkey()

def live_gray():
    import cv2

    # load cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # to capture video by webcam
    cap = cv2.VideoCapture(0)

    while True:
        # read the frame
        _, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # draw rectangle around faces
        for (x, y, w, h) in faces:
            cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # show the image
        cv2.imshow('image', gray)

        # stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    # release the video capture
    cap.waitkey()

def live_hsv():
    import cv2

    # load cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # to capture video by webcam
    cap = cv2.VideoCapture(0)

    while True:
        # read the frame
        _, img = cap.read()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # detect faces
        faces = face_cascade.detectMultiScale(hsv, 1.1, 4)

        # draw rectangle around faces
        for (x, y, w, h) in faces:
            cv2.rectangle(hsv, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # show the image
        cv2.imshow('image', hsv)

        # stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    # release the video capture
    cap.waitkey()

lbl1=Label(win, width=150,height=20,bg='#E6E6FA',borderwidth=2, relief="solid")
lbl1.place(x=190,y=40)

btn1=Button(win,text='Open Image',bg='#7863e9',fg='black',width=15,height=2,font=('bold',13),borderwidth=2, relief="solid",command=open_image)
btn1.place(x=320,y=70)
btn1.bind('<Enter>', lambda e: btn1.config(bg='#2a07e4'))
btn1.bind('<Leave>', lambda e: btn1.config(bg='#7863e9'))

btn2=Button(win,text='Face Detect ',bg='#7863e9',fg='black',width=15,height=2,font=('bold',13),borderwidth=2, relief="solid",command=detect_face)
btn2.place(x=650,y=70)
btn2.bind('<Enter>', lambda e: btn2.config(bg='#2a07e4'))
btn2.bind('<Leave>', lambda e: btn2.config(bg='#7863e9'))

btn3=Button(win,text='Eye Detect',bg='#7863e9',fg='black',width=15,height=2,font=('bold',13),borderwidth=2, relief="solid",command=detect_eye)
btn3.place(x=960,y=70)
btn3.bind('<Enter>', lambda e: btn3.config(bg='#2a07e4'))
btn3.bind('<Leave>', lambda e: btn3.config(bg='#7863e9'))

btn4=Button(win,text='Face & Eye',bg='#7863e9',fg='black',width=15,height=2,font=('bold',13),borderwidth=2, relief="solid",command=face_eye)
btn4.place(x=320,y=170)
btn4.bind('<Enter>', lambda e: btn4.config(bg='#2a07e4'))
btn4.bind('<Leave>', lambda e: btn4.config(bg='#7863e9'))

btn5=Button(win,text='Go Live',bg='#7863e9',fg='black',width=15,height=2,font=('bold',13),borderwidth=2, relief="solid",command=go_live)
btn5.place(x=650,y=170)
btn5.bind('<Enter>', lambda e: btn5.config(bg='#2a07e4'))
btn5.bind('<Leave>', lambda e: btn5.config(bg='#7863e9'))

btn6=Button(win,text='Live Face & Eye',bg='#7863e9',fg='black',width=15,height=2,font=('bold',13),borderwidth=2, relief="solid",command=live_face_eye)
btn6.place(x=960,y=170)
btn6.bind('<Enter>', lambda e: btn6.config(bg='#2a07e4'))
btn6.bind('<Leave>', lambda e: btn6.config(bg='#7863e9'))

btn7=Button(win,text='Live Gray Scale',bg='#7863e9',fg='black',width=15,height=2,font=('bold',13),borderwidth=2, relief="solid",command=live_gray)
btn7.place(x=320,y=270)
btn7.bind('<Enter>', lambda e: btn7.config(bg='#2a07e4'))
btn7.bind('<Leave>', lambda e: btn7.config(bg='#7863e9'))

btn8=Button(win,text='Live HSV',bg='#7863e9',fg='black',width=15,height=2,font=('bold',13),borderwidth=2, relief="solid",command=live_hsv)
btn8.place(x=960,y=270)
btn8.bind('<Enter>', lambda e: btn8.config(bg='#2a07e4'))
btn8.bind('<Leave>', lambda e: btn8.config(bg='#7863e9'))


lbl2=Label(win)
lbl2.place(x=90,y=450)

lbl3=Label(win)
lbl3.place(x=450,y=450)

lbl4=Label(win)
lbl4.place(x=795,y=450)

lbl5=Label(win)
lbl5.place(x=1150,y=450)



win.mainloop()
