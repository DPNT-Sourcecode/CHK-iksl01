from lib.solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3
    
    def test_sum_large(self):
        assert sum_solution.compute(10000, 2200) == 12200
