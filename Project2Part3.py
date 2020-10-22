#Project2Part3.py
#project part 3
#python simulation
from random import *
listA1 = [0]
listA2 = [0]
for i in range(1000000):
    LA1 = 6
    LA2 = 2
    CA1 = 4
    CA2 = 4

    #random customer location between 0 and 10
    customerLocation = uniform(0, 10)

    #calculate score A1
    distanceToA1 = abs(customerLocation-LA1)
    scoreA1 = round((10 - distanceToA1) + 3 * (6 - CA1), 5)

    #calculate score A2
    distanceToA2 = abs(customerLocation-LA2)
    scoreA2 = (10 - distanceToA2) + 3 * (6 - CA2)

    #define our B location constant variables
    LB1 = 4
    LB2 = 8
    CB1 = 5
    CB2 = 5
    #calculate scores of B1 and B2
    distanceToB1 = abs(customerLocation-LB1)
    scoreB1 = (10 - distanceToB1) + 3 * (6 - CB1)
    distanceToB2 = abs(customerLocation-LB2)
    scoreB2 = (10 - distanceToB2) + 3 * (6 - CB2)

    #calculate wich A Cafe has a higher score(one of these will always be higher than either B cafe)
    if scoreA1 >= scoreA2:
        listA1.append(2)
    else:
        listA2.append(2)

    #optional code to show table for each customer(uncomment line below:)
    # print("Customer Location:", customerLocation, "Score A1:", scoreA1, "Score A2:", scoreA2, "Score B1:", scoreB1, "Score B2:", scoreB2)

profitA1 = sum(listA1)
profitA2 = sum(listA2)
print("Expected profit at A1 per customer:", profitA1/1000000)
print("Total profit at A1:", profitA1)
print("Expected profit A2 per customer:", profitA2/1000000)
print("Total profit at A2:", profitA2)
print('Total Profit at 1 million trials:', profitA1+profitA2)









