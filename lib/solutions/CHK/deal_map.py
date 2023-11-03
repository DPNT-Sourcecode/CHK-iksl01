
class Deals:
    def __init__(k,v,sku_map):
        k=k
        v=v
        sku_map=sku_map
        counter_map=counter_map
        total = total

    def buy_x_get_y_free_remaining(self, num_x, num_y, count_x):  
        y_free= num_x//count_x
        y_left = num_y-y_free
        if y_left<=0:
            y_left=0
        return y_left

    def buy_x_get_for_y(self, num_x, count_x, deal_value):
        deal_total = (num_x//count_x)*deal_value
        remainder = num_x%count_x
        return deal_total, remainder

    def no_deal(self):
        self.total+=self.sku_map[self.k]*self.v
        return self.total

    def deal_A(self):
        five_deal_total, five_deal_remainder = self.buy_x_get_for_y(self.v,5,200)
        three_deal_total, three_deal_remainder = self.buy_x_get_for_y(five_deal_remainder,3,130)
        total+=(five_deal_total+three_deal_total+(three_deal_remainder*self.sku_map[self.k]))
        return total

    def deal_B(self):
        B_left = self.buy_x_get_y_free_remaining(self.checkout_map['E'],self.v,2)
        if B_left==0:
            total+=0
        else:
            deal_total = (B_left//2)*45
            remainder = (B_left%2)*self.sku_map[self.k]
            total+=(deal_total+remainder)
        return total

    def deal_F(self):
        F_left=self.buy_x_get_y_free_remaining(self.v,self.v,3)
        self.total+=self.sku_map[self.k]*F_left
        return self.total

    def deal_H(self):
        ten_deal_total, ten_deal_remainder = self.buy_x_get_for_y(self.v,10,80)
        five_deal_total, five_deal_remainder = self.buy_x_get_for_y(ten_deal_remainder,5,45)
        self.total+=(ten_deal_total+five_deal_total+(five_deal_remainder*self.sku_map[self.k]))
        return self.total

    # def deal_

    deal_map={}
    deal_map['A'] = deal_A
    deal_map['B'] = deal_B
    deal_map['C'] = no_deal
    deal_map['D'] = no_deal
    deal_map['E'] = no_deal
    deal_map['F'] = deal_F
    deal_map['G'] = no_deal
    deal_map['H'] = deal_H
    deal_map['I'] = no_deal
    deal_map['J'] = no_deal
    deal_map['K'] = deal_K
    deal_map['L'] = no_deal
    deal_map['M'] = no_deal
    deal_map['N'] = deal_N
    deal_map['O'] = no_deal
    deal_map['P'] = deal_P
    deal_map['Q'] = deal_Q
    deal_map['R'] = deal_R
    deal_map['S'] = no_deal
    deal_map['T'] = no_deal
    deal_map['U'] = deal_U
    deal_map['V'] = deal_V
    deal_map['W'] = no_deal
    deal_map['X'] = no_deal
    deal_map['Y'] = no_deal
    deal_map['Z'] = no_deal
