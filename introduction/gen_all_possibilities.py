#generate all possibilities for a tic-tac-toe game
n=3
cnt={'X':0,'O':0,'D':0}
def any_winner(table):
    for c in ['X','O']:
        moves_X=table[c]
        for (x,y) in moves_X:
            if ((x-1,y) in moves_X) and ((x+1,y) in moves_X):
                return c
            if ((x,y-1) in moves_X ) and ((x,y+1) in moves_X):
                return c
            if ((x-1,y-1) in moves_X) and  ((x+1,y+1) in moves_X):
                return c
    return '#'
def print_possibility(dc):
    moves_X=dc['X']
    moves_O=dc['O']
    for i in range(n):
        for j in range(n):
            if (i,j) in moves_X:
                print("X",end=' ')
            elif (i,j) in moves_O:
                print("O",end=' ')
            else:
                print("#",end=' ')
        print()
    if any_winner(dc)!='#':
        print("the winner is "+any_winner(dc))
        cnt[any_winner(dc)]+=1
    else:
        cnt['D']+=1
        print("It's a draw !")
def check(table):
    m=len(table['X'])+len(table['O'])
    move1=(m)//2
    move2= m - move1
    return (len(table['X'])==move1 and len(table['O'])==move2) or (len(table['O'])==move1 and len(table['X'])==move2)
def generate():
    moves=[]
    for i in range(n):
        for j in range(n):
            moves.append((i,j))
    m=len(moves)
    for mask in range((1<<m)):
        table={'X':[],'O':[]}
        for bit in range(9):
            if any_winner(table)!='#':
                break
            if mask&(1<<bit):
                table['X'].append(moves[bit])
            else:
                table['O'].append(moves[bit])
        if check(table):
            print_possibility(table)
generate()
print("Obvious statistics for nerds :")
print("X wins "+str(cnt['X'])+" times")
print("O wins "+str(cnt['O'])+" times")
print("Draw "+str(cnt['D'])+" times")
