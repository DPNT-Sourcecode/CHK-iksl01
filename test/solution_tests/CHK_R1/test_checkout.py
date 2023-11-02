from lib.solutions.CHK import checkout_solution


class TestCheckout:
    def test_checkout_no_deal(self):
        assert checkout_solution.checkout('ABCD') == 50+30+20+15
    
    def test_checkout_A_deal(self):
        assert checkout_solution.checkout('ABCDAACAA') == 130+30+20+15+20+50+50
    
    def test_checkout_B_deal(self):
        assert checkout_solution.checkout('ABCBBBD') == 45+45+50+20+15
    
    def test_checkout_both_deals(self):
        assert checkout_solution.checkout('ABCDAAB') == 130+45+20+15
    
    def test_checkout_empty(self):
        assert checkout_solution.checkout('') == 0
    
    def test_checkout_invalid(self):
        assert checkout_solution.checkout('ABCDG') == -1
