def inputter(input_descripton, arg_error, arg_is, agr_not_more, agr_not_less):
    while True:
        try:
            i = input(input_descripton)
            if i < agr_not_less or i > agr_not_more or i == arg_is or arg_is is True:
                print(arg_error)
                continue
            return i
            break
        except:
            print(arg_error)
            continue

class Category:
    pass

class User:
    pass

class Testings:
    pass

class Behaviour:
    pass


    def Create_Habit_Good(self, name):
        name = self.local_inputter(f"Name of the Habit: ")
        habit_category = {}
        triggers_to = {}
        triggers_from = {}
        impact = {}
        density = float()
        fun = float()
        time = 0

        self.habit_name = habit_name
        self.habit_type = habit_type
        self.habit_category = habit_category
        self.triggers_to = triggers_to
        self.triggers_from = triggers_from
        self.place = place
        self.impact = impact
        self.density = density
        self.fun = fun
        self.need_minutes = need_minutes
        self.up_to_minutes = up_to_minutes
        self.need_money = need_money
        self.need_gear = need_gear
        Habit.habit_count += 1

class Habit:
    def __init__(self, habit_name, density, fun):
        self.habit_name = habit_name
        self.density = density
        self.fun = fun

    """Base class for Good Habits"""