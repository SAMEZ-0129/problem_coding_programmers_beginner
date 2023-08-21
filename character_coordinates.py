def solution(keyinput, board):
    curr_pos = [0,0]
    x_board = (board[0]-1)//2
    y_board = (board[1]-1)//2
    for i in keyinput:
        if i == 'left' and curr_pos[0] > -x_board: curr_pos[0]-=1
        elif i == 'right' and curr_pos[0] < x_board: curr_pos[0]+=1
        elif i == 'up' and curr_pos[1] < y_board: curr_pos[1]+=1
        elif i == 'down' and curr_pos[1] > -y_board: curr_pos[1]-=1
    return curr_pos

print(solution(["left", "left", "left", "left", "right", "right", "right", "right"],[5,5]))