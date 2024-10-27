#number of slices per pizza
# full pizza is 8 slices
x=.5
#how many slices per person
p1=(int(input('How many slices is the first person eating?')))
p2=(int(input('How many slices is the second person eating?')))
p3=(int(input('How many slices is the third person eating?')))
p4=(int(input('How many slices is the fourth person eating?')))

if p1 <0:
    print('Please try again.')

if p2 <0:
        print('Please try again.')

if p3 <0:
         print('Please try again.')

if p4 <0:
          print('Please try again.')
#how many slices total
total=(p1+p2+p3+p4)
dividend=total
divisor=8
pizzaLeftover=dividend%8
wholePizzas=total/8
totalPizzas=((wholePizzas+0.5)//1)
if total >=0:
    print('You will need', (int(totalPizzas)) ,' whole pizzas and have', pizzaLeftover ,'slices left over')
if total <0:    print('No. Try again')
