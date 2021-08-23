from tkinter import *

from PIL import ImageTk, Image
from tkinter import filedialog
import os
from infer import BGRemove
from IPython.display import clear_output
import cv2

root = Tk()
root.geometry("720x480")
root.resizable(width=True, height=True)
bg_remove = BGRemove('pretrained/modnet_photographic_portrait_matting.ckpt')

class tik:
    def bg():
        back_fn = filedialog.askopenfilename(title='open')
        f = open('b.txt','w')
        f.write(back_fn)
        return back_fn
    
    def openfn(self):
        self.filename = filedialog.askopenfilename(title='open')
        f = open('w.txt','w')
        f.write(self.filename)
        return self.filename
    
    def save_file():
        file = filedialog.asksaveasfilename(title='open')
        print(file)
        f = open('n.txt','w')
        f.write(file)
        return file
    
    def process_file():
       

        f = open('w.txt','r')
        s = open('b.txt','r')
        n = open('n.txt','r')
        
        # image  
        r = f.readlines()
        r = r[0]
        img_name = os.path.basename(r)
        
        # background
        t = s.readlines()
        t = t[0]
        
        # name 
        v = n.readlines()
        v = v[0]
        v = os.path.basename(v)
    
        outputs = 'result'
        if os.path.exists(outputs):
            bg_remove.image(r,t,output=outputs,image_name=v)
            
        else:
            os.mkdir(outputs)
        '''
        img = cv2.imread(outputs+'/'+img_name)
        cv2.imshow('frame', img)
        cv2.waitKey()
        cv2.destroyAllWindows()
        '''
    
    def button():
        
        btn = Button(root, text='open image',command=tik.open_img).pack()
        bg = Button(root, text='BACKGROUND',command=tik.back_img).pack()
        pr = Button(root, text='PROCESS',command=tik.process_file).pack()
        t = Button(root,text='SAVE AS',command=tik.save_file).pack()
        root.mainloop()
    
    def back_img():
        x = tik.bg()
        img = Image.open(x)
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(root, image=img)
        panel.image = img
        panel.pack()
    
    def open_img():
        x = tik().openfn()
        img = Image.open(x)
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(root, image=img)
        panel.image = img
        panel.pack()
        
        
def res():
    
    r = tik
    r.button()

res()
