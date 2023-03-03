class Account:
    def __init__(self, user_id: int, balance: int, pin: int):
        self.__id = user_id
        self.__pin = pin
        self.balance = balance

    def get_id(self, pin):
        if pin != self.__pin:
            return "Wrong pin"
        return self.__id

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "Pin changed"
        return "Wrong pin"
