import tkinter as tk
import random
import colorsys

def move_circle(event):
    global counter
    if canvas.find_withtag(tk.CURRENT):
        counter += 1
        counter_label.config(text=f"Counter: {counter}")
        
        flash_screen("#85ff85") 
        

        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        
        x1, y1 = random.randint(0, canvas_width - 100), random.randint(0, canvas_height - 100)
        x2, y2 = x1 + 80, y1 + 80  
        

        hue = random.random()
        rgb_color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        hex_color = f"#{int(rgb_color[0] * 255):02x}{int(rgb_color[1] * 255):02x}{int(rgb_color[2] * 255):02x}"
        
        canvas.coords(circle, x1, y1, x2, y2)
        canvas.itemconfig(circle, fill=hex_color)
    else:
        counter = 0
        counter_label.config(text=f"Counter: {counter}")

def reset_counter(event):
    global counter
    if not canvas.find_withtag(tk.CURRENT):
        flash_screen("#FF0000") 
        counter = 0
        counter_label.config(text=f"Counter: {counter}")

def flash_screen(color):
    canvas.configure(bg=color)
    canvas.after(100, lambda: canvas.configure(bg="white"))

root = tk.Tk()
root.configure(bg="white")

counter = 0

canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()

x1, y1, x2, y2 = 100, 100, 180, 180  
circle = canvas.create_oval(x1, y1, x2, y2, outline="black", fill="blue", width=2)

canvas.tag_bind(circle, "<Button-1>", move_circle)

canvas.bind("<Button-1>", reset_counter)

counter_label = tk.Label(root, text=f"Counter: {counter}")
counter_label.pack()

root.mainloop()
