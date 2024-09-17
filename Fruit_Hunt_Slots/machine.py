import pygame
from settings import *
from reel import *
from player import Player
from ui import UI

class Machine:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.reel_list = {}
        self.reel_index = 0
        self.can_toggle = True
        self.spinning = False
        self.machine_balance = 10000.00
        
        self.prev_result = {0:None, 1:None, 2:None, 3:None, 4:None}
        self.spin_result = {0:None, 1:None, 2:None, 3:None, 4:None}

        self.set_reels()
        self.currentPlayer = Player()
        self.ui = UI(self.currentPlayer)

    
    def cooldowns(self):
        for reel in self.reel_list:
            if self.reel_list[reel].reel_is_moving:
                self.can_toggle = False
                self.spinning = True
        if not self.can_toggle and [self.reel_list[reel].reel_is_moving for reel in self.reel_list].count(False) == 5:
            self.can_toggle = True
            self.spin_result = self.get_result()

            if self.check_wins(self.spin_result):
                self.win_data = self.check_wins(self.spin_result)
                self.pay_player(self.win_data, self.currentPlayer)

    
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.can_toggle and self.currentPlayer.balance >= self.currentPlayer.bet_size:
            self.toggle_spinning()
            self.spin_time = pygame.time.get_ticks()
            self.currentPlayer.place_bet()
            self.machine_balance += self.currentPlayer.bet_size
            self.currentPlayer.last_payout = None

    def update(self, delta_time):
        self.cooldowns()
        self.get_input()
        self.draw_reels(delta_time)
        for reel in self.reel_list:
            self.reel_list[reel].symbol_list.draw(self.display_surface)
            self.reel_list[reel].symbol_list.update()
        self.ui.update()
        
    def draw_reels(self, delta_time):
        for reel in self.reel_list:
            self.reel_list[reel].animate(delta_time)

    def set_reels(self):
        if not self.reel_list:
            x_tl = 10
            y_tl = -220
        while self.reel_index < 5:
            if self.reel_index > 0:
                x_tl = x_tl + 220 + X_OFFSET
                y_tl = y_tl
            self.reel_list[self.reel_index] = Reel((x_tl, y_tl))
            self.reel_index += 1
    
    def toggle_spinning(self):
        if self.can_toggle:
            self.spin_time = pygame.time.get_ticks()
            self.spinning = not self.spinning
            self.can_toggle = False

            for reel in self.reel_list:
                self.reel_list[reel].start_spin(int(reel) * 200)

    def get_result(self):
        for reel in self.reel_list:
            self.spin_result[reel] = self.reel_list[reel].reel_spin_result()
        return self.spin_result
    
    def check_wins(self, result):
        hits = {}
        
        horizontal_values = []
        for value in result.values():
            horizontal_values.append(value)
        rows, cols = len(horizontal_values), len(horizontal_values[0])
        
        for row in horizontal_values:
            for symbol in row:
                if row.count(symbol) >= 3:
                    possible_win = [index for index, value in enumerate(row) if symbol == value]

                    if len(self.longest_sequence(possible_win)) >= 3:
                        hits[f'Row {horizontal_values.index(row) + 1}'] = [symbol, self.longest_sequence(possible_win)]

        for col_idx in range(cols):
            column = [horizontal_values[row_idx][col_idx] for row_idx in range(rows)]  # Extract column
            for symbol in column:
                if column.count(symbol) >= 3:
                    possible_win = [index for index, value in enumerate(column) if symbol == value]

                    if len(self.longest_sequence(possible_win)) >= 3:
                        hits[f'Column {col_idx + 1}'] = [symbol, self.longest_sequence(possible_win)]
        
        if hits:
            return hits

    def longest_sequence(self, hit):
        subSeqLength, longest = 1, 1
        start, end = 0, 0
        for i in range(len(hit) - 1):
            if hit[i] == hit[i + 1] - 1:
                subSeqLength += 1
                if subSeqLength > longest:
                    longest = subSeqLength
                    start = i + 2 - subSeqLength
                    end = i + 2
            else:
                subSeqLength = 1
        return hit[start:end]


    def pay_player(self, win_data, currentPlayer):
        multiplier = 0
        spin_payout = 0
        for v in win_data.values():
            if len(v[1]) >= 5:
                multiplier += len(v[1]) * 2
            else:
                multiplier += len(v[1]) - 1
        spin_payout = (multiplier * currentPlayer.bet_size)
        currentPlayer.balance += spin_payout
        self.machine_balance -= spin_payout
        currentPlayer.last_payout = spin_payout
        currentPlayer.total_won += spin_payout






