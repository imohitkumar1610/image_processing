from tkinter import *
from tkinter import ttk
from tkinter import filedialog

#models_available = {"U-Net":unet_am,"X-Net":x_net_model} xnet as an example
models_available = ["U-Net","X-Net"]


def select_model():
    pass

def load_file():
    
    def read_path(load_for):
        root.Path = filedialog.askopenfilename(filetypes = (("NII files","*.nii"),("all files","*.*")))
        load_for.set(root.Path)
        var.set(root.Path.rstrip("/"))

    def OK_windows():
        top.destroy()

    def quit_windows():
        top.destroy()
        if hasattr(root,'Path'):
            delattr(root,'Path')
    
    top = Toplevel(root)
    top.title("Select File")
    top.geometry("475x95")
    root.eval(f'tk::PlaceWindow {str(top)} center')
    DWI_path = StringVar()
    FLAIR_path = StringVar()
    
    Label(top, text="DWI", width=15).grid(row=0, column=0,padx=5,pady=2)
    Label(top, text="FLAIR", width=15).grid(row=1, column=0,padx=5,pady=2)
    # selectborderwidth=2
    ttk.Entry(top,textvariable=DWI_path, width=30).grid(row=0,column=1,columnspan=2,padx=5,pady=2,sticky=W+E)
    ttk.Entry(top,textvariable=FLAIR_path, width=30).grid(row=1,column=1,columnspan=2,padx=5,pady=2,sticky=W+E)
    ttk.Button(top, text='Load DWI', command=lambda:read_path(DWI_path),width=15).grid(row=0, column=3, columnspan=1, rowspan=1,padx=5,pady=2)
    ttk.Button(top, text='Load FLAIR', command=lambda:read_path(FLAIR_path),width=15).grid(row=1, column=3, columnspan=1, rowspan=1,padx=5,pady=2)

    ttk.Button(top, text='OK', command=OK_windows,width=13).grid(row=5, column=1, columnspan=1, rowspan=1,padx=5,pady=2,sticky=E+W)
    ttk.Button(top, text='Cancel', command=quit_windows,width=13).grid(row=5, column=2, columnspan=1, rowspan=1,padx=5,pady=2,sticky=W+E)
    
    top.mainloop()
        
def read_file():
    #img_frame = Frame(root).grid(row=0,column=4,rowspan=12,columnspan=6,sticky=E+W)
    Axial = Label(root,text="AXIAL",borderwidth=1,width=20, relief="solid").grid(row=0,column=4,rowspan=6,columnspan=2,padx=3,pady=5,sticky=E+W+N+S)
    SEGl = Label(root,text="segi",borderwidth=1,width=20, relief="solid").grid(row=0,column=6,rowspan=6,columnspan=2,padx=3,pady=5,sticky=E+W+N+S)
    CORl = Label(root,text="corro",borderwidth=1,width=20, relief="solid").grid(row=0,column=8,rowspan=6,columnspan=2,padx=3,pady=5,sticky=E+W+N+S)

def preprocessing_Data():
    pass

def Predict_Data():
    pass

def Skul_radio():
    pass

def Overlay_radio():
    pass

def Show_result():
    pass

root = Tk()
root.geometry("300x400")
root.title("Stroke Lesion Segmentation")

#root.iconbitmap(bitmap=None, default=None) for icon to be displayed if any
root.Path = None

model_name = StringVar()
model_name.set("Select a Segmentation Model")
select_model = ttk.OptionMenu(root,model_name, "Select a Segmentation Model", *models_available)
#options = {padx:5, pady:5}
select_model.configure(width = 25)
select_model.grid(row=0,column=0,columnspan = 4, sticky=E+W)

LoadData=ttk.Button(root, text='Load File', command=load_file)
LoadData.grid(row=1, column=0, columnspan=1, rowspan=1, padx=5,pady=2, sticky=E+W+S+N)

ttk.Button(root, text='upload', command=read_file).grid(row=1, column=1, columnspan=3, rowspan=1, padx=5,pady=2, sticky=E+W+S+N)

