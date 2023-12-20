

#%%


sc_blue='#00144d'
sc_light_green='#09e1c0'
sc_alt_green='#7EBEC5'



import tkinter as tk
from tkinter import ttk


root=tk.Tk()
root.geometry('300x200')

frame=ttk.Frame(root,width=200)
frame.grid()

ttk.Style().theme_create('my_style', parent='alt',
                         settings = {
                                    'TCombobox':
                                        {'configure':
                                            {'fieldbackground': sc_alt_green,
                                            'background': sc_alt_green,
                                            'foreground' : 'white'
                                            }
                                        },
                                    'TFrame':
                                        {'configure':
                                            {'background': sc_alt_green,
                                            'foreground' : 'white'
                                            }
                                        }
                                    }
                         )

# ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
ttk.Style().theme_use('my_style') 


fill_form_title2 = tk.Label(frame,text="fill the following form",bg='green')
fill_form_title2.grid(column=0,row=0)

fill_form_title1 = tk.Label(frame,text="fill the following form",bg='red')
fill_form_title1.grid(column=0,row=0)


root.mainloop()


# %%
