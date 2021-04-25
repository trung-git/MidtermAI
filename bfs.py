# -*- coding: utf-8 -*-
"""BFS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19HJ1jJLhI9ZUOL5JPqnylhMt8CucrpQ7
"""

class island():
  def __init__(self):
    self.grid = []
  def display(self):
    print("Display island : ")
    for i in self.grid:
        print(i)
def countNumIslands_BFS(grid):
  if(grid == None or len(grid) == 0):
    print("Island is empty")
    return
  countIsland = 0
  row = len(grid)
  col = len(grid[0])
  visited = [[False for i in range(row)] for i in range(col)]
  moveDirections = [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]

  queue = []


  for i in range(row):
    for j in range(col):
      if(grid[i][j] == 1 and visited[i][j] == False):
        countIsland += 1
        queue.append([i,j])
        visited[i][j] = True
        grid[i][j] = countIsland
        
        while(len(queue)> 0) :
          current = queue.pop(0)
          ##print("*******Current : ",current,countIsland)
          for direct in moveDirections:
            
            temp_row = current[0] + direct[0]
            temp_col = current[1] + direct[1]
            ##print("++++Direct: ",direct)
            
            if(temp_row >= 0 and temp_row < row and temp_col < col and temp_col >= 0 ):
              if(grid[temp_row][temp_col] == 1 and visited[temp_row][temp_col] == False):
                queue.append([temp_row,temp_col])
                ##print("Temp :",[temp_row,temp_col],countIsland )
                grid[temp_row][temp_col] = countIsland
                visited[temp_row][temp_col] = True
             
  return countIsland

  
if __name__ == "__main__" :
  data = [[1,0,1,0,0,0,1,1,1,1],
          [0,0,1,0,0,0,1,0,0,0],
          [1,1,1,1,0,0,1,0,0,0],
          [1,0,0,1,0,1,0,0,0,0],
          [1,1,1,1,0,0,0,1,1,1],
          [0,1,0,1,0,0,1,1,1,1],
          [0,0,0,0,0,1,1,1,0,0],
          [0,0,0,1,0,0,1,1,1,0],
          [1,0,1,0,1,0,0,1,0,0],
          [1,1,1,1,0,0,0,1,1,1]]
  island = island()
  island.grid = data
  island.display()
  c = countNumIslands_BFS(island.grid)
  island.display()