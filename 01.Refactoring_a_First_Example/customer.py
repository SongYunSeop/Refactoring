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

    def statement(self):
        total_amount = 0
        frequent_renter_points = 0
        rentals = self._rentals
        result = 'Rental history for ' + self.name + '\n'

        for rental in self._rentals:
            this_amount = self.amount_for(rental)

            # 적립 포인트를 1 포인트 증가
            frequent_renter_points += 1

            # 최신물을 이틀 이상 대여하면 보너스 포인트 지급
            if rental.movie.price_code == Movie.NEW_RELEASE and rental.days_rented > 1:
                frequent_renter_points += 1

            # 대여하는 비디오 정보와 대여료 출력
            result += '\t' + rental.movie.title + '\t' + str(this_amount) + '\n'

            # 현재까지 누적된 총 대여료
            total_amount += this_amount


        # 푸터 행 추가
        result += "누적 대여료: " + str(total_amount) + '\n'
        result += "적립 포인트: " + str(frequent_renter_points)
        return result


    def amount_for(self, rental):
        result = 0
        # 비디오 종류별 대여료 계산
        if rental.movie.price_code == Movie.REGULAR:
            result += 2
            if rental.days_rented > 2:
                result += (rental.days_rented - 2) * 1.5
        elif rental.movie.price_code == Movie.NEW_RELEASE:
            result += rental.days_rented * 3
        elif rental.movie.price_code == Movie.CHILDRENS:
            result += 1.5
            if rental.days_rented > 3:
                result += (rental.days_rented - 3) * 1.5

        return result
