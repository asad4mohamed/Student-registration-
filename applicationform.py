from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

class MyApp(App):
    def build(self):
        self.tab = TabbedPanel(do_default_tab = False)
        self.tab.tab_width = Window.width/2
        registration_tab = TabbedPanelItem(text = "Student registration")
        self.form = self.build_form()
        registration_tab.add_widget(self.form)
        self.tab.add_widget(registration_tab)

        view_student = TabbedPanelItem(text = "Student view")
        self.doc = self.view()
        view_student.add_widget(self.doc)
        self.tab.add_widget(view_student)
        return self.tab
        



    def build_form(self):
        #main layout 
        layout = BoxLayout(orientation= "vertical", padding = 20, spacing = 10)
        #text input boxes
        form = GridLayout(cols = 2, spacing = 10, row_force_default = True, row_default_height  = 60)

        self.student_registration_Label = Label(text = "Student Registration form")
        layout.add_widget(self.student_registration_Label)

        #name input
        self.name_label = Label(text = "Name: ")
        form.add_widget(self.name_label)
        self.name_input = TextInput()
        form.add_widget(self.name_input)

        #age input
        self.age_label = Label(text = "Age: ")
        form.add_widget(self.age_label)
        self.age_input = TextInput()
        form.add_widget(self.age_input)
        

        #gender input
        self.gender_label = Label(text = "Gender ")
        form.add_widget(self.gender_label)
        self.gender_spinner = Spinner(text = "select", values = ["male", "female"])
        form.add_widget(self.gender_spinner)


        #grade input
        self.grade_label = Label(text = "grade: ")
        form.add_widget(self.grade_label)
        self.grade_spinner = Spinner(text = "select", values = ["1","2","3","4","5","6","7","8","9","10","11","12"])
        form.add_widget(self.grade_spinner)
        

        #address input
        self.address_label = Label(text = "address")
        form.add_widget(self.address_label)
        self.address_input= TextInput()
        form.add_widget(self.address_input)
        layout.add_widget(form)


        #subject label
        self.select_subject_label = Label(text = "Select subject: ",size_hint_y = None, height = 150)
        layout.add_widget(self.select_subject_label)

        #grid layout holding subjects and checkboxes
        grid =  GridLayout(cols = 2, padding = [400,0,400,0])


        #math checkboxes input
        self.cb_math = CheckBox(active = True, color = (1,0,0,1))
        grid.add_widget(self.cb_math)
        self.lb_math = Label(text = "Math")
        grid.add_widget(self.lb_math)

        #english checkboxes input
        self.cb_english = CheckBox()
        grid.add_widget(self.cb_english)
        self.lb_english = Label(text = "English")
        grid.add_widget(self.lb_english)

        #physics checkboxes input
        self.cb_physics = CheckBox()
        grid.add_widget(self.cb_physics)
        self.lb_physics = Label(text = "Physics")
        grid.add_widget(self.lb_physics)
        layout.add_widget(grid)

        #submit button
        self.submit = Button(text = "submit", size_hint_y = None, height  = 80, on_press = self.submit_data)
        layout.add_widget(self.submit)
        self.status_label = Label(text = "")
        layout.add_widget(self.status_label) 
        
        return layout

    def view(self):
        layout = BoxLayout(orientation = "vertical", spacing = 10)
        refresh = Button(text = "refresh", size_hint_y = None, height = 45)
        self.scroll = ScrollView(size_hint = (1,1), bar_width = 12)
        self.cards = BoxLayout(orientation = "vertical", spacing = 10)
        self.cards.bind(minimum_height = self.cards.setter("height"))
        self.scroll.add_widget(self.cards)
        layout.add_widget(refresh)
        layout.add_widget(self.scroll)
        self.load_students()
        return layout
    
    def load_students(self):
        self.cards.clear_widgets()
        try:
            with open("students_data.txt", "r") as f:
                for line in f:
                    card = self.create_student_card(line)
                    self.cards.add_widget(card) 
        except:
            print("no data")
                    
    def create_student_card(self, line):
        name,age,address,gender,grade, subject = line.strip().split(",")
        student_card = BoxLayout(orientation = "vertical")
        student_card.add_widget(Label(text = f'name: {name}'))
        student_card.add_widget(Label(text = f'age: {age}'))
        student_card.add_widget(Label(text = f'address: {address}'))
        student_card.add_widget(Label(text = f'gender: {gender}'))
        student_card.add_widget(Label(text = f'grade: {grade}'))
        student_card.add_widget(Label(text = f'subject: {subject}'))
        return student_card





    def submit_data(self,instance):
        #storing as variables
        name = self.name_input.text.strip()
        age = self.age_input.text.strip()
        gender = self.gender_spinner.text
        grade = self.grade_spinner.text
        address = self.address_input.text.strip()
        subjects = []

    
        if self.cb_math:
            subjects.append("math")
        elif self.cb_english:
            subjects.append("English")
        else:
            subjects.append("Physics")
        
        if not name or not age or not address or not subjects or gender == "select" or grade == "select":
            self.status_label.text = "Please fill all the options"
        else:
            with open("students_data.txt", "a",) as f:
                survey_data = f"{name},{age},{address},{gender},{grade},{','.join(subjects)}\n"
                f.write(survey_data)
                self.status_label.text = "Data saved successfully"
                self.clearform()
    

    def clearform(self):
        self.name_input.text = ""
        self.age_input.text = ""
        self.address_input.text = ""
        self.grade_spinner.text = "select"
        self.gender_spinner.text = "Select"
        self.cb_math.active = False
        self.cb_english.active = False
        self.cb_physics.active = False




            


        

        


if __name__ == "__main__":
    MyApp().run()

