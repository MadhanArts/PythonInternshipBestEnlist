from tkinter import *
from tkinter import filedialog
import day16_project.ocr_converter as ocr_converter
from webbrowser import open


class OCRConverter(Tk):
    def __init__(self):
        super().__init__()
        self.title("OCR Converter")
        self.geometry("1000x500")

        container = Frame(self, padx=30, pady=20,
                          highlightbackground="green", highlightcolor="green", highlightthickness=1, bd=0)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.selectFileLabel = Label(container, text="Select Files", padx=30, pady=20, font=("Courier", 15, "bold"))
        self.selectFileLabel.pack()

        self.browseFileButton = Button(container, text="Browse", font=("Courier", 15),
                                       command=self.open_file_dialog)
        self.browseFileButton.pack()

        self.fileNamesLabel = Label(container, text="", font=("Courier", 15, "bold"))
        self.convertButton = Button(container, text="Convert to pdf", font=("Courier", 15))

        self.open_output_file_button = Button(container, text="OPEN", font=("Courier", 15))
        self.output_file_path_label = Label(container, font=("Courier", 15, "bold"))

        self.clear_all_button = Button(container, text="Clear All", font=("Courier", 15))

    def open_file_dialog(self):
        file_names = filedialog.askopenfilenames(initialdir="/", title="Select a file",
                                                 filetype=(("png", "*.png"), ("jpeg", "*.jpg"), ("All Files", "*.*")))

        formatted_file_names = ""
        for file_name in file_names:
            formatted_file_names += file_name + "\n"

        if file_names:
            self.fileNamesLabel.config(text=formatted_file_names)
            self.fileNamesLabel.pack()
            self.convertButton.config(command=lambda: self.convert_to_pdf(file_names))
            self.convertButton.pack()

    def convert_to_pdf(self, file_names):
        output_file = ""
        output_file += ocr_converter.convert_To_PDF(file_names)
        self.open_output_file_button.config(command=lambda: open(output_file))
        self.open_output_file_button.pack()
        self.output_file_path_label.config(text=output_file)
        self.output_file_path_label.pack()

        self.clear_all_button.config(command=self.clear_all)
        self.clear_all_button.pack()

    def clear_all(self):
        self.fileNamesLabel.pack_forget()
        self.convertButton.pack_forget()
        self.open_output_file_button.pack_forget()
        self.output_file_path_label.pack_forget()
        self.clear_all_button.pack_forget()


if __name__ == '__main__':
    root = OCRConverter()
    root.mainloop()
