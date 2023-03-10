class Integer:
    def __init__(self, value: int):
        self.value = value

    def from_float(self, float_value):
        if type(float_value) != float:
            return "value is not a float"
        return float(self.value)

    def from_roman(self, value):
        pass

    def from_string(self,value):
        pass


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
