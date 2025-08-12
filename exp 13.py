import itertools

def solve_cryptarithmetic():
    # Unique letters in the puzzle
    letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')
    digits = range(10)

    for perm in itertools.permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))

        # Leading letters can't be zero
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue

        # Convert letters to numbers
        send = mapping['S']*1000 + mapping['E']*100 + mapping['N']*10 + mapping['D']
        more = mapping['M']*1000 + mapping['O']*100 + mapping['R']*10 + mapping['E']
        money = mapping['M']*10000 + mapping['O']*1000 + mapping['N']*100 + mapping['E']*10 + mapping['Y']

        if send + more == money:
            print(f"SEND: {send}, MORE: {more}, MONEY: {money}")
            print("Mapping:", mapping)
            return

if __name__ == "__main__":
    solve_cryptarithmetic()
