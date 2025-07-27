def minCoins(coins, V, mem):
    if len(coins)==0:
        return -1
    og_V = V
    if f"{V}-{coins}" in mem:
        return mem[f"{V}-{coins}"]
    min_count = []
    for i in range(len(coins)):
        if V<coins[i]:
            continue
        coins_count1 = 0
        coins_count2 = 0
        
        coins_count2 = minCoins(coins[i+1:len(coins)],V,mem)                    
        
        while V>=coins[0]:
            V=V-coins[0]
            coins_count1+=1
        if V != 0:
            rem_coins = minCoins(coins[i+1:len(coins)],V,mem)
            if rem_coins == -1:
                coins_count1 = -1
            else:
                coins_count1 = coins_count1 + rem_coins
        
        
        if coins_count1 == -1:
            min_count.append(coins_count2)
        elif coins_count2 == -1:
            min_count.append(coins_count1)
        else:
            min_count.append(min(coins_count1, coins_count2))
    min_coins=-1
    for i in min_count:
        if (i>min_coins and min_coins == -1) or (i<min_coins and i!=-1):
            min_coins = i
    mem[f"{og_V}-{coins}"] = min_coins
    return min_coins

# Suffix Code 
coins = [9, 6, 5, 1]
V = 11
mem = {}
m = minCoins(coins, V, mem)
print(m)