def can_see_stage(seats: list[list[int]]) -> bool:
    for col in range(len(seats[0])):
        for row in range(len(seats) - 1):
            if seats[row][col] >= seats[row + 1][col]:
                return False
    return True


print(can_see_stage([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))

print(can_see_stage([
  [2, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]))

print(can_see_stage([
  [1, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]))

print(can_see_stage([
  [0, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]))

print(can_see_stage([[1, 2, 3, 2, 1, 1],
[2, 4, 4, 3, 2, 2],
[5, 5, 5, 10, 4, 4],
[6, 6, 7, 6, 5, 5]]))