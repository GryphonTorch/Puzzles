# -*- coding: utf-8 -*-
"""
EIGHT QUEENS PROBLEM:
Place eight chess queens on an 8×8 chessboard so that no 
two queens threaten each other
Quasi~Brute force approach here?
    
"""

# observe that no two queens can share the same column or row
# so at most 8x7x6...x1 = 8! = 40320 cases to try
# Pseudocode:
# (Populate queens) In first column, pick one of eight; in second
# column, pick one from seven...
#
# Check for those that fail
# Save solutions

def placeQueens(y1,y2,y3,y4,y5,y6,y7,y8):
    """Represents placing queens on 8x8 chessboard.
    Returns position as list of [xi,yi] list for 1 to 8."""
    position = [[1,y1],[2,y2],[3,y3],[4,y4],\
                [5,y5],[6,y6],[7,y7],[8,y8]]
    return position

def checkSafe(position):
    """returns boolean true or false based on position 
    of Eight Queens. Express each Queen position as [x,y] list
    position is list of list: [[x1,y1],[x2,y2]...[x8,y8]]"""
    
    # in this layout, we know the rows and columns are distinct
    # just check diagonals. if abs(gap) is (k,k) --> fail
    for i in range(0,8):      # 8 lists in list 
        for j in range(i+1,8): 
            xgap = i - j
            ygap = position[i][1] - position[j][1]
            if abs(xgap) == abs(ygap):
                return False   
    return True

def drawSolution(position):
    """Draw a simple solution 
    Call example: drawSolution(safeSpots[4])  
    
    position = [[1,y1],[2,y2],[3,y3],[4,y4],\
                [5,y5],[6,y6],[7,y7],[8,y8]]
    
    """
    
    picture = ["","","","","","","",""]
    
    for i in range(0,8):
        yi = position[i][1]  # gets y value (row), 1 to 8
        xi = position[i][0]  # gets x value (column), 1 to 8

        #print(xi,yi)
        
        row = ""    # to draw. note xi loop in order
        for xempty in range(1,xi):
            row += "_ "
        row += "Q "
        for xempty in range(xi+1,9):
            row += "_ "
                
        picture[yi-1] = row

    for j in range(0,8):
        print(picture[j])
    return picture

    #print("_ _ _ _ X _ _ ")    # underscore, space character combination
    



safeSpots = []   # result list

for y1 in range(1,9):           # column 1
    for y2 in range(1,9):       # column 2
        if y2 != y1:
            for y3 in range(1,9): # column 3
                if y3 != y1 and y3 != y2:
                    for y4 in range(1,9): # column 4
                        if y4 != y1 and y4 != y2 and y4 != y3:
                            for y5 in range(1,9):           # column 5
                                 if y5 != y1 and y5 != y2 and y5 != y3 and y5 != y4:
                                     for y6 in range(1,9):       # column 6
                                         if y6 != y1 and y6 != y2 and y6 != y3 and y6 != y4 and y6 != y5:    
                                             for y7 in range(1,9): # column 7
                                                 if y7 != y1 and y7 != y2 and y7 != y3 and y7 != y4 and y7 != y5 and y7 != y6:    
                                                     for y8 in range(1,9): # column 8
                                                         if y8 != y1 and y8 != y2 and y8 != y3 and y8 != y4 and y8 != y5 and y8 != y6 and y8 != y7:
                                                             positions = placeQueens(y1,y2,y3,y4,y5,y6,y7,y8)
                                                             result = checkSafe(positions)
                                                             if result == True:
                                                                 safeSpots.append(positions)
                            
print(len(safeSpots)) 
print("Some sample solutions: ")  
     
for i in range(0,4):
    result = drawSolution(safeSpots[i]) 
    print("  ")       