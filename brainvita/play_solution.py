import os
import time
import pandas as pd

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

solution_csv = 'solution.csv'
df = pd.read_csv(solution_csv)

INITIAL_MATRIX = [
            [3,3,1,1,1,3,3],
            [3,3,1,1,1,3,3],
            [1,1,1,1,1,1,1],
            [1,1,1,0,1,1,1],
            [1,1,1,1,1,1,1],
            [3,3,1,1,1,3,3],
            [3,3,1,1,1,3,3]]
mat = INITIAL_MATRIX

for i,row in df.iterrows():
    display_matrix(mat)
    time.sleep(2)
    mat = modify_matrix(row['x'],row['y'],row['move'],mat)
display_matrix(mat)
