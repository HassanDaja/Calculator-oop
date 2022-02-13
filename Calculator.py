from tkinter import *
from functools import partial
light_grey="#F5F5F5"
light_blue="#ADD8E6"
label_color="#00013E"
grey='#e0e0e0'
small_fontstyle=("arial",16)
large_fontstyle=('arial',40,"bold")
class calculator:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")
        self.window.configure(background=grey)
        self.totalexpession="0"
        self.answer="0"
        self.last_used=''
        self.total_lab,self.curr_lab=self.total_label()
        self.display_frame=self.creat_display_frame()
        self.button_frame = self.creat_buttons_frame()
        self.digits={7:(1,1),8:(1,2),9:(1,3),
                     4:(2,1),5:(2,2),6:(2,3),
                     1:(3,1),2:(3,2),3:(3,3),
                     0:(4,1),".":(4,2),"-/+":(4,3)}
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.create_digit_buttons()
        self.create_operators_buttons()
        self.create_extra_button()
    def total_label(self):
        total_lab=Label(self.window,text=self.totalexpession,font=small_fontstyle,fg=label_color,anchor=E,bg=grey)
        total_lab.pack(fill="x",pady=20,padx=20)
        curr_lab = Label(self.window, text=self.answer, font=large_fontstyle, fg=label_color,bg=grey, anchor=E)
        curr_lab.pack(fill="x", pady=0, padx=20)
        return total_lab,curr_lab
    def run(self):
        self.window.mainloop()
    def creat_display_frame(self):
        frame=Frame(self.window,height=100,bg=grey)
        frame.pack(expand=True,fill="both")
        return frame
    def creat_buttons_frame(self):
        frame = Frame(self.window,bg=light_blue)
        frame.pack(expand=True, fill="both")
        return frame
    def create_digit_buttons(self):
        for key,val in self.digits.items():
            if str(key).isdigit() or key == '.':
                button=Button(self.button_frame,borderwidth=0,highlightbackground = grey, highlightcolor= grey,height=3,width=7,text=str(key),font=small_fontstyle,bg="#FFFFFF",command=partial(self.add_to_amswer, key),relief="solid")
                button.grid(row=val[0],column=val[1])
            else:
                button = Button(self.button_frame, borderwidth=0,relief="solid", height=3, width=7, text=str(key),
                                font=small_fontstyle, bg="#FFFFFF", command=self.minus_plus)
                button.grid(row=val[0], column=val[1])
    def create_operators_buttons(self):
        i=0
        for key,val in self.operations.items():
            button = Button(self.button_frame,highlightthickness=1, height=3,highlightbackground = grey, highlightcolor= grey,relief="solid", width=9, text=val,background=grey, font=small_fontstyle, bg="#FFFFFF",borderwidth=0,command=partial(self.operators_func,val))
            button.grid(row=i, column=4,sticky=NSEW)
            i+=1
    def create_extra_button(self):
        button = Button(self.button_frame,highlightbackground = grey, highlightcolor= grey, height=3,relief="solid", width=4, text="C",background=grey, font=small_fontstyle, bg="#FFFFFF",
                        borderwidth=0,command=self.clear_button)
        button.grid(row=0,column=1,columnspan=2,sticky=NSEW)
        button = Button(self.button_frame,highlightbackground = grey, highlightcolor= grey, height=3, width=4,background=grey, text="Del", font=small_fontstyle, bg="#FFFFFF",
                        borderwidth=0,highlightthickness=1,relief="solid", command=self.delete_last)
        button.grid(row=0, column=3, sticky=NSEW)
        button = Button(self.button_frame,highlightbackground = grey, highlightcolor= grey, height=3, width=9,background=grey, text="=", font=small_fontstyle, bg="#FFFFFF",
                        borderwidth=0,highlightthickness=1,relief="solid",command=self.get_answer)
        button.grid(row=4, column=4, sticky=NSEW)
    def update(self):
        self.curr_lab.config(text=self.answer)
        self.total_lab.config(text=self.totalexpession)
    def delete_last(self):
        if len(self.answer)>1:
            self.answer=self.answer[:-1]
        else:
            self.answer='0'
            self.totalexpession=self.answer
        self.update()
    def add_to_amswer(self,value):
        if self.answer=='0' and "." not in self.answer:
            self.answer=""
        if value=='.' and '.' not in self.answer:
            self.answer+=str(value)
            self.update()
        elif value!='.':
            self.answer += str(value)
            self.update()
    def minus_plus(self):
        self.answer=str(float(self.answer)* -1)
        self.update()
    def clear_button(self):
        self.answer="0"
        self.totalexpession="0"
        self.update()
    def get_answer(self):
        x = self.answer.replace(self.operations[self.last_used],self.last_used)
        self.answer=str(eval(x))
        self.totalexpession = self.answer
        self.update()

    def operators_func(self,operator):
        if self.answer[-1] not in self.operations.values() and self.answer!='0':
            if any(ext in self.answer for ext in self.operations.values()):
                self.get_answer()
                self.update()
                self.answer+=operator
                self.totalexpession=self.answer

            else:
                key = list(self.operations.keys())
                vals = list(self.operations.values())
                self.last_used = key[vals.index(operator)]
                self.answer+=operator
                self.totalexpession=self.answer
                self.update()
















if __name__ =="__main__":
    calc=calculator()
    calc.run()
