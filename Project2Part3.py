#Project2Part3.py
#project part 3
#python simulation
from random import *

def getProfit(LA1, LA2, CA1, CA2):
    listA1 = [0]
    listA2 = [0]

    #iterates 1 million times
    for i in range(1000000):


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

        #calculate which A Cafe has a higher score(one of these will always be higher than either B cafe)
        #adds a 2 to list if condition is true(profit will be 2 for both because we charge $4)
        if scoreA1 >= scoreA2:
            listA1.append(2)
        else:
            listA2.append(2)

        #optional code to show table for each customer(uncomment line below:)
        print("Customer Location:", customerLocation, "Score A1:", scoreA1, "Score A2:", scoreA2, "Score B1:", scoreB1, "Score B2:", scoreB2)

    #calculates our profit by compiling all the items in our list and getting the sum
    profitA1 = sum(listA1)
    profitA2 = sum(listA2)


    print("Expected profit at A1 per customer:", profitA1/1000000)
    print("Total profit at A1:", profitA1)
    # print(listA1)
    print("Expected profit A2 per customer:", profitA2/1000000)
    print("Total profit at A2:", profitA2)
    # print(listA2)
    print('Total Profit at 1 million trials:', profitA1+profitA2)


if __name__ == '__main__':
    getProfit(6, 2, 4, 4)






