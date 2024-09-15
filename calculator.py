from tkinter import *

class Calculator():
    def __init__(self, window) -> None:
        self.text = "0"
        self.num1 = ""
        self.num2 = ""
        self.result = 0
        self.operation = None

        self.display = Canvas(window, width=200, height=40, bg="gray")
        self.display.grid(column=0, row=0, columnspan=4)
        self.text_disp = self.display.create_text(200, 20, text="0", font=("Arial", 40, "italic"), anchor='e')

        self.button_ac = Button(text="AC",width=2, height=2, command=self.reset_display)
        self.button_ac.grid(column=0, row=1)

        self.button_change = Button(text="+/-",width=2, height=2)
        self.button_change.grid(column=1, row=1)

        self.button_percent = Button(text="%",width=2, height=2)
        self.button_percent.grid(column=2, row=1)

        self.button_divide = Button(text="÷",width=2, height=2, command= self.divide)
        self.button_divide.grid(column=3, row=1)

        self.button_7 = Button(text="7",width=2, height=2, command=lambda: self.type_number("7"))
        self.button_7.grid(column=0, row=2)

        self.button_8 = Button(text="8",width=2, height=2, command=lambda: self.type_number("8"))
        self.button_8.grid(column=1, row=2)

        self.button_9 = Button(text="9",width=2, height=2, command=lambda: self.type_number("9"))
        self.button_9.grid(column=2, row=2)

        self.button_X = Button(text="x",width=2, height=2, command=self.multiplicate)
        self.button_X.grid(column=3, row=2)

        self.button_4 = Button(text="4",width=2, height=2, command=lambda: self.type_number("4"))
        self.button_4.grid(column=0, row=3)

        self.button_5 = Button(text="5",width=2, height=2, command=lambda: self.type_number("5"))
        self.button_5.grid(column=1, row=3)

        self.button_6 = Button(text="6",width=2, height=2, command=lambda: self.type_number("6"))
        self.button_6.grid(column=2, row=3)

        self.button_minus = Button(text="-",width=2, height=2, command=self.minus)
        self.button_minus.grid(column=3, row=3)

        self.button_1 = Button(text="1",width=2, height=2, command=lambda: self.type_number("1"))
        self.button_1.grid(column=0, row=4)

        self.button_2 = Button(text="2",width=2, height=2, command=lambda: self.type_number("2"))
        self.button_2.grid(column=1, row=4)

        self.button_3 = Button(text="3",width=2, height=2, command=lambda: self.type_number("3"))
        self.button_3.grid(column=2, row=4)

        self.button_plus = Button(text="+",width=2, height=2, command=self.sum)
        self.button_plus.grid(column=3, row=4)

        self.button_0 = Button(text="0",width=9, height=2, command=lambda: self.type_number("0"))
        self.button_0.grid(column=0, row=5, columnspan=2)

        self.button_dot = Button(text=".",width=2, height=2, command=lambda: self.type_number("."))
        self.button_dot.grid(column=2, row=5)

        self.button_equal = Button( text="=",width=2, height=2, command=self.equal)
        self.button_equal.grid(column=3, row=5)


    def type_number(self, number):
        number_enter = str(number)
        if number_enter == ".":
            if "." not in self.text:
                self.num1 += "."
                self.text = self.num1
            else:
                return
        elif self.text == "0" and number_enter != ".":
            self.text = number_enter
            self.button_ac.config(text="C")
        else:
            self.text += number_enter
        self.display.itemconfig(self.text_disp, text=self.text)
        self.num1 = self.num1 + number_enter
        try:
            self.num1 = self.text
        except ValueError:
            pass
        print(self.num1)

    def reset_display(self):
        self.display.itemconfig(self.text_disp, text="0")
        self.text = "0"
        self.num1 = ""
        self.num2 = 0
        self.result = 0
        self.operation = None
        self.button_ac.config(text="AC")
        print(self.text)

    def sum(self):
        if self.text != "":
            if self.operation == None:
                self.operation = "+"
                self.num2 = float(self.num1)
                self.num1 = ""
                self.text = ""
            else:
                self.result = self.calculate(self.num2, float(self.num1), self.operation)
                print(f"num1: {self.num1}, num2: {self.num2}, result = {self.result}")
                self.operation = None
                self.num1 = self.result
                self.display.itemconfig(self.text_disp, text=self.result)
                self.sum()
        else:
            self.operation = "+"
            num = float(self.result)
            self.result = self.calculate(num, num, self.operation)
            print(f"num1: {self.num1}, num2: {self.num2}, result = {self.result}")
            self.operation = None
            self.num1 = self.result
            self.display.itemconfig(self.text_disp, text=self.result)
            
    def minus(self):
        if self.text != "":
            if self.operation == None:
                self.operation = "-"
                self.num2 = float(self.num1)
                self.num1 = ""
                self.text = ""
            else:
                self.result = self.calculate(self.num2, float(self.num1), self.operation)
                print(f"num1: {self.num1}, num2: {self.num2}, result = {self.result}")
                self.operation = None
                self.num1 = self.result
                self.display.itemconfig(self.text_disp, text=self.result)
                self.minus()
        else:
            self.operation = "-"
            num = float(self.result)
            self.result = self.calculate(num, num, self.operation)
            print(f"num1: {self.num1}, num2: {self.num2}, result = {self.result}")
            self.operation = None
            self.num1 = self.result
            self.display.itemconfig(self.text_disp, text=self.result)

    def multiplicate(self):
        if self.text != "":
            if self.operation == None:
                self.operation = "*"
                self.num2 = float(self.num1)
                self.num1 = ""
                self.text = ""
            else:
                self.result = self.calculate(self.num2, float(self.num1), self.operation)
                print(f"num1: {self.num1}, num2: {self.num2}, result = {self.result}")
                self.operation = None
                self.num1 = self.result
                self.display.itemconfig(self.text_disp, text=self.result)
                self.multiplicate()
        else:
            self.operation = "*"
            num = float(self.result)
            self.result = self.calculate(num, num, self.operation)
            print(f"num1: {self.num1}, num2: {self.num2}, result = {self.result}")
            self.operation = None
            self.num1 = self.result
            self.display.itemconfig(self.text_disp, text=self.result)

    def divide(self):
        if self.text != "":
            if self.operation == None:
                self.operation = "/"
                self.num2 = float(self.num1)
                self.num1 = ""
                self.text = ""
            else:
                self.result = self.calculate(self.num2, float(self.num1), self.operation)
                print(f"num1: {self.num1}, num2: {self.num2}, result = {self.result}")
                self.operation = None
                self.num1 = self.result
                self.display.itemconfig(self.text_disp, text=self.result)
                self.divide()
        else:
            self.operation = "/"
            num = float(self.result)
            self.result = self.calculate(num, num, self.operation)
            print(f"num1: {self.num1}, num2: {self.num2}, result = {self.result}")
            self.operation = None
            self.num1 = self.result
            self.display.itemconfig(self.text_disp, text=self.result)
    

    def calculate(self, a, b, op):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            if b != 0:
                return a / b
            else:
                return "Error"  # Evitamos la división por cero
        return b  # En caso de no tener operación, devolvemos b (el número ingresado)

    def equal(self):
        if self.num1 != "":
            self.result = self.calculate(self.num2, float(self.num1), self.operation)
            print(f"num1: {self.num1}, num2: {self.num2}, result = {self.result}")
            self.operation = None
            self.num1 = self.result
            self.display.itemconfig(self.text_disp, text=self.result)

    