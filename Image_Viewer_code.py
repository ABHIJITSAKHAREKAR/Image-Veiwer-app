from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import os



root=Tk()
root.title("Image Viewer")
root.geometry("650x650")

i=0

def op():
    
    global directory
    global files
    global i
    global length_of_files
    files=[]
    
    directory=filedialog.askdirectory()
    filenames=os.listdir(directory)
    
    for j in filenames:
        
        splitlist=j.split(".")
        if len(splitlist)==1:
            continue
        
        elif splitlist[1]=="jpg" or  splitlist[1]=="jpeg" or splitlist[1]=="png":
            
            files.append(j) 
        
       
       # print(splitlist)
    
    length_of_files=len(files)
    
    
    #print(files)
    
    tst=Image.open(directory+"/"+str(files[i]))
    size=(500,500)
    tst=tst.resize(size)
    img=ImageTk.PhotoImage(tst)
    L.configure(image=img)
    L.image=img


def frwrd():
    
    global i
    if i == length_of_files-1:
        tst=Image.open(directory+"/"+str(files[i]))
        size=(500,500)
        tst=tst.resize(size)
        img=ImageTk.PhotoImage(tst)
        L.configure(image=img)
        L.image=img        
    
    else:
        i=i+1
        tst=Image.open(directory+"/"+str(files[i]))
        size=(500,500)
        tst=tst.resize(size)
        img=ImageTk.PhotoImage(tst)
        L.configure(image=img)
        L.image=img    


def backwrd():
    global i
    if i ==0:
        tst=Image.open(directory+"/"+str(files[i]))
        size=(500,500)
        tst=tst.resize(size)
        img=ImageTk.PhotoImage(tst)
        L.configure(image=img)
        L.image=img        
    
    else:
        i=i-1
        tst=Image.open(directory+"/"+str(files[i]))
        size=(500,500)
        tst=tst.resize(size)
        img=ImageTk.PhotoImage(tst)
        L.configure(image=img)
        L.image=img        
    
angle=90
def rot():
    global angle 
    tst=Image.open(directory+"/"+str(files[i]))
    size=(500,500)
    tst=tst.resize(size)
    tst=tst.rotate(angle)
    angle=angle+90
    img=ImageTk.PhotoImage(tst)
    L.configure(image=img)
    L.image=img    



Open=Button(root,text="Browse Files",command=op)
Open.grid(row=0,column=1)

frame=LabelFrame(root,text="IMAGE VIEWER BY ABHIJIT",padx=10,pady=10)
frame.grid(row=1,column=0,columnspan=3,padx=58,pady=10)

forward=Button(root,text="NEXT",command=frwrd)
forward.grid(row=3,column=2)


backward=Button(root,text="BACK",command=backwrd)
backward.grid(row=3,column=0)

rotate=Button(root,text="ROTATE",command=rot)
rotate.grid(row=3,column=1)




#file="D:/photos/boaating@pune18july/IMG_20210717_173033.jpg"
#temp=Image.open(file)
#size=(500,500)
#temp=temp.resize(size,Image.ANTIALIAS)
#temp=temp.rotate(90)
#img=ImageTk.PhotoImage(temp)
L=Label(frame,text="Your IMAGE Will be Shown Here")
L.pack()





root.mainloop()
