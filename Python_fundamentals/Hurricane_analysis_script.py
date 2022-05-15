# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damage(damages):
  float_damage = []
  for damage in damages:
    if damage[-1] == "M":
      float_damage.append(float(damage[:-1]) * conversion["M"])
    elif damage[-1] == "B":
      float_damage.append(float(damage[:-1]) * conversion["B"])
    else:
      float_damage.append(damage)
  return float_damage
  
updated_damages = update_damage(damages)
print(updated_damages)

# write your construct hurricane dictionary function here:

def create_dictionary(name, month, year, max_sustained_wind, areas_affected, damage, deaths):
  hurricane_dictionary = {}
  for i in range(len(names)):
    hurricane_dictionary.update({name[i]: {"Name": name[i], "Month": month[i], "Year": year[i], "Max Sustained Wind": max_sustained_wind[i], "Areas Affected": areas_affected[i], "Damage": damage[i], "Deaths": deaths[i]}})
  return(hurricane_dictionary)

hurricane_dictionary = create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)


# write your construct hurricane by year dictionary function here:

def year_dictionary(hurricanes):
  hurricanes_by_year= dict()
  for hurricane in hurricanes:
      current_year = hurricanes[hurricane]['Year']
      current_hurricane = hurricanes[hurricane]
      if current_year not in hurricanes_by_year:
          hurricanes_by_year[current_year] = [current_hurricane]
      else:
          hurricanes_by_year[current_year].append(current_hurricane)
  return hurricanes_by_year

hurricanes_by_year = year_dictionary(hurricane_dictionary)

# write your count affected areas function here:

def by_area(dictionary):
  by_area = dict()
  all_hurricane_areas = []
  for hurricane in hurricane_dictionary:
    for i in hurricane_dictionary[hurricane]["Areas Affected"]:
      all_hurricane_areas.append(i)
  hurricane_areas = set(all_hurricane_areas)
  for area in hurricane_areas:
    by_area[area] = all_hurricane_areas.count(area)
  return by_area
hits_by_area = by_area(hurricane_dictionary)
print(hits_by_area)


# write your find most affected area function here:

def most_affected_area(dictionary):
  max_hits = max(dictionary.values())
  max_hit_area = []
  for area, hits in dictionary.items():
    if hits == max_hits:
      max_hit_area.append(area)
  return max_hit_area
print(most_affected_area(hits_by_area))

# write your greatest number of deaths function here:

def deadliest_hurricane(dictionary):
  all_deaths = []
  for hurricane, details in hurricane_dictionary.items():
    all_deaths.append(details["Deaths"])
  for details in hurricane_dictionary.values():
    if details["Deaths"] == max(all_deaths):
      return details["Name"]

print(deadliest_hurricane(hurricane_dictionary))


# write your catgeorize by mortality function here:

def by_mortality_rate(hurricane_dictionary):
  by_mortality = {0: [], 1: [], 2: [], 3: [], 4: []}
  for details in hurricane_dictionary.values():
    if details["Deaths"] == 0:
      by_mortality[0].append(details)
    elif 0 < details["Deaths"] <= 100:
      by_mortality[1].append(details)
    elif 101 < details["Deaths"] <= 500:
      by_mortality[2].append(details)
    elif 501 < details["Deaths"] <= 1000:
      by_mortality[3].append(details)
    elif 1001 < details["Deaths"] <= 10000:
      by_mortality[4].append(details)
  return by_mortality


# write your greatest damage function here:

def most_damaging_hurricane(dictionary):
  all_damages = []
  for hurricane, details in dictionary.items():
    if isinstance(details["Damage"], float):
      all_damages.append(details["Damage"])
  for details in dictionary.values():
    if details["Damage"] == max(all_damages):
      return details["Name"] + ", Damage: " + str(details["Damage"])



# write your catgeorize by damage function here:
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def rate_by_damage(dictionary):
  by_damage = {0: [], 1: [], 2: [], 3: [], 4: []}
  for details in dictionary.values():
    if details["Damage"] == "Damages not recorded":
      continue
    elif details["Damage"] == damage_scale[0]:
      by_damage[0].append(details)
    elif damage_scale[0] < details["Damage"] <= damage_scale[1]:
      by_damage[1].append(details)
    elif damage_scale[1] < details["Damage"] <= damage_scale[2]:
      by_damage[2].append(details)
    elif damage_scale[2] < details["Damage"] <= damage_scale[3]:
      by_damage[3].append(details)
    elif damage_scale[3] < details["Damage"] <= damage_scale[4]:
      by_damage[4].append(details)
  return by_damage


