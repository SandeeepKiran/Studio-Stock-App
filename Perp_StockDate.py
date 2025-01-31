import customtkinter as ctk
from PIL import Image, ImageTk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set the appearance mode to dark
        ctk.set_appearance_mode("dark")
        
        # Set window size and title
        self.geometry("600x400")
        self.title("Sandeep's Program")
        
        # Load and set background image
        self.bg_image = Image.open(r"C:\Users\sande\Music\Myp\Blue_Mountains.jpg")  # Use raw string or escape backslashes
        self.bg_image = self.bg_image.resize((600, 400), Image.LANCZOS)  # Change ANTIALIAS to LANCZOS
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        # Create a label for the background image
        self.background_label = ctk.CTkLabel(self, image=self.bg_photo)
        self.background_label.place(relwidth=1, relheight=1)

        # Create a label for the program title
        self.title_label = ctk.CTkLabel(self, text="Sandeep's Program", font=("Arial", 24))
        self.title_label.pack(pady=(150, 10))

        # Create a button
        self.start_button = ctk.CTkButton(self, text="Start Program", command=self.start_program)
        self.start_button.pack(pady=(10, 20))

    def start_program(self):
        print("Program Started!")

if __name__ == "__main__":
    app = App()
    app.mainloop()
