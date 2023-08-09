import tkinter as tk
from PIL import Image, ImageTk
from generate_image import resize_image

def display_dependency_tree_image(png_data, initial_width=800, initial_height=600):
    # Create a new Tkinter window
    root = tk.Tk()
    root.title("Dependency Tree")

    # Set a fixed initial window size
    root.geometry(f"{initial_width}x{initial_height}")

    def fit_image(event):
        # Get the available space within the window
        width = event.width
        height = event.height

        # Load the image and resize it to fit within the window
        img_resized = resize_image(png_data, width, height)

        # Update the image in the Tkinter window
        tk_image = ImageTk.PhotoImage(img_resized)
        label.config(image=tk_image)
        label.image = tk_image  # Keep a reference to avoid garbage collection

    # Load the initial image and display it in the Tkinter window
    img_resized = resize_image(png_data, initial_width, initial_height)
    tk_image = ImageTk.PhotoImage(img_resized)
    label = tk.Label(root, image=tk_image)
    label.pack(fill=tk.BOTH, expand=tk.YES)

    # Bind the <Configure> event to the fit_image function
    label.bind("<Configure>", fit_image)

    # Start the Tkinter main loop
    root.mainloop()
