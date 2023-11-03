from collections import Counter 
import re

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

def combo_deal(k,v, combo_deal_count,sku_map, total):
    if combo_deal_count>=3:
        combo_deal_count-=v
    else:
        total+=sku_map[k]*v

def checkout(skus):
    if bool(re.match('^[A-Z]*$', skus)) is False:
        return -1

    total = 0
    sku_map = {'A':50, 'B':30, 'C':20, 'D':15, 'E':40, 'F':10, 'G':20, 'H':10, 'I':35, 'J':60, 'K':80, 'L':90, 'M':15, 'N':40, 'O':10, 'P':50, 'Q':30, 'R':50, 'S':30, 'T':20, 'U':40, 'V':50, 'W':20, 'X':90, 'Y':10,'Z':50}
    checkout_map = Counter(skus)
    total=0
    combo_deal_count=checkout_map['X']+checkout_map['Y']+checkout_map['Z']+checkout_map['S']+checkout_map['T']
    for k,v in checkout_map.items():
        # if k in ['S','T','X','Y','Z']:
        #     combo_deal_count+=v
        if k=='Z':
            if combo_deal_count>=3:
                combo_deal_count-=v
            else:
                total+=sku_map[k]*v
        elif k in ['S','T','Y']:
            if combo_deal_count>=3:
                combo_deal_count-=v
            else:
                total+=sku_map[k]*v
        elif k=='X':
            if combo_deal_count>=3:
                combo_deal_count-=v
            else:
                total+=sku_map[k]*v
        elif k=='A':
            five_deal_total, five_deal_remainder = buy_x_get_for_y(v,5,200)
            three_deal_total, three_deal_remainder = buy_x_get_for_y(five_deal_remainder,3,130)
            total+=(five_deal_total+three_deal_total+(three_deal_remainder*sku_map[k]))
        elif k=='B':
            B_left = buy_x_get_y_free_remaining(checkout_map['E'],v,2)
            if B_left==0:
                total+=0
            else:
                deal_total, remainder = buy_x_get_for_y(B_left,2,45)
                total+=(deal_total+remainder*sku_map[k])
        elif k=='F':
            F_left=buy_x_get_y_free_remaining(v,v,3)
            total+=sku_map[k]*F_left
        elif k=='H':
            ten_deal_total, ten_deal_remainder = buy_x_get_for_y(v,10,80)
            five_deal_total, five_deal_remainder = buy_x_get_for_y(ten_deal_remainder,5,45)
            total+=(ten_deal_total+five_deal_total+(five_deal_remainder*sku_map[k]))
        elif k=='K':
            deal_total, remainder = buy_x_get_for_y(v,2,150)
            total+=deal_total+remainder*sku_map[k]
        elif k=='M':
            M_left = buy_x_get_y_free_remaining(checkout_map['N'],v,3)
            total+=M_left*sku_map[k]
        elif k=='P':
            deal_total, remainder = buy_x_get_for_y(v,5,200)
            total+=deal_total+(remainder*sku_map[k])
        elif k=='Q':
            Q_left = buy_x_get_y_free_remaining(checkout_map['R'],v,3)
            if Q_left==0:
                total+=0
            else:
                deal_total, remainder = buy_x_get_for_y(Q_left,3,80)
                total+=deal_total+(remainder*sku_map[k])
        elif k=='U':
            U_left=buy_x_get_y_free_remaining(v,v,4)
            total+=sku_map[k]*U_left
        elif k=='V':
            three_deal_total,three_deal_remainder = buy_x_get_for_y(v,3,130)
            two_deal_total, two_deal_remainder = buy_x_get_for_y(three_deal_remainder,2,90)
            total+=(three_deal_total+two_deal_total+(two_deal_remainder*sku_map[k]))
        else:
            total+=sku_map[k]*v
        print(combo_deal_count)
        print(total)
    return total





