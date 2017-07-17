from movie import Movie

class Rental():
    def __init__(self, movie, days_rented):
        self._movie = movie
        self._days_rented = days_rented

    @property
    def days_rented(self):
        return self._days_rented

    @property
    def movie(self):
        return self._movie

    @property
    def charge(self):
        return self.movie.get_charge(self.days_rented)

    @property
    def frequent_renter_points(self):
        return self.movie.get_frequent_renter_points(self.days_rented)
