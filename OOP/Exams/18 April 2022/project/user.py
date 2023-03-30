from typing import List


class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked: List = []
        self.movies_owned: List = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == '':
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        liked_movies = ["\n".join([movie.details() for movie in self.movies_liked])
                        if self.movies_liked else "No movies liked."]
        owned_movies = ["\n".join([movie.details() for movie in self.movies_owned])
                        if self.movies_owned else "No movies owned."]

        result = [f"Username: {self.username}, Age: {self.age}", "Liked movies:",
                  '\n'.join(x for x in liked_movies),
                  "Owned movies:",
                  '\n'.join(x for x in owned_movies)]

        return '\n'.join(result)
