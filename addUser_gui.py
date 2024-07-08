# Python program to create a basic GUI
# application using the customtkinter module

import customtkinter as ctk
import tkinter as tk

# Basic parameters and initializations
# Supported modes : Light, Dark, System
ctk.set_appearance_mode("System")



appWidth, appHeight = 600, 700


# App Class
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Add Customer")
        self.geometry(f"{appWidth}x{appHeight}")

        # Name Label
        self.first_name_label = ctk.CTkLabel(self,
                                      text="First Name")
        self.first_name_label.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")
        self.last_name_label = ctk.CTkLabel(self,
                                             text="Last Name")
        self.last_name_label.grid(row=1, column=0,
                                   padx=20, pady=20,
                                   sticky="ew")

        # Name Entry Field
        self.first_name_entry = ctk.CTkEntry(self,
                                      placeholder_text="Jad")
        self.first_name_entry.grid(row=0, column=1,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")

        self.last_name_entry = ctk.CTkEntry(self,
                                             placeholder_text="Jad")
        self.last_name_entry.grid(row=1, column=1,
                                   columnspan=3, padx=20,
                                   pady=20, sticky="ew")

        # Age Label
        self.ageLabel = ctk.CTkLabel(self,
                                     text="Age")
        self.ageLabel.grid(row=2, column=0,
                           padx=20, pady=20,
                           sticky="ew")

        # Age Entry Field
        self.ageEntry = ctk.CTkEntry(self,
                                     placeholder_text="18")
        self.ageEntry.grid(row=2, column=1,
                           columnspan=3, padx=20,
                           pady=20, sticky="ew")

        # Gender Label
        self.genderLabel = ctk.CTkLabel(self,
                                        text="Gender")
        self.genderLabel.grid(row=3, column=0,
                              padx=20, pady=20,
                              sticky="ew")

        # Gender Radio Buttons
        self.genderVar = tk.StringVar()

        self.maleRadioButton = ctk.CTkRadioButton(self,
                                                  text="Male",
                                                  variable=self.genderVar,
                                                  value="Male")
        self.maleRadioButton.grid(row=3, column=1, padx=20,
                                  pady=20, sticky="ew")

        self.femaleRadioButton = ctk.CTkRadioButton(self,
                                                    text="Female",
                                                    variable=self.genderVar,
                                                    value="Female")
        self.femaleRadioButton.grid(row=3, column=2,
                                    padx=20,
                                    pady=20, sticky="ew")


        # Choice Label
        self.choiceLabel = ctk.CTkLabel(self,
                                        text="Payment State")
        self.choiceLabel.grid(row=4, column=0,
                              padx=20, pady=20,
                              sticky="ew")

        # Choice Check boxes
        self.checkboxVar = tk.StringVar()

        self.choice1 = ctk.CTkCheckBox(self, text="Non-Paid",
                                       variable=self.checkboxVar,
                                       onvalue="Paid",
                                       offvalue="Non-Paid")
        self.choice1.grid(row=4, column=1, padx=20,
                          pady=20, sticky="ew")

        self.choice2 = ctk.CTkCheckBox(self, text="Non-Paid 2",
                                       variable=self.checkboxVar,
                                       onvalue="Non-Paid",
                                       offvalue="Paid")
        self.choice2.grid(row=4, column=2, padx=20, pady=20,
                          sticky="ew")



        # Generate Button
        self.generateResultsButton = ctk.CTkButton(self,
                                                   text="Submit")
        self.generateResultsButton.grid(row=5, column=1,
                                        columnspan=2,
                                        padx=20, pady=20,
                                        sticky="ew")

        # Text Box
        self.displayBox = ctk.CTkTextbox(self, width=200,
                                         height=100)
        #self.displayBox.grid(row=6, column=0, columnspan=4,
                            # padx=20, pady=20, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()