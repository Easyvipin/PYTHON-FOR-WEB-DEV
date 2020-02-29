#tic tac toe

#This a tic tac toe game
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
nm = theBoard.get('top-L' , '0')
print(nm)

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


 
turn = 'X'


for i in range(9):
    printBoard(theBoard)
    print(f"Turn for  '{ turn }' . Move on which space?'  :   ")
    move=input()
    if move in theBoard :
        theBoard[move] = turn
        if turn == 'X' :
            turn = 'O'
        else :
            turn = 'X'
    else :
        print("print the correct value")

print(theBoard)

if ()


        
        
            
        
    
    
    
