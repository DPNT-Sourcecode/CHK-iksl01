

# noinspection PyUnusedLocal
# skus = unicode string

#illegal input return -1
#example input 'ABCBDCCA'

from collections import Counter 
import re
def checkout(skus):
    if bool(re.match('^[ABCD]+$', skus)) is False:
        return -1

    total = 0
    sku_map = {'A':50, 'B':30, 'C':20, 'D':15}
    checkout_map = Counter(skus)
    for k,v in checkout_map.items():
        if k=='A':
            deal_total = (v//3)*130
            remainder = (v%3)*sku_map[k]
            total+=(deal_total+remainder)
        elif k=='B':
            deal_total = (v//2)*45
            remainder = (v%2)*sku_map[k]
            total+=(deal_total+remainder)
        else:
            total+=sku_map[k]*v
    return total


