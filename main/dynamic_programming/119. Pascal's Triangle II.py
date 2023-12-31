'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]

'''
def getRow(rowIndex): 
    if rowIndex == 0:
        return [1]
    
    row = [1] # 因爲 rowIndex = 0 =>[1] 因此設置row=[1]
    
    for i in range(1, rowIndex + 1):
        new_row = [1]
        for j in range(1, i):
            new_row.append(row[j - 1] + row[j])
        new_row.append(1)
        row = new_row
    
    return row

print(getRow(3))
