import sys 
try:
    def rearrange_txt_file_name(x): #this func is being used for deleting "" s from input name
        x.replace("\"","")
    absent_sys_files = []  #this list is being used for how many input that given by user
    try:
        player1_txt_file = sys.argv[1]
    except:
        absent_sys_files.append("Player1 ships locations")   #if this input was not given by user then being added to list.
    try:
        player2_txt_file = sys.argv[2]
    except:
        absent_sys_files.append("Player2 ships locations")
    try:
        player1_in = sys.argv[3]
    except:
        absent_sys_files.append("Player1 shoots")
    try:
        player2_in = sys.argv[4]
    except:
        absent_sys_files.append("Player2 shoots")
    if len(absent_sys_files) != 0:  #if any command has not taken from user then raise ındexerror.
        raise IndexError
    for x in(player1_txt_file,player2_txt_file,player1_in,player2_in): #in here for every input; every \n will be deleted in every input list.
        rearrange_txt_file_name(x)  #for every input
    wrong_input_list = []  #this list is being used for if there is no such that file then being added to list that is wrong file.
    try:
        f = open(player1_txt_file,"r")  #reading input
        player1_ships_locations = f.readlines()
    except:
        wrong_input_list.append(player1_txt_file)
    try:
        f = open(player2_txt_file,"r") #reading input
        player2_ships_locations = f.readlines()
    except:
        wrong_input_list.append(player2_txt_file)
    try:
        f = open(player1_in,"r") #reading input
        player1_moves = f.readlines()
    except:
        wrong_input_list.append(player1_in)
    try:
        f = open(player2_in,"r") #reading input
        player2_moves = f.readlines()
    except:
        wrong_input_list.append(player2_in)
    
    if len(wrong_input_list) !=0:  #if any of them is wrong then raise IOError.
        raise IOError
    
    f = open("OptionalPlayer1.txt","r")    #reading optional input
    OptionalPlayer1 = f.readlines()
    f = open("OptionalPlayer2.txt","r")   #reading optional input
    OptionalPlayer2 = f.readlines()
    for a in (player1_ships_locations,player2_ships_locations,OptionalPlayer1,OptionalPlayer2): #this loop is being used for deleting \n from all inputs and turning to list.
        for b in range(len(a)):
            a[b] = a[b].replace("\n","")
    def adding_empty_board(x): #this func is being used for creating empty list for a row.
        for i in range(10):
            row = ["-","-","-","-","-","-","-","-","-","-"]
            x.append(row)
    
    player1_board , player2_board ,player1_hidden_board,player2_hidden_board= [],[],[],[]  #for player boards 4 list is being created two of them for printing two of them for controlling
    adding_empty_board(player1_board)  #player1_board will be ships locations shower to programmer and end of the game this list is going to be used
    adding_empty_board(player2_board)  #player2_board will be ships locations shower to programmer and end of the game this list is going to be used
    adding_empty_board(player1_hidden_board)  #player1_board will be ships locations shower to user and before end of the game every round this list is going to be used
    adding_empty_board(player2_hidden_board)   #player2_board will be ships locations shower to user and before end of the game every round this list is going to be used
    

    def detecting_ships_locations(x,y):  #this func is being used for detecting ships location and put them into their chechking board.
        for a in range(len(y)):
            temp_ship_locations = y[a].split(";")
            for b in range(len(temp_ship_locations)):
                if temp_ship_locations[b] == "":
                    pass
                else:
                    x[a][b] = temp_ship_locations[b]
    
    detecting_ships_locations(player1_board,player1_ships_locations) #to the player1_board player1 's ships locations will be added to in the list.
    detecting_ships_locations(player2_board,player2_ships_locations)  #to the player2_board player2 's ships locations will be added to in the list. 
    
    players_ships_numbers_for1,players_ships_numbers_for2= dict(),dict()
    
    def detecting_location_by_optional_txt(player,players_ships_numbers): #in this func; two ship type(battleship,patrol boat) have more than one ship thats why we have locate every ships location:
        #thats why this function locate the every pointed ships. 
        for a in range(len(player)): #for a in range len of the optional player
            player[a]= player[a].split(";") #the optional variable row will be splitted by ;
            if player[a][0][0] == "B": #if in this line starts with B
                #ship_type = "B"  
                times_number = 4 # this variable being used for how many ships will be choose for.
            else:
                #ship_type = "P"
                times_number = 2  # this variable being used for how many ships will be choose for.
            ships_first_location = player[a][0].split(":") #this variable will be used for first place of ships.

            if times_number == 2:   #if it is battleship:
                if player[a][1] == "right": #if it goes to the right:
                    players_ships_numbers[ships_first_location[0]] = [[int(ships_first_location[1][:-2]), ord(ships_first_location[1][-1])-64],[int(ships_first_location[1][:-2]), ord(ships_first_location[1][-1])-63]]  
                    #to this dict ships places are going to be added. In later this dict is going to be used for controlling if the ship is sank or not.This dict is going to be executed for 4 statement in the under.
                else:  #if it goes to down
                    players_ships_numbers[ships_first_location[0]] = [[int(ships_first_location[1][:-2])+x, ord(ships_first_location[1][-1])-64] for x in range(2)] 
            else:   #if it is patrol boat:
                if player[a][1] == "right":  #if it goes to the right:
                    players_ships_numbers[ships_first_location[0]] = [[int(ships_first_location[1][:-2]), ord(ships_first_location[1][-1])-64 + x] for x in range(4) ]  
                else:   #if it goes to down
                    players_ships_numbers[ships_first_location[0]] = [[int(ships_first_location[1][:-2])+x, ord(ships_first_location[1][-1])-64] for x in range(4)] 
    
    for_optional_detect = "1"
    detecting_location_by_optional_txt(OptionalPlayer1,players_ships_numbers_for1) #battleship and patrol boat ships locations will be added players_ships_numbers_for1 dict.
    for_optional_detect = "2"
    detecting_location_by_optional_txt(OptionalPlayer2,players_ships_numbers_for2) #battleship and patrol boat ships locations will be added players_ships_numbers_for2 dict.

    player1_moves,player2_moves = player1_moves[0].split(";"),player2_moves[0].split(";") #player moves is going to be added into their player_moves list.
    def error_detecter(player_move,player_move_calculator): #this func is being used for if there is any error in shooting input.
        control_list = ["A","B","C","D","E","F","G","H","I","J"] #this 2 list is being used for if shooting line is true or not.
        global output_message,check_for_check #output_message is a printed message for every round , check_for_check is being used for if there is any error then this variable is going to be True.
        check_for_check = False #firstly there is no error.
        try:
            if len(player_move)-1< player_move_calculator: #if one of the players shoot move is ended then not check the shoot.
                quit()
            if len(player_move[player_move_calculator]) ==0:  #if shoot move is empty:
                raise IndexError("IndexError: row and colum coordinate could not be defined because of nothing has typed to command.Wrong command is: "+player_move[player_move_calculator])
            if "," not in player_move[player_move_calculator]: #if shoot move is not be parted by comma:
                raise IndexError("IndexError: row and column coordinate could not be defined,Please type a comma when you define a command.Wrong command is: "+player_move[player_move_calculator]) 
            else:
                player_movements_location = player_move[player_move_calculator].split(",") #shoot move splitted by comma.
            if len(player_movements_location) >2:  #if there is more than one comma in shoot move :
                raise ValueError("ValueError: there is more than two coordinate,Please type a command which has 2 dimension.Wrong command is: "+player_move[player_move_calculator])
            if len(player_move[player_move_calculator]) <3: #if len of shoot move is smaller than 3 which is wrong:
                if len(player_move[player_move_calculator]) == 1 or len(player_move[player_move_calculator])==0: #if shoot move len is 0 or 1:
                    raise IndexError("IndexError: row and column coordinate could not be defined,Please type defined column.Wrong command is: "+player_move[player_move_calculator])
                if player_move[player_move_calculator][0] == "," and player_move[player_move_calculator][0] == player_move[player_move_calculator][1]: #if shoot move is ,,
                    raise IndexError("IndexError: row and column coordinate could not be defined,Please type defined column.Wrong command is: "+player_move[player_move_calculator])
                if player_move[player_move_calculator][0] == ",":  #if shoot move is ,... .. could be everything.
                    raise IndexError("IndexError: column coordinate could not be defined because row is not typed in (A to J),Please type defined column.Wrong command is: "+player_move[player_move_calculator])
                else: #if -, - will be everything , but column not typed:
                    raise IndexError("IndexError: row coordinate could not be defined because row is not typed in .(1 to 10) just empty is typed,Please type defined column.Wrong command is: "+player_move[player_move_calculator])
            if len(player_move[player_move_calculator]) >4: #if len of shoot move is larger than 4:
                if len(player_movements_location[0]) > 2 and len(player_movements_location[1]) >1: #if both of sides are not in their boundaries:
                    raise AssertionError("AssertionError: row and column coordinates could not be defined because of coordinates are not in boundary,Please type defined valid command.Wrong command is: "+player_move[player_move_calculator])
                elif len(player_movements_location[0]) > 2: #if just row coordinate not in its boundary:
                    raise AssertionError("AssertionError: row coordinate could not be defined because of coordinate is not in boundary,Please type defined valid command.Wrong command is: "+player_move[player_move_calculator])
                elif len(player_movements_location[1]) > 1: #if just column coordinate not in its boundary:
                    raise AssertionError("AssertionError: column coordinate could not be defined because of coordinate is not in boundary,Please type defined valid command.Wrong command is: "+player_move[player_move_calculator])
            if len(player_move[player_move_calculator]) ==3: #if shoot move len is 3:
                if ord(player_movements_location[1]) >74: #ord is being used in here; which is turning to ascii number of this character.
                    #in ascii 74 is "J" thats why if it is larger than 74 column not is in boundary:
                    raise AssertionError("AssertionError: columm coordinate could not be defined because column is not typed in (A to J).Wrong output is: "+player_move[player_move_calculator])   
                if player_movements_location[0] in control_list: #if row coordinate in A to J:
                    if player_movements_location[1] not in control_list: #if column coordinate not in A to J:
                        raise ValueError("ValueError: row and column coordinate could not be defined because row (1 to 10) and column (A to J) are not typed in their intervals.Wrong command is: "+player_move[player_move_calculator]) 
                    else:  #just row is wrong then:
                        raise ValueError("ValueError:row coordinate could not be defined because row coordinate is not in its interval(1 to 10).Wrong command is: "+player_move[player_move_calculator])
                if player_movements_location[1] not in control_list: #if just column not in its boundary:
                    raise ValueError("ValueError: column coordinate could not be defined because column coordinate is not in its interval(A to J).Wrong command is: "+player_move[player_move_calculator])
            if len(player_move[player_move_calculator]) ==4: #if len of shoot move is 4:
                try:
                    if len(player_movements_location[1]) >1: #if column len is larger than 1:
                        if player_movements_location[0] == "0": #if also row coordinate is 0 then both is wrong.
                            raise ValueError("ValueError: row and column coordinates could not be defined because row is under the boundary and column is not typed in (A to J).Wrong command is: "+player_move[player_move_calculator])
                        else: #else just one of them which column is wrong.
                            raise ValueError("ValueError: column coordinate could not be defined because column is not typed in (A to J).Wrong command is: "+player_move[player_move_calculator])
                    else:
                        if int(player_movements_location[0]) >10:  #if column coordinate is larger than 10:
                            raise AssertionError("AssertionError: row coordinate could not be defined because row is not typed in (1 to 10).Wrong output is: "+player_move[player_move_calculator])   
                        elif ord(player_movements_location[1]) >74: #if ascii turning of column coordinate is larger than 74(Which is "J"):
                            raise AssertionError("AssertionError: columm coordinate could not be defined because column is not typed in (A to J).Wrong output is: "+player_move[player_move_calculator])   
                except ValueError as e: #if ValueError happens than raise another ValueEror to write its output.
                    raise ValueError(e)
        except IndexError as e:    
            check_for_check = True #which mean error is occurred.
            x = "\n\n"+str(e) 
            output_message = output_message+ x # #this message x is being added to output message.
        except ValueError as e:
            check_for_check = True  #which mean error is occurred.
            x = "\n\n"+str(e)
            output_message = output_message+ x  # #this message x is being added to output message.
        except AssertionError as e:
            check_for_check = True  #which mean error is occurred.
            x = "\n\n"+str(e)
            output_message = output_message+ x  # #this message x is being added to output message.
        except:
            check_for_check = True  #which mean error is occurred.
            x = "\n\n"+"Kaboom: run for your life."
            output_message = output_message+ x  # #this message x is being added to output message.

    players_board,players_hidden_board = "Player1’s Board\t\t\t\tPlayer2’s Board\n  A B C D E F G H I J\t\t  A B C D E F G H I J\n"    ,   "Player1’s Hidden Board\t\tPlayer2’s Hidden Board\n  A B C D E F G H I J\t\t  A B C D E F G H I J\n"
    #this strings in the upper will be used for while printing output these strings will be added to top of table.Just players_board will be used in end of raunds.
    #this 2 string in upper; are going to be used for writing the output of the every round top.
    def output_for_table(for_player1_board,for_player2_board): #this func will be used for arranging output message for entrance lists.
        def for_optional_case_ships(players_ships_numbers,player_board): #this func will be used for ships that detected with optional txt's. This func returns nothing but it detects if that ship sink or not.
            global battleship_controller,patrol_boat_controller #this variables being used for if ship sink or not.
            battleship_controller = 0;patrol_boat_controller = 0 #for starting these variables are 0 if ship sink then this variable will stay 0 again.
            for a in players_ships_numbers: #for optional cases dict will be in loop.
                if a == "B1" or a == "B2": #if ship is battleship which mean.
                    shooting_calculator = 0 #this detects for how many part of the ship sink.
                    for b in players_ships_numbers[a]:  #for that key's variables:
                        if player_board[b[0]-1][b[1]-1] != "X":  #if it is not shooted
                            shooting_calculator +=1 #add 1
                    if shooting_calculator ==0:  #if ship sink:
                        battleship_controller +=1 #then one of ships sink
                else:  #if ship is patrol boat:
                    shooting_calculator = 0 #this detects for how many part of the ship sink.
                    for b in players_ships_numbers[a]:   #for that key's variables:
                        if player_board[b[0]-1][b[1]-1] != "X":   #if it is not shooted
                            shooting_calculator +=1  #add 1
                    if shooting_calculator ==0:  #if ship sink:
                        patrol_boat_controller +=1 #then one of ships sink

        global output_message #general output message is being called.
        if game_finished_detecter: #if game is finished which is will be detected in mainloop.
            output_message = players_board +"" #if game is finished then players open board will be added to output
        else:
            output_message = players_hidden_board + ""  #if game is not finished then players hidden board will be added to output
        carrier1_counter,carrier2_counter ,destroyer1_counter,destroyer2_counter,submarine1_counter,submarine2_counter = 0,0,0,0,0,0 #this for counting ships left.
        for a in range(10): #because of grid size of row is10 that why loop ended at 10
            if a ==9: #if a is equal to end of the loop
                output_message = output_message + str(a+1) #adding to row number beginning of the table. if it is 10, space is not adding to table
            else:
                output_message = output_message + str(a+1)+" "
            for b in for_player1_board[a]: #firstly player1 board is base case in loop (it could be hidden or player_board which will be choosen while func is being called.)
                output_message = output_message + b + " " #If part of the ship shooted or not, it does not matter.Just on the lists element will be added.
            if a ==9:  #if a is equal to end of the loop
                output_message = output_message + "\t\t"+str(a+1) #adding to row number beginning of the table. if it is 10, space is not adding to table
            else:
                output_message = output_message + "\t\t"+str(a+1)+" "
            for b in for_player2_board[a]: #secondly player2 board is base case in loop (it could be hidden or player_board which will be choosen while func is being called.)
                output_message = output_message + b + " " #If part of the ship shooted or not, it does not matter.Just on the lists element will be added.
            output_message = output_message + "\n" #end of the row new line is being added.
            carrier1_counter,carrier2_counter = carrier1_counter+ player1_board[a].count("C"),carrier2_counter+ player2_board[a].count("C") #this count processes will be showed that how many part of the that ship has left.
            destroyer1_counter,destroyer2_counter = destroyer1_counter+ player1_board[a].count("D"),destroyer2_counter+ player2_board[a].count("D")
            submarine1_counter,submarine2_counter = submarine1_counter+ player1_board[a].count("S"), submarine2_counter+ player2_board[a].count("S")
     
        def transletor(x,y): #this will be return for in circumstances if player shoot that ship or not.This returns for player1 board and player2 board.
            if x ==0 and y ==0: #if two player shoots their opponents ships.
                return ["X","X"]
            elif x ==0 : #if player1's ship is shooted.
                return["X","-"]
            elif y ==0: #if player2's ship is shooted.
                return ["-","X"]
            else: #if any ship is not shooted.
                return["-","-"]

        def battleship_controllers(battleship_controller): #this func will return for just one player to showing how many battleship sink.
            if battleship_controller ==0:
                return ["-","-"]
            elif battleship_controller == 1:
                return ["X","-"]
            else:
                return ["X","X"]
        
        def patrol_boat_controllers(patrol_boat_controller): #this func will return for just one player to showing how many patrol boat sink.
            if patrol_boat_controller == 0:
                return ["-","-","-","-"]
            elif patrol_boat_controller ==1:
                return ["X","-","-","-"]
            elif patrol_boat_controller ==2 :
                return ["X","X","-","-"]
            elif patrol_boat_controller ==3:
                return ["X","X","X","-"]
            else:
                return ["X","X","X","X"]

        output_message = output_message + "\n"  #new line is being added.
        ship_list = transletor(carrier1_counter,carrier2_counter) #transletor func is being called for carrier ship number. 
        output_message = output_message + "Carrier\t\t"+ship_list[0] +"\t\t\t\tCarrier\t\t"+ship_list[1]+"\n" #under the table carrier shower is being added by ship_list.

        for_optional_case_ships(players_ships_numbers_for1,player1_board) #for_optional_case_ships is being called for player1 to learn if ship is sink or not.
        battleship_control_list1 = battleship_controllers(battleship_controller) #by battleship_controllers its list will be returned.
        output_message = output_message + "Battleship\t"+battleship_control_list1[0]+" "+battleship_control_list1[1]+"\t\t\t\t" #list is being added to table.

        for_optional_case_ships(players_ships_numbers_for2,player2_board) #now for player2 optional cases ship situations are being learned by this func.
        battleship_control_list2 = battleship_controllers(battleship_controller)
        output_message = output_message + "Battleship\t"+battleship_control_list2[0]+" "+battleship_control_list2[1] + "\n"

        ship_list = transletor(destroyer1_counter,destroyer2_counter) #transletor func is being called for Destroyer ship number.
        output_message = output_message + "Destroyer\t"+ship_list[0] +"\t\t\t\tDestroyer\t"+ship_list[1]+"\n"

        ship_list = transletor(submarine1_counter,submarine2_counter) #transletor func is being called for Submarine ship number.
        output_message = output_message + "Submarine\t"+ship_list[0] +"\t\t\t\tSubmarine\t"+ship_list[1]+"\n"

        for_optional_case_ships(players_ships_numbers_for1,player1_board) #for_optional_case_ships is being called for player1 to learn if ship is sink or not.
        patrol_boat_control_list1 = patrol_boat_controllers(patrol_boat_controller)
        output_message = output_message + "Patrol Boat\t"+patrol_boat_control_list1[0]+" "+patrol_boat_control_list1[1]+" "+patrol_boat_control_list1[2]+" "+patrol_boat_control_list1[3]+"\t\t\t"

        for_optional_case_ships(players_ships_numbers_for2,player2_board) #now for player2 optional cases ship situations are being learned by this func.
        patrol_boat_control_list2 = patrol_boat_controllers(patrol_boat_controller)
        output_message = output_message + "Patrol Boat\t"+patrol_boat_control_list2[0]+" "+patrol_boat_control_list2[1]+" "+patrol_boat_control_list2[2]+" "+patrol_boat_control_list2[3]
    
    game_finished_detecter = False #this variable will be used for if game is finished or not.

    def shooting(target,player_board,player_hidden_board): #this function will be used for shooting the target by player.
        target_list = target.split(",") #target variable splitted by comma.
        
        if player_board[int(target_list[0])-1][ord(target_list[1])-65] == "-": #if there is no target in that positon:
            player_board[int(target_list[0])-1][ord(target_list[1])-65] = "O" #change both hidden and normal board.
            player_hidden_board[int(target_list[0])-1][ord(target_list[1])-65] = "O"
        else: #if one of ships in here.
            player_board[int(target_list[0])-1][ord(target_list[1])-65] = "X" #target is shooted.
            player_hidden_board[int(target_list[0])-1][ord(target_list[1])-65] = "X"
            
    output_for_table(player1_board,player2_board)  
    output_for_table(player1_hidden_board,player2_hidden_board)
    general_output_message = "Battle of Ships Game\n\n"  #this variable is for output message. This variable will be our output.
    move1_calculator ,move2_calculator = -1, -1 #this move calculator's start by -1 because in every loop's starting it increased by 1 .

    for mainloop in range(max(len(player1_moves),len(player2_moves))): #this is general loop looping by max of one of the players moves:
        general_output_message = general_output_message + "Player1's Move\n\nRound : "+str(mainloop+1)+"\t\t\t\t\tGrid Size: 10x10\n\n"+output_message
        #player1's starts every round thats why above strings added to general output message.
        tester = True #this variable being used for if there is any mistake in player_in shoot list then increasing the player moves.
        while tester:
            output_message = "" #output message is being used for adding every message to general output message.
            tester = False
            move1_calculator +=1
            general_output_message = general_output_message +"\n"+"\nEnter your move: "+str(player1_moves[move1_calculator]) +"\n"
            error_detecter(player1_moves,move1_calculator)
            if check_for_check == True: #if there is any error then:
                general_output_message = general_output_message[:-1] + output_message[1:]
                tester = True
        if move1_calculator >= len(player1_moves)-1: #if player1 moves ended before game ended:
            pass
        else: #else shoot the target:
            shooting(player1_moves[move1_calculator],player2_board,player2_hidden_board)
        
        general_output_message = general_output_message + "\nPlayer2's Move\n\nRound : "+str(mainloop+1)+"\t\t\t\t\tGrid Size: 10x10\n\n"
        output_for_table(player1_board,player2_board)  #second time output table is calling because it changes after shooting.
        output_for_table(player1_hidden_board,player2_hidden_board)
        general_output_message = general_output_message + output_message 
        
        tester = True
        while tester:
            output_message = ""
            tester = False
            move2_calculator +=1
            general_output_message = general_output_message +output_message+"\n\nEnter your move: "+str(player2_moves[move2_calculator])+"\n"
            error_detecter(player2_moves,move2_calculator)
            if check_for_check == True:
                general_output_message = general_output_message[:-1]+output_message[1:]
                tester = True
        general_output_message = general_output_message + "\n" #because of adding \n again its that if any error happens in above then it should print \n again
        output_for_table(player1_board,player2_board) #third is being called because if there is any error then index's line is changing.
        output_for_table(player1_hidden_board,player2_hidden_board)
        if move2_calculator >= len(player2_moves)-1:
            pass 
        else:
            shooting(player2_moves[move2_calculator],player1_board,player1_hidden_board)
        def Game_finished_check(player_board): #this function is controlling if one of the player shooted the every ship to his enemy.
            ship_counter = 0
            for a in player_board:
                for b in a:
                    if b == "C" or b == "B" or b == "D" or b == "S" or b == "P" :
                        ship_counter +=1
            if ship_counter ==0: #if there is not any ships left then game is finished:
                return True
            else:
                return False 
        check_for_player1 = Game_finished_check(player1_board) #checking for player1
        check_for_player2 = Game_finished_check(player2_board) #checking for player2
        if check_for_player1 and check_for_player2: #if both player shooted them in same round then it is draw:
            game_finished_detecter = True
            output_for_table(player1_board,player2_board)
            general_output_message = general_output_message + "Game Draw!\n\nFinal Information\n\n"+output_message
            break
        elif check_for_player1: #if just player2 shooted all ships to player1's table: player2 wins
            game_finished_detecter = True
            output_for_table(player1_board,player2_board)
            general_output_message = general_output_message + "Player2 Wins!\n\nFinal Information\n\n"+output_message
            break
        elif check_for_player2: #if just player1 shooted all ships to player2's table: player1 wins
            game_finished_detecter = True
            output_for_table(player1_board,player2_board)
            general_output_message = general_output_message + "Player1 Wins!\n\nFinal Information\n\n"+output_message
            break
    g = open("Battleship.out","w")
    g.write(general_output_message) #general message is being writed to in this output file.
    g.close() 
    #Sondaki errorları g.write yapmayı unutma  fıle ıo error olursa hata ismini yakalamayı hallet.
    print(general_output_message) #also message is printed into the cmd.
except IOError: #if there is any can not openable file:
    message = "IOError: " 
    g = open("Battleship.out","w")
    if len(wrong_input_list) ==1: #if one of the file is not being opened:
        print(message+ wrong_input_list[0]+"is not reachable")
        g.write(message+ wrong_input_list[0]+"is not reachable")
    else:
        for x in wrong_input_list:
            message = message+ x+","
        print(message[:-1]+" are not reachable.")
        g.write(message[:-1]+" are not reachable.")
    g.close()
except IndexError: #if there is missing input:
    message = "IndexError: "
    g = open("Battleship.out","w")
    for x in absent_sys_files:
        message = message + x +" "   
    print(message+"has not given as a input.")
    g.write(message+"has not given as a input.")
    g.close()
except: #except any mistakes:
    g = open("Battleship.out","w")
    g.write("Kaboom: run for your life.")
    g.close()
    print("Kaboom: run for your life.")
#Student Name : Ufuk Cefaker
#Student ID: 2220356171