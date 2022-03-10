import csv
import tui

def list_years(data):
    tui.started("Listing years")
    years = set()
    for record in data:
        year = record[9]
        years.add(year)
        tui.display_years(years)

def tally_medals(data):
    dictionary = {"Gold": 0, "Silver": 0, "Bronze": 0}
    NA = 0
    for record in data:
        if record[14] == "Gold":
            dictionary['Gold'] =+ 1
        elif record[14] == "Silver":
            dictionary['Silver'] =+ 1
        elif record[14] == "Bronze":
            dictionary['Bronze'] =+ 1
        else:
            NA = NA + 1
    tui.display_medal_tally(dictionary)





tally_medals(data="athlete_events.csv")
