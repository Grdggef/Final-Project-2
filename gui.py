from tkinter import *
import grading


class Gui:
    grades = []

    def __init__(self, window):
        self.top1 = None
        self.gpa_label = None
        self.grading_window = window
        self.grading_frame = Frame(self.grading_window)
        self.grading_label = Label(self.grading_frame, text='Grading \n \n')
        self.grading_label.pack(side='top')
        self.grading_frame.pack(anchor='n')

        self.student = Frame(self.grading_window)
        self.student_label = Label(self.student, text='Student')
        # takes int only
        self.student_entry = Entry(self.student)
        self.student_label.pack(side='left', padx=30)
        self.student_entry.pack(side='left', padx=15, pady=15)
        self.student.pack(anchor='w')

        self.history = Frame(self.grading_window)
        self.history_label = Label(self.history, text='History')
        # takes int only
        self.history_entry = Entry(self.history)
        self.history_label.pack(side='left', padx=30)
        self.history_entry.pack(side='left', padx=18)
        self.history.pack(anchor='w')

        self.math = Frame(self.grading_window)
        self.math_label = Label(self.math, text='Math')
        # takes int only
        self.math_entry = Entry(self.math)
        self.math_label.pack(side='left', padx=30)
        self.math_entry.pack(side='left', padx=27, pady=15)
        self.math.pack(anchor='w')

        self.science = Frame(self.grading_window)
        self.science_label = Label(self.science, text='Science')
        # takes int only
        self.science_entry = Entry(self.science)
        self.science_label.pack(side='left', padx=30)
        self.science_entry.pack(side='left', padx=15)
        self.science.pack(anchor='w')

        self.english = Frame(self.grading_window)
        self.english_label = Label(self.english, text='English')
        # takes int only
        self.english_entry = Entry(self.english)
        self.english_label.pack(side='left', padx=30)
        self.english_entry.pack(side='left', padx=14, pady=15)
        self.english.pack(anchor='w')

        self.buttons = Frame(self.grading_window)
        self.convert_grades = Button(self.buttons, text='Convert Grades', command=self.convert)
        self.clear = Button(self.buttons, text='Clear', command=self.clear)
        self.convert_grades.pack(side='left')
        self.clear.pack(side='left', padx=15)
        self.buttons.pack()

        self.exceptions_frame = Frame(self.grading_window)
        self.exception_text = Label(self.exceptions_frame, text="")
        self.exception_text.pack(side="bottom")
        self.exceptions_frame.pack(anchor='s')

    def clear(self):
        # clears all text boxes
        self.student_entry.delete(0, END)
        self.history_entry.delete(0, END)
        self.math_entry.delete(0, END)
        self.science_entry.delete(0, END)
        self.english_entry.delete(0, END)

    def convert(self):
        # attempts to convert all entries to ints
        try:
            history_num = int(self.history_entry.get())
            math_num = int(self.math_entry.get())
            science_num = int(self.science_entry.get())
            english_num = int(self.english_entry.get())
        # if it fails raises a value error and puts text in a label on screen
        except ValueError:
            self.exception_text.config(text="Please enter numeric values for all grades")
            return

        self.exception_text.config(text="")
        self.top1 = Toplevel()
        self.top1.title(self.student_entry.get().strip().upper() + "'s " + "Grades")
        self.top1.geometry('310x300')

        history_frame = Frame(self.top1)
        history_label = Label(history_frame, text='History - ')
        # runs the formula to calculate grade and prints in this label
        grade1_label = Label(history_frame, text="Grade in History is a(n):  " + grading.history_grade(history_num))
        history_label.pack(side='left')
        grade1_label.pack(side='left')
        history_frame.pack()

        math_frame = Frame(self.top1)
        math_label = Label(math_frame, text='Math - ')
        # runs the formula to calculate grade and prints in this label
        grade2_label = Label(math_frame, text="Grade in Math is a(n):  " + grading.math_grade(math_num))
        math_label.pack(side='left', pady=20)
        grade2_label.pack(side='left', pady=20)
        math_frame.pack()

        science_frame = Frame(self.top1)
        science_label = Label(science_frame, text='Science - ')
        # runs the formula to calculate grade and prints in this label
        grade3_label = Label(science_frame, text="Grade in Science is a(n):  " + grading.science_grade(science_num))
        science_label.pack(side='left')
        grade3_label.pack(side='left')
        science_frame.pack()

        english_frame = Frame(self.top1)
        english_label = Label(english_frame, text='English - ')
        # runs the formula to calculate grade and prints in this label
        grade4_label = Label(english_frame, text="Grade in English is a(n):  " + grading.english_grade(english_num))
        english_label.pack(side='left', pady=20)
        grade4_label.pack(side='left', pady=20)
        english_frame.pack()

        gpa_check_frame = Frame(self.top1)
        gpa_button = Button(gpa_check_frame, text="Calculate GPA", command=self.press)
        new_button = Button(gpa_check_frame, text='New Grades', command=self.destroy)
        # runs the formula to calculate GPA and prints in this label upon button press
        self.gpa_label = Label(gpa_check_frame, text="")
        self.gpa_label.pack()
        gpa_button.pack(side='left')
        new_button.pack(side='left', padx=15)
        gpa_check_frame.pack()

    # calculates GPA
    def press(self):
        self.gpa_label.config(text=" Your overall GPA is  " + str(grading.gpa(self.grades)))

    # destroys the toplevel window, clears all text boxes, and returns to main window
    def destroy(self):
        self.top1.destroy()
        self.student_entry.delete(0, END)
        self.history_entry.delete(0, END)
        self.math_entry.delete(0, END)
        self.science_entry.delete(0, END)
        self.english_entry.delete(0, END)

