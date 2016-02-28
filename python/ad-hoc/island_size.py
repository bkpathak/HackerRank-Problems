# Find the size of the island.
# Input:
# 2D array containing 0 and 1 where 1 means island and 0 means water
# Sample input
# [
#   [1,1,1,1,0,0,0,0,1,1]
#   [1,1,1,1,0,0,0,0,1,1]
#   [1,1,1,1,0,0,0,0,0,0]
#   [0,0,0,0,1,1,1,0,0,0]
#   [0,0,0,0,1,1,1,0,0,0]
# ]
# Output : [12,4,6] # Diagonal are not consider as join

def find_island_util(island_grid, visited, i , j):
    if i < 0 or i >= len(island_grid) or j < 0 or j >= len(island_grid[0]):
        return 0

    if not visited[i][j] and island_grid[i][j]:
        visited[i][j] = True
        return ( 1 + find_island_util(island_grid, visited, i+1, j)
                   + find_island_util(island_grid, visited, i, j+1 )
                   + find_island_util(island_grid, visited, i, j-1))
    return 0

def find_island(island_grid):
    # Create the visited array
    visited = [[False]* len(island_grid[0]) for i in range(len(island_grid))]
    island_count = []

    for i in range(len(island_grid)):
        for j in range(len(island_grid[0])):
            if not visited[i][j] and island_grid[i][j]:
                count = find_island_util(island_grid, visited, i, j)
                island_count.append(count)

    return island_count

if __name__ == "__main__":
    island_grid = [
                    [1,1,1,1,0,0,0,0,1,1],
                    [1,1,1,1,0,0,0,0,1,1],
                    [1,1,1,1,0,0,0,0,0,0],
                    [0,0,0,0,1,1,1,0,0,0],
                    [0,0,0,0,1,1,1,0,0,0]]
    print(find_island(island_grid))
