import time
from random import randint
import os


def log(function):
    """Décorateur log qui va etre appelé a la definition des mes fonctions"""
    def modif(*param):
        start = time.time()
        unit = ["s", "ms", "ns"]
        with open("machine.log", "a") as log_file:
            if len(param) == 2:
                res = function(param[0], param[1])
            else:
                res = function(param[0])
            elapsed = time.time() - start
            i = 0
            while elapsed < 1 and i < 1 and elapsed != 0:
                elapsed *= 1000
                i += 1
            log_file.write((
                "(nlecaill)Running: {:<40}[ exec-time = {} {:<3}]\n"
                    .format(str(function.__name__).capitalize(),
                            str(elapsed)[:5], unit[i])))
            log_file.close()
            return res
    return modif


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
