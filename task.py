import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os

def play():
    text = text_entry.get("1.0", "end").strip()
    if text:
        try:
            tts = gTTS(text=text, lang='en')
            tts.save("output.mp3")
            os.system("start output.mp3")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")
    else:
        messagebox.showwarning("Input Error", "Please enter some text.")

def set1():
    text_entry.delete("1.0", "end")

def exit1():
    root.destroy()

root = tk.Tk()
root.title("Text to Speech")
root.geometry("400x300")

label = tk.Label(root, text="Enter your text:", font=("Arial", 14))
label.pack(pady=10)

text_entry = tk.Text(root, height=5, width=40, font=("Arial", 12))
text_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

play_button = tk.Button(button_frame, text="Play", command=play, font=("Arial", 12), fg="white", bg="blue", width=10)
play_button.grid(row=0, column=0, padx=5)

exit_button = tk.Button(button_frame, text="Exit", command=exit1, font=("Arial", 12), fg="white", bg="red", width=10)
exit_button.grid(row=0, column=1, padx=5)

save_button = tk.Button(button_frame, text="Set", command=set1, font=("Arial", 12), fg="white", bg="orange", width=10)
save_button.grid(row=0, column=2, padx=5)

root.mainloop()
