import random

board = [" " for _ in range(9)]

def show_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(player):
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    return any(board[a] == board[b] == board[c] == player for a,b,c in win_conditions)

def is_draw():
    return " " not in board

def player_move():
    while True:
        try:
            move = int(input("เลือกตำแหน่ง (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("ตำแหน่งนี้ถูกใช้แล้ว")
        except:
            print("กรุณาใส่ตัวเลข 1-9")

def bot_move():
    empty = [i for i in range(9) if board[i] == " "]
    move = random.choice(empty)
    board[move] = "O"
    print(f"บอทเลือกตำแหน่ง {move + 1}")

# เกมหลัก
print("=== Tic Tac Toe ===")
print("ตำแหน่ง:")
print("1 | 2 | 3")
print("4 | 5 | 6")
print("7 | 8 | 9")

show_board()

while True:
    player_move()
    show_board()
    if check_winner("X"):
        print("คุณชนะ! 🎉")
        break
    if is_draw():
        print("เสมอ!")
        break

    bot_move()
    show_board()
    if check_winner("O"):
        print("บอทชนะ! 🤖")
        break
    if is_draw():
        print("เสมอ!")
        break
