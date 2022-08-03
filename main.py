class Person:

    def __init__(self, name):
        self.name = name
        self.age = 22

class Habit:

    def __init__(self, habit_name):
        self.habit_name = habit_name
        self.habit_type = {}
        self.habit_category = {}
        self.triggers_to = {}
        self.triggers_from = {}
        self.place = {}
        self.impact = {}
        self.density = float()
        self.fun = float()
        self.fun = float()
        self.need_minutes = int()
        self.up_to_minutes = int()
        self.need_money = int()
        self.need_gear = {}

tom = Person("Tom")
oleg = Habit("Oleg")