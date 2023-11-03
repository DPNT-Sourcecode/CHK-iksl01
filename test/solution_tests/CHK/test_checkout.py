from lib.solutions.CHK.checkout_solution import Checkout


# class TestCheckout:
def test_checkout_no_deal():
    assert Checkout.checkout(self,skus='ABCDEF') == 50+30+20+15+40+10

def test_checkout_3A_deal(self):
    assert Checkout.checkout('ABCDAACA') == 130+30+20+15+20+50

def test_checkout_5A_deal(self):
    assert Checkout.checkout('ABCDAAAACA') == 200+30+20+15+20+50

def test_checkout_both_A_deal(self):
    assert Checkout.checkout('ABCDAAAACAAA') == 200+130+30+20+15+20

def test_checkout_B_deal(self):
    assert Checkout.checkout('ABCBBBD') == 45+45+50+20+15

def test_checkout_E_deal(self):
    assert Checkout.checkout('ABCDEE') == 50+20+15+40+40

def test_checkout_B_and_E_deals(self):
    assert Checkout.checkout('ABCDBEE') == 50+30+20+15+40+40

def test_checkout_3A_and_B_deals(self):
    assert Checkout.checkout('ABCDAAB') == 130+45+20+15

def test_checkout_F_deal(self):
    assert Checkout.checkout('ABCFFFDEFFF') == 50+30+20+15+40+10+10+10+10


def test_checkout_empty(self):
    assert Checkout.checkout('') == 0

def test_checkout_invalid(self):
    assert Checkout.checkout('ABCDEG') == -1

