deal_map={}
deal_map['A'] = deal_functoin_A
deal_map['B'] = deal_function_B
deal_map['C'] = deal_functoin_C
deal_map['D'] = deal_function_D
deal_map['E'] = deal_functoin_E
deal_map['F'] = deal_function_F
deal_map['G'] = deal_functoin_G
deal_map['H'] = deal_function_H
deal_map['I'] = deal_functoin_I
deal_map['J'] = deal_function_J
deal_map['K'] = deal_functoin_K
deal_map['L'] = deal_function_L
deal_map['M'] = deal_functoin_M
deal_map['N'] = deal_function_N
deal_map['O'] = deal_functoin_O
deal_map['P'] = deal_function_P
deal_map['Q'] = deal_functoin_Q
deal_map['R'] = deal_function_R
deal_map['S'] = deal_functoin_S
deal_map['T'] = deal_function_T
deal_map['U'] = deal_functoin_U
deal_map['V'] = deal_function_V
deal_map['W'] = deal_functoin_W
deal_map['X'] = deal_function_X
deal_map['Y'] = deal_functoin_Y
deal_map['Z'] = deal_function_Z

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

def deal_function_A(k,v,total,sku_map):
    five_deal_total, five_deal_remainder = buy_x_get_for_y(v,5,200)
    three_deal_total, three_deal_remainder = buy_x_get_for_y(five_deal_remainder,3,130)
    total+=(five_deal_total+three_deal_total+(three_deal_remainder*sku_map[k]))

def deal_function_b(k,v,sku_map,checkout_map):
    B_left = buy_x_get_y_free_remaining(checkout_map['E'],v,2)
        if B_left==0:
            total+=0
        else:
            deal_total = (B_left//2)*45
            remainder = (B_left%2)*sku_map[k]
            total+=(deal_total+remainder)
