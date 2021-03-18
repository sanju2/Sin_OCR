import os
import pygubu
import tkinter as tk
import tkinter.ttk as ttk
from Ocr import Ocr
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *


PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "frontend.ui")


class FillerUI:
    # Initializing pygubu builder and objects
    def __init__(self, parent):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('top_level', parent)
        self.name_entry = builder.get_object('name_entry', parent)
        self.gender_entry = builder.get_object('gender_entry', parent)
        self.dob_entry = builder.get_object('dob_entry', parent)
        self.pob_entry = builder.get_object('pob_entry', parent)
        self.nic_entry = builder.get_object('nic_entry', parent)
        self.address_entry = builder.get_object('address_entry', parent)
        self.selected_template_label = builder.get_object(
            'selected_template_label', parent)
        self.loading_label = builder.get_object(
            'loading_label', parent)
        builder.connect_callbacks(self)

    # function called on NIC back image button click
    def getBackImageData(self):
        self.loading_label['text'] = "Processing image ..."
        # open file dialog
        root.filename = filedialog.askopenfilename(
            initialdir="/", title="Select Back Image", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

        # checking if select image dialog is canceled
        if(not isinstance(root.filename, str)or root.filename == ""):
            self.loading_label['text'] = ""
            return
        # creating instance of Ocr class in Ocr.py file
        ocr = Ocr()
        # response contains address and place of birth
        address, pob = ocr.extractBackImageData(root.filename)

        # processing image label is set to empty(Can adapt a progress bar in future)
        self.loading_label['text'] = ""

        # response is set to input fields in UI.
        # Here it's a best practice to delete field data before inserting
        self.address_entry.delete(0, tk.END)
        self.address_entry.insert(0, address)

        self.pob_entry.delete(0, tk.END)
        self.pob_entry.insert(0, pob)

    # function called on NIC front image button click
    def getFrontImageData(self):
        # open file dialog
        self.loading_label['text'] = "Processing image ..."
        root.filename = filedialog.askopenfilename(
            initialdir="/", title="Select Front Image", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

        # checking if select image dialog is canceled
        if(not isinstance(root.filename, str) or root.filename == ""):
            self.loading_label['text'] = ""
            return

        ocr = Ocr()
        name, gender, dob, nic = ocr.extractFrontImageData(root.filename)
        self.loading_label['text'] = ""
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, name)

        self.gender_entry.delete(0, tk.END)
        self.gender_entry.insert(0, gender)

        self.dob_entry.delete(0, tk.END)
        self.dob_entry.insert(0, dob)

        self.nic_entry.delete(0, tk.END)
        self.nic_entry.insert(0, nic)

    # function called on Select template button
    def openTemplateDialog(self):
        # opens file dialog
        root.filename = filedialog.askopenfilename(
            initialdir="/", title="Select Template Document", filetypes=(("docx files", "*.docx"), ("all files", "*.*")))

        # checking if select image dialog is canceled
        if(not isinstance(root.filename, str) or root.filename == ""):
            self.selected_template_label['text'] = "Selected template"
            return

        # selected file path is set to the label
        self.selected_template_label['text'] = root.filename

    # function called on Fill template button
    def fillTemplate(self):
        # selected file path is retrieved from the label
        template = self.selected_template_label['text']

        # if no template files selected will return with warning msg
        if(template == "Selected template"):
            messagebox.showwarning(
                title="No template", message="Select template document first")
            return

        name = self.name_entry.get()
        gender = self.gender_entry.get()
        nic = self.nic_entry.get()
        dob = self.dob_entry.get()
        address = self.address_entry.get()
        pob = self.pob_entry.get()
        ocr = Ocr()
        # response contains the name of the genrated file
        saved_name = ocr.fillForm(
            template, name, gender, nic, dob, address, pob)
        messagebox.showinfo(
            title="Success", message="Document generated successfully as "+saved_name)

    # function called on clear button click
    def clear(self):
        self.name_entry.delete(0, tk.END)
        self.gender_entry.delete(0, tk.END)
        self.nic_entry.delete(0, tk.END)
        self.dob_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.pob_entry.delete(0, tk.END)
        self.selected_template_label['text'] = "Selected template"
        self.loading_label['text'] = ""

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    root.title("Document Filler using NIC")
    app = FillerUI(root)
    app.run()
