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

## 리팩토링!

`statement` 메서드에 너무 많은 기능을 가지고 있으므로 쪼개보자

### Extract Method - 메서드 추출

논리적 코드 뭉치를 찾아서 메서드화 하는 방법

`statement` 안의 `if`문을 아래처럼 하나의 메서드로 추출하자

```python
class Customer():
    ...

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
        this_amount = 0
        # 비디오 종류별 대여료 계산
        if rental.movie.price_code == Movie.REGULAR:
            this_amount += 2
            if rental.days_rented > 2:
                this_amount += (rental.days_rented - 2) * 1.5
        elif rental.movie.price_code == Movie.NEW_RELEASE:
            this_amount += rental.days_rented * 3
        elif rental.movie.price_code == Movie.CHILDRENS:
            this_amount += 1.5
            if rental.days_rented > 3:
                this_amount += (rental.days_rented - 3) * 1.5

        return this_amount
```

테스트를 수행하고 잘 돌아가는지 확인하자

> 리팩토링은 프로그램을 조금씩 단계적으로 수정하므로 실수해도 버그를 찾기 쉽다.

추출한 `amount_for` 메서드 안의 변수명이 마음에 들지 않는데 바꿔주자

좋은 코드는 그거이 무슨 기능을 하는지 분명히 드러나야 한다.

> 컴퓨터가 인식 가능한 코드는 바보라도 작성할 수 있지만, 인간이 이해할 수 있는 코드는 실력 있는 프로그래머만 작성할 수 있다.

```python
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
```

### Move Method - 메서드 옮기기

`Customer` 클래스의 `amount_for` 메서드는 `Rental` 클래스의 정보를 이용하고 `Customer` 의 정보는 사용하지 않는다.

그러므로 메서드 이동 기법 `amount_for`를 `Rental` 클래스로 옮기자

```python
from movie import Movie

class Rental():
    ...

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
```

메서드를 옮기면서 매개변수가 삭제되고 메서드의 이름도 적절하게 바꿨다.

`Customer`의 `amount_for` 메서드도 바꿔주자

```python
from movie import Movie

class Customer():
    ...

    def statement(self):
        total_amount = 0
        frequent_renter_points = 0
        rentals = self._rentals
        result = 'Rental history for ' + self.name + '\n'

        for rental in self._rentals:
            this_amount = rental.charge

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

그 다음으로 `this_amount` 변수의 중복이 있는데   
임시변수를 메서드 호출로 전환(Replace Temp with Query) 기법을 사용해서 `this_amount` 변수를 삭제하자

```python
from movie import Movie

class Customer():
    ...

    def statement(self):
        total_amount = 0
        frequent_renter_points = 0
        rentals = self._rentals
        result = 'Rental history for ' + self.name + '\n'

        for rental in self._rentals:
            # 적립 포인트를 1 포인트 증가
            frequent_renter_points += 1

            # 최신물을 이틀 이상 대여하면 보너스 포인트 지급
            if rental.movie.price_code == Movie.NEW_RELEASE and rental.days_rented > 1:
                frequent_renter_points += 1

            # 대여하는 비디오 정보와 대여료 출력
            result += '\t' + rental.movie.title + '\t' + str(rental.charge) + '\n'

            # 현재까지 누적된 총 대여료
            total_amount += rental.charge

        # 푸터 행 추가
        result += "누적 대여료: " + str(total_amount) + '\n'
        result += "적립 포인트: " + str(frequent_renter_points)
        return result
```

### 적립 포인트 메서드 추출

`frequent_renter_points`를 계산하는 부분을 메서드로 빼서 `Rental` 클래스로 옮겼다.

```python
class Customer():
    ...

    def statement(self):
        total_amount = 0
        frequent_renter_points = 0
        rentals = self._rentals
        result = 'Rental history for ' + self.name + '\n'

        for rental in self._rentals:
            this_amount = rental.charge
            frequent_renter_points += rental.frequent_renter_points

            # 대여하는 비디오 정보와 대여료 출력
            result += '\t' + rental.movie.title + '\t' + str(this_amount) + '\n'

            # 현재까지 누적된 총 대여료
            total_amount += this_amount

        # 푸터 행 추가
        result += "누적 대여료: " + str(total_amount) + '\n'
        result += "적립 포인트: " + str(frequent_renter_points)
        return result

class Rental():
    ...

    @property
    def frequent_renter_points(self):
        # 최신물을 이틀 이상 대여하면 보너스 포인트 지급
        if self.movie.price_code == Movie.NEW_RELEASE and self.days_rented > 1:
            return 2
        else
            return 1
```

### 임시변수 없애기

`Customer`의 `total_amount` 변수와 `frequent_renter_points` 변수는 출력할 때만 사용되므로 변수를 제거해 메서드로 바꾸자

```python
class Customer():
    ...

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
```

잠깐 멈추고 생각해보면 리팩토링을 하면 코드가 줄어들고 성능이 좋아질 거라 예상하지만  
지금의 리팩토링은 코드가 늘어나고 반복문이 늘어남으로 성능이 저하되었다.

이러한 문제들은 최적화 단계에서 수정하자.
