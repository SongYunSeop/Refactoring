# 맛보기 예제

비디오 대여점에서 고객의 대여로 내역을 계산하고 출력하는 간단한 프로그램

## 맛보기 프로그램

### Movie Class

```python
# movie.py

class Movie():
    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    def __init__(self, title, price_code):
        self._title = title
        self._price_code = price_code

    @property
    def price_code(self):
        return self._price_code

    @price_code.setter
    def price_code(self, price_code):
        self._price_code = price_code

    @property
    def title(self):
        return self._title
```

### Rental Class

```python
# rental.py

class Rental():
    def __init__(self, movie, days_rented):
        self._movie = movie
        self._days_rented = days_rented

    @property
    def dyas_rendted(self):
        return self._days_rented

    @property
    def movie(self):
        return self._movie
```

### Customer Class

```python
# customer.py

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
        frequent_renter_ponits = 0
        rentals = self._rentals
        result = 'Rental history for ' + self.name + '\n'

        for rental in self.rentals:
            this_amount = 0

            # 비디오 종류별 대여료 계산
            if rental.movie.price_code == Movie.REGULAR:
                this_amount += 2
                if rental.days_rented > 2:
                    this_amout += (rental.days_rented - 2) * 1.5
            elif rental.movie.price_code == Movie.NEW_RELEASE:
                this_amount += rantal.days_rented * 3
            elif rental.movie.price_code == Movie.CHILDRENS:
                this_amount += 1.5
                if rental.days_rented > 3:
                    this_amount += (rental.days_rented - 3) * 1.5


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
```

### 이 프로그램은...

사실 이런 코드들은 오료없이 돌아가고 알아보기도 쉬워서 별 문제가 안될 수도 있다.

일단 `Customer` 클래스에서 너무 많은 일을 하고 있다.

그리고 `statement` 메서드와 비슷한 기능으로 결과를 HTML로 받고 싶다면 `html_statement`라는 메서드를 또 만들어야하는데  
대부분 기능이 같기 때문에 **중복 코드**가 발생하게 된다.

중복 코드를 추후에 수정하게 된다면 중복된 만큼 수정을 해야하는 번거롭고 에러 발생 위험이 있는 작업을 해야한다.

## 리팩토링 첫 단계

리팩토링의 첫 단계는 늘 **신뢰도 높은 각종 테스트를 작성**하는 것으로 시작

테스트에서 중요한 것 중 하나는 **테스트 코드가 결과를 출력하는 방식**

테스트를 통과한다면 `OK`를 출력하고 실패한다면 실패 사유를 출력하자

[테스트코드](./test_video_store.py)를 작성하고 리팩토링을 해보자








