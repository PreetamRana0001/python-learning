import tkinter as tk
import math

# Function for button click
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen.set(result)
        except:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    elif text == "⌫":  # Backspace
        current = screen.get()
        screen.set(current[:-1])
    elif text == "√":
        try:
            result = math.sqrt(float(screen.get()))
            screen.set(result)
        except:
            screen.set("Error")
    elif text == "x²":
        try:
            result = float(screen.get()) ** 2
            screen.set(result)
        except:
            screen.set("Error")
    elif text == "+/-":
        try:
            current = float(screen.get())
            screen.set(str(-current))
        except:
            screen.set("Error")
    else:
        screen.set(screen.get() + text)

# Create window
root = tk.Tk()
root.title("🧮 Advanced Calculator")
root.geometry("340x480")
root.config(bg="black")

# Display screen
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 20 bold", justify="right", bg="#222", fg="white")
entry.pack(fill=tk.X, ipadx=8, padx=10, pady=10)

# Buttons layout
buttons = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["+/-", "0", ".", "="],
    ["√", "x²"]
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root, bg="black")
    frame.pack(expand=True, fill="both")
    for text in row:
        button = tk.Button(
            frame,
            text=text,
            font="lucida 15 bold",
            relief="ridge",
            border=1,
            bg="#333",
            fg="white",
            activebackground="#555",
            activeforeground="yellow",
            padx=20,
            pady=15
        )
        button.pack(side=tk.LEFT, expand=True, fill="both", padx=2, pady=2)
        button.bind("<Button-1>", click)

root.mainloop()
