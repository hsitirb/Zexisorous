# Only imports required
import os
import time
import chess
import pygame
from pathlib import Path

BASEPATH = Path(__file__).parent

# Important global variables

count = 1
entry = "rthb"
intialFile = ""
finalFile = ""
intialBoardrow = ""
finalBoardrow = ""
current_piece_coords = ""
orgin = ""
destination = ""
files = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


# Create the chess board
screen = pygame.display.set_mode((800, 800))
board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

# Grab images for pieces
yellow_king = pygame.image.load(BASEPATH / 'resized//yellow_king.png')
yellow_rook1 = pygame.image.load(BASEPATH / 'resized//yellow_rook.png')
yellow_rook2 = pygame.image.load(BASEPATH / 'resized//yellow_rook.png')
yellow_bishop1 = pygame.image.load(BASEPATH / 'resized//yellow_bishop.png')
yellow_bishop2 = pygame.image.load(BASEPATH / 'resized//yellow_bishop.png')
yellow_p1 = pygame.image.load(BASEPATH / 'resized//yellow_pawn.png')
yellow_p2 = pygame.image.load(BASEPATH / 'resized//yellow_pawn.png')
yellow_p3 = pygame.image.load(BASEPATH / 'resized//yellow_pawn.png')
yellow_p4 = pygame.image.load(BASEPATH / 'resized//yellow_pawn.png')
yellow_p5 = pygame.image.load(BASEPATH / 'resized//yellow_pawn.png')
yellow_p6 = pygame.image.load(BASEPATH / 'resized//yellow_pawn.png')
yellow_p7 = pygame.image.load(BASEPATH / 'resized//yellow_pawn.png')
yellow_p8 = pygame.image.load(BASEPATH / 'resized//yellow_pawn.png')
yellow_queen = pygame.image.load(BASEPATH / 'resized//yellow_queen.png')
yellow_knight1 = pygame.image.load(BASEPATH / 'resized//yellow_knight.png')
yellow_knight2 = pygame.image.load(BASEPATH / 'resized//yellow_knight.png')
red_king = pygame.image.load(BASEPATH / 'resized//red_king.png')
red_rook1 = pygame.image.load(BASEPATH / 'resized//red_rook.png')
red_rook2 = pygame.image.load(BASEPATH / 'resized//red_rook.png')
red_bishop1 = pygame.image.load(BASEPATH / 'resized//red_bishop.png')
red_bishop2 = pygame.image.load(BASEPATH / 'resized//red_bishop.png')
red_p1 = pygame.image.load(BASEPATH / 'resized//red_pawn.png')
red_p2 = pygame.image.load(BASEPATH / 'resized//red_pawn.png')
red_p3 = pygame.image.load(BASEPATH / 'resized//red_pawn.png')
red_p4 = pygame.image.load(BASEPATH / 'resized//red_pawn.png')
red_p5 = pygame.image.load(BASEPATH / 'resized//red_pawn.png')
red_p6 = pygame.image.load(BASEPATH / 'resized//red_pawn.png')
red_p7 = pygame.image.load(BASEPATH / 'resized//red_pawn.png')
red_p8 = pygame.image.load(BASEPATH / 'resized//red_pawn.png')
red_queen = pygame.image.load(BASEPATH / 'resized//red_queen.png')
red_knight1 = pygame.image.load(BASEPATH / 'resized//red_knight.png')
red_knight2 = pygame.image.load(BASEPATH / 'resized//red_knight.png')

# Squares coords
sq = {
    'a1': (0, 700), 'a2': (0, 600), 'a3': (0, 500), 'a4': (0, 400),
    'a5': (0, 300), 'a6': (0, 200), 'a7': (0, 100), 'a8': (0, 0),
    'b1': (100, 700), 'b2': (100, 600), 'b3': (100, 500), 'b4': (100, 400),
    'b5': (100, 300), 'b6': (100, 200), 'b7': (100, 100), 'b8': (100, 0),
    'c1': (200, 700), 'c2': (200, 600), 'c3': (200, 500), 'c4': (200, 400),
    'c5': (200, 300), 'c6': (200, 200), 'c7': (200, 100), 'c8': (200, 0),
    'd1': (300, 700), 'd2': (300, 600), 'd3': (300, 500), 'd4': (300, 400),
    'd5': (300, 300), 'd6': (300, 200), 'd7': (300, 100), 'd8': (300, 0),
    'e1': (400, 700), 'e2': (400, 600), 'e3': (400, 500), 'e4': (400, 400),
    'e5': (400, 300), 'e6': (400, 200), 'e7': (400, 100), 'e8': (400, 0),
    'f1': (500, 700), 'f2': (500, 600), 'f3': (500, 500), 'f4': (500, 400),
    'f5': (500, 300), 'f6': (500, 200), 'f7': (500, 100), 'f8': (500, 0),
    'g1': (600, 700), 'g2': (600, 600), 'g3': (600, 500), 'g4': (600, 400),
    'g5': (600, 300), 'g6': (600, 200), 'g7': (600, 100), 'g8': (600, 0),
    'h1': (700, 700), 'h2': (700, 600), 'h3': (700, 500), 'h4': (700, 400),
    'h5': (700, 300), 'h6': (700, 200), 'h7': (700, 100), 'h8': (700, 0),
}

