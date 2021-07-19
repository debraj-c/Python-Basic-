import random

# take the seed as input and set the random seed accordingly
x = int(input("For testing, what is the random seed?  >"))
random.seed(x)

money = float(input("How many dollars do you have?  >"))

# declare variables to store the count of roll, highest money earned and the roll of highest earn
count = 0
highest = money 
highestDice = 0

# infinite loop runs until earning becomes 0.0
while(1):
    # generate 2 random numbers between 1 and 6
    x1 = random.randint(1,6)    
    x2 = random.randint(1,6)
    
    count += 1 # increase the count of dice by 1
    # print the dice count and the random numbers within brackets
    print(str(count) + " Dice = (" + str(x1) + ", " + str(x2) + ")", end = "    ")
    
    if x1 + x2 == 7: # if the sum is 7, add 4 to the earning and display it
        money += 4
        print("You win $4!", end = "    ")
        print("Money = $ " + str(money))
    else: # else, subtract 1 from the earning and display it
        money -= 1 
        print("You lose $1.", end = "    ")
        print("Money = $ " + str(money))
        
    # if the money becomes 0.0, terminate the loop    
    if money == 0.0:
        break
    
    # if the money is the highest yet, store the money and the dice count
    if money > highest:
        highest = money
        highestDice = count 
        
# display the highest money and the respective dice count        
print("You should have stopped at roll " + str(highestDice) + " with $" + str("%.2f" % highest))
