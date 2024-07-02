import tkinter as tk
import random
import colorsys

# Function to move the circle to a new random position and change its color
def move_circle(event):
    global counter
    # Check if the click is within the current circle
    if canvas.find_withtag(tk.CURRENT):
        # Increment the counter
        counter += 1
        # Update the counter display
        counter_label.config(text=f"Counter: {counter}")
        
        # Flash the screen green
        flash_screen("#85ff85")  # Green color
        
        # Calculate random position for the new circle
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        
        x1, y1 = random.randint(0, canvas_width - 100), random.randint(0, canvas_height - 100)
        x2, y2 = x1 + 80, y1 + 80  # Smaller circle size
        
        # Generate a random color
        hue = random.random()
        rgb_color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        hex_color = f"#{int(rgb_color[0] * 255):02x}{int(rgb_color[1] * 255):02x}{int(rgb_color[2] * 255):02x}"
        
        # Move the existing circle and change its color
        canvas.coords(circle, x1, y1, x2, y2)
        canvas.itemconfig(circle, fill=hex_color)
    else:
        # Flash the screen red
         # Red color
        
        # Reset the counter if clicked outside the circle
        counter = 0
        counter_label.config(text=f"Counter: {counter}")

# Function to reset the counter if the canvas is clicked outside the circle
def reset_counter(event):
    global counter
    if not canvas.find_withtag(tk.CURRENT):
        flash_screen("#FF0000") 
        counter = 0
        counter_label.config(text=f"Counter: {counter}")

# Function to flash the screen with a specific color
def flash_screen(color):
    canvas.configure(bg=color)
    canvas.after(100, lambda: canvas.configure(bg="white"))  # Change back to white after 100ms

# Create the main window
root = tk.Tk()
root.title("Random Circle Drawing with Counter")
root.configure(bg="white")  # Set initial background color

# Initialize the counter
counter = 0

# Create a canvas widget
canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()

# Draw the initial circle
x1, y1, x2, y2 = 100, 100, 180, 180  # Initial smaller circle size
circle = canvas.create_oval(x1, y1, x2, y2, outline="black", fill="blue", width=2)

# Bind the click event to the move_circle function
canvas.tag_bind(circle, "<Button-1>", move_circle)

# Bind the canvas to reset the counter if clicked outside the circle
canvas.bind("<Button-1>", reset_counter)

# Create a label to display the counter
counter_label = tk.Label(root, text=f"Counter: {counter}")
counter_label.pack()

# Run the Tkinter event loop
root.mainloop()
