#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import random

class Board:
    """
    Board Class represent the basic game board of one player in battleship game
    Each board class contains board size, grid data, ships details and shipment remaining for data storage.
    """
    def __init__(self, size=10):
        """
        

        Parameters
        ----------
        size : int 
            The default is 10. Representing the battleship board size, 10*10 square

        Returns
        -------
        None.

        """
        self.size = size
        
        # Representing the board cells:
        # '.' indicates empty, 'S' indicates ship, 'X' indicates hit, 'O' indicates miss
        self.grid = [['.' for _ in range(size)] for _ in range(size)]
        self.ships = []  # List to store ship details, format: (row, col, length, orientation)
        self.ships_remaining = 0  # Number of remaining ships

    def place_ship(self, row, col, length, orientation):
        """
        

        Parameters
        ----------
        row : int
            Row coordinator of that ship starting location
        col : int
            Col coordinator of that ship starting location
        length : int
            Ships length
        orientation : char
            Orientation for that ship. 'H' Represents horizontally, 'V' represents vertically

        Returns
        -------
        Boolean
            True for the ship is a valid selection for ship placement. False otherwise.

        """
        if orientation == 'H':  # Horizontal placement
            if col + length > self.size:
                return False  # Ship exceeds board boundaries
            for c in range(col, col + length):
                if self.grid[row][c] != '.':
                    return False
            for c in range(col, col + length):
                self.grid[row][c] = 'S'
            self.ships.append((row, col, length, orientation))
            self.ships_remaining += 1
            return True
        else:  # Vertical placement
            if row + length > self.size:
                return False
            for r in range(row, row + length):
                if self.grid[r][col] != '.':
                    return False
            for r in range(row, row + length):
                self.grid[r][col] = 'S'
            self.ships.append((row, col, length, orientation))
            self.ships_remaining += 1
            return True

    def receive_strike(self, row, col):
        """

        Parameters
        ----------
        row : int
            Row coordinator for receiving a strike
        col : int
            Row coordinator for receiving a strike

        Returns
        -------
        str
            The return provides grid status data for later parts
            updating the real status for game board
            It returns the string outcome for later printing result part

        """
        cell = self.grid[row][col]
        if cell == 'S':  # Ship hit
            self.grid[row][col] = 'X'
            self.check_ships_remaining()
            return 'hit'
        elif cell == '.' or cell == 'O':  # Empty or previously missed cell
            self.grid[row][col] = 'O'
            return 'miss'
        elif cell == 'X':  # Cell already hit
            return 'already'

    def check_ships_remaining(self):
        """Update the number of remaining ships."""
        destroyed_ships = 0
        for ship in self.ships:
            row, col, length, orientation = ship
            ship_cells = []
            if orientation == 'H':
                ship_cells = [self.grid[row][c] for c in range(col, col + length)]
            else:
                ship_cells = [self.grid[r][col] for r in range(row, row + length)]
            if all(cell == 'X' for cell in ship_cells):
                destroyed_ships += 1
        self.ships_remaining = len(self.ships) - destroyed_ships

    def display(self, hide_ships=False):
        """
        

        Parameters
        ----------
        hide_ships : Boolean
            Default is set to False. It set to be True, if it is the opponent
            "AI" board, which displaying that board should not showing AI's Ships
            Locations. 

        Returns
        -------
        None.

        """
        print("   " + " ".join([str(i) for i in range(self.size)]))
        for i, row in enumerate(self.grid):
            display_row = [cell if not (hide_ships and cell == 'S') else '.' for cell in row]
            print(str(i).rjust(2), " ".join(display_row))

