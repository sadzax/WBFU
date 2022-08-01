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

class Habit:
    def local_inputter(self, message):
        input(message)
    def Create_Habit_Good(self, name):
        name = self.local_inputter(f"Name of the Habit: ")
        habit_category = {}
        triggers_to = {}
        triggers_from = {}
        impact = {}
        density = float()
        fun = float()
        time = 0
    def Create_Habit_Bad(self, name):
        name = self.local_inputter(f"Name of the Habit: ")
        habit_category = {}
        damage = {}

