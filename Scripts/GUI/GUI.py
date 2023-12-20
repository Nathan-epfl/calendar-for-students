#%%no comments


'''
    Blue : RGB: 0, 20, 77 - HEX : #00144d

    Light Green : RGB: 9, 225, 192 - HEX : #09e1c0

    There is also a "Muted" Green (for the icons)   
    Alt Green : RGB: 126, 190, 197 - HEX : #7EBEC5
'''
sc_blue = '#00144d'
sc_light_green = '#09e1c0'
sc_alt_green = '#7EBEC5'



from os import chdir,path
import re
file_directory= path.dirname(__file__)
wd = re.findall(".+Scripts",file_directory)[0]
chdir(wd)

from week_calendar.python_files.week_calendar_for_students import week_calendar_for_students

import tkinter.filedialog
import tkinter as tk



# def callbackFunc():
#     resultString.set("{} - {}".format(landString.get(),
#                                       cityString.get()))





root = tk.Tk()


from tkinter import ttk
# ttk.Style().theme_create('my_style', parent = 'alt',
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
rubik_bold = tkFont.Font(root,family = 'Rubik', size = 10)
rubik_big = tkFont.Font(root,family = 'Rubik', size = 14)
rubik_medium = tkFont.Font(root,family = 'Rubik', size = 9)
rubik_small = tkFont.Font(root,family = 'Rubik', size = 7)

# width_of_root_frame = 800
# height_of_root_frame = 600
# root.geometry(str(width_of_root_frame) + "x" + str(height_of_root_frame))
root.resizable(width = False, height = False)






#Set root background color 
root.config(background = sc_blue) 
default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(family = 'Rubik', size = 10)


root.title('Timetable maker')
##########################################################
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
title_frame = tk.Frame(root,bg = sc_blue)
title_frame.grid(row = 0,column = 0,columnspan = 2)
instruction_text = "\
This app creates a timetable for the student.\n\
\n\
first open \'template_timetable.xlsx\'.\n\
Modify it without moving or merging the cells, save it,\n\
then add it with the \'browse xls file\' button, and select all the\n\
options.\n\
\n\
when you're ready, click the \"Go!\" button. It should open\n\
the timetable on Excel, where you can make some last\n\
modifications before finalization.\
"
fill_form_title = tk.Label(root,text = instruction_text, justify = 'left',fg = "white",bg = sc_blue,font = rubik_big)
fill_form_title.grid(row = 0,column = 0,padx = 20)








##########################################################
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
##########################################################
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##                          ##                          ##
##########################################################












# # # logo at the end
import os
image_path = wd + '\\GUI\\images\\LOGO_blue_white_small.png'
logo = tk.PhotoImage(master = root,file = image_path)
labelExample = tk.Label(root, image = logo,bg = sc_blue)


labelExample.grid(row = 0,column = 1)


   

   
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




coeff_per_day_frame = tk.Frame(root,bg = sc_blue)


coeff_per_day_frame.grid(row = 1,column = 0,padx = 50)


coeff_per_day_title = tk.Label(coeff_per_day_frame, text = "choose hours of work per day:", fg = "white",bg = sc_blue,font = rubik_big,height = 4)
coeff_per_day_title.grid(columnspan = 7)


list_of_days=[['Monday'],['Tuesday'],['Wednesday'],['Thursday'],['Friday'],['Saturday'],['Sunday']]

iter_on_days = 0

for day in sum(list_of_days, []):


    list_of_days[iter_on_days].append(tk.Label(coeff_per_day_frame,text = day,fg = '#ffffff',bg = sc_blue,activebackground = sc_light_green,highlightbackground = sc_alt_green))
    list_of_days[iter_on_days].append(tk.IntVar())
    list_of_days[iter_on_days].append(tk.Scale(coeff_per_day_frame, from_ = 14, to = 0, orient = 'vertical',bg = sc_alt_green,fg = 'black'))
    if iter_on_days < 5:
        list_of_days[iter_on_days][3].set(3)
    else:
        list_of_days[iter_on_days][3].set(8)
    list_of_days[iter_on_days][1].grid(row = 2,column = iter_on_days)
    list_of_days[iter_on_days][3].grid(row = 1,column = list_of_days[iter_on_days][1].grid_info()['column'])
    iter_on_days = iter_on_days + 1





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
option_frame = tk.Frame(root,bg = sc_blue)
option_frame.grid(row = 2,column = 0)


options_title = tk.Label(option_frame, text = "", fg = "white",bg = sc_blue,font = rubik_big,height = 2)
options_title.grid(columnspan = 3)
###browse excel button
# file explorer root 
import re
calendar_from_student_name = ''
folder_with_templates= wd + '\\week_calendar\\excel_templates'



