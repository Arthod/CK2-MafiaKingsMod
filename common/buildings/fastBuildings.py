# Apologies if this is hardcoding.

    
class Building:
    def __init__(self, name, gold_cost, build_time, tax_income, prestige_income, hide_if_not, upgrades_from, prerequisites, fertility=0):
        self.str = "" \
        + "\n   # " + str(name) \
        + "\n   " + str(name) + " = {" \
        + "\n       desc = " + str(name) + "_desc" \
        + "\n       potential = {" \
        + "\n           religion_group = legal_group"
        self.str +=  "" \
        + "\n           FROMFROM = { has_building = " + str(hide_if_not) + " }"  if (hide_if_not != "none") else ""
        self.str += "" \
        + "\n       }" \
        + "\n       trigger = { FROM = { government = business_government } }"
        self.str += "" \
        + "\n       upgrades_from = " + str(upgrades_from) + " " if (upgrades_from != "none") else ""
        self.str += "" \
        + "\n       gold_cost = " + str(gold_cost) \
        + "\n       build_time = " + str(build_time) \
        + "\n       ai_creation_factor = 100"
        self.str += "" \
        + "\n       prerequisites = { " + str(prerequisites) + " }" if (prerequisites != "none") else ""
        self.str += "" \
        + "\n"  \
        + "\n       tax_income = " + str(tax_income)
        self.str += "" \
        + "\n       monthly_character_prestige = " + str(prestige_income) if (prestige_income != 0) else ""
        self.str += "" \
        + "\n       fertility = " + str(fertility) if (fertility != 0) else ""
        self.str += "" \
        + "\n   }"

    def __str__(self):
        return(self.str)

b = []

# Restaurant main.
b.append(Building("legal_restaurant_main_1", 250, 365, -2, 0.1, "none", "none", "none"))
for i in range(1, 6):
    b.append(Building("legal_restaurant_main_" + str(i+1), 250+50*(i-1), 365+65*i, -2, 0.1, "none", "legal_restaurant_main_" + str(i), "none"))

# Dining room.
b.append(Building("legal_restaurant_dining_1", 250, 80, 4, 0, "legal_restaurant_main_1", "none", "legal_restaurant_main_1"))
for i in range(1, 6):
    b.append(Building("legal_restaurant_dining_" + str(i+1), 250+12*(i-1), 80+35*i, 4, 0, "legal_restaurant_main_1", "legal_restaurant_dining_" + str(i), "legal_restaurant_main_" + str(i+1)))

# Wine cellar.
b.append(Building("legal_restaurant_wine_cellar_1", 80, 30, 2, 0.2, "legal_restaurant_main_1", "none", "legal_restaurant_main_1"))
for i in range(1, 3):
    b.append(Building("legal_restaurant_wine_cellar_"+str(i+1), 80+40*i, 30+10*i, 2, 0.2, "legal_restaurant_main_1", "legal_restaurant_wine_cellar_" + str(i), "legal_restaurant_main_" + str(i*3)))

# Food variation.
b.append(Building("legal_restaurant_food_1", 120, 30, 2, 0, "legal_restaurant_main_1", "none", "legal_restaurant_main_1"))
for i in range(1, 3):
    b.append(Building("legal_restaurant_food_"+str(i+1), 120+40*i, 30+10*i, 2, 0, "legal_restaurant_main_1", "legal_restaurant_food_" + str(i), "legal_restaurant_main_" + str(i*3)))



file = open("00_legalBuildings.txt", "w")

file.write("castle = {")
for building in b:
    file.write(building.str) 
file.write("\n}")

file.close()
