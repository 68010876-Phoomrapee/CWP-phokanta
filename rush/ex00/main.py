# ex00/main.py
from checkmate import checkmate
 
 
def main():
    """ลองกระดานหลายแบบ แล้วเรียก checkmate"""
    # ตัวอย่างจากโจทย์ -> Success (Pawn กิน King)
    board = """\
R...
.K..
..P.
....\
"""
    checkmate(board)
 
    # ตัวอย่างจากโจทย์ -> Fail (ไม่มีหมากศัตรู)
    board = """\
..
.K\
"""
    checkmate(board)
 
    # Queen กินแนวทแยง -> Success
    board = """\
Q...
....
....
...K\
"""
    checkmate(board)
 
    # Rook โดน Pawn บังทาง -> Fail
    board = """\
.....
.....
R.P.K
.....
.....\
"""
    checkmate(board)
 
    # Pawn อยู่เหนือ King กินถอยหลังไม่ได้ -> Fail
    board = """\
P..
.K.
...\
"""
    checkmate(board)
 
    # กระดานไม่เป็นจัตุรัส -> Error
    board = """\
...
.K.\
"""
    checkmate(board)
 
    # King สองตัว -> Error
    board = """\
K..
...
..K\
"""
    checkmate(board)
 
 
if __name__ == "__main__":
    main()
 