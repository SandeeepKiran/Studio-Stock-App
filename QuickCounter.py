import tkinter as tk
from tkinter import ttk  # Import the themed Tk widgets
import tkinter.font as tkFont  # Import the font module

class CounterApp:
    def __init__(self, master):
        """
        Initializes the Counter Application.

        Args:
            master: The Tkinter root window.
        """
        self.master = master
        master.title("Sand's Counter App")  # Set the window title

        # Window Titlebar App icon
        try:
            root.iconbitmap("C:/Users/sande/Music/Myp/App_Icons/Counter_App.ico")  # This may work for some systems
        except:
            pass

        # --- Styling ---
        bg_color = "white"  # Background color
        fg_color = "black"  # Foreground color (text color)
        button_color = "#E0E0E0" # Light gray button color, similar to Material You

        master.configure(bg=bg_color) # Set background color of the main window.

        # --- Font ---
        self.font = tkFont.Font(family="Calibri", size=12, weight="bold")  # Use Calibri font

        # --- Counter Variable ---
        self.counter = 0  # Initialize the counter
        self.counter_label = tk.Label(master, text="Sand's Counter App", font=tkFont.Font(family="Calibri", size=12), bg=bg_color, fg=fg_color)
        self.counter_label.pack(pady=(10,0)) # Add some padding above the label.

        self.number_font = tkFont.Font(family="Calibri", size=16, weight="bold")  # New font for the number
        self.number_label = tk.Label(master, text=str(self.counter), font=self.number_font, bg=bg_color, fg=fg_color)  # Label to display the counter value
        self.number_label.pack(pady=5)  # Add some vertical padding

        # --- Frame for Buttons ---
        button_frame = tk.Frame(master, bg=bg_color) # Create frame to hold buttons
        button_frame.pack(pady=10) # Add padding around the frame

        # --- Minus Button ---
        self.minus_button = tk.Button(button_frame, text="-", command=self.decrement_counter, width=3, height=1, bg=button_color, fg=fg_color, font=self.font)
        self.minus_button.pack(side=tk.LEFT, padx=7) # Add some horizontal padding

        # --- Reset Button ---
        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset_counter, bg=button_color, fg=fg_color)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        # --- Plus Button ---
        self.plus_button = tk.Button(button_frame, text="+", command=self.increment_counter, width=3, height=1, bg=button_color, fg=fg_color, font=self.font)
        self.plus_button.pack(side=tk.LEFT, padx=7)  # Add some horizontal padding


    def increment_counter(self):
        """Increments the counter and updates the label."""
        self.counter += 1
        self.number_label.config(text=str(self.counter))  # Update the label text

    def decrement_counter(self):
        """Decrements the counter and updates the label."""
        self.counter -= 1
        self.number_label.config(text=str(self.counter))  # Update the label text

    def reset_counter(self):
        """Resets the counter to 0 and updates the label."""
        self.counter = 0
        self.number_label.config(text=str(self.counter))  # Update the label text

# --- Main Program ---
if __name__ == "__main__":
    root = tk.Tk()  # Create the main Tkinter window
    app = CounterApp(root)  # Create the CounterApp object
    root.geometry("200x150") # Set the size of the window
    root.mainloop()  # Start the Tkinter event loop