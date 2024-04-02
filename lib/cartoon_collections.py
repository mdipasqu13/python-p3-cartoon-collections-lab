def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves, 1):
        print(f"{i}. {dwarf}")

def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + '!' for call in planeteer_calls]
    
def long_planeteer_calls(list_of_calls):
    for call in list_of_calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(list_of_snacks):
    list_of_cheese = ["cheddar", "gouda", "camembert"]
    for item in list_of_snacks:
        if item in list_of_cheese:
            return item
    return None