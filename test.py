
import surfshop
import unittest

class SurfshopTests(unittest.TestCase):
    def setUp(self):
        self.cart = surfshop.ShoppingCart()

    def test_add_surfboard(self):
        message = self.cart.add_surfboards(1)
        self.assertEqual(message, f'Successfully added 1 surfboard to cart!')

    def test_add_surfboards(self):
        for num in [2, 3]:
            with self.subTest():
                message = self.cart.add_surfboards(num)
                self.assertEqual(message, f'Successfully added {num} surfboards to cart!')

    def test_to_many_boards(self):
        self.assertRaises( surfshop.TooManyBoardsError, self.cart.add_surfboards, 6)


    def test_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)




unittest.main()