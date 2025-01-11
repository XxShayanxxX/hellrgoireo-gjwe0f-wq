from tkinter import * 

window = Tk()
window.title("Number Converter")
window .geometry("500x500")

nums = [[7,8,9],[4,5,6],[1,2,3],["*",0,"#"]]

for i in range(4):
    window.columnconfigure(i, weight = 20 , minsize = 120)
    window.rowconfigure(i, weight = 20, minsize = 120)

    for j in range(3):
        frame = Frame(master = window , relief= RAISED , borderwidth = 5 )
        frame.grid(row = i , column = j )

        label = Label(master = frame, text = nums[i][j] , bg = "cyan", width= 20 , height = 20 )
        label.pack() 



window.mainloop()