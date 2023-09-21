"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the 
i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts. 
The richest customer is the customer that has the maximum wealth.

Approach:

Vi vill kunna ha en lista på formen [[1,2,3],[3,2,1]]
Det programmet ska göra är att det ska ta nummrena från listan och sedan addera dem med varandra.
Summan av den additionen ska motsvara någon form av rikedom.
Programmet ska också kunna jämföra listorna med varandra. 

Lösning: 

Vi vill göra så att elementen i listan adderas 
--> Detta kan vi göra genom en for i in range 

Vi vill sen att resultatet från additionen ska sparas i en ny lista och sedan jämföras



"""
sum_list = []

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        global accounts
        for i in range (1,len(accounts)):
            accounts[i] = accounts[i-1] + accounts[i]
        sum_list.append(accounts)

    
    
    def comparison():
        for i in range(1,sum_list):
            sumlist[i] 