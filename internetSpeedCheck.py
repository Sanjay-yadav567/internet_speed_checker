from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    downloading = str(round(sp.download()/(10**6),3))+"Mbps"
    uploading = str(round(sp.upload()/(10**6),3))+"Mbps"
    lab_downloading.config(text=downloading)
    lab_uploading.config(text=uploading)


sp = Tk()
sp.title("Internet Speed Test ")
sp.geometry("500x600")
sp.config(bg="PaleVioletRed4")


label = Label(sp,text="Internet Speed Test", font=("Time New Roman",30,"bold"),bg="PaleVioletRed4",fg="mint cream")
label.place(x = 55, y = 40, height=50,width=380)


label = Label(sp,text="Downloading Speed", font=("Time New Roman",30,"bold"),bg="PaleVioletRed4",fg="mint cream")
label.place(x = 55, y = 130, height=50,width=380)


lab_downloading = Label(sp,text="00", font=("Time New Roman",30,"bold"),bg="PaleVioletRed4",fg="mint cream")
lab_downloading.place(x = 55, y = 200, height=50,width=380)


label = Label(sp,text="Uploading Speed", font=("Time New Roman",30,"bold"),bg="PaleVioletRed4",fg="mint cream")
label.place(x = 55, y = 290, height=50,width=380)

lab_uploading = Label(sp,text="00", font=("Time New Roman",30,"bold"),bg="PaleVioletRed4",fg="mint cream")
lab_uploading.place(x = 55, y = 360,height=50,width=380)


button = Button(sp, text="Check Speed",  font=("Time New Roman",30,"bold"),relief=RAISED, bg = "plum3", command=speedcheck)
button.place(x = 55, y = 450,height=50,width=380)

sp.mainloop()