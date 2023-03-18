from typing import List

from project.movie_specification.action import Action
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int):
        for user in self.users_collection:
            if user.username == username:
                raise Exception("User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        for u in self.users_collection:
            if u.username == username:
                current_user = u
                break
        # 2
        else:
            raise Exception("This user does not exist!")

        if movie.owner != current_user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        # 4
        for m in self.movies_collection:
            if m.title in movie.title:
                raise Exception("Movie already added to the collection!")

        current_user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        for m in self.movies_collection:
            if m.title == movie.title:
                current_movie = m
                break
        else:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        for u in self.users_collection:
            if u.username == username:
                if movie not in u.movies_owned:
                    raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            if key == "title":
                current_movie.title = value
            elif key == "year":
                current_movie.year = value
            elif key == "age_restriction":
                current_movie.age_restriction = value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        current_user = None
        for u in self.users_collection:
            if u.username == username:
                current_user = u
                break

        if movie.owner.username != current_user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        current_user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        current_user = None
        for u in self.users_collection:
            if u.username == username:
                current_user = u

        if movie in current_user.movies_owned:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in current_user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        current_user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        current_user = None
        for u in self.users_collection:
            if u.username == username:
                current_user = u

        if movie not in current_user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        current_user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        output = []
        for m in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
            output.append(m.details())

        return '\n'.join(output)

    def __str__(self):
        output = [
            f"All users: {', '.join(x.username for x in self.users_collection)}" if self.users_collection else "All users: No users.",
            f"All movies: {', '.join(x.title for x in self.movies_collection)}" if self.movies_collection else "All movies: No movies."]
        return "\n".join(output)