class Player:
    """
    Player class represents player or AI cpu player data.
    It stores player name, board data, opponents player, 
    and game board ship length data.
    """
    def __init__(self, name="Player"):
        """
        

        Parameters
        ----------
        name : str
            Player name. The default is "Player".

        """
        self.name = name
        self.board = Board()  # Player's board data
        self.opponent = None  # Opponent player. Later will be set to AI player
        self.ship_lengths = [2,3,3,4,5] #int_list of every ship length
    def AI_place_ships(self):
        """
        Help AI player create ship placement process before strikes starts. 
        """
        for l in self.ship_lengths:
            #Looping from ship lengths data. Place ship for every shipment settled down.
            while True:
                #Creating the True-Except block preventing the invalid cases of shipment
                #invalid Case: Ships located will be out of board range
                try:
                    #Row and column coordinator should be random int from 0 to 9
                    row,col = random.randint(0,9),random.randint(0,9)
                    #Orientation should be selected randomly for either horizontally or veritcally.
                    orientation = random.choice(['H','V'])
                    if self.board.place_ship(row,col,l,orientation):
                        #If it's a valid placement 
                        #break the while loop to consider next ship placement
                        break
                except ValueError:
                    #Prevent ValueError such that placement out of board range. 
                    print("")
    def user_place_ships(self):
        """
        User Ship Placement Function. It ask users to input locations and orientation of ships.
        And it updates the ships data to player board data. 

        """
        print("Place your ships on the board!")
        self.board.display()  # Make sure to use self.board to access the board instance
        for length in self.ship_lengths:
            #Loop for every ship placement
            while True:
                try:
                    print(f"Place a ship of length {length}.")
                    #User Input Coordinator and Orientation data
                    row = int(input("Enter the starting row (0-indexed): "))
                    col = int(input("Enter the starting column (0-indexed): "))
                    orientation = input("Enter orientation ('H' for horizontal, 'V' for vertical): ").strip().upper()
                    if self.board.place_ship(row, col, length, orientation):
                        print("Ship placed successfully!")
                        self.board.display()  # Display the board after placing a ship
                        break
                    else:
                        print("Invalid placement. Try again.")
                except ValueError:
                    #Similar as AI_place_ships, if user inputted data out of board range, 
                    #we refer that for preventing program breaks.
                    print("Invalid input. Please enter numbers for row and column.")

    def make_move(self):
        """
        Function is used to take action on each round for player's movement. 

        Returns
        -------
        result : str
            The result string returned by function receive_strike

        """
        print(f"{self.name}'s turn.")
        #initialize the checker boolean. Checker boolean represents the 
        #whether the user inputted location is valid to be attacked. 
        #True if it's not valid, false otherwise. 
        checker = True
        while checker:
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            checker = row >=0 and col >= 0 and row<=9 and col <=9
            if checker:
                result = self.opponent.board.receive_strike(row, col)
                print("You", result, f"at ({row}, {col})")
                checker = False
            else:
                print("Out of range for input value, Try again!")
                checker = True
        return result

    def has_ships_left(self):
        """
        
        Returns
        -------
        Boolean
            Return whether there's still ship remained'

        """
        return self.board.ships_remaining > 0


class EasyAI(Player):
    """
    Creates EasyAI bot class, inside the player class as a subclass
    """
    def make_move(self):
        """
        Easy AI bot just randomly makes the strike for player battleship baord. 
        Returns
        -------
        result : str
            The status string of grid data for EasyAI. 

        """
        while True:
            row, col = random.randint(0, self.board.size - 1), random.randint(0, self.board.size - 1)
            result = self.opponent.board.receive_strike(row, col)
            if result != 'already':
                print(f"{self.name} strikes at ({row}, {col}) and {result}s!")
                return result


class MediumAI(Player):
    """
    Medium AI bot class creates a medium difficulty level AI bot for battleship game
    It has memory on previous attack selection, and it has strategy for next movement
    if last attack is successful. It will target the adjacent cells.
    """
    def __init__(self, name="Medium AI"):
        """
        

        Parameters
        ----------
        name : str, optional
           AI-Bot name.  The default is "Medium AI".

        """
        super().__init__(name)
        self.previous_moves = set() #Memory of movement set
        self.target_queue = [] #Memory on Target Queue

    def make_move(self):
        """Targets adjacent cells if a ship is hit."""
        if self.target_queue:
            row, col = self.target_queue.pop(0)#Pop up the first target queue location and record. 
        else:
            #If there's no target_queue, we trying find a new location to append randomly. 
            while True:
                #Similarly, random generate a coordinator. 
                row, col = random.randint(0, self.board.size - 1), random.randint(0, self.board.size - 1)
                
                if (row, col) not in self.previous_moves:
                    #Break the loop, such that we find a new random attack location
                    #besides previous move.
                    break
        #Update the movement, and record the strike. 
        self.previous_moves.add((row, col))
        result = self.opponent.board.receive_strike(row, col)
        print(f"{self.name} strikes at ({row}, {col}) and {result}s!")
        if result == 'hit':
            #If this movement results in a hit, then the next movement we have target. 
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                #On each direction, we could take a guess to see whether it hits a ship. 
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < self.board.size and 0 <= new_col < self.board.size and (new_row, new_col) not in self.previous_moves:
                    #If the new coordinators are valid, and they are not been checked before,
                    #We append the target queue for the next movement. 
                    self.target_queue.append((new_row, new_col))
        return result


