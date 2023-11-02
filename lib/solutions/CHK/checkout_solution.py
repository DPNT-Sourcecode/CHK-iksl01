

# noinspection PyUnusedLocal
# skus = unicode string

#illegal input return -1
#example input 'ABCBDCCA'

from collections import Counter 
import re
def checkout(skus):
    if bool(re.match('^[ABCDE]*$', skus)) is False:
        return -1

    total = 0
    sku_map = {'A':50, 'B':30, 'C':20, 'D':15, 'E':40}
    checkout_map = Counter(skus)
    for k,v in checkout_map.items():
        if k=='A':
            five_deal_total = (v//5)*500
            five_deal_remainder = v%5
            three_deal_total = (five_deal_remainder//3)*130
            three_deal_remainder = (five_deal_remainder%3)*sku_map[k]
            total+=(five_deal_total+three_deal_total+three_deal_remainder)
        elif k=='B':
            total_B_free=checkout_map['E']//2
            B_left = v-total_B_free
            if B_left<=0:
                total+=0
            else:
                deal_total = (B_left//2)*45
                remainder = (B_left%2)*sku_map[k]
                total+=(deal_total+remainder)
        else:
            total+=sku_map[k]*v
    return total

