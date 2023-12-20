#%%no comments


'''
    Blue : RGB: 0, 20, 77 - HEX : #00144d

    Light Green : RGB: 9, 225, 192 - HEX : #09e1c0

    There is also a "Muted" Green (for the icons)   
    Alt Green : RGB: 126, 190, 197 - HEX : #7EBEC5
'''
sc_blue='#00144d'
sc_light_green='#09e1c0'
sc_alt_green='#7EBEC5'



# from os import chdir,path
import re
# wd= path.dirname(__file__)
# main_dir=re.findall('(.*)(?:\\\GUI)',wd)[0]
# chdir(main_dir+'\\week_calendar')
from week_calendar_for_students import week_calendar_for_students

import tkinter as tk
import tkinter.filedialog
from tkinter import ttk



# def callbackFunc():
#     resultString.set("{} - {}".format(landString.get(),
#                                       cityString.get()))





root=tk.Tk()


from tkinter import ttk
# ttk.Style().theme_create('my_style', parent='alt',
#                          settings = {
#                                     'TCombobox':
#                                         {'configure':
#                                             {'fieldbackground': sc_alt_green,
#                                             'background': sc_alt_green,
#                                             'foreground' : 'white'
#                                             }
#                                         }
#                                     }
#                          )

# # ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
# ttk.Style().theme_use('my_style') 



import tkinter.font as tkFont
rubik_bold = tkFont.Font(root,family='Rubik', size=10,weight='bold')


width_of_root_frame=800
height_of_root_frame=600
root.geometry(str(width_of_root_frame)+"x"+str(height_of_root_frame))
root.resizable(width=False, height=False)
#Set root background color 
root.config(background = sc_blue) 
default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(family='Rubik', size=10,weight='bold')


root.title('make a nice calendar')

##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##########################################################
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##########################################################

##title frame
title_frame=tk.Frame(root,bg=sc_blue)
title_frame.grid(columnspan=2)
fill_form_title = tk.Label(title_frame,text="fill the following form", fg="white",bg=sc_blue,font=rubik_bold)
fill_form_title.grid(columnspan=3)


# # # logo at the end
# import os
# base_folder = os.path.dirname(__file__)+'\\images'
# image_path = os.path.join(base_folder, 'LOGO_blue_white_small.png')
# logo = tk.PhotoImage(master=title_frame,file=image_path)
# labelExample = tk.Label(title_frame, image=logo,bg=sc_blue)


# labelExample.grid(row=0,column=3,sticky='nw')


   

   
#button_exit.grid(column = 1,row = 3) 






##########################################################
##                                                      ##
##                                                      ##
##                                                      ##
##########################################################
##############################                          ##
##############################                          ##
##############################                          ##
##############################                          ##
##############################                          ##
##############################                          ##
##########################################################
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##########################################################


##add coeffs per day frame
coeff_per_day_frame=tk.Frame(root,bg=sc_blue,
#highlightbackground=sc_light_green, highlightthickness=4
)


coeff_per_day_frame.grid(row=1)



list_of_days=[['Monday'],['Tuesday'],['Wednesday'],['Thursday'],['Friday'],['Saturday'],['Sunday']]

iter_on_days=0

for day in sum(list_of_days, []):


    list_of_days[iter_on_days].append(tk.Label(coeff_per_day_frame,text = day,fg='#ffffff',bg=sc_blue,activebackground=sc_light_green,highlightbackground=sc_alt_green))
    list_of_days[iter_on_days].append(tk.IntVar())
    list_of_days[iter_on_days].append(tk.Scale(coeff_per_day_frame, from_=8, to=0, orient='vertical',bg=sc_alt_green,fg='black'))
    if iter_on_days<5:
        list_of_days[iter_on_days][3].set(1)
    else:
        list_of_days[iter_on_days][3].set(4)
    list_of_days[iter_on_days][1].grid(row=2,column=iter_on_days)
    list_of_days[iter_on_days][3].grid(row=1,column = list_of_days[iter_on_days][1].grid_info()['column'])
    iter_on_days=iter_on_days+1





coeff_per_day_frame.update()


