import tkinter
import tkinter as tk
from datetime import *
from dateutil.relativedelta import relativedelta
import ttkbootstrap as ttk

def search():
    pass
def add_customer():
    state.set("تمت العملية بنجاح")
    success_lable.configure(background='green',foreground='white')

root = ttk.Window(themename='darkly')
root.title("Sami Gym")
root.geometry("900x800")
styl = ttk.Style()
styl.configure('Custom.TFrame',bordercolor='white')
payment_state = tkinter.BooleanVar()
add_customer_frame = ttk.Frame(master=root,padding=20,borderwidth=2,style='Custom.TFrame')
name_entry =    ttk.Entry(master=add_customer_frame,font=('arial',12))
date_entry =    ttk.DateEntry(master=add_customer_frame,bootstyle='darkly')
payment_button = ttk.Checkbutton(master=add_customer_frame,text='واصل',variable=payment_state,bootstyle = "success",command=add_customer)
name_label = ttk.Label(master=add_customer_frame,text='اسم العميل')
date_label = ttk.Label(master=add_customer_frame,text='تارخ الاشتراك')



name_entry.grid   (row=1,column=2,padx=5,sticky='e')
date_entry.grid   (row=1,column=1,padx=5,sticky='e')
payment_button.grid(row=1,column=0,padx=1)
name_label.grid   (row=0,column=2,padx=5)
date_label.grid   (row=0,column=1,padx=5)
add_customer_frame.grid(row=0, column=1, sticky='ne')
root.columnconfigure(0, weight=1)

submit = ttk.Button(master=add_customer_frame,text="اضافة",padding=(40,5),command=add_customer)
state= tkinter.StringVar()
success_lable = ttk.Label(master=add_customer_frame,textvariable=state)
success_lable.grid(row=2,column=0,pady=10)
submit.grid(row=2,pady=10,column=1)


# searching for a user
search_var = tkinter.StringVar()
search_frame = ttk.Frame(root,padding=20)
search_entry = ttk.Entry(search_frame,font=('arial',15))
search_lable = ttk.Label(search_frame,text="ادخل اسم المستخدم",font=('arial',15))
search_button = ttk.Button(search_frame,text='بحث')
search_entry.grid(row=1,column=3,padx=5,pady=10)
search_lable.grid(row=0,column=3,padx=5,pady=10)
search_button.grid(row=2,column=3,padx=5,pady=10)
search_frame.grid(row=1,column=1,sticky='ne')
#search results
def add_b():
    sub_window = ttk.Toplevel(root)
    paid_var = tkinter.StringVar()
    sub_window.title("Sami Gym")
    sub_window.geometry("400x400")
    name_label = ttk.Label(sub_window, text='جاد عطعوط', font=('arial', 15))
    current_date = datetime.now()
    next_date = current_date + relativedelta(months=1)
    date_entry = ttk.DateEntry(sub_window, bootstyle='primary', dateformat='%Y-%m-%d', startdate=next_date)
    payment_state = ttk.Checkbutton(sub_window, text='واصل', variable=paid_var)
    note_label = ttk.Label(sub_window, text='ملاحظات', font=('arial', 15))
    note_entry = ttk.Entry(sub_window, bootstyle="info")
    note_label.grid(row=1, column=3)
    note_entry.grid(row=1, columnspan=3, sticky='ew', pady=10)
    name_label.grid(row=0, column=2, sticky='ew')
    date_entry.grid(row=0, column=1, )
    payment_state.grid(row=0, column=0, )
    sub_window.columnconfigure(0, weight=1)
    sub_window.columnconfigure(1, weight=1)
    sub_window.columnconfigure(2, weight=1)

    sub_window.mainloop()
result_frame = ttk.Frame(root,padding=(20,20))
result_name_label =ttk.Label(result_frame,text="جاد عطعوط",font=('arial',15))
result_state_label = ttk.Label(result_frame,text="مستمر",font=('arial',15),bootstyle='inverse-success')
result_date_label = ttk.Label(result_frame,text="24/10/2024",font=('arial',15))
subsicription_button = ttk.Button(result_frame,text='تجديد الاشتراك' ,command=add_b)
output_name_lable = ttk.Label(result_frame,text=":الاسم ",font=('arial',15))
output_state_lable = ttk.Label(result_frame,text=":الحالة ",font=('arial',15))
output_date_lable = ttk.Label(result_frame,text=":تارخ الانتهاء ",font=('arial',15))

result_name_label.grid(row=0,column=2,padx=5,pady=10)
output_name_lable.grid(row=0,column=3,padx=5,pady=10)

result_state_label.grid(row=0,column=0,padx=5,pady=10)
output_state_lable.grid(row=0,column=1,padx=5,pady=10)

output_date_lable.grid(row=1,column=3,padx=5,pady=10)
result_date_label.grid(row=1,column=2,padx=5,pady=10)

subsicription_button.grid(row=1,column=0,padx=5,pady=10)

result_frame.grid_columnconfigure(2, weight=1)
result_frame.grid_columnconfigure(1, weight=1)
result_frame.grid(row=1,column=0,sticky='ne')
root.mainloop()