ttk.Button(root, text='Preprocessing', command=preprocessing_Data).grid(row=2, column=0, columnspan=1, rowspan=1, padx=5,pady=2, sticky=E+W+S+N)

ttk.Button(root, text='Predict', command=Predict_Data).grid(row=2, column=1, columnspan=3, rowspan=1, padx=5,pady=2, sticky=E+W+S+N)

Skull_label=Label(root, text='Skull Removal').grid(row=3, column=0,padx=5,pady=2,sticky=W)
Skull_var = IntVar()
Skull_var.set(2)

R1 = ttk.Radiobutton(root, text="Yes", variable=Skull_var, value=1, command=Skul_radio).grid(row=3, column=1,padx=5,pady=2,sticky=W)
R2 = ttk.Radiobutton(root, text="No", variable=Skull_var, value=2, command=Skul_radio).grid(row=3, column=2,padx=0,pady=2,sticky=W)

Overlay_label=Label(root, text='Region Color').grid(row=4, column=0,padx=5,pady=2,sticky=W)
Overlay_var = IntVar()
Overlay_var.set(2)

R3 = ttk.Radiobutton(root, text="Yes", variable=Overlay_var, value=1, command=Overlay_radio).grid(row=4, column=1,padx=5,pady=2,sticky=W)
R4 = ttk.Radiobutton(root, text="No", variable=Overlay_var, value=2, command=Overlay_radio).grid(row=4, column=2,padx=0,pady=2,sticky=W)

var = StringVar()
L1=Label(root, text='Path').grid(row=5, column=0,padx=5,pady=2,sticky=W)
#selectborderwidth=2
E1=ttk.Entry(root,textvariable=var, width=30).grid(row=5, column=1,columnspan=3,padx=5,pady=2,sticky=W)

var_BB = StringVar()
B1=Label(root, text='Bounding Box').grid(row=7, column=0,padx=5,pady=2,sticky=W)
#selectborderwidth=2
BE1=ttk.Entry(root,textvariable=var_BB, width=30).grid(row=7, column=1,columnspan=3, rowspan=1,padx=5,pady=2,sticky=W)

var_Ax = StringVar()
B2=Label(root, text='Axial').grid(row=8, column=0,padx=5,pady=2,sticky=W)
BS2 = ttk.Spinbox(root, textvariable=var_Ax, from_=0, to=30, width=30).grid(row=8, column=1,columnspan=3, rowspan=1,padx=5,pady=2,sticky=W)

var_Se = StringVar()
B3=Label(root, text='Seggital').grid(row=9, column=0,padx=5,pady=2,sticky=W)
BS3 = ttk.Spinbox(root, textvariable=var_Se, from_=0, to=30, width=30).grid(row=9, column=1,columnspan=3, rowspan=1,padx=5,pady=2,sticky=W)

var_Co = StringVar()
B4=Label(root, text='Corronal').grid(row=10, column=0,padx=5,pady=2,sticky=W)
BS4 = ttk.Spinbox(root, textvariable=var_Co, from_=0, to=30, width=30).grid(row=10, column=1,columnspan=3, rowspan=1,padx=5,pady=2,sticky=W)

Result=ttk.Button(root,text="Show Result",command=Show_result)
Result.grid(row=11, column=0, columnspan=4, rowspan=1, padx=5,pady=2, sticky=E+W+S+N)

SC1_Var = DoubleVar()
Scale1 = Scale(root, variable=SC1_Var, from_=-100, to=100, orient=HORIZONTAL)
Scale1.grid(row=12,column=0,columnspan=4,padx=5,pady=2,sticky=W+E)

SC2_Var = DoubleVar()
Scale2 = Scale(root, variable=SC2_Var, from_=-100, to=100, orient=HORIZONTAL)
Scale2.grid(row=13,column=0,columnspan=4,padx=5,pady=2,sticky=W+E)


root.mainloop()
