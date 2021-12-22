#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:08:25 2021

@author: macbook
"""

from tkinter import*

root = Tk()  
root.geometry("900x600")
root.title("Classes")
root.config(bg ="hot pink")

percentage_grade_1_label = Label(root)
percentage_grade_2_label = Label(root)
percentage_grade_4_label = Label(root)

class grade_1():
    def __init__(self,  language_arts, mathematics):
        self.language_arts = language_arts
        self.mathematics = mathematics
    def percentage(self):
        total_marks = self.language_arts +self.mathematics
        total_marks_with_100 = total_marks * 100
        grade_1_percentage = total_marks_with_100/200
        percentage_grade_1_label["text"] = grade_1_percentage
       
class grade_2():
    def __init__(self,  language_arts, mathematics,social_studies):
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies
    def percentage(self):
        total_marks = self.language_arts +self.mathematics + self.social_studies
        total_marks_with_100 = total_marks * 100
        grade_2_percentage = total_marks_with_100/300
        percentage_grade_2_label["text"] = grade_2_percentage
       
class grade_4():
    def __init__(self, language_arts, mathematics,social_studies,foreign_language):
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies
        self.foreign_language = foreign_language
    def percentage(self):
        total_marks =self.language_arts +self.mathematics + self.social_studies +  self.foreign_language
        total_marks_with_100 = total_marks * 100
        grade_4_percentage = total_marks_with_100/400
        percentage_grade_4_label["text"] = grade_4_percentage
       
object_grade_1 = grade_1(40,50)
grade_1_btn=Button(root,text="Grade 1",command=object_grade_1.percentage)
grade_1_btn.pack(padx=20, pady =20)
percentage_grade_1_label.pack(padx=20, pady =20)

object_grade_2 = grade_2(40,50,90)
grade_1_btn=Button(root,text="Grade 2",command=object_grade_2.percentage)
grade_1_btn.pack(padx=20, pady =20)
percentage_grade_2_label.pack(padx=20, pady =20)

object_grade_4 = grade_4(40, 50,70,90)
grade_4_btn=Button(root,text="Grade 4",command=object_grade_4.percentage)
grade_4_btn.pack(padx=20, pady =20)
percentage_grade_4_label.pack(padx=20, pady =20)

root.mainloop()