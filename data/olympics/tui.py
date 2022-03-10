def started(msg=""):
    print("-------------------------------------------------------------------------------------")
    print(f"Operation started: {msg}")

def completed():
    print()
    print("Operation completed")
    print("-------------------------------------------------------------------------------------")

def error(msg):
    print(f"Error! {msg}!")


def menu():
    entry = input("Please select one of the following options:\n  [years]   List unique years\n  [tally]   Tally up medals\n  [team]   Tally up the medals for each team\n  [exit]   Exit the program\n")
    print(f"Your selection: {entry}")

def display_medal_tally(tally):
    tally = {}
    tally["Gold"] = 10
    tally["Silver"] = 5
    tally["Bronze"] = 2
    tally_list = list(tally)
    print(f"|Gold    |{tally['Gold']}    |")
    print(f"|Silver  |{tally['Silver']}  |")
    print(f"|Bronze  |{tally['Bronze']}  |")

def display_team_medal(team_tally):
    for team, tally in team_tally.items():
        print(team)
        print(f"\tGold:{tally['Gold']}, Silver:{tally['Silver']}, Bronze:{tally['Bronze']}")

def display_years(years):
    sorted_years = sorted(years, reverse=True)
    for year in sorted_years:
        print(year)


