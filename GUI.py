import os
import sqlite3
from datetime import datetime
from pathlib import Path

import customtkinter
from PIL import Image
customtkinter.set_widget_scaling(1.5)
current_date = datetime.now()
db_path = os.path.join(Path.cwd(), r"Sami Gym.db")
def over_due_lister():

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    sql_statement = "SELECT Name FROM Subscribers WHERE End_Date < current_date "
    cursor.execute(sql_statement)

    result = cursor.fetchall()

    print(result)
    for row in result:
        name = row[0]

        app.scrollable_label_button_frame.add_customer(f"{name}")
def search():
    pass
class main_page(customtkinter.CTk):
    def __init__(self):
        super(main_page, self).__init__()
        # configure window
        self.title("Sami Gym")
        self.geometry(f"{1100}x{580}")
        
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_columnconfigure(3, weight=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self,placeholder_text='Enter User Name',width=600)
        self.entry.place(x=250, y=20)

        self.search_button = customtkinter.CTkButton(self,border_width=2,fg_color="transparent",text_color=("gray10", "#DCE4EE"),text="Search",command=search)
        self.search_button.place(y= 20,x=925)
        
        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self,width=140,corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0,rowspan=4,sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5,weight=1)
        # create label widget
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame,text="Hello, Sami!",
                                                 font=customtkinter.CTkFont(size=20,weight="bold"))
        self.logo_label.grid(row=0,column=0, padx=20,pady=(20,10))
        # create side buttons frame
        self.sidebar_buttons_frame = customtkinter.CTkFrame(self.sidebar_frame,width=140,corner_radius=0)
        #self.sidebar_buttons_frame.grid(row=1,column=0,padx=20,pady=10)
        # create sidebar buttons
        self.sidebar_button_1 = customtkinter.CTkButton(master=self.sidebar_frame,text="Add User",command=over_due_lister)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Non-paid Users")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Non-renewing Users")
        self.sidebar_button_3.grid(row=4, column=0, padx=20, pady=10)
        
        self.mode_label= customtkinter.CTkLabel(self.sidebar_frame,text="Appearance Mode:",anchor="w")
        self.mode_label.place(x=60, y=515)
        
        self.mode_option_menu = customtkinter.CTkOptionMenu(self.sidebar_frame,values=["Light", "Dark", "System"],
                                                            command=self.change_mode)
        self.mode_option_menu.grid(row=6,column=0,padx=20,pady=(10,10))

        # creating user image
        image_path = os.path.join(Path.cwd(), r"pics")
        self.user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path,r"light_user.png")),
                                                 dark_image=Image.open(os.path.join(image_path,r"dark_user.png")))

        self.scrollable_label_button_frame = Scrollable_label_button_frame(self, width=800, height=500,
                                                                           command=self.label_button_frame_event,
                                                                           corner_radius=0)
        self.scrollable_label_button_frame.place(x=250, y=60)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        sql_statement = "SELECT Name FROM Subscribers WHERE End_Date < current_date "
        cursor.execute(sql_statement)
        result = cursor.fetchall()
        print(result)
        for row in result:
            name = row[0]
            self.scrollable_label_button_frame.add_customer(f"{name}")


    def label_button_frame_event(self,customer):
        pass
    def change_mode(self):
        pass


class Scrollable_label_button_frame(customtkinter.CTkScrollableFrame):
    def __init__(self,master,command=None,**kwargs):
        super().__init__(master,**kwargs)
        self.grid_columnconfigure(0,weight=1)
        self.command = command
        self.radio_button_variable = customtkinter.StringVar()
        self.label_list = []
        self.button_list = []

    def add_customer(self,customer,image=None):
        label = customtkinter.CTkLabel(self,text=customer,image=image,compound="left",padx=5,anchor="w")
        button = customtkinter.CTkButton(self,text="manage",width=100,height=24)
        if self.command is not None:
            button.configure(command=lambda:self.command(customer))
        label.grid(row = len(self.label_list), column=0, pady=(0, 10), sticky="w")
        button.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5)
        self.label_list.append(label)
        self.button_list.append(button)


    def remove_customer(self,customer):
        for label,button in zip(self.label_list, self.button_list):
            if customer == label.cget("text"):
                label.destroy()
                button.destroy()
                self.label_list.remove(label)
                self.button_list.remove(button)
                return 
            
            


if __name__ == "__main__":
    app = main_page()
    app.mainloop()