class HardAI(Player):
    """
    Define a Hard Difficult Level of AI bot for this game. 
    It uses checkboard strategy for attack movement.
    """
    def __init__(self, name="Hard AI"):
        """
        
        Parameters
        ----------
        name : str, 
           The default is "Hard AI".

        """
        super().__init__(name)
        self.previous_moves = set() #Memory of previous moves set
        #Creates checkerboard for Hard AI-bot. It checks the ship by dividing board into two parts for efficiency
        self.checkerboard = [(r, c) for r in range(self.board.size) for c in range(self.board.size) if (r + c) % 2 == 0]

    def make_move(self):
        """
        Uses a checkerboard pattern for more efficient targeting.

        Returns
        -------
        result : Str
            Board Grid Data results

        """
        while True:
            #We check the locations on the division line in priority. 
            if self.checkerboard:
                row, col = self.checkerboard.pop(0)#Pop up and record the first check location
            else:
                #If no remained target, randomly choose a new location for attack. 
                row, col = random.randint(0, self.board.size - 1), random.randint(0, self.board.size - 1)
            if (row, col) not in self.previous_moves:
                break
        self.previous_moves.add((row, col))#Add the attack record to memory set. 
        result = self.opponent.board.receive_strike(row, col)
        print(f"{self.name} strikes at ({row}, {col}) and {result}s!")
        return result


class Game:
    """
    Game class for setup the game board
    It directly relates to the main function, starting up the game interaction. 
    """
    def __init__(self, ai_type="Easy"):
        """
        

        Parameters
        ----------
        ai_type : str, 
            Easy, Medium, Hard 3 level of AI bot
        """
        self.player = Player("You")
        self.ai = self.create_ai(ai_type)
        self.player.opponent = self.ai
        self.ai.opponent = self.player

    def create_ai(self, ai_type):
        """

        Parameters
        ----------
        ai_type : str
            Easy, Medium, Hard 3 level AI bot

        Raises
        ------
        ValueError
            If input value is not Easy, Medium, Hard 3 level AI bot

        Returns
        -------
        Player
            The player bot. 

        """
        if ai_type == "Easy":
            return EasyAI("Easy AI")
        elif ai_type == "Medium":
            return MediumAI("Medium AI")
        elif ai_type == "Hard":
            return HardAI("Hard AI")
        else:
            raise ValueError("Invalid AI type! Choose 'Easy', 'Medium', or 'Hard'.")

    def setup(self):
        """
        Game Set up function
        """
        print("Setting up your board...")
        #Player Setup board
        self.player.user_place_ships()
        print("Your board:")
        self.player.board.display()
        #Opponent AI setup board.
        print("\nSetting up AI board...")
        self.ai.AI_place_ships()

    def run(self):
        current_player = self.player
        while self.player.has_ships_left() and self.ai.has_ships_left():
            if current_player == self.player:
                print("\nYour board:")
                self.player.board.display()
                print("\nOpponent's board (hidden):")
                self.ai.board.display(hide_ships=True)
                current_player.make_move()
                current_player = self.ai
            else:
                current_player.make_move()
                current_player = self.player

        if self.player.has_ships_left():
            print("You win!")
        else:
            print("Computer wins!")


if __name__ == "__main__":
    print("Select AI difficulty: Easy, Medium, Hard")
    ai_difficulty = input("Enter AI type: ").strip()
    game = Game(ai_difficulty)
    game.setup()
    game.run()


# In[ ]:




