def cc(amount, coin_values):
    
    def first_denomination(elem):
        if elem:
            return elem[0]
        return 0
    
    no_more = lambda list_: not len(list_)
    except_first_denomination = lambda list_: list_[1::]
    
    if amount == 0:
        return 1
    if amount < 0 or no_more(coin_values):
        return 0
    else:
        return cc(amount, except_first_denomination(coin_values)) + cc(amount - first_denomination(coin_values), coin_values)



    
us_coins = [50, 25, 10, 5, 1]
uk_coins = [100, 50, 20, 10, 5, 2, 1, 0.5]


print(cc(30, us_coins[::-1]))
print(cc(30, us_coins))
print(cc(100, us_coins[::-1]))
print(cc(100, us_coins))


    
    
    