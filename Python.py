class Coins: 
  def get_change(self,x,y):
    change = round((x-y)*100)
    coins = [100,50,25,10,5,1] #in paise

    change_coins = [0]*len(coins)

    for i in range(len(coins)): 
       while change>= coins[i]:

         change-=coins [i]

         change_coins[i]+=1

    return change_coins[::-1]

obj = Coins()

#TastCases

print(obj.get_change(5,0.99))
print(obj.get_change(3.14,1.99))
print(obj.get_change(4,3.14))
print(obj.get_change(0.45,0.34))