##########################################################
##                                                      ##
##                                                      ##
##                                                      ##
##########################################################
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##########################################################
##############################                          ##
##############################                          ##
##############################                          ##
##############################                          ##
##############################                          ##
##############################                          ##
##########################################################





#####options subframe
option_frame=tk.Frame(root,bg=sc_blue)
option_frame.grid(row=2)


###browse excel button
# file explorer root 
import re
calendar_from_student_name=''
folder_with_templates='c:\\Users\\vicki_la_tombe\\Dropbox\\Boulots\\Scientia\\Developping\\calendar_for_students\\Scripts\\week_calendar\\excel_templates'


rubik_medium = tkFont.Font(root,family='Rubik', size=9,weight='bold')
def browseFiles(): 
    global calendar_from_student_name
    filename = tk.filedialog.askopenfilename(initialdir = folder_with_templates, 
                                          title = "Select a File", 
                                          filetypes = (("Excel files", 
                                                        "*.xlsx*"), 
                                                       ("all files", 
                                                        "*.*"))) 
       
    # Change label contents 
    label_file_explorer.configure(text="File: "+re.findall('\w*\.xlsx',filename)[0],fg='white') 
    calendar_from_student_name=filename
                                                                                                   


   
# Create a File Explorer label 
label_file_explorer = tk.Label(option_frame,  
                            text = "",   
                            bg=sc_blue) 
   
       
button_explore = tk.Button(option_frame,  
                        text = "Browse File", 
                        command = browseFiles,
                        fg='black',
                        bg=sc_alt_green
                        )  
   
#button_exit = tk.Button(root,  
#                     text = "Exit", 
#                     command = exit)  
   
button_explore.grid(sticky='w') 
label_file_explorer.grid(row=0,column=0,columnspan=4,sticky='e') 
##choosing name of output
output_label=tk.Label(option_frame, 
                        text='choose a name for the final timetable:',
                        fg='white',
                        bg=sc_blue,
                        justify='right')

output_entry=tk.Entry(option_frame,justify='right',bg='white')
xslx_label=tk.Label(option_frame, text='.xlsx',
                        fg='white',
                        bg=sc_blue,
                        justify='left')

output_label.grid(rowspan=2,sticky='e')
output_entry.grid(row=1,column=2)
xslx_label.grid(row=1,column=3)
##choosing amount of hours
hours_label=tk.Label(option_frame, text='choose a total amount of hours:',
                        fg='white',
                        bg=sc_blue,
                        justify='right')
hours_entry=tk.Entry(option_frame,justify='right')

hours_label.grid(rowspan=2,sticky='e')
hours_entry.grid(row=3,column=2)


##check button for deleting original calendar
delete_original = tk.BooleanVar() 
#delete_original.set(True)
 
check_button_delete = tk.Checkbutton(option_frame,
                            text='delete original calendar entries',
                            var=delete_original,bg=sc_blue,fg='white',selectcolor='black') 




##text before running the macro option
fill_form = tk.Label(option_frame, text="do you want the calendar in final form?",height=3, fg="white",bg=sc_blue)

check_button_delete.grid(columnspan=4)
fill_form.grid(columnspan=4)



##run macro or not
run_the_macro = tk.BooleanVar()
#tk.IntVar() if integer values
 
macro_on = tk.Radiobutton(option_frame, text='make the calendar nice straight ahead',
                             variable=run_the_macro, value=True,fg='white',bg=sc_blue,selectcolor='black') 
macro_off = tk.Radiobutton(option_frame, text='let me modify it a bit before',
                             variable=run_the_macro, value=False,fg='white',bg=sc_blue,selectcolor='black') 

macro_on.grid(columnspan=4)
macro_off.grid(columnspan=4)



option_frame.update()
col_count, row_count = option_frame.grid_size()
for row in range(row_count):
    option_frame.grid_rowconfigure(row, minsize=10)



##########################################################
##                                                      ##
##                                                      ##
##                                                      ##
##########################################################
##                          ##############################
##                          ##############################
##                          ##############################
##                          ##############################
##                          ##############################
##                          ##############################
##########################################################
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##########################################################



