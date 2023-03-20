import csv


class Board():
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.board = self.create_2D_board()

    def create_2D_board(self):
        board = []
        # TODO is this encoding proper?
        with open(self.csv_file, 'r', encoding='utf-8-sig') as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                temp = []
                for value in row:
                    if value == "B":
                        temp.append(0)
                    else:
                        temp.append(int(value))
                board.append(temp)
        return board

    def __str__(self):
        return str(self.board)
