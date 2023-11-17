def create_bingo_board(size):
    line = [0] * size
    return [line.copy() for _ in range(size)]

def input_bingo_data(size):
    board = create_bingo_board(size)
    for i in range(size):
        row = input() # (i + 1) 行目をスペース区切りで入力
        board[i] = row.split()
    return board

def input_selected_words():
    number_of_selected_words = int(input())
    return [input() for _ in range(number_of_selected_words)]

def is_bingo(board, selected_words):
    # 横の判定
    if any(all(word in selected_words for word in row) for row in board):
        return True

    # 縦の判定
    if any(all(word in selected_words for word in col) for col in board):
        return True

    # 斜めの判定
    if all(board[i][i] in selected_words for i in range(len(board))) or \
        all(board[i][len(board) - i - 1] in selected_words for i in range(len(board))):
        return True

    return False

def main():
    # サイズの入力
    bingo_size = int(input())

    # ビンゴのデータ入力
    bingo_board = input_bingo_data(bingo_size)

    # 選ばれた単語の入力
    selected_words = input_selected_words()

    # ビンゴの判定
    if is_bingo(bingo_board, selected_words):
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()