rubik_small = tkFont.Font(root,family='Rubik', size=7,weight='bold')
rubik_big = tkFont.Font(root,family='Rubik', size=12,weight='bold')

list_of_subs_and_coeffs_widgets=[]
iterator_on_subs_and_coeffs=0

def add_sub_and_coeff(my_frame,my_canvas):
    global iterator_on_subs_and_coeffs
    global button_add_sub_and_coeff #defined later because uses add_sub_and_coeff function
    global label_add_sub_coeff
    list_of_subs_and_coeffs_widgets.append([])
    list_of_subs_and_coeffs_widgets[iterator_on_subs_and_coeffs].append(tk.Entry(my_frame,justify='right',font=rubik_big,width=10))
    list_of_subs_and_coeffs_widgets[iterator_on_subs_and_coeffs].append(tk.Scale(my_frame, from_=0, to=10, orient='horizontal',bg=sc_alt_green,fg='black',font=rubik_small, width=12))
    list_of_subs_and_coeffs_widgets[iterator_on_subs_and_coeffs][1].set(0)
    list_of_subs_and_coeffs_widgets[iterator_on_subs_and_coeffs][0].grid(row=iterator_on_subs_and_coeffs+1,padx=5,pady=5,sticky='nsew') 
    list_of_subs_and_coeffs_widgets[iterator_on_subs_and_coeffs][1].grid(
                                                                        row=list_of_subs_and_coeffs_widgets[iterator_on_subs_and_coeffs][0].grid_info()['row'],
                                                                        column=list_of_subs_and_coeffs_widgets[iterator_on_subs_and_coeffs][0].grid_info()['column']+1,
                                                                        pady=5
                                                                        )
    
    button_add_sub_and_coeff.destroy()
    label_add_sub_coeff.destroy()

    label_add_sub_coeff=tk.Label(my_frame,text='click on \'+\' to add a subject',fg='white',bg=sc_blue)
    button_add_sub_and_coeff=tk.Button(my_frame,text = "+",bg=sc_alt_green,command=lambda: add_sub_and_coeff(my_frame,my_canvas))

    label_add_sub_coeff.grid(row=list_of_subs_and_coeffs_widgets[iterator_on_subs_and_coeffs][0].grid_info()['row']+1,
                                column=list_of_subs_and_coeffs_widgets[iterator_on_subs_and_coeffs][0].grid_info()['column'])
    button_add_sub_and_coeff.grid(row=label_add_sub_coeff.grid_info()['row'],
                                column=label_add_sub_coeff.grid_info()['column']+1)

    
    #getting total width of all widgets
    list_of_subs_and_coeffs_widgets[iterator_on_subs_and_coeffs][1].update() #width of combobox
    label_add_sub_coeff.update() #width of "clic on "+"...
    print(
            list_of_subs_and_coeffs_widgets[iterator_on_subs_and_coeffs][1].winfo_width()+label_add_sub_coeff.winfo_width()
    )
    #resizing canvas
    my_canvas.config(scrollregion=my_canvas.bbox("all"))
    iterator_on_subs_and_coeffs=iterator_on_subs_and_coeffs+1





frame_sub_and_coeffs = tk.Frame(root, bg=sc_blue)
frame_sub_and_coeffs.grid(row=1, column=1,rowspan=2,sticky='news')


# Create a frame for the canvas with non-zero row&column weights
canvas_sub_and_coeff = tk.Frame(frame_sub_and_coeffs,bg=sc_blue,highlightthickness=0,highlightbackground=sc_alt_green)
canvas_sub_and_coeff.grid(row=2, column=0, pady=(5, 0), sticky='nw')
canvas_sub_and_coeff.grid_rowconfigure(0, weight=1)
canvas_sub_and_coeff.grid_columnconfigure(0, weight=1)
# Set grid_propagate to False to allow 5-by-5 sub_and_coeff resizing later
canvas_sub_and_coeff.grid_propagate(False)

