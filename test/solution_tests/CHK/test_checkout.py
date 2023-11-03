from lib.solutions.CHK import checkout_solution


class TestCheckout:
    def test_checkout_no_deal(self):
        assert checkout_solution.checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 965
    
    def test_checkout_3A_deal(self):
        assert checkout_solution.checkout('ABCDAACA') == 130+30+20+15+20+50
    
    def test_checkout_5A_deal(self):
        assert checkout_solution.checkout('ABCDAAAACA') == 200+30+20+15+20+50

    def test_checkout_both_A_deal(self):
        assert checkout_solution.checkout('ABCDAAAACAAA') == 200+130+30+20+15+20
    
    def test_checkout_B_deal(self):
        assert checkout_solution.checkout('ABCBBBD') == 45+45+50+20+15
    
    def test_checkout_E_deal(self):
        assert checkout_solution.checkout('ABCDEE') == 50+20+15+40+40
    
    def test_checkout_B_and_E_deals(self):
        assert checkout_solution.checkout('ABCDBEE') == 50+30+20+15+40+40
    
    def test_checkout_3A_and_B_deals(self):
        assert checkout_solution.checkout('ABCDAAB') == 130+45+20+15
    
    def test_checkout_F_deal(self):
        assert checkout_solution.checkout('ABCFFFDEFFF') == 50+30+20+15+40+10+10+10+10
    
    def test_checkout_M_deal(self):
        assert checkout_solution.checkout('NNNM') == 40+40+40
    
    def test_combo_deal(self):
        assert checkout_solution.checkout('ZZYXZST') == 45+45+17+20

    def test_checkout_empty(self):
        assert checkout_solution.checkout('') == 0
    
    def test_checkout_invalid(self):
        assert checkout_solution.checkout('ABCDE1') == -1
    
    