# Number of Islands
'''
Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''
import queue

class Solution:
  def numIslands(self, grid: [[str]]) -> int:
    if grid == []:
        return 0
    grid = grid.copy()
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Once land has been identified, mark it off and
    # identify every neighboring land item until you reach
    # only water
    def findIsland(x, y):
      q = queue.Queue()
      q.put((x, y))
      # for entire island
      while not q.empty():
        # get next value and put in the subsequent ones
        x, y = q.get()
        spot = grid[x][y]
        # if it's still land, into the queue
        if spot == '1':
          if x+1 < rows:
            q.put((x+1, y))
          if y+1 < cols:
            q.put((x, y+1))
          if x-1 >= 0:
            q.put((x-1, y))
          if y-1 >= 0:
            q.put((x, y-1))
        # All spots get marked to 'x'
        grid[x][y] = 'x'

    # For each item, if it's land, find its mass
    # If it's water, mark it as X and move on
    for x in range(rows):
      for y in range(cols):
        if grid[x][y] == '1':
          count += 1
          findIsland(x, y)
        else:
          grid[x][y] = 'x'

    return count