class Thermostat:
    def __init__(self, target):
        if self._is_valid(target):
            self._target = target
        else:
            raise ValueError("Invalid value")
        self.temp = 20

    def set_target(self, value):
        if self._is_valid(value):
            self._target = value
            return True
        else:
            return False

    def get_target(self):
        return self._target

    def tick(self):
        if self.temp < self._target:
            self.temp += 1
        elif self.temp > self._target:
            self.temp -= 1

    def _is_valid(self, value):
        return 10 <= value <= 30

    def __str__(self):
        return f"Room: {self.temp}°C, target: {self.get_target()}"


if __name__ == "__main__":
    t = Thermostat(22)
    print(t)  # Room: 20°C, target: 22°C
    t.tick()
    t.tick()
    t.tick()
    print(t)  # Room: 22°C, target: 22°C
    print(t.set_target(50))  # False
    print(t.get_target())  # 22
    print(t.set_target(15))  # True
    t.tick()
    print(t)  # Room: 21°C, target: 15°C

    try:
        Thermostat(5)
    except ValueError:
        print("OK")  # OK
