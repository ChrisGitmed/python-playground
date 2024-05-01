from random import choice
from tkinter import Button, END, Label, mainloop, Text, Tk
from deepface import DeepFace
from PIL import Image, ImageTk

# Gui should contain a displayed image, generated information about an image,
# and a random button to select another image.

# List any filepaths of images to be used for facial recognition
paths = ['person1.jpg', 'person2.jpg', 'person3.jpg', 'person4.jpg', 'person5.jpg', 'person6.jpg']

# Define the root of the Tkinter application
root = Tk()
root.title('Face Recognition Program')

# Create a button to analyze a random face
def analyzeFace():
    face = choice(paths)

    # Render the selected image
    image = Image.open(face)
    tk_image = ImageTk.PhotoImage(image)
    label.configure(image = tk_image)
    label.image = tk_image

    # Insert the analyzed text into the textbox
    result = DeepFace.analyze(face)
    analysisTextBox.insert(1.0, result)
analyzeButton = Button(root, text='Get a new face to analyze', command=analyzeFace)
analyzeButton.grid(row=0, pady=(24, 12))

# Create a button to clear the text box
def clear():
    analysisTextBox.delete(1.0, END)
clearButton = Button(root, text='Clear', command=clear)
clearButton.grid(row=1, pady=(0, 24))

# Create a window to show the generated text
analysisTextBox = Text(root, height=12, padx=24, pady=12)
analysisTextBox.grid(row=3, padx=24, pady=(0, 24))

# Create a window to show the image the text was generated from
label = Label(root, width=100, height=100)
label.grid(row=4, pady=(0, 24))

# Start the application
mainloop()
