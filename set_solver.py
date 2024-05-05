# Contains helper functions for selenium based automation of SET

def dec_to_ternary_card(card_id):
    """
    INPUT: numeric string (1-81) corresponding to one of the 81 SET game cards
    OUTPUT: ternary ordered quadruple -> e.g. [0, 2, 1, 2]
    Helper function converts each id to the equivalent ternary representation minus 1 in order to index from 0 instead of 1. This saves us from using a 5th ternary bit to represent each card.
    """
    value = int(card_id) - 1
    return [value//27, (value%27)//9, (value%9)//3, value%3]


def is_set(card1, card2, card3):
    """
    INPUTS: 3 cards as ternary ordered quadruple -> [a, b, c, d] where a, b, c, and d are ternary digits (0-2)
    OUTPUT: Boolean
    Helper Function is_set takes in three cards as ordered quadruples and returns True only if for each category all cards are either the same or all different.
    """
    for i in range(4):
        if not (((card1[i] == card2[i]) and (card2[i] == card3[i])) or ((card1[i] != card2[i]) and (card2[i] != card3[i]) and (card1[i] != card3[i]))):
            return False
    # print(f"Cards {card1}, {card2}, {card3} ARE A MATCH!")
    return True

def get_matches(card_list):
    """
    INPUT: List of cards in order as ternary ordered quadruples
    OUTPUT: List of integer lists of triples
    Helper function get_matches takes in a list of cards and checks every combination of cards to calculate all combinations which would form a valid SET. Returns the found sets as a list of integer lists where each sublist contains the card #'s of a valid SET. 
    """
    all_matches = []
    for i in range(len(card_list)-2):
        for j in range(i+1, len(card_list)-1):
            for k in range(j+1, len(card_list)):
                if is_set(card_list[i], card_list[j], card_list[k]):
                    all_matches.append([i,j,k])
    return all_matches