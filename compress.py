import os
from tkinter import Tk, Button, Label
from tkinter.filedialog import askdirectory
from PIL import Image

def compress_image(infile, outfile):
    with Image.open(infile) as img:
        # convert the image to RGB mode if it's in RGBA mode
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        img.save(outfile, format='JPEG', quality=50)

def compress_all_images(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            infile = os.path.join(directory, filename)
            outfile = os.path.join(directory, 'compressed_' + filename)
            compress_image(infile, outfile)

def select_directory():
    Tk().withdraw() 
    directory = askdirectory()
    if directory:
        compress_all_images(directory)
        Label(text="Compression done!").pack()

# create a simple UI with a button to select a directory
root = Tk()
root.geometry("300x100")
root.title("Image Compressor")
root.iconbitmap('icon.ico')
Button(text="Select directory", command=select_directory).place(relx=.5, rely=.5,anchor="center")
root.mainloop()

