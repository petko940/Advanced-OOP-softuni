from typing import List

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int):
        try:
            [x for x in self.users_collection if x.username == username][0]
        except IndexError:
            new_user = User(username, age)
            self.users_collection.append(new_user)
            return f"{username} registered successfully."

        raise Exception("User already exists!")

    def upload_movie(self, username: str, movie: Movie):
        try:
            user = [x for x in self.users_collection if x.username == username][0]
        except IndexError:
            raise Exception("This user does not exist!")

        if movie.owner.username != user.username:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        user = [x for x in self.users_collection if x.username == username][0]
        if movie not in user.movies_owned:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for movie_attribute, new_value in kwargs.items():
            if movie_attribute == 'title':
                movie.title = new_value
            elif movie_attribute == 'year':
                movie.year = new_value
            elif movie_attribute == 'age_restriction':
                movie.age_restriction = new_value
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        user = [x for x in self.users_collection if x.username == username][0]

        if movie not in user.movies_owned:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = [x for x in self.users_collection if x.username == username][0]

        if username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = [x for x in self.users_collection if x.username == username][0]

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        output = [x.details() for x in movies]
        return '\n'.join(output)

    def __str__(self):
        all_users = ', '.join([x.username for x in self.users_collection]) if self.users_collection else "No users."
        all_movies = ', '.join([x.title for x in self.movies_collection]) if self.movies_collection else "No movies."

        return f"All users: {all_users}\n" \
               f"All movies: {all_movies}"