def browseFiles(): 
    global calendar_from_student_name
    filename = tk.filedialog.askopenfilename(initialdir = folder_with_templates, 
                                          title = "Select a File", 
                                          filetypes = (("Excel files", 
                                                        "*.xlsx*"), 
                                                       ("all files", 
                                                        "*.*"))) 
       
    # Change label contents 
    label_file_explorer.configure(text = "File: " + re.findall('\w*\.xlsx',filename)[0],fg = 'white') 
    calendar_from_student_name = filename
                                                                                                   


   
# Create a File Explorer label 
label_file_explorer = tk.Label(option_frame,  
                            text = "",   
                            bg = sc_blue) 
   
       
button_explore = tk.Button(option_frame,  
                        text = "browse xls source File", 
                        command = browseFiles,
                        fg = 'black',
                        bg = sc_alt_green
                        )  
   
#button_exit = tk.Button(root,  
#                     text = "Exit", 
#                     command = exit)  
   
button_explore.grid(sticky = 'w') 
label_file_explorer.grid(row = 1,column = 0,columnspan = 4,sticky = 'e') 
##choosing name of output
output_label = tk.Label(option_frame, 
                        text = 'choose a name for the final timetable:',
                        fg = 'white',
                        bg = sc_blue,
                        justify = 'right')

output_entry = tk.Entry(option_frame,justify = 'right',bg = 'white',font = rubik_medium)
xslx_label = tk.Label(option_frame, text = '.xlsx',
                        fg = 'white',
                        bg = sc_blue,
                        justify = 'left')

output_label.grid(rowspan = 2,sticky = 'e')
output_entry.grid(row = 2,column = 2,sticky = 'w')
xslx_label.grid(row = 2,column = 3)



##check button for deleting original calendar
delete_original = tk.BooleanVar() 
#delete_original.set(True)
 
check_button_delete = tk.Checkbutton(option_frame,
                            text = 'delete original calendar entries',
                            var = delete_original,bg = sc_blue,fg = 'white',selectcolor = 'black') 



###choosing part of the day priority


coeff_per_day_title = tk.Label(option_frame, text = "choose values from 1 to 3 to set priorities within a day. \n 1 means first and 3 last.\n \'1\',\'2\',\'3\' must appear on each line", fg = "white",bg = sc_blue,font = rubik_big,height = 3)
coeff_per_day_title.grid(row = 6,columnspan = 7)


priority_frame = tk.Frame(option_frame,bg = sc_blue)
priority_frame.grid(row = 7,column = 0, columnspan = 3)




##labels first column

weekdays_label = tk.Label(priority_frame, text = 'weekdays',
                        fg = 'white',
                        bg = sc_blue,
                        justify = 'right')
weekdays_label.grid(row = 1,sticky = 'e')

weekend_label = tk.Label(priority_frame, text = 'weekend',
                        fg = 'white',
                        bg = sc_blue,
                        justify = 'right')
weekend_label.grid(sticky = 'e')

#labels first row, not first column
first_priority_label = tk.Label(priority_frame, text = 'morning',
                        fg = 'white',
                        bg = sc_blue,
                        justify = 'right')
first_priority_label.grid(row = 0,column = 1,sticky = 'e')

second_priority_label = tk.Label(priority_frame, text = 'afternoon',
                        fg = 'white',
                        bg = sc_blue,
                        justify = 'right')
second_priority_label.grid(row = 0,column = 2,sticky = 'e')

second_priority_label = tk.Label(priority_frame, text = 'evening',
                        fg = 'white',
                        bg = sc_blue,
                        justify = 'right')
second_priority_label.grid(row = 0,column = 3,sticky = 'e')

#entries
morning_wd_entry = tk.Entry(priority_frame,justify = 'right',bg = 'white',font = rubik_medium,width = 5)
morning_wd_entry.grid(row = 1,column = 1)
morning_wd_entry.insert(0,3)

afternoon_wd_entry = tk.Entry(priority_frame,justify = 'right',bg = 'white',font = rubik_medium,width = 5)
afternoon_wd_entry.grid(row = 1,column = 2)
afternoon_wd_entry.insert(0,2)

evening_wd_entry = tk.Entry(priority_frame,justify = 'right',bg = 'white',font = rubik_medium,width = 5)
evening_wd_entry.grid(row = 1,column = 3)
evening_wd_entry.insert(0,1)
#

