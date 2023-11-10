"""
description: the well known TIC TAC TOE game (Marvyn edition)
"""

#dictionary with lists to contain the parameters
ttt_space = {"t": ["_", "_", "_"], "m": ["_", "_", "_"], "b": ["_", "_", "_"]}

spaces = ["t0", "t1", "t2", "m0", "m1", "m2", "b0", "b1", "b2"]
space_index = ["positions; ", "t1  t2  t3", "m1  m2  m3", "b1  b2  b3"]

def print_space_index():
    for i in space_index:
        print(f"\t{i}")


#prints dictionary (after every insertion)
def disp_status(space):
    for k, v in space.items():
     print(f"\t{v[0]}\t{v[1]}\t{v[2]}")


#prompts insertion of "O" in dictioary
def prompt_X_input():
    while True:
        Xpos = input("select position for X: \n")
        try:
            Xpos = [Xpos[0], str(int(Xpos[1])-1)]
            Xpos = Xpos[0] + Xpos[1]    
        except Exception:
            print("invalid position, select valid position")
            continue
        
        if Xpos in spaces:
            return ["X", Xpos]
        else:
            print("invalid position, select valid position")
            continue


#prompts for insertion of X in dictionary   
def prompt_O_input():
    while True:
        Opos = input("select position for O: \n")
        try:
            Opos = [Opos[0], str(int(Opos[1])-1)]
            Opos = Opos[0] + Opos[1]
        except Exception:
            print("invalid position, select valid position")
            continue
        
        if Opos in spaces:
            return ["O", Opos]
        else:
            print("invalid position, select valid position")
            continue
 
        
#updates the dictionary list with X or O in the selected position
def update_ttt_space(vnp):
    row = vnp[1][0]
    col = int(vnp[1][1])
    val = vnp[0]
    ttt_space[row][col] = val
    

#checks if "piece" has made a line in the play space to confirm win
def check_win(piece):
    #checking column similarity
    if ttt_space["t"][0] == ttt_space["m"][0] == ttt_space["b"][0] == piece:
        return True
    elif ttt_space["t"][1] == ttt_space["m"][1] == ttt_space["b"][1] == piece:
        return True
    elif ttt_space["t"][2] == ttt_space["m"][2] == ttt_space["b"][2] == piece:
        return True
    #checking row similarity
    elif ttt_space["t"][0] == ttt_space["t"][1] == ttt_space["t"][2] == piece:
        return True
    elif ttt_space["m"][0] == ttt_space["m"][1] == ttt_space["m"][2] == piece:
        return True
    elif ttt_space["b"][0] == ttt_space["b"][1] == ttt_space["b"][2] == piece:
        return True
    #checking diagonal similarity
    elif ttt_space["t"][0] == ttt_space["m"][1] == ttt_space["b"][2] == piece:
        return True
    elif ttt_space["t"][2] == ttt_space["m"][1] == ttt_space["b"][0] == piece:
        return True
    else:
        return False
    
#main function
def main():
    num = 0
    already_taken = []
    print_space_index()
    
    while True:
        #prompting input for X
        px = prompt_X_input()
        if px[1] in already_taken:
            print("select an empty position")
            continue
        else:
            #updating space position with X
            already_taken.append(px[1])
            update_ttt_space(px)
            num += 1
            disp_status(ttt_space)
        
        #checking if line has been made    
        if check_win(px[0]):
            print("X Wins!!")
            break
        
        if num == 9:
            print("Its a Draw!!!")
            break
        
        #prompting input for O    
        while True:
            po = prompt_O_input()
            if po[1] in already_taken:
                print("select an empty position")
                continue
            else:
                already_taken.append(po[1])
                update_ttt_space(po)
                num +=1
                disp_status(ttt_space)
                break
        if check_win(po[0]):
            print("O Wins!!")
            break

main()
input("PRESS ENTER TO EXIT")