# Piece positions
yellow_king_coords = sq['e1']
yellow_knight1_coords = sq['b1']
yellow_knight2_coords = sq['g1']
yellow_rook1_coords = sq['a1']
yellow_rook2_coords = sq['h1']
yellow_bishop1_coords = sq['c1']
yellow_bishop2_coords = sq['f1']
yellow_queen_coords = sq['d1']
yellow_p1_coords = sq['a2']
yellow_p2_coords = sq['b2']
yellow_p3_coords = sq['c2']
yellow_p4_coords = sq['d2']
yellow_p5_coords = sq['e2']
yellow_p6_coords = sq['f2']
yellow_p7_coords = sq['g2']
yellow_p8_coords = sq['h2']
red_king_coords = sq['e8']
red_knight1_coords = sq['b8']
red_knight2_coords = sq['g8']
red_rook1_coords = sq['a8']
red_rook2_coords = sq['h8']
red_bishop1_coords = sq['c8']
red_bishop2_coords = sq['f8']
red_queen_coords = sq['d8']
red_p1_coords = sq['a7']
red_p2_coords = sq['b7']
red_p3_coords = sq['c7']
red_p4_coords = sq['d7']
red_p5_coords = sq['e7']
red_p6_coords = sq['f7']
red_p7_coords = sq['g7']
red_p8_coords = sq['h7']


# Update GUI
def yellow_move_piece():
    global yellow_king_coords
    global yellow_queen_coords
    global yellow_bishop1_coords
    global yellow_bishop2_coords
    global yellow_p1_coords
    global yellow_p2_coords
    global yellow_p3_coords
    global yellow_p4_coords
    global yellow_p5_coords
    global yellow_p6_coords
    global yellow_p7_coords
    global yellow_p8_coords
    global yellow_rook1_coords
    global yellow_rook2_coords
    global yellow_knight1_coords
    global yellow_knight2_coords
    location = entry[-2:]
    piece = entry[0]
    piece_location = (entry[1] + entry[2])
    charafterpiece = entry[1]
    if piece == "Q" or piece == "q":
        if str(yellow_queen_coords) == str(sq[piece_location]):
            yellow_queen_coords = sq[location]
    if piece == "K" or piece == "k":
        if str(yellow_king_coords) == str(sq[piece_location]):
            yellow_queen_coords = sq[location]
    if piece == "B" or piece == "b":
        if charafterpiece == "b" or charafterpiece == "B":
            if str(yellow_bishop1_coords) == str(sq[piece_location]):
                yellow_bishop1_coords = sq[location]
            if str(yellow_bishop2_coords) == str(sq[piece_location]):
                yellow_bishop2_coords = sq[location]
        else:
            piece_location = entry[0] + entry[1]
            if str(yellow_p1_coords) == str(sq[piece_location]):
                yellow_p1_coords = sq[location]
            if str(yellow_p2_coords) == str(sq[piece_location]):
                yellow_p2_coords = sq[location]
            if str(yellow_p3_coords) == str(sq[piece_location]):
                yellow_p3_coords = sq[location]
            if str(yellow_p4_coords) == str(sq[piece_location]):
                yellow_p4_coords = sq[location]
            if str(yellow_p5_coords) == str(sq[piece_location]):
                yellow_p5_coords = sq[location]
            if str(yellow_p6_coords) == str(sq[piece_location]):
                yellow_p6_coords = sq[location]
            if str(yellow_p7_coords) == str(sq[piece_location]):
                yellow_p7_coords = sq[location]
            if str(yellow_p8_coords) == str(sq[piece_location]):
                yellow_p8_coords = sq[location]
    if piece == "R" or piece == "r":
        if str(yellow_rook1_coords) == str(sq[piece_location]):
            yellow_rook1_coords = sq[location]
        if str(yellow_rook2_coords) == str(sq[piece_location]):
            yellow_rook2_coords = sq[location]
    if piece == "N" or piece == "n":
        if str(yellow_knight1_coords) == str(sq[piece_location]):
            yellow_knight1_coords = sq[location]
        if str(yellow_knight2_coords) == str(sq[piece_location]):
            yellow_knight2_coords = sq[location]
    else:
        piece_location = entry[0] + entry[1]
        if str(yellow_p1_coords) == str(sq[piece_location]):
            yellow_p1_coords = sq[location]
        if str(yellow_p2_coords) == str(sq[piece_location]):
            yellow_p2_coords = sq[location]
        if str(yellow_p3_coords) == str(sq[piece_location]):
            yellow_p3_coords = sq[location]
        if str(yellow_p4_coords) == str(sq[piece_location]):
            yellow_p4_coords = sq[location]
        if str(yellow_p5_coords) == str(sq[piece_location]):
            yellow_p5_coords = sq[location]
        if str(yellow_p6_coords) == str(sq[piece_location]):
            yellow_p6_coords = sq[location]
        if str(yellow_p7_coords) == str(sq[piece_location]):
            yellow_p7_coords = sq[location]
        if str(yellow_p8_coords) == str(sq[piece_location]):
            yellow_p8_coords = sq[location]


def red_move_piece():
    global red_king_coords
    global red_queen_coords
    global red_bishop1_coords
    global red_bishop2_coords
    global red_p1_coords
    global red_p2_coords
    global red_p3_coords
    global red_p4_coords
    global red_p5_coords
    global red_p6_coords
    global red_p7_coords
    global red_p8_coords
    global red_rook1_coords
    global red_rook2_coords
    global red_knight1_coords
    global red_knight2_coords
    location = entry[-2:]
    piece = entry[0]
    piece_location = (entry[1] + entry[2])
    charafterpiece = entry[1]
    if piece == "Q" or piece == "q":
        if str(red_queen_coords) == str(sq[piece_location]):
            red_queen_coords = sq[location]
    if piece == "K" or piece == "k":
        if str(red_king_coords) == str(sq[piece_location]):
            red_queen_coords = sq[location]
    if piece == "B" or piece == "b":
        if charafterpiece == "b" or charafterpiece == "B":
            if str(red_bishop1_coords) == str(sq[piece_location]):
                red_bishop1_coords = sq[location]
            if str(red_bishop2_coords) == str(sq[piece_location]):
                red_bishop2_coords = sq[location]
        else:
            piece_location = entry[0] + entry[1]
            if str(red_p1_coords) == str(sq[piece_location]):
                red_p1_coords = sq[location]
            if str(red_p2_coords) == str(sq[piece_location]):
                red_p2_coords = sq[location]
            if str(red_p3_coords) == str(sq[piece_location]):
                red_p3_coords = sq[location]
            if str(red_p4_coords) == str(sq[piece_location]):
                red_p4_coords = sq[location]
            if str(red_p5_coords) == str(sq[piece_location]):
                red_p5_coords = sq[location]
            if str(red_p6_coords) == str(sq[piece_location]):
                red_p6_coords = sq[location]
            if str(red_p7_coords) == str(sq[piece_location]):
                red_p7_coords = sq[location]
            if str(red_p8_coords) == str(sq[piece_location]):
                red_p8_coords = sq[location]
    if piece == "R" or piece == "r":
        if str(red_rook1_coords) == str(sq[piece_location]):
            red_rook1_coords = sq[location]
        if str(red_rook2_coords) == str(sq[piece_location]):
            red_rook2_coords = sq[location]
    if piece == "N" or piece == "n":
        if str(red_knight1_coords) == str(sq[piece_location]):
            red_knight1_coords = sq[location]
        if str(red_knight2_coords) == str(sq[piece_location]):
            red_knight2_coords = sq[location]
    else:
        piece_location = entry[0] + entry[1]
        if str(red_p1_coords) == str(sq[piece_location]):
            red_p1_coords = sq[location]
        if str(red_p2_coords) == str(sq[piece_location]):
            red_p2_coords = sq[location]
        if str(red_p3_coords) == str(sq[piece_location]):
            red_p3_coords = sq[location]
        if str(red_p4_coords) == str(sq[piece_location]):
            red_p4_coords = sq[location]
        if str(red_p5_coords) == str(sq[piece_location]):
            red_p5_coords = sq[location]
        if str(red_p6_coords) == str(sq[piece_location]):
            red_p6_coords = sq[location]
        if str(red_p7_coords) == str(sq[piece_location]):
            red_p7_coords = sq[location]
        if str(red_p8_coords) == str(sq[piece_location]):
            red_p8_coords = sq[location]


# Make clear function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Screen touch input
def translate_mousepos_to_filerow(mouse_position):
    if mouse_position[0] <= 100:
        intialFile = "a"
    if 200 >= mouse_position[0] > 100:
        intialFile = "b"
    if 300 >= mouse_position[0] > 200:
        intialFile = "c"
    if 400 >= mouse_position[0] > 300:
        intialFile = "d"
    if 500 >= mouse_position[0] > 400:
        intialFile = "e"
    if 600 >= mouse_position[0] > 500:
        intialFile = "f"
    if 700 >= mouse_position[0] > 600:
        intialFile = "g"
    if 800 >= mouse_position[0] > 700:
        intialFile = "h"
    if mouse_position[1] <= 100:
        intialBoardrow = "8"
    if 200 >= mouse_position[1] > 100:
        intialBoardrow = "7"
    if 300 >= mouse_position[1] > 200:
        intialBoardrow = "6"
    if 400 >= mouse_position[1] > 300:
        intialBoardrow = "5"
    if 500 >= mouse_position[1] > 400:
        intialBoardrow = "4"
    if 600 >= mouse_position[1] > 500:
        intialBoardrow = "3"
    if 700 >= mouse_position[1] > 600:
        intialBoardrow = "2"
    if 800 >= mouse_position[1] > 700:
        intialBoardrow = "1"
    return intialFile, intialBoardrow


def screeninput():
    global intialFile
    global intialBoardrow
    global finalFile
    global finalBoardrow
    global orgin
    global destination
    orgin = ""
    destination = ""

    while True:
        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT:
                pass
            if event1.type == pygame.MOUSEBUTTONDOWN:
                if event1.button == 1:
                    mouse_position = event1.pos
                    print(mouse_position)

                    intialFile, intialBoardrow = translate_mousepos_to_filerow(mouse_position)
                    orgin = intialFile + intialBoardrow

                    print("orgin:"+orgin)
        if len(orgin) != 0:
            break
    while True:
        for event1 in pygame.event.get():
            if event1.type == pygame.MOUSEBUTTONDOWN:
                if event1.button == 1:
                    mouse_position = event1.pos
                    print(mouse_position)
                    finalFile, finalBoardrow = translate_mousepos_to_filerow(mouse_position)
                    destination = finalFile + finalBoardrow
                    print("Destination:"+destination)
        if len(str(orgin+"-"+destination)) == 6 or len(str(orgin+"-"+destination)) == 5:
            break
    global current_piece_coords
    current_piece_coords = intialFile+intialBoardrow
    if yellow_king_coords == sq[current_piece_coords]:
        orgin = "K" + current_piece_coords
    if yellow_queen_coords == sq[current_piece_coords]:
        orgin = "Q" + current_piece_coords
    if yellow_knight1_coords == sq[current_piece_coords] \
            or yellow_knight2_coords == sq[current_piece_coords]:
        orgin = "N" + current_piece_coords
    if yellow_bishop1_coords == sq[current_piece_coords] \
            or yellow_bishop2_coords == sq[current_piece_coords]:
        orgin = "B" + current_piece_coords
    if yellow_rook1_coords == sq[current_piece_coords] \
            or yellow_rook2_coords == sq[current_piece_coords]:
        orgin = "R" + current_piece_coords
    if yellow_p1_coords == sq[current_piece_coords] \
            or yellow_p2_coords == sq[current_piece_coords] \
            or yellow_p3_coords == sq[current_piece_coords] \
            or yellow_p4_coords == sq[current_piece_coords] \
            or yellow_p5_coords == sq[current_piece_coords] \
            or yellow_p6_coords == sq[current_piece_coords] \
            or yellow_p7_coords == sq[current_piece_coords] \
            or yellow_p8_coords == sq[current_piece_coords]:
        orgin = "" + current_piece_coords
    if red_king_coords == sq[current_piece_coords]:
        orgin = "K" + current_piece_coords
    if red_queen_coords == sq[current_piece_coords]:
        orgin = "Q" + current_piece_coords
    if red_knight1_coords == sq[current_piece_coords] \
            or red_knight2_coords == sq[current_piece_coords]:
        orgin = "N" + current_piece_coords
    if red_bishop1_coords == sq[current_piece_coords] \
            or red_bishop2_coords == sq[current_piece_coords]:
        orgin = "B" + current_piece_coords
    if red_rook1_coords == sq[current_piece_coords] \
            or red_rook2_coords == sq[current_piece_coords]:
        orgin = "R" + current_piece_coords
    if red_p1_coords == sq[current_piece_coords] \
            or red_p2_coords == sq[current_piece_coords] \
            or red_p3_coords == sq[current_piece_coords] \
            or red_p4_coords == sq[current_piece_coords] \
            or red_p5_coords == sq[current_piece_coords] \
            or red_p6_coords == sq[current_piece_coords] \
            or red_p7_coords == sq[current_piece_coords] \
            or red_p8_coords == sq[current_piece_coords]:
        orgin = current_piece_coords