morning_we_entry = tk.Entry(priority_frame,justify = 'right',bg = 'white',font = rubik_medium,width = 5)
morning_we_entry.grid(row = 2,column = 1)
morning_we_entry.insert(0,2)

afternoon_we_entry = tk.Entry(priority_frame,justify = 'right',bg = 'white',font = rubik_medium,width = 5)
afternoon_we_entry.grid(row = 2,column = 2)
afternoon_we_entry.insert(0,1)

evening_we_entry = tk.Entry(priority_frame,justify = 'right',bg = 'white',font = rubik_medium,width = 5)
evening_we_entry.grid(row = 2,column = 3)
evening_we_entry.insert(0,3)






option_frame.update()
col_count, row_count = option_frame.grid_size()
for row in range(row_count):
    option_frame.grid_rowconfigure(row, minsize = 10)



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








list_of_subs_and_coeffs_widgets=[]
iterator_on_subs_and_coeffs = 0

def add_sub_and_coeff(my_frame,my_canvas):
    global iterator_on_subs_and_coeffs
    global button_add_sub_and_coeff #defined later because uses add_sub_and_coeff function
    global label_add_sub_coeff
    list_of_subs_and_coeffs_widgets.append([])
    list_of_subs_and_coeffs_widgets[iterator_on_subs_and_coeffs].append(tk.Entry(my_frame,justify = 'right',font = rubik_big,width = 10))
    list_of_subs_and_coeffs_widgets[iterator_on_subs_and_coeffs].append(tk.Scale(my_frame, from_ = 0, to = 10, orient = 'horizontal',bg = sc_alt_green,fg = 'black',font = rubik_small, width = 12))
    list_of_subs_and_coeffs_widgets[iterator_on_subs_and_coeffs][1].set(0)
    list_of_subs_and_coeffs_widgets[iterator_on_subs_and_coeffs][0].grid(row = iterator_on_subs_and_coeffs + 1,padx = 5,pady = 5,sticky = 'nsew') 
    list_of_subs_and_coeffs_widgets[iterator_on_subs_and_coeffs][1].grid(
                                                                        row = list_of_subs_and_coeffs_widgets[iterator_on_subs_and_coeffs][0].grid_info()['row'],
                                                                        column = list_of_subs_and_coeffs_widgets[iterator_on_subs_and_coeffs][0].grid_info()['column'] + 1,
                                                                        pady = 5
                                                                        )
    
    button_add_sub_and_coeff.destroy()
    label_add_sub_coeff.destroy()

    label_add_sub_coeff = tk.Label(my_frame,text = 'click on \'+\' to add a subject',fg = 'white',bg = sc_blue)
    button_add_sub_and_coeff = tk.Button(my_frame,text = "+",bg = sc_alt_green,command = lambda: add_sub_and_coeff(my_frame,my_canvas))

    label_add_sub_coeff.grid(row = list_of_subs_and_coeffs_widgets[iterator_on_subs_and_coeffs][0].grid_info()['row'] + 1,
                                column = list_of_subs_and_coeffs_widgets[iterator_on_subs_and_coeffs][0].grid_info()['column'])
    button_add_sub_and_coeff.grid(row = label_add_sub_coeff.grid_info()['row'],
                                column = label_add_sub_coeff.grid_info()['column'] + 1)

    
    #getting total width of all widgets
    list_of_subs_and_coeffs_widgets[iterator_on_subs_and_coeffs][1].update() #width of combobox
    label_add_sub_coeff.update() #width of "clic on "+"...
    my_canvas.config(scrollregion = my_canvas.bbox("all"))
    iterator_on_subs_and_coeffs = iterator_on_subs_and_coeffs + 1




frame_sub_and_coeffs = tk.Frame(root, bg = sc_blue,padx = 50)
frame_sub_and_coeffs.grid(row = 1, column = 1,rowspan = 2,sticky = 'news')



sub_and_coeff_title = tk.Label(frame_sub_and_coeffs, text = "choose subjects and weighting per subject:", fg = "white",bg = sc_blue,font = rubik_big,height = 4,justify = 'right')
sub_and_coeff_title.grid(row = 0)
# Create a frame for the canvas with non-zero row&column weights
canvas_sub_and_coeff = tk.Frame(frame_sub_and_coeffs,bg = sc_blue,highlightthickness = 0,highlightbackground = sc_alt_green)
canvas_sub_and_coeff.grid(row = 2, column = 0, sticky = 'ne')
canvas_sub_and_coeff.grid_rowconfigure(0, weight = 1)
canvas_sub_and_coeff.grid_columnconfigure(0, weight = 1)
# Set grid_propagate to False to allow 5-by-5 sub_and_coeff resizing later
canvas_sub_and_coeff.grid_propagate(False)

