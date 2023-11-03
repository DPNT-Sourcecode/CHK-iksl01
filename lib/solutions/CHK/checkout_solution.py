from collections import Counter 
import re
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
    for k,v in checkout_map.items():
        if k=='A':
            five_deal_total, five_deal_remainder = buy_x_get_for_y(v,5,200)
            three_deal_total, three_deal_remainder = buy_x_get_for_y(five_deal_remainder,3,130)
            total+=(five_deal_total+three_deal_total+(three_deal_remainder*sku_map[k]))

            # five_deal_total = (v//5)*200
            # five_deal_remainder = v%5
            # three_deal_total = (five_deal_remainder//3)*130
            # three_deal_remainder = (five_deal_remainder%3)*sku_map[k]
            # total+=(five_deal_total+three_deal_total+three_deal_remainder)
        elif k=='B':
            B_left = buy_x_get_y_free_remaining(checkout_map['E'],v,2)
            if B_left==0:
                total+=0
            else:
                deal_total = (B_left//2)*45
                remainder = (B_left%2)*sku_map[k]
                total+=(deal_total+remainder)

            
            # total_B_free=checkout_map['E']//2
            # B_left = v-total_B_free
            # if B_left<=0:
            #     total+=0
            # else:
            #     deal_total = (B_left//2)*45
            #     remainder = (B_left%2)*sku_map[k]
            #     total+=(deal_total+remainder)
        elif k=='F':
            if v>=3:
                total_F_free=v//3
                v=v-total_F_free
            total+=sku_map[k]*v
        else:
            total+=sku_map[k]*v
    return total


