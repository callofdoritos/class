#number of slices per pizza
fullPizza=8
x=.5
#how many slices per person
num_slices=(int(input('How many slices are each person eating?')))
#how many slices total
total=num_slices*4
dividend=total
divisor=8
pizzaLeftover=dividend%8
wholePizzas=total/8
totalPizzas=((wholePizzas+0.5)//1)
if total >=0:
    print('You will need', (int(totalPizzas)) ,' whole pizzas and have', pizzaLeftover ,'slices left over')
if total <0:
    print('No. Try again')
