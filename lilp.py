from pathlib import Path
from tkinter import Canvas, PhotoImage, messagebox, Label, Entry, Button
import tkinter as tk
from src.utils import selectFiles, singleFile
from src.merge import mergeFiles
from src.split import splitFile
from src.pdftodocx import pdftodocx


OUTPUT_PATH = str(Path(__file__).parent)
ASSETS_PATH = OUTPUT_PATH + r"\assets\frame0"
def relative_to_assets( path: str) -> Path:
    return ASSETS_PATH / Path(path)
assets = {}

class SplitDialog:
    def __init__(self, parent, file):
        self.file = file
        top = self.top = tk.Toplevel(parent,padx=30, pady=30)
        top.resizable(False,False)
        top.title("Enter split range")
        l1 = Label(top, text="start:").grid(row=0,pady=(0,10))
        l2 = Label(top, text="end:").grid(row=1,pady=(0,10))

        self.e1 = Entry(top)
        self.e2 = Entry(top)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.b = Button(top, text ="Split", command = self.send)
        self.b.grid(row=2,column=1)

    def send(self):
        start = self.e1.get()
        end = self.e2.get()
        if start.isnumeric() and end.isnumeric():
            splitFile(self.file,int(start),int(end))
            self.top.destroy()
            messagebox.showinfo("Success",f"Splitted file from {start} to {end}")
        else:
            messagebox.showinfo("Error",f"Make sure input is correct")
            self.top.destroy()



class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        global assets

        canvas = Canvas(
            self,
            bg = "#F5F5FA",
            height = 529,
            width = 707,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        canvas.place(x = 0, y = 0)

        assets["image_1"] = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            127.0,
            416.0,
            image=assets["image_1"]
        )
        canvas.create_text(
            107.0,
            458.0,
            anchor="nw",
            text="Scan",
            fill="#EE6C4D",
            font=("Inter", 16 * -1)
        )

        assets["image_2"] = PhotoImage(file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            127.0,
            399.0,
            image=assets["image_2"]
        )

        assets["image_3"] = PhotoImage(file=relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(
            580.0,
            208.0,
            image=assets["image_3"]
        )

        canvas.create_text(
            534.0,
            249.0,
            anchor="nw",
            text="Pdf to Docx",
            fill="#EE6C4D",
            font=("Inter", 16 * -1)
        )

        assets["image_4"] = PhotoImage(file=relative_to_assets("image_4.png"))
        image_4 = canvas.create_image(
            602.0,
            211.0,
            image=assets["image_4"]
        )

        assets["image_5"] = PhotoImage(file=relative_to_assets("image_5.png"))
        image_5 = canvas.create_image(
            564.0,
            180.0,
            image=assets["image_5"]
        )

        assets["image_6"] = PhotoImage(file=relative_to_assets("image_6.png"))
        image_6 = canvas.create_image(
            352.0,
            208.0,
            image=assets["image_6"]
        )

        canvas.create_text(
            334.0,
            246.0,
            anchor="nw",
            text="Split",
            fill="#EE6C4D",
            font=("Inter", 16 * -1)
        )

        assets["image_7"] = PhotoImage(file=relative_to_assets("image_7.png"))
        image_7 = canvas.create_image(
            352.0,
            189.0,
            image=assets["image_7"]
        )

        assets["image_8"] = PhotoImage(file=relative_to_assets("image_8.png"))
        image_8 = canvas.create_image(
            127.0,
            208.0,
            image=assets["image_8"]
        )

        canvas.create_text(
            100.0,
            249.0,
            anchor="nw",
            text="Merge",
            fill="#EE6C4D",
            font=("Inter", 16 * -1)
        )

        assets["image_9"] = PhotoImage(file=relative_to_assets("image_9.png"))
        image_9 = canvas.create_image(
            126.0,
            189.0,
            image=assets["image_9"]
        )

        canvas.create_text(
            187.0,
            74.0,
            anchor="nw",
            text="Local ILuvPdf : Tool for pdf operations locally",
            fill="#B2B2B8",
            font=("Inter Bold", 15 * -1)
        )

        canvas.create_text(
            310.0,
            16.0,
            anchor="nw",
            text="LiLP",
            fill="#E5322D",
            font=("Inter Bold", 40 * -1)
        )

        canvas.bind("<Button-1>", self.on_click)


    def on_click(self, event):
        x, y = event.x, event.y
        if x>=45 and x <= 210 and y>=120 and y<295:
            self.merge()
        elif x>=270 and x <= 435 and y>=120 and y<295:
            self.split()
        elif x>=500 and x <= 665 and y>=120 and y<295:
            self.pdftodocx()
        elif x>=45 and x <= 210 and y>=330 and y<505:
            messagebox.showinfo("Scan",f"Comming soon!")

    
    def merge(self):
        files = selectFiles(window)
        if len(files) != 0:
            mergeFiles(files)
            messagebox.showinfo("Success",f"Merged {len(files)} files successfully")

        
    def split(self):
        file = singleFile(self)
        if file != "":
            inputDialog = SplitDialog(self,file)
            self.wait_window(inputDialog.top) 


    def pdftodocx(self):
        file = singleFile(self)
        if file != "":
            pdftodocx(file)
            messagebox.showinfo("Success",f"Converted to docx successfully")


if __name__ == "__main__":
    window = GUI()
    window.geometry("707x529")
    window.configure(bg = "#F5F5FA")
    window.resizable(False, False)
    window.mainloop()

