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
        result = 0
        # 비디오 종류별 대여료 계산
        if self.movie.price_code == Movie.REGULAR:
            result += 2
            if self.days_rented > 2:
                result += (self.days_rented - 2) * 1.5
        elif self.movie.price_code == Movie.NEW_RELEASE:
            result += self.days_rented * 3
        elif self.movie.price_code == Movie.CHILDRENS:
            result += 1.5
            if self.days_rented > 3:
                result += (self.days_rented - 3) * 1.5

        return result

    @property
    def frequent_renter_points(self):
        # 최신물을 이틀 이상 대여하면 보너스 포인트 지급
        if self.movie.price_code == Movie.NEW_RELEASE and self.days_rented > 1:
            return 2
        else:
            return 1
