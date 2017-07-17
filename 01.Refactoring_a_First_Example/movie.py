from abc import ABCMeta, abstractmethod

class Movie():
    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    def __init__(self, title, price_code):
        self._title = title
        self.price_code = price_code

    @property
    def price_code(self):
        return self._price_code.get_price_code()

    @price_code.setter
    def price_code(self, price_code):
        if price_code == Movie.REGULAR:
            self._price_code = RegularPrice()
        elif price_code == Movie.NEW_RELEASE:
            self._price_code = NewReleasePrice()
        elif price_code == Movie.CHILDRENS:
            self._price_code = ChildrensPrice()

    @property
    def title(self):
        return self._title

    def get_charge(self, days_rented):
        return self._price_code.get_charge(days_rented)

    def get_frequent_renter_points(self, days_rented):
        return self._price_code.get_frequent_renter_points(days_rented)


class Price:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_price_code(self):
        pass

    @abstractmethod
    def get_charge(self, days_rented):
        pass

    @abstractmethod
    def get_frequent_renter_points(self, days_rented):
        pass


class ChildrensPrice(Price):

    def get_price_code(self):
        return Movie.CHILDRENS

    def get_charge(self, days_rented):
        result = 1.5
        if days_rented > 3:
            result += (days_rented - 3) * 1.5
        return result

    def get_frequent_renter_points(self, days_rented):
        return 1


class NewReleasePrice(Price):

    def get_price_code(self):
        return Movie.NEW_RELEASE

    def get_charge(self, days_rented):
        return days_rented * 3

    def get_frequent_renter_points(self, days_rented):
        return 2 if days_rented > 1 else 1


class RegularPrice(Price):

    def get_price_code(self):
        return Movie.REGULAR

    def get_charge(self, days_rented):
        result = 2
        if days_rented > 2:
            result += (days_rented - 2) * 1.5
        return result

    def get_frequent_renter_points(self, days_rented):
        return 1
