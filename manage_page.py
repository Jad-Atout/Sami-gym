import tkinter
from datetime import timedelta, datetime

import customtkinter as ctk
import tkinter as tk
from tkcalendar import DateEntry
import ttkbootstrap

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
        self.name_label = ctk.CTkLabel(self,
                                      text="Name")
        self.name_label.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")
        customer_name  =tk.StringVar(value="Jad Atout")

        # Name Entry Field
        self.customer_name_label = ctk.CTkLabel(self,
                                      textvariable=customer_name)
        self.customer_name_label.grid(row=0, column=1,
                            columnspan=1, padx=20,
                            pady=20, sticky="ew")


        self.age_label = ctk.CTkLabel(self,text="Age")
        self.age_label.grid(row=0, column=2,
                            padx=20, pady= 20,
                            sticky= "ew")
        self.age_value_label = ctk.CTkLabel(self, text="18")
        self.age_value_label.grid(row=0, column=3,
                            padx=20, pady=20,
                            sticky="ew")

        # Generate Date
        self.last_subscription_label = ctk.CTkLabel(self, text="Last Subscription")
        self.last_subscription_label.grid(row=4, column=0,
                                               padx=20, pady=20,
                                               sticky="ew")
        self.last_subscription_date_label= ctk.CTkLabel(self,text="7/7/2024")
        self.last_subscription_date_label.grid(row=4, column=1,
                                          padx=(10,20), pady=20,
                                          sticky="ew")

        self.new_subscription_label = ctk.CTkLabel(self, text="New Date")
        self.new_subscription_label.grid(row=4, column=2,
                                          padx=20, pady=20,
                                          sticky="ew")
        current_date = datetime.now()
        future_date = current_date + timedelta(days=30)
        default_date = tk.StringVar(value=future_date.strftime("%d/%m/%Y"))
        self.new_date_label = ctk.CTkButton(self,textvariable=default_date,command=self.set_date)
        self.new_date_label.grid(row=4,column=3,
                                 padx=20, pady=20,
                                 sticky="ew")


        # Choice Label
        self.choiceLabel = ctk.CTkLabel(self,
                                        text="Payment State")
        self.choiceLabel.grid(row=5, column=0,
                              padx=20, pady=20,
                              sticky="ew")



        # Choice Check boxes
        self.checkboxVar = tk.StringVar()

        self.choice1 = ctk.CTkCheckBox(self, text="Non-Paid",
                                       variable=self.checkboxVar,
                                       onvalue="Paid",
                                       offvalue="Non-Paid")
        self.choice1.grid(row=5, column=1, padx=20,
                          pady=20, sticky="ew")

        self.choice2 = ctk.CTkCheckBox(self, text="Non-Paid",
                                       variable=self.checkboxVar,
                                       onvalue="Non-Paid",
                                       offvalue="Paid")
        self.choice2.grid(row=5, column=2, padx=20, pady=20,
                          sticky="ew")


        # Generate Button
        self.columnconfigure(0,weight=1)
        self.columnconfigure(2, weight=1)
        self.delete_customer = ctk.CTkButton(self,
                                   text="Submit")
        self.delete_customer.grid(row=6, column=0,
                        columnspan=1,
                        padx=20, pady=20,
                        sticky="ew")
        # Generate Button
        self.renew = ctk.CTkButton(self,
                                   text="Delete Customer")
        self.renew.grid(row=6, column=2,
                        columnspan=1,
                        padx=20, pady=20,
                        sticky="ew")
        # Text Box
        self.displayBox = ctk.CTkTextbox(self, width=200,
                                         height=100)
        #self.displayBox.grid(row=6, column=0, columnspan=4,
                            # padx=20, pady=20, sticky="nsew")
    def set_date(self):
        root =tkinter.Tk()
        cal = DateEntry(root, width=30, bg="darkblue", fg="white")
        cal.grid()
        root.mainloop()


if __name__ == "__main__":
    app = App()
    app.mainloop()