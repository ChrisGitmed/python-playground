from tkinter import Button, END, messagebox, Text, Tk, ttk
from googletrans import LANGUAGES, Translator

# Define the translator
translator = Translator()
languageValues = list(LANGUAGES.values())
languageKeys = list(LANGUAGES.keys())
languageItems = list(LANGUAGES.items())

# Translate function
def translate():
    try:
        # Clean the text from the destination text box
        translatedText.delete('1.0', END)

        # Get the source and destination languages, as entered
        sourceLanguage = sourceLanguageInput.get()
        destinationLanguage = destinationLanguageInput.get()

        # Use the entered languages and bracket notation to deduce the source and destination keys
        sourceKey = languageKeys[languageValues.index(sourceLanguage)]
        destinationKey = languageKeys[languageValues.index(destinationLanguage)]

        # Translate the text
        enteredWords = sourceText.get(1.0, END)
        translatedObject = translator.translate(enteredWords, src=sourceKey, dest=destinationKey)
        translatedString = translatedObject.text

        # Insert the text into the destination text box
        translatedText.insert(1.0, translatedString)

    except Exception as e:
        messagebox.showerror("Error", e)

# Clear function
def clear():
    sourceText.delete('1.0', END)
    translatedText.delete('1.0', END)

# Construct the GUI
root = Tk()
root.title("Translator Application")

sourceText = Text(root, height=5, width=30)
sourceText.grid(row=0, column=0, padx=20, pady=10)

translateButton = Button(root, text="Translate", command=translate)
translateButton.grid(row=0, column=1, padx=10, pady=10)

translatedText = Text(root, height=5, width=30)
translatedText.grid(row=0, column=2, padx=20, pady=10)

sourceLanguageInput = ttk.Combobox(root, value=languageValues)
sourceLanguageInput.grid(row=1, column=0)
sourceLanguageInput.current(21)

destinationLanguageInput = ttk.Combobox(root, value=languageValues)
destinationLanguageInput.grid(row=1, column=2)
destinationLanguageInput.current(0)

clearButton = Button(root, text="Clear text", command=clear)
clearButton.grid(row=2, column=1, pady='20')

root.mainloop()