# Making valid moves
def gamemove():
    if board.is_game_over():
        print("Game Over")
    else:
        clear()
        global entry
        legal_moves = [board.san(move) for move in board.legal_moves]
        if len(legal_moves) == 0:
            if board.is_checkmate():
                print('Mate!')
            elif board.is_stalemate():
                if board.has_insufficient_material(board.turn):
                    print('Draw: Insufficient material')
                else:
                    print('Stalemate!')
        else:
            legal_moves = [board.san(move) for move in board.legal_moves]
            if board.is_check():
                king_square = board.king(board.turn)
                legal_moves = [move for move in legal_moves if str(king_square) in move]
            if board.has_castling_rights(board.turn):
                if board.has_kingside_castling_rights(board.turn):
                    legal_moves.append('O-O')
                if board.has_queenside_castling_rights(board.turn):
                    legal_moves.append('O-O-O')
            print(board)
            screeninput()
            if orgin[0] == 'K' and orgin[1] == files[4] and destination[0] == files[4+2]:
                entry = 'O-O'
            if orgin[0] == 'K' and orgin[1] == files[4] and destination[0] == files[4-2]:
                entry = 'O-O-O'
            else:
                entry = str(orgin + "-" + destination)
            try:
                move = chess.Move.from_uci(entry)
                if move in board.legal_moves:
                    board.push(move)
                else:
                    print('Illegal move')
                    time.sleep(2)
                    return gamemove()
            except ValueError:
                try:
                    board.push_san(entry)
                except ValueError:
                    print('Illegal move')
                    time.sleep(2)
                    return gamemove()
        if board.is_checkmate():
            print('Mate!')
        elif board.is_stalemate():
            print('Stalemate!')
        elif board.has_insufficient_material(board.turn):
            print('Draw: Insufficient material')


