import intcode

code = [3,8,1005,8,311,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,28,1,1104,0,10,1006,0,71,2,1002,5,10,2,1008,5,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,66,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,87,1006,0,97,2,1002,6,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,116,1006,0,95,1,1009,10,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,145,1,1002,19,10,2,1109,7,10,1006,0,18,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,179,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,200,1,1105,14,10,1,1109,14,10,2,1109,11,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,235,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1002,8,1,257,2,101,9,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,282,2,1109,19,10,1,105,0,10,101,1,9,9,1007,9,1033,10,1005,10,15,99,109,633,104,0,104,1,21102,937268368140,1,1,21102,328,1,0,1106,0,432,21102,1,932700599052,1,21101,0,339,0,1105,1,432,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,0,209421601831,1,21102,1,386,0,1106,0,432,21102,235173604443,1,1,21102,1,397,0,1106,0,432,3,10,104,0,104,0,3,10,104,0,104,0,21101,825439855372,0,1,21102,1,420,0,1106,0,432,21101,0,988220907880,1,21102,431,1,0,1106,0,432,99,109,2,22101,0,-1,1,21101,40,0,2,21102,1,463,3,21102,453,1,0,1106,0,496,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,458,459,474,4,0,1001,458,1,458,108,4,458,10,1006,10,490,1102,1,0,458,109,-2,2106,0,0,0,109,4,2102,1,-1,495,1207,-3,0,10,1006,10,513,21102,0,1,-3,22102,1,-3,1,21202,-2,1,2,21102,1,1,3,21101,532,0,0,1105,1,537,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,560,2207,-4,-2,10,1006,10,560,21201,-4,0,-4,1106,0,628,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21102,1,579,0,1106,0,537,21202,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,598,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,620,21201,-1,0,1,21102,1,620,0,105,1,495,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]

intcode = intcode.IntCodeRunner(code)

def get_color(pos_x, pos_y):
    if (pos_x, pos_y) in grid:
        return grid[(pos_x, pos_y)]
    else:
        return 1 # white by default

def move(facing, turn):
    turn = turn if turn == 1 else -1

    delta_x = 0
    delta_y = 0
    new_facing = (facing + turn) % 4
    if new_facing == 0:  #up
        delta_y = 1
    elif new_facing == 1:  #right
        delta_x = 1
    elif new_facing == 2:  #down
        delta_y = -1
    elif new_facing == 3:  #left
        delta_x = -1

    return (new_facing, delta_x, delta_y)

grid = {}
pos_x = 0
pos_y = 0
facing = 0
ret_code = -1


while ret_code != 0:
    cur_color = get_color(pos_x, pos_y)
    ret_code = intcode.resume([cur_color])
    if intcode.output[-2] != cur_color:
        grid[(pos_x, pos_y)] = intcode.output[-2]
    
    turn = intcode.output[-1]
    move_data = move(facing, turn)
    facing = move_data[0]
    pos_x += move_data[1]
    pos_y += move_data[2]




# print(len(grid))

min_x = min([i[0] for i in grid])
max_x = max([i[0] for i in grid])
min_y = min([i[1] for i in grid])
max_y = max([i[1] for i in grid])

# print(f"x: [{min_x} ,{max_x}], y: [{min_y}, {max_y}]")
# print(f"{max_x - min_x}x{max_y - min_y}")

painting = []

for y in range(0,max_y - min_y + 10):
    painting.append([1 for x in range(0,max_x - min_x + 10)])

for cell in grid:
    painting[cell[1] + 10][cell[0] + 4] = grid[cell]

painting.reverse()
for line in painting:
    print(*['#' if c == 1 else ' ' for c in line])