# dictionary and lists
# dictionaries are typically what?
# key and value pairings => HASH TABLES
# what is a list? => Arrays! perfect, no keys. index values
list_example = ["bacon", "eggs", "potatoes", "lettuce"]  # O(N) time
# if we knew array[2] = potaotes
print(list_example[2])

cool_basketball_players = {"Kawhi Leonard": 2,
                           "Kevin Durant": 35, "Stephen Curry": 30}
print(cool_basketball_players)
# accessing and printing an element
print(cool_basketball_players['Kawhi Leonard'])

# a for loop would be handly here
# how to escape a character
for player in cool_basketball_players:
    # stretch: use .values() to pull values from key value pairs
    print(f'{player}\'s jersey numbers are: {cool_basketball_players[player]}')