# Add a canvas in that frame
sub_canvas_sub_and_coeff = tk.Canvas(canvas_sub_and_coeff, bg = sc_blue,highlightthickness = 0)
sub_canvas_sub_and_coeff.grid(row = 0, column = 0,padx=(10, 0),sticky = "news")

# Link a scrollbar to the canvas
vsb = tk.Scrollbar(canvas_sub_and_coeff, orient = "vertical", command = sub_canvas_sub_and_coeff.yview)
vsb.grid(row = 0, column = 1, sticky = 'ns')
sub_canvas_sub_and_coeff.configure(yscrollcommand = vsb.set)

# Create a frame to contain the sub_and_coeff
frame_sub_and_coeff = tk.Frame(sub_canvas_sub_and_coeff, bg = sc_blue)
sub_canvas_sub_and_coeff.create_window((0, 0), window = frame_sub_and_coeff, anchor = 'nw')

#Add 9-by-5 sub_and_coeff to the frame
label_add_sub_coeff = tk.Label(frame_sub_and_coeff,text = 'click on \'+\' to add a subject')
label_add_sub_coeff.grid(row = 2)
button_add_sub_and_coeff = tk.Button(frame_sub_and_coeff,text = "+",bg = sc_alt_green,fg = 'white',command = lambda:add_sub_and_coeff(frame_sub_and_coeff,sub_canvas_sub_and_coeff))
button_add_sub_and_coeff.grid(row = label_add_sub_coeff.grid_info()['row'],
                                column = label_add_sub_coeff.grid_info()['column'] + 1)




for x in range(6):
    add_sub_and_coeff(frame_sub_and_coeff,sub_canvas_sub_and_coeff)


# Update sub_and_coeff frames idle tasks to let tkinter calculate sub_and_coeff sizes
frame_sub_and_coeff.update_idletasks()

# Resize the canvas frame to show what we need
canv_sub_coeff_width = 287 + 20 + 10 + 20
canv_sub_coeff_height =button_add_sub_and_coeff.winfo_height()*(iterator_on_subs_and_coeffs + 8)
canvas_sub_and_coeff.config(width = canv_sub_coeff_width + vsb.winfo_width(),
                    height = canv_sub_coeff_height)

# Set the canvas scrolling region
sub_canvas_sub_and_coeff.config(scrollregion = sub_canvas_sub_and_coeff.bbox("all"))




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
# openBtn.grid(column = 0,row = 12)
# def load(event):
#     file = open(textField.GetValue())
#     txt.SetValue(file.read())
#     file.close()

##go button fram
go_frame = tk.Frame(root,bg = sc_blue)
go_frame.grid(row = 3,column = 1)


def getting_all_subj_and_coeffs():
    list_of_sub_and_coeff=[[list_of_subs_and_coeffs_widgets[k][0].get(),int(list_of_subs_and_coeffs_widgets[k][1].get())] for k in range(len(list_of_subs_and_coeffs_widgets))]
    final_list_of_sub_and_coeff=[]
    for sub_and_coeff in range(len(list_of_sub_and_coeff)):
        if list_of_sub_and_coeff[sub_and_coeff][1] != 0:
            final_list_of_sub_and_coeff.append(list_of_sub_and_coeff[sub_and_coeff])
    return final_list_of_sub_and_coeff

openBtn = tk.Button(go_frame, text = 'Go!',bg = sc_alt_green,bd = 3,relief = 'raised', command = lambda:
                                        week_calendar_for_students(
                                                                    calendar_from_student_name,
                                                                    getting_all_subj_and_coeffs(),
                                                                    float((sum(list_of_days[i][3].get() for i in range(7)))),
                                                                    str(output_entry.get()),
                                                                    [int(list_of_days[k][3].get()) for k in range(7)],
                                                                    order=[
                                                                        [int(morning_wd_entry.get()),int(afternoon_wd_entry.get()),int(evening_wd_entry.get())],
                                                                        [int(morning_we_entry.get()),int(afternoon_we_entry.get()),int(evening_we_entry.get())]
                                                                    ], 
                                                                    time_unit = 0.5,
                                                                    delete_original_calendar = True,
                                                                    #delete_original.get()
                                                                    run_macro = False
                                                                    # run_macro = run_the_macro.get()
                                                                 )
                    )

openBtn.config(width = 10,height = 5)
openBtn.grid(sticky = 'ne',pady = 10)


def center_window(width = 300, height = 200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = ((screen_height / 2) - (height / 2)) 
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

center_window(width = 1050,height = 900)




root.mainloop()
#%%
