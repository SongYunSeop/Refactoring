import unittest

from movie import Movie
from rental import Rental
from customer import Customer

class TestVideoStore(unittest.TestCase):

    def setUp(self):
        # Create customer
        self.customer = Customer('yunseop')


    def test_for_rent_one_new_release_movie(self):
        # Create movie 'The Avengers'
        avengers = Movie('The Avengers', Movie.NEW_RELEASE)

        # Rent avengers for 3 days
        rent_avengers_for_3_days = Rental(avengers, 3)

        self.customer.add_rental(rent_avengers_for_3_days)

        expected_result = 'Rental history for yunseop\n\tThe Avengers\t9\n누적 대여료: 9\n적립 포인트: 2'
        self.assertEquals(self.customer.statement(), expected_result)


    def test_for_rent_one_children_movie(self):
        # Create movie 'The Avengers'
        avengers = Movie('The Avengers', Movie.CHILDRENS)

        # Rent avengers for 2 days
        rent_avengers_for_2_days = Rental(avengers, 2)

        self.customer.add_rental(rent_avengers_for_2_days)

        expected_result = 'Rental history for yunseop\n\tThe Avengers\t1.5\n누적 대여료: 1.5\n적립 포인트: 1'
        self.assertEquals(self.customer.statement(), expected_result)


    def test_for_rent_one_regular_movie(self):
        # Create movie 'The Avengers'
        avengers = Movie('The Avengers', Movie.REGULAR)

        # Rent avengers for 2 days
        rent_avengers_for_2_days = Rental(avengers, 2)

        self.customer.add_rental(rent_avengers_for_2_days)

        expected_result = 'Rental history for yunseop\n\tThe Avengers\t2\n누적 대여료: 2\n적립 포인트: 1'
        self.assertEquals(self.customer.statement(), expected_result)


    def test_for_rent_two_movie(self):
        # Create movie 'The Avengers'
        avengers = Movie('The Avengers', Movie.NEW_RELEASE)

        # Create movie 'Okja'
        okja = Movie('Okja', Movie.NEW_RELEASE)

        # Rent avengers for 3 days
        rent_avengers_for_3_days = Rental(avengers, 3)

        # Rent okja for 3 days
        rent_okja_for_3_days = Rental(okja, 3)

        self.customer.add_rental(rent_avengers_for_3_days)
        self.customer.add_rental(rent_okja_for_3_days)

        expected_result = 'Rental history for yunseop\n\tThe Avengers\t9\n\tOkja\t9\n누적 대여료: 18\n적립 포인트: 4'
        self.assertEquals(self.customer.statement(), expected_result)

    
    def test_for_rent_three_movie(self):
        # Create movie 'The Avengers'
        avengers = Movie('The Avengers', Movie.NEW_RELEASE)

        # Create movie 'Okja'
        okja = Movie('Okja', Movie.CHILDRENS)
        
        # Create movie 'Limitless'
        limitless = Movie('Limitless', Movie.REGULAR)

        # Rent avengers for 3 days
        rent_avengers_for_3_days = Rental(avengers, 3)

        # Rent okja for 3 days
        rent_okja_for_3_days = Rental(okja, 3)

        # Rent limitless for 3 days
        rent_limitless_for_3_days = Rental(limitless, 3)

        self.customer.add_rental(rent_avengers_for_3_days)
        self.customer.add_rental(rent_okja_for_3_days)
        self.customer.add_rental(rent_limitless_for_3_days)

        expected_result = 'Rental history for yunseop\n\tThe Avengers\t9\n\tOkja\t1.5\n\tLimitless\t3.5\n누적 대여료: 14.0\n적립 포인트: 4'
        self.assertEquals(self.customer.statement(), expected_result)

    
