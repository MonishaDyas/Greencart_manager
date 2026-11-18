"""Handles member registration and concession eligibility."""

def calculate_balance(wallet, fee=5):
    return wallet - fee

def check_senior(age, balance):
    return age >= 60 and balance > 0