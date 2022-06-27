#!/usr/bin/env python3
from brain_games.main_logic import welcome_user
from brain_games.games.brain_prime_game import welcome_game_prime
from brain_games.games.brain_prime_game import checking_data


def main():
    welcome_user()
    welcome_game_prime()
    checking_data()


if __name__ == '__main__':
    main()
