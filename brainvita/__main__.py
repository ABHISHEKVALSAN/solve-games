import os
import time
import sys

MATRIX_LENGTH = 7
FINAL_MATRIX = [
            [3,3,0,0,0,3,3],
            [3,3,0,0,0,3,3],
            [0,0,0,0,0,0,0],
            [0,0,0,1,0,0,0],
            [0,0,0,0,0,0,0],
            [3,3,0,0,0,3,3],
            [3,3,0,0,0,3,3]]
INITIAL_MATRIX = [
            [3,3,1,1,1,3,3],
            [3,3,1,1,1,3,3],
            [1,1,1,1,1,1,1],
            [1,1,1,0,1,1,1],
            [1,1,1,1,1,1,1],
            [3,3,1,1,1,3,3],
            [3,3,1,1,1,3,3]]
INVALID_POS = [(0,0),(0,1),
               (0,5),(0,6),
               (1,0),(1,1),
               (1,5),(1,6),
               (5,0),(5,1),
               (5,5),(5,6),
               (6,0),(6,1),
               (6,5),(6,6)]
CORRECT_MOVES = []
moves = ['right','left','down','up']

def is_valid_pos(x,y):
    if x<0 or y<0:
        return False
    if x>=MATRIX_LENGTH or y>=MATRIX_LENGTH:
        return False
    if (x,y) in INVALID_POS:
        return False
    return True

def display_matrix(mat):
    os.system('clear')
    for row in mat:
        for ele in row:
            if ele==3:
                print('#',end=' ')
            elif ele==1:
                print('@',end=' ')
            elif ele==0:
                print('•',end=' ')
        print('')

def modify_matrix(x,y,mov,mat):
    if mov == 'right':
        mat[x][y]=0
        mat[x][y+1]=0
        mat[x][y+2]=1
        return mat
    elif mov == 'down':
        mat[x][y]=0
        mat[x+1][y]=0
        mat[x+2][y]=1
        return mat
    elif mov=='left':
        mat[x][y]=0
        mat[x][y-1]=0
        mat[x][y-2]=1
        return mat
    elif mov=='up':
        mat[x][y]=0
        mat[x-1][y]=0
        mat[x-2][y]=1
        return mat
    else:
        print(mat)
        print(x,y,mov)
        print('Unknown Error')
        raise

def can_modify_matrix(x,y,mov,mat):
    if len(mat)!=len(mat[0]) or len(mat)!=MATRIX_LENGTH:
        #print('INVALID_LENGTH')
        return False
    if (x,y) in INVALID_POS:
        #print('INVALID_POS')
        return False
    if mov not in moves:
        #print('INVALID_MOVETYPE')
        return False
    if mat[x][y]!=1:
        #print('INVALID_VALUE')
        return False
    if mov == 'right':
        if not is_valid_pos(x,y+2):
            #print('INVALID_POS2r')
            return False
        if not is_valid_pos(x,y+1):
            #print('INVALID_POS1r')
            return False
        if mat[x][y]==1 and mat[x][y+1]==1 and mat[x][y+2]==0:
            return True
        else:
            #print('INVALID_MOVE')
            return False
    elif mov == 'down':
        if not is_valid_pos(x+2,y):
            #print('INVALID_POS2d')
            return False
        if not is_valid_pos(x+1,y):
            #print('INVALID_POS1d')
            return False
        if mat[x][y]==1 and mat[x+1][y]==1 and mat[x+2][y]==0:
            return True
        else:
            #print('INVALID_MOVE')
            return False
    elif mov=='left':
        if not is_valid_pos(x,y-1):
            #print('INVALID_POS1l')
            return False
        if not is_valid_pos(x,y-2):
            #print('INVALID_POS2l')
            return False
        if mat[x][y]==1 and mat[x][y-1]==1 and mat[x][y-2]==0:
            return True
        else:
            #print('INVALID_MOVE')
            return False
    elif mov=='up':
        if not is_valid_pos(x-1,y):
            #print('INVALID_POS1u')
            return False
        if not is_valid_pos(x-2,y):
            #print('INVALID_POS2u')
            return False
        if mat[x][y]==1 and mat[x-1][y]==1 and mat[x-2][y]==0:
            return True
        else:
            #print('INVALID_MOVE')
            return False
    else:
        print(mat)
        print(x,y,mov)
        print('Unknown Error')
        raise

def inverse_modify(x,y,mov,mat):
    if mov == 'right':
        mat[x][y]=1
        mat[x][y+1]=1
        mat[x][y+2]=0
        return mat
    elif mov == 'down':
        mat[x][y]=1
        mat[x+1][y]=1
        mat[x+2][y]=0
        return mat
    elif mov=='left':
        mat[x][y]=1
        mat[x][y-1]=1
        mat[x][y-2]=0
        return mat
    elif mov=='up':
        mat[x][y]=1
        mat[x-1][y]=1
        mat[x-2][y]=0
        return mat

def can_inverse_modify(x,y,mov,mat):
    if len(mat)!=len(mat[0]) or len(mat)==MATRIX_LENGTH:
        return False
    if (x,y) in INVALID_POS:
        return False
    if mov not in moves:
        return False
    if mat[x][y]!=0:
        return False
    if mov == 'right':
        if not is_valid_pos(x,y+2):
            return False
        if not is_valid_pos(x,y+1):
            return False
        if mat[x][y]==0 and mat[x][y+1]==0 and mat[x][y+2]==1:
            return True
        else:
            return False
    elif mov == 'down':
        if not is_valid_pos(x+2,y):
            return False
        if not is_valid_pos(x+1,y):
            return False
        if mat[x][y]==0 and mat[x+1][y]==0 and mat[x+2][y]==1:
            return True
        else:
            return False
    elif mov=='left':
        if not is_valid_pos(x,y-1):
            return False
        if not is_valid_pos(x,y-2):
            return False
        if mat[x][y]==0 and mat[x][y-1]==0 and mat[x][y-2]==1:
            return True
        else:
            return False
    elif mov=='up':
        if not is_valid_pos(x-1,y):
            return False
        if not is_valid_pos(x-2,y):
            return False
        if mat[x][y]==0 and mat[x-1][y]==0 and mat[x-2][y]==1:
            return True
        else:
            return False

def is_same_matrix(mat1, mat2):
    for i in range(MATRIX_LENGTH):
        for j in range(MATRIX_LENGTH):
            if mat1[i][j]!=mat2[i][j]:
                return False
    return True

def is_game_solved(mat):
    matrix_sum=0
    for row in mat:
        matrix_sum+=sum(row)
    if matrix_sum==49:
        return True
    return False

def next_step(mat):
    global CORRECT_MOVES
    if is_same_matrix(mat, FINAL_MATRIX):
        print('Solved!!!')
        print(CORRECT_MOVES)
        sys.exit(0)
    # display_matrix(mat)
    # time.sleep(2)
    i=0
    while i<MATRIX_LENGTH:
        j=0
        while j<MATRIX_LENGTH:
            for mov in moves:
                if can_modify_matrix(i,j,mov,mat):
                    CORRECT_MOVES.append([i,j,mov])
                    mat = modify_matrix(i,j,mov,mat)
                    next_step(mat)
                    mat = inverse_modify(i,j,mov,mat)
                    CORRECT_MOVES.pop()
            j+=1
        i+=1

# display_matrix(INITIAL_MATRIX)
# print(can_modify_matrix(3,1,'right',INITIAL_MATRIX))
next_step(INITIAL_MATRIX)
print('GAME IS NOT SOLVED!!!')
