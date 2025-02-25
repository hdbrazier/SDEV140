
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import PIL
from PIL import Image, ImageTk  

# Function for validating entries 
#def validateInput():
 

# Callback function for opening the second window
def requestTransfer():
    secondWindow = tk.Tk()
    secondWindow.title("Transfer Details")
    secondWindow.geometry("500x400")
    
    # Label in the second window
    message = tk.Label(secondWindow, text="Please fill in the form", font=("Arial", 14))
    message.pack()
    
    # Label and Input Field for patient name
    patientNameLbl = tk.Label(secondWindow, text="Patient Name:")
    patientNameLbl.pack()
    patientNameInput = tk.Entry(secondWindow)
    patientNameInput.pack()
    
    # Label and Input Field for patient weight
    patientWeightLbl = tk.Label(secondWindow, text="Patient Weight:")
    patientWeightLbl.pack()
    patientWeightInput = tk.Entry(secondWindow)
    patientWeightInput.pack()
    
    # Label and Input Field for reason for transfer
    reasonLbl = tk.Label(secondWindow, text="Reason for transfer:")
    reasonLbl.pack()
    reasonInput = tk.Entry(secondWindow)
    reasonInput.pack()

    # Button to Submit the form data
    buttonSubmit = tk.Button(secondWindow, text="Submit", command=submitFormData(sendingList, receivingList, patientNameInput, patientWeightInput, reasonInput), font=("Arial", 12))
    buttonSubmit.pack()
    
    # Button to Close the second window
    buttonClose = tk.Button(secondWindow, text="Close", command=secondWindow.destroy)
    buttonClose.pack()

# Function to handle form submission in the second window
def submitFormData(sendingList, receivingList, patientNameInput, patientWeightInput, reasonInput):
    From = sendingList.get()
    To = receivingList.get()
    Name = patientNameInput.get()
    Weight = patientWeightInput.get()
    Reason = reasonInput.get()
    
# Callback function for the "Exit" button
#def exitProgram():
    # response = 
    # if response:
      #  window.quit()

# Main window
window = tk.Tk()
window.title("Request Air Medical Transport")
window.geometry("500x400")

# First Dropdown Menu (options to choose) 
sendingLbl = tk.Label(window, text="Choose Sending Facility:")
sendingLbl.pack()
sendingList = ttk.Combobox(window, values=["Marion General", "Kokomo St.V", "Anderson St.V"])
sendingList.pack()

# Second Dropdown Menu (options to choose)
receivingLbl = tk.Label(window, text="Choose Receiving Facility:")
receivingLbl.pack()
receivingList = ttk.Combobox(window, values=["86th St", "Methodist", "Heart Center", "Ezkenazi", "Riley"])
receivingList.pack()

# Label in the main window
greeting = tk.Label(window, text="Request Air Medical Transport", font=("Arial", 16))
greeting.pack()

# Load and display image 1 in the main window
img1 = Image.open("image1.jpg")  

# Load and display image 2 in the main window
img2 = Image.open("image2.jpg")  

# Button to request transfer
buttonTransfer = tk.Button(window, text="Request Transfer", command=requestTransfer, font=("Arial", 12))
buttonTransfer.pack()

# Button to exit the program
#buttonExit = tk.Button(window, text="Exit", command=exitProgram, font=("Arial", 12))
#buttonExit.pack()

# Run the program
window.mainloop()
