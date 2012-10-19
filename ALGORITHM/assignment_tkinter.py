import tkinter

class Application(tkinter.Frame):
    def __init__(self,master):
        tkinter.Frame.__init__(self,master)
        self.pack()

        self.morningbutton=tkinter.Button()
        self.morningbutton["text"]="morning"
        self.morningbutton["command"]=self.morning
        self.morningbutton.pack()
        
    
        self.afternoonbutton=tkinter.Button()
        self.afternoonbutton["text"]="afternoon"
        self.afternoonbutton["command"]=self.afternoon
        self.afternoonbutton.pack()

        self.eveningbutton=tkinter.Button()
        self.eveningbutton["text"]="evening"
        self.eveningbutton["command"]=self.evening
        self.eveningbutton.pack()

        self.quitbutton=tkinter.Button()
        self.quitbutton["text"]="quit"
        self.quitbutton["command"]=self.quit
        self.quitbutton.pack()

    def morning(self):
            print("good morning!")

    def afternoon(self):
            print("good afternoon!")

    def evening(self):
            print("good night!")

    def quit(self):
            print("bye! bye!")
        

root=tkinter.Tk()
app=Application(master=root)
app.mainloop()



