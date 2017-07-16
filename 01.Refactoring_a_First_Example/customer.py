from movie import Movie

class Customer():
    def __init__(self, name):
        self._name = name
        self._rentals = []

    def add_rental(self, rental):
        self._rentals.append(rental)

    @property
    def name(self):
        return self._name

    @property
    def total_amount(self):
        result = 0
        for rental in self._rentals:
            # 현재까지 누적된 총 대여료
            result += rental.charge

        return result

    @property
    def frequent_renter_points(self):
        result = 0
        for rental in self._rentals:
            result += rental.frequent_renter_points

        return result

    def statement(self):
        rentals = self._rentals
        result = 'Rental history for ' + self.name + '\n'

        for rental in self._rentals:
            # 대여하는 비디오 정보와 대여료 출력
            result += '\t' + rental.movie.title + '\t' + str(rental.charge) + '\n'

        # 푸터 행 추가
        result += "누적 대여료: " + str(self.total_amount) + '\n'
        result += "적립 포인트: " + str(self.frequent_renter_points)
        return result
