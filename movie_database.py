from tkinter import *
from tkinter import messagebox
import os
f=open("database_proj",'a+')
root = Tk()
root.configure(background='black')
ijklm=-1


def additem():
    global ijklm
    num_lines = 0
    with open("database_proj", 'r') as f10:
        for line in f10:
            num_lines += 1
    ijklm=num_lines-1
    e1= ent1.get()
    e2=ent2.get()
    e3=ent3.get()
    e4=ent4.get()
    e5=ent5.get()
    e6=ent6.get()
    e7=ent7.get()
    f.write('{0} {1} {2} {3} {4} {5} {6}\n'.format(str(e1),e2,str(e3),str(e4),str(e5),e6,str(e7)))
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent4.delete(0, END)
    ent3.delete(0, END)
    ent5.delete(0, END)
    ent6.delete(0, END)
    ent7.delete(0, END)


def deleteitem():
    e1=ent1.get()
    with open(r"database_proj") as f, open(r"database_proj1", "w") as working:
        for line in f:
            if str(e1) not in line:
                working.write(line)
    os.remove(r"database_proj")
    os.rename(r"database_proj1", r"database_proj")
    f.close()
    working.close()
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent4.delete(0, END)
    ent3.delete(0, END)
    ent5.delete(0, END)
    ent6.delete(0, END)
    ent7.delete(0, END)

def firstitem():
    global ijklm
    ijklm=0
    f.seek(ijklm)
    c=f.readline()
    jkl=list(c.split(" "))
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent4.delete(0, END)
    ent3.delete(0, END)
    ent5.delete(0, END)
    ent6.delete(0, END)
    ent7.delete(0, END)
    ent1.insert(0,str(jkl[0]))
    ent2.insert(0,str(jkl[1]))
    ent4.insert(0,str(jkl[3]))
    ent3.insert(0,str(jkl[2]))
    ent5.insert(0,str(jkl[4]))
    ent6.insert(0,str(jkl[5]))
    ent7.insert(0,str(jkl[6]))

def nextitem():
    global ijklm
    ijklm = ijklm + 1
    f.seek(ijklm)
    try:
        c=f.readlines()
        xyz = c[ijklm]
        jkl = list(xyz.split(" "))
        ent1.delete(0, END)
        ent2.delete(0, END)
        ent4.delete(0, END)
        ent3.delete(0, END)
        ent5.delete(0, END)
        ent6.delete(0, END)
        ent7.delete(0, END)
        ent1.insert(0, str(jkl[0]))
        ent2.insert(0, str(jkl[1]))
        ent4.insert(0, str(jkl[3]))
        ent3.insert(0, str(jkl[2]))
        ent5.insert(0, str(jkl[4]))
        ent6.insert(0,str(jkl[5]))
        ent7.insert(0,str(jkl[6]))
    except:
        messagebox.showinfo("Title", " NO MORE RECORDS ")
def previousitem():
        global ijklm
        ijklm=ijklm-1
        f.seek(ijklm)
        try:
            z = f.readlines()
            xyz=z[ijklm]
            jkl = list(xyz.split(" "))
            ent1.delete(0, END)
            ent2.delete(0, END)
            ent4.delete(0, END)
            ent3.delete(0, END)
            ent5.delete(0, END)
            ent6.delete(0, END)
            ent7.delete(0, END)
            ent1.insert(0, str(jkl[0]))
            ent2.insert(0, str(jkl[1]))
            ent4.insert(0, str(jkl[3]))
            ent3.insert(0, str(jkl[2]))
            ent5.insert(0, str(jkl[4]))
            ent6.insert(0,str(jkl[5]))
            ent7.insert(0,str(jkl[6]))
        except:
            messagebox.showinfo("Title", " NO MORE RECORDS ")


def lastitem():
    global ijklm
    f4=open("database_proj",'r')
    x=f4.read().splitlines()
    last_line= x[-1]
    num_lines = 0
    with open("database_proj", 'r') as f8:
        for line in f8:
            num_lines += 1
    ijklm=num_lines-1
    print(last_line)
    try:
        jkl = list(last_line.split(" "))
        ent1.delete(0, END)
        ent2.delete(0, END)
        ent4.delete(0, END)
        ent3.delete(0, END)
        ent5.delete(0, END)
        ent6.delete(0, END)
        ent7.delete(0, END)
        ent1.insert(0, str(jkl[0]))
        ent2.insert(0, str(jkl[1]))
        ent4.insert(0, str(jkl[3]))
        ent3.insert(0, str(jkl[2]))
        ent5.insert(0, str(jkl[4]))
        ent6.insert(0,str(jkl[5]))
        ent7.insert(0,str(jkl[6]))
    except:
        messagebox.showinfo("Title", " NO MORE RECORDS ")


