tops = int(input("Number of tops:\n"))
legs = int(input("Number of legs:\n"))
screws = int(input("Number of screws:\n"))

tables = int(min(tops, legs / 4, screws / 8))

remaining_table_tops = tops - tables
remaining_table_legs = legs - tables * 4
remaining_table_screws = screws - tables * 8

print(str(tables) + " tables assembled. Leftover parts: " + str(remaining_table_tops) + " table tops, " + str(remaining_table_legs) + " legs, " + str(remaining_table_screws) + " screws.")