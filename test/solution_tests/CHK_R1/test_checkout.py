from lib.solutions.CHK import checkout_solution


class TestCheckout:
    def test_checkout_no_deal(self):
        assert checkout_solution.checkout('ABCD') == 50+30+20+15
