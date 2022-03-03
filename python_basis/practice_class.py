class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

# class FlyableUnit(Unit, Flyable):
class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__()    # 문제 발생
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()