# Add a canvas in that frame
sub_canvas_sub_and_coeff = tk.Canvas(canvas_sub_and_coeff, bg=sc_blue,highlightthickness=0)
sub_canvas_sub_and_coeff.grid(row=0, column=0, pady=(10, 0),padx=(10, 0),sticky="news")

# Link a scrollbar to the canvas
vsb = tk.Scrollbar(canvas_sub_and_coeff, orient="vertical", command=sub_canvas_sub_and_coeff.yview)
vsb.grid(row=0, column=1, sticky='ns')
sub_canvas_sub_and_coeff.configure(yscrollcommand=vsb.set)

# Create a frame to contain the sub_and_coeff
frame_sub_and_coeff = tk.Frame(sub_canvas_sub_and_coeff, bg=sc_blue)
sub_canvas_sub_and_coeff.create_window((0, 0), window=frame_sub_and_coeff, anchor='nw')

#Add 9-by-5 sub_and_coeff to the frame
label_add_sub_coeff=tk.Label(frame_sub_and_coeff,text='click on \'+\' to add a subject')
label_add_sub_coeff.grid(row=2)
button_add_sub_and_coeff=tk.Button(frame_sub_and_coeff,text = "+",bg=sc_alt_green,fg='white',command=lambda:add_sub_and_coeff(frame_sub_and_coeff,sub_canvas_sub_and_coeff))
button_add_sub_and_coeff.grid(row=label_add_sub_coeff.grid_info()['row'],
                                column=label_add_sub_coeff.grid_info()['column']+1)




for x in range(2):
    add_sub_and_coeff(frame_sub_and_coeff,sub_canvas_sub_and_coeff)


# Update sub_and_coeff frames idle tasks to let tkinter calculate sub_and_coeff sizes
frame_sub_and_coeff.update_idletasks()

# Resize the canvas frame to show what we need
canv_sub_coeff_width = 287+20+10+20
canv_sub_coeff_height =button_add_sub_and_coeff.winfo_height()*(iterator_on_subs_and_coeffs+8)
canvas_sub_and_coeff.config(width=canv_sub_coeff_width + vsb.winfo_width(),
                    height=canv_sub_coeff_height)

# Set the canvas scrolling region
sub_canvas_sub_and_coeff.config(scrollregion=sub_canvas_sub_and_coeff.bbox("all"))




##########################################################
##                                                      ##
##                                                      ##
##                                                      ##
##########################################################
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##########################################################
##                          ##############################
##                          ##############################
##                          ##############################
##                          ##############################
##                          ##############################
##                          ##############################
##########################################################



## will use later to open files
# openBtn = tk.Button(root, text = 'Open', command = load)
# openBtn.grid(column=0,row=12)
# def load(event):
#     file = open(textField.GetValue())
#     txt.SetValue(file.read())
#     file.close()

##go button fram
go_frame=tk.Frame(root)
go_frame.grid(row=4,column=1)
final_list_of_sub_and_coeff=[[list_of_subs_and_coeffs_widgets[k][0].get(),int(list_of_subs_and_coeffs_widgets[k][1].get())] for k in range(len(list_of_subs_and_coeffs_widgets))]
for sub_and_coeff in final_list_of_sub_and_coeff:
    if sub_and_coeff[1]==0:
        final_list_of_sub_and_coeff.remove(sub_and_coeff)

openBtn = tk.Button(go_frame, text = 'Go!',bg=sc_alt_green,bd=3,relief='raised', command = lambda:
                                        week_calendar_for_students(
                                            calendar_from_student_name,
                                            [[list_of_subs_and_coeffs_widgets[k][0].get(),int(list_of_subs_and_coeffs_widgets[k][1].get())] for k in range(len(list_of_subs_and_coeffs_widgets))],
                                            int(hours_entry.get()),
                                            str(output_entry.get()),
                                            [int(list_of_days[k][3].get()) for k in range(7)], 
                                            time_unit=0.5,
                                            delete_original_calendar=delete_original.get(),
                                            run_macro=run_the_macro.get())
                                            )
openBtn.config(width=10,height=5)
openBtn.grid(sticky='se')









root.mainloop()
#%%
class Example:
  "A basic example class"
  variable = 123

#%%
