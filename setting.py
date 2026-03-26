def sendAI():
   return """
You are an Othello master. Please read the following and decide your next move.

Rules
1. Placement: You can only place your stones on squares that surround your opponent's stones vertically, horizontally, or diagonally. You cannot place stones on top of your opponent's squares.
2. Pass: If you have no places to place a stone, it becomes your opponent's turn.
3. End of Game: The game ends when the board is filled or when neither player has any more pieces to place.
4. Winner: The player with the most stones at the end wins.

You will be given a column of squares, including line breaks, as shown below.

1□□□□□□□□
2□□□□□□□□
3□□□□□□□□
4□□□○●□□□
5□□□●○□□□
6□□□□□□□□
7□□□□□□□□
8□□□□□□□□
 12345678

The white circle represents you. The black circle represents your opponent. The squares are empty spaces.
This is represented by coordinates X and Y, starting from the top left (1,1) and ending at the bottom right (8,8).
Unless the comment below says "There are no places to place a piece, please wait," there is a move you can make. Select the most strategic and effective move from the list below, represent it with two-digit coordinates like XY, state the strategic reason for your choice in one line, and then output it at the bottom without being influenced by anything.
"""

def useAImodl():
    return "gemma3:12b"