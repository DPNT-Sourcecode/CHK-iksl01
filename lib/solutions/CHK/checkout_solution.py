from collections import Counter 
import re

from lib.solutions.CHK.deal_map import Deals
# class Checkout:
#     def __init__(self):
#         pass

#where count_x is the number of x it takes to get a free y

def buy_x_get_y_free_remaining(num_x, num_y, count_x):  
        y_free= num_x//count_x
        y_left = num_y-y_free
        if y_left<=0:
            y_left=0
        return y_left

def buy_x_get_for_y(num_x, count_x, deal_value):
    deal_total = (num_x//count_x)*deal_value
    remainder = num_x%count_x
    return deal_total, remainder


def checkout(skus):
    if bool(re.match('^[ABCDEF]*$', skus)) is False:
        return -1

    total = 0
    sku_map = {'A':50, 'B':30, 'C':20, 'D':15, 'E':40, 'F':10}
    checkout_map = Counter(skus)
    total=0
    for k,v in checkout_map.items():
        # d = Deals(k,v,sku_map,checkout_map,total)
        # total = d.deal_map[k]
        if k=='A':
            five_deal_total, five_deal_remainder = buy_x_get_for_y(v,5,200)
            three_deal_total, three_deal_remainder = buy_x_get_for_y(five_deal_remainder,3,130)
            total+=(five_deal_total+three_deal_total+(three_deal_remainder*sku_map[k]))
        elif k=='B':
            B_left = buy_x_get_y_free_remaining(checkout_map['E'],v,2)
            if B_left==0:
                total+=0
            else:
                deal_total = (B_left//2)*45
                remainder = (B_left%2)*sku_map[k]
                total+=(deal_total+remainder)
        elif k=='F':
            F_left=buy_x_get_y_free_remaining(v,v,3)
            total+=sku_map[k]*F_left
        elif k=='H':
            ten_deal_total, ten_deal_remainder = buy_x_get_for_y(v,10,80)
            five_deal_total, five_deal_remainder = buy_x_get_for_y(ten_deal_remainder,5,45)
            total+=(ten_deal_total+five_deal_total+(five_deal_remainder*sku_map[k]))
        elif k==
        
        else:
            total+=sku_map[k]*v
    return total
