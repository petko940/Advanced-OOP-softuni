class ValueCannotBeNegative(Exception):
    def __init__(self, message):
        self.message = message

    # def __str__(self):
    #     return self.message


for _ in range(5):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative(f"{number} must be {abs(number)}")

# try:
#     for _ in range(5):
#         number = int(input())
#         if number < 0:
#             raise ValueCannotBeNegative("ValueCannotBeNegative")
# except ValueCannotBeNegative:
#     print('ValueCannotBeNegative')
