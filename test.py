
import surfshop
import unittest

class SurfshopTests(unittest.TestCase):
    def setUp(self):
        self.cart = surfshop.ShoppingCart()

    def test_add_surfboards(self):
        message = self.cart.add_surfboards(1)
        self.assertEqual(message, f'Successfully added 1 surfboard to cart!')



unittest.main()