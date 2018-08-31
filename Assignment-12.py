#Q.1- Print the current day using Datetime module.
import datetime as dt
day=dt.date.today()
print(day.day)


#Q.2- Open your browser and play a video using webbrowser module in python.
import webbrowser as wb
search=input("Search Youtube")
wb.open_new_tab("https://www.youtube.com/search?q=%s"%search)


#Q.3- Write a program to rename all the files in a directory and convert them into .jpg file format.
import os
filenames=os.listdir("main_folder")
i = 1
for filename in filenames:
    dst ="pankaj" + str(i) + ".jpg"
    src = filename
    os.rename(src, dst)
    i += 1