if __name__ == "__main__":
    # Board GUI
    pygame.init()
    light_brown = (240, 217, 181)
    brown = (181, 136, 99)
    clock = pygame.time.Clock()
    rects = []
    for y in range(8):
        for x in range(8):
            rect = pygame.Rect(x * 100, y * 100, 100, 100)
            rects.append(rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, light_brown, rects[0])
        pygame.draw.rect(screen, brown, rects[1])
        pygame.draw.rect(screen, light_brown, rects[2])
        pygame.draw.rect(screen, brown, rects[3])
        pygame.draw.rect(screen, light_brown, rects[4])
        pygame.draw.rect(screen, brown, rects[5])
        pygame.draw.rect(screen, light_brown, rects[6])
        pygame.draw.rect(screen, brown, rects[7])
        pygame.draw.rect(screen, brown, rects[8])
        pygame.draw.rect(screen, light_brown, rects[9])
        pygame.draw.rect(screen, brown, rects[10])
        pygame.draw.rect(screen, light_brown, rects[11])
        pygame.draw.rect(screen, brown, rects[12])
        pygame.draw.rect(screen, light_brown, rects[13])
        pygame.draw.rect(screen, brown, rects[14])
        pygame.draw.rect(screen, light_brown, rects[15])
        pygame.draw.rect(screen, light_brown, rects[16])
        pygame.draw.rect(screen, brown, rects[17])
        pygame.draw.rect(screen, light_brown, rects[18])
        pygame.draw.rect(screen, brown, rects[19])
        pygame.draw.rect(screen, light_brown, rects[20])
        pygame.draw.rect(screen, brown, rects[21])
        pygame.draw.rect(screen, light_brown, rects[22])
        pygame.draw.rect(screen, brown, rects[23])
        pygame.draw.rect(screen, brown, rects[24])
        pygame.draw.rect(screen, light_brown, rects[25])
        pygame.draw.rect(screen, brown, rects[26])
        pygame.draw.rect(screen, light_brown, rects[27])
        pygame.draw.rect(screen, brown, rects[28])
        pygame.draw.rect(screen, light_brown, rects[29])
        pygame.draw.rect(screen, brown, rects[30])
        pygame.draw.rect(screen, light_brown, rects[31])
        pygame.draw.rect(screen, light_brown, rects[32])
        pygame.draw.rect(screen, brown, rects[33])
        pygame.draw.rect(screen, light_brown, rects[34])
        pygame.draw.rect(screen, brown, rects[35])
        pygame.draw.rect(screen, light_brown, rects[36])
        pygame.draw.rect(screen, brown, rects[37])
        pygame.draw.rect(screen, light_brown, rects[38])
        pygame.draw.rect(screen, brown, rects[39])
        pygame.draw.rect(screen, brown, rects[40])
        pygame.draw.rect(screen, light_brown, rects[41])
        pygame.draw.rect(screen, brown, rects[42])
        pygame.draw.rect(screen, light_brown, rects[43])
        pygame.draw.rect(screen, brown, rects[44])
        pygame.draw.rect(screen, light_brown, rects[45])
        pygame.draw.rect(screen, brown, rects[46])
        pygame.draw.rect(screen, light_brown, rects[47])
        pygame.draw.rect(screen, light_brown, rects[48])
        pygame.draw.rect(screen, brown, rects[49])
        pygame.draw.rect(screen, light_brown, rects[50])
        pygame.draw.rect(screen, brown, rects[51])
        pygame.draw.rect(screen, light_brown, rects[52])
        pygame.draw.rect(screen, brown, rects[53])
        pygame.draw.rect(screen, light_brown, rects[54])
        pygame.draw.rect(screen, brown, rects[55])
        pygame.draw.rect(screen, brown, rects[56])
        pygame.draw.rect(screen, light_brown, rects[57])
        pygame.draw.rect(screen, brown, rects[58])
        pygame.draw.rect(screen, light_brown, rects[59])
        pygame.draw.rect(screen, brown, rects[60])
        pygame.draw.rect(screen, light_brown, rects[61])
        pygame.draw.rect(screen, brown, rects[62])
        pygame.draw.rect(screen, light_brown, rects[63])
        screen.blit(yellow_king, yellow_king_coords)
        screen.blit(yellow_queen, yellow_queen_coords)
        screen.blit(yellow_knight1, yellow_knight1_coords)
        screen.blit(yellow_knight2, yellow_knight2_coords)
        screen.blit(yellow_bishop1, yellow_bishop1_coords)
        screen.blit(yellow_rook1, yellow_rook1_coords)
        screen.blit(yellow_rook2, yellow_rook2_coords)
        screen.blit(yellow_bishop2, yellow_bishop2_coords)
        screen.blit(red_king, red_king_coords)
        screen.blit(red_queen, red_queen_coords)
        screen.blit(red_knight1, red_knight1_coords)
        screen.blit(red_knight2, red_knight2_coords)
        screen.blit(red_bishop1, red_bishop1_coords)
        screen.blit(red_rook1, red_rook1_coords)
        screen.blit(red_rook2, red_rook2_coords)
        screen.blit(red_bishop2, red_bishop2_coords)
        screen.blit(red_bishop2, red_bishop2_coords)
        screen.blit(red_p1, red_p1_coords)
        screen.blit(red_p2, red_p2_coords)
        screen.blit(red_p3, red_p3_coords)
        screen.blit(red_p4, red_p4_coords)
        screen.blit(red_p5, red_p5_coords)
        screen.blit(red_p6, red_p6_coords)
        screen.blit(red_p7, red_p7_coords)
        screen.blit(red_p8, red_p8_coords)
        screen.blit(yellow_p1, yellow_p1_coords)
        screen.blit(yellow_p2, yellow_p2_coords)
        screen.blit(yellow_p3, yellow_p3_coords)
        screen.blit(yellow_p4, yellow_p4_coords)
        screen.blit(yellow_p5, yellow_p5_coords)
        screen.blit(yellow_p6, yellow_p6_coords)
        screen.blit(yellow_p7, yellow_p7_coords)
        screen.blit(yellow_p8, yellow_p8_coords)
        count += 1
        pygame.display.update()
        gamemove()
        if count % 2 == 0:
            yellow_move_piece()
        else:
            red_move_piece()
        pygame.display.flip()
        clock.tick(60)