import customtkinter
from PIL import Image
from customtkinter import CTkImage

def start_program_command():
    print("Program Started")

# Set appearance to dark
customtkinter.set_appearance_mode("dark")

# Create the main window
root = customtkinter.CTk()
root.title("Sandeep's App")
root.geometry("800x600")

# Load the background image
try:
    bg_image = Image.open("Blue_Mountains.jpg")
    bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)
    # Convert the PIL image to a CTkImage for background
    bg_ctkimage = CTkImage(light_image=bg_image, dark_image=bg_image, size=bg_image.size)
    bg_label = customtkinter.CTkLabel(root, image=bg_ctkimage, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

except FileNotFoundError:
    print("Error: Background image not found. Please ensure bg.jpg exists in the same directory as the script.")
    bg_label = None

# Create the text label
text_label = customtkinter.CTkLabel(root, text="Sandeep's Program", font=("Helvetica", 36, "bold"))
text_label.place(relx=0.5, rely=0.4, anchor="center")

# Create the start button
start_button = customtkinter.CTkButton(root, text="Start Program", command=start_program_command, font=("Helvetica", 20), corner_radius=10)
start_button.place(relx=0.5, rely=0.6, anchor="center")

root.mainloop()