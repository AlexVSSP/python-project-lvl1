#!/usr/bin/env python3
from brain_games.main_logic import welcome_user
from brain_games.games.brain_calc_game import welcome_game_calc
from brain_games.games.brain_calc_game import checking_data


def main():
    welcome_user()
    welcome_game_calc()
    checking_data()


if __name__ == '__main__':
    main()