def updateitem():

    e1 = ent1.get()
    e2 = ent2.get()
    e3 = ent3.get()
    e4 = ent4.get()
    e5 = ent5.get()
    e6 = ent6.get()
    e7 = ent7.get()
    with open(r"database_proj") as f1, open(r"database_proj1", "w") as working:
        for line in f1:
            if str(e1) not in line:
                working.write(line)
            else:
                working.write('{0} {1} {2} {3} {4} {5} {6}'.format(str(e1),e2,str(e3),str(e4),str(e5),e6,str(e7)))
    os.remove(r"database_proj")
    os.rename(r"database_proj1", r"database_proj")


def searchitem():
    i=0
    e11 = ent1.get()
    with open(r"database_proj") as working:
        for line in working:
            i=i+1
            if str(e11) in line:
                break
        try:
            jkl = list(line.split(" "))
            ent1.delete(0, END)
            ent2.delete(0, END)
            ent4.delete(0, END)
            ent3.delete(0, END)
            ent5.delete(0, END)
            ent6.delete(0, END)
            ent7.delete(0, END)
            ent1.insert(0, str(jkl[0]))
            ent2.insert(0, str(jkl[1]))
            ent4.insert(0, str(jkl[3]))
            ent3.insert(0, str(jkl[2]))
            ent5.insert(0, str(jkl[4]))
            ent6.insert(0,str(jkl[5]))
            ent7.insert(0,str(jkl[6]))
        except:
            messagebox.showinfo("Title", "error end of file")
    working.close()


lbl0= Label(root,text="MOVIE DATABASE MANAGEMENT SYSTEM", font=("Algerian", 30))
lbl1=Label(root,text="MOVIE NAME", font=("Comic Sans MS", 12))
ent1=Entry(root , font=("Helvetica", 12))
lbl2=Label(root, text="DURATION", font=("Comic Sans MS", 12))
ent2= Entry(root, font=("Helvetica", 12))
lbl3=Label(root, text="LANGUAGE", font=("Comic Sans MS", 12))
ent3= Entry(root, font=("Helvetica", 12))
lbl4=Label(root, text="STAR CASTE", font=("Comic Sans MS", 12))
ent4= Entry(root, font=("Helvetica", 12))
lbl5=Label(root, text="GENRE", font=("Comic Sans MS", 12))
ent5= Entry(root, font=("Helvetica", 12))
lbl6=Label(root, text="RATING", font=("Comic Sans MS", 12))
ent6= Entry(root, font=("Helvetica", 12))
lbl7=Label(root, text="REVIEW", font=("Comic Sans MS", 12))
ent7= Entry(root, font=("Helvetica", 12))
b1= Button(root, text="ADD ITEM", bg="black", fg="white", width=20, font=("Comic Sans MS", 12), command=additem)
b2= Button(root, text="DELETE ITEM", bg="black", fg="white", width =20, font=("Comic Sans MS", 12), command=deleteitem)
b3= Button(root, text="<<" , bg="black", fg="white", width =20, font=("Comic Sans MS", 12), command=firstitem)
b4= Button(root, text=">" , bg="black", fg="white", width =20, font=("Comic Sans MS", 12), command=nextitem)
b5= Button(root, text="<", bg="black", fg="white", width =20, font=("Comic Sans MS", 12), command=previousitem)
b6= Button(root, text=">>", bg="black", fg="white", width =20, font=("Comic Sans MS", 12), command=lastitem)
b7= Button(root, text="UPDATE ITEM", bg="black", fg="white", width =20, font=("Comic Sans MS", 12), command=updateitem)
b8= Button(root, text="SEARCH ITEM", bg="black", fg="white", width =20, font=("Comic Sans MS", 12), command=searchitem)
lbl0.grid(columnspan=6, padx=10, pady=10)
lbl1.grid(row=6,column=1, sticky=W, padx=10, pady=10)
lbl2.grid(row=7,column=1, sticky=W, padx=10, pady=10)
lbl3.grid(row=8,column=1, sticky=W, padx=10, pady=10)
lbl4.grid(row=9,column=1, sticky=W, padx=10, pady=10)
lbl5.grid(row=10,column=1, sticky=W, padx=10, pady=10)
lbl6.grid(row=11,column=1, sticky=W, padx=10, pady=10)
lbl7.grid(row=12,column=1, sticky=W, padx=10, pady=10)
ent1.grid(row=6,column=2, padx=10, pady=10)
ent2.grid(row=7,column=2, padx=10, pady=10)
ent3.grid(row=8,column=2, padx=10, pady=10)
ent4.grid(row=9,column=2, padx=10, pady=10)
ent5.grid(row=10,column=2, padx=10, pady=10)
ent6.grid(row=11,column=2, padx=10, pady=10)
ent7.grid(row=12,column=2, padx=10, pady=10)
b1.grid(row=14,column=0, padx=4, pady=10)
b2.grid(row=14,column=1, padx=4, pady=10)
b3.grid(row=13,column=0, padx=4, pady=10)
b4.grid(row=13,column=2, padx=4, pady=10)
b5.grid(row=13,column=1, padx=4, pady=10)
b6.grid(row=13,column=3, padx=4, pady=10)
b7.grid(row=14,column=2, padx=4, pady=10)
b8.grid(row=14,column=3, padx=4, pady=10)
root.mainloop()
