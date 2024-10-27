#basic variables
totalMuffins=10
totalCupcakes=1
#other stuff
while totalMuffins>0 or totalCupcakes>0:
    purchase=input('Would you like a muffin or a cupcake?')
    if purchase!=('muffin') and purchase!=('cupcake') and purchase!=('0'):
        print('Please enter muffin or cupcake.')
    if purchase==("muffin") and totalMuffins>0:
            totalMuffins-=1
    elif purchase==('muffin')and totalMuffins==0:
            print("Out of Stock")
    if purchase==('cupcake') and totalCupcakes>0:
            totalCupcakes-=1
    elif purchase==('cupcake'):
        if totalCupcakes==0:
            print('Out of stock')
            
    if purchase==('0'):
        break
print('You have', totalMuffins ,'muffin(s) and', totalCupcakes ,'cupcake(s) left over')
    
    
