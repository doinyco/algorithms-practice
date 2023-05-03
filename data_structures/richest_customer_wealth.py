# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

# Input: accounts = [[1,5],[7,3],[3,5]]
# Output: 10
# Explanation: 
# 1st customer has wealth = 6
# 2nd customer has wealth = 10 
# 3rd customer has wealth = 8
# The 2nd customer is the richest with a wealth of 10.

def maximumWealth(accounts):
        max_wealth = 0
        
        for customer in accounts:
            wealth = sum(customer)
            
            if wealth > max_wealth:
                max_wealth = wealth
                
        return max_wealth

accounts = [[1,5],[7,3],[3,5]]
print(maximumWealth(accounts))