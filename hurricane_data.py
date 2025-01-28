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

# 1
# Update Recorded Damages

def convert_data(damages):
  converted_data = []
  for cost in damages:
    if cost == 'Damages not recorded':
      converted_data.append(cost) 
    elif 'M' in cost:
      cleaned_data = cost.replace('M', '')
      converted_data.append(float(cleaned_data) * 1000000)
    elif "B" in cost:
      cleaned_data = cost.replace('B', '')
      converted_data.append(float(cleaned_data) * 1000000000)
  return converted_data

converted_damages  = convert_data(damages)

print(converted_damages)
    
# 2 
# Create a Table
hurricane_data_dict = {}

# Create and view the hurricanes dictionary
def create_dict(names, months, years, max_sust_wind, area_affected, deaths):
  for i in range(len(names)):
        hurricane_data_dict[names[i]] = {
          "Name": names[i],
          "Month": months[i],
          "Year": years[i],
          "Max Sustained Wind": max_sustained_winds[i],
          "Areas Affected": areas_affected[i],
          "Damage": converted_damages[i],
          "Deaths": deaths[i]}


create_dict(names,months, years, max_sustained_winds, areas_affected, deaths)

#print(hurricane_data_dict)
#3
# Organizing by Year
def organize_by_year(hurricane_data_dict):
    data_by_year = {}
    for name, data in hurricane_data_dict.items():
        print(f"{data}\n")
        year = data["Year"] 
        data_by_year[year] = ({"name": name, **data}) 
    return data_by_year
   
data_by_year = organize_by_year(hurricane_data_dict)

# 4
# Counting Damaged Area
print(len(areas_affected))
# create dictionary of areas to store the number of hurricanes involved in
def convert_areas_affected(hurricane_data_dict):
  times_area_affected = {}
  for  name, data in hurricane_data_dict.items():
    for area in data['Areas Affected']:
      if not times_area_affected.get(area, 0):
        times_area_affected[area] = 1
      else:
        times_area_affected[area] += 1
  return times_area_affected

times_areas_affected= convert_areas_affected(hurricane_data_dict)
print(times_areas_affected)
# 5 
# Calculating Maximum Hurricane Count
def most_affected_area(times_areas_affected):
  num = 0
  most_affected = ''
  for location, times_hit in times_areas_affected.items():
    if times_hit > num:
      num = times_hit
      most_affected = location

    return f"The location that has been affected the most is {most_affected} which has been hit {num} times."
# find most frequently affected area and the number of hurricanes involved in
most_affected = most_affected_area(times_areas_affected)
print(most_affected)


# 6
# Calculating the Deadliest Hurricane
hurricane_deaths = list(zip(names, deaths))

def deadliest_hurricane(hurricane_deaths):
  most_deaths = max(hurricane_deaths, key=lambda x: x[1])
  return most_deaths
# find highest mortality hurricane and the number of deaths
most_deaths  = deadliest_hurricane(hurricane_deaths)
print(most_deaths)

# 7
# Rating Hurricanes by Mortality
def hurricane_rating(hurricane_deaths):
  rating_dict = {0:[], 1:[], 2:[], 3:[], 4:[]}
  mortality_scale = {4: 10000, 3: 1000, 2:500, 1: 100, 0:0}
  for data in hurricane_deaths:
    for key, value in mortality_scale.items():
       if data[1] >= value:
         rating_dict[key].append(data[0])
         break 
  return rating_dict




# categorize hurricanes in new dictionary with mortality severity as key
ratings = hurricane_rating(hurricane_deaths)
print(ratings)

# 8 Calculating Hurricane Maximum Damage
damage_data = list(zip(names,damages))
def greatest_damage(names, damages):
  damage_data = list(zip(names,damages))
  #print(damage_data)
  name_worst = ''
  highest_cost= 0
  for name, cost in damage_data:
    if  isinstance(cost, str):
      continue
    else: 
      if cost > highest_cost:
        highest_cost = cost;
        name_worst  = name
  
  return f"The most destructive hurricane was {name_worst} it did ${highest_cost} in damages."


# find highest damage inducing hurricane and its total cost
greatest_damage = greatest_damage(names, convert_data(damages))
print(greatest_damage)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
                
reversed_damage_scale = {4: 50000000000, 3: 10000000000,2: 1000000000,1: 100000000, 0: 0,}
# categorize hurricanes in new dictionary with damage severity as key
def catagorize_damage(names, damages):
  organized_scaled_data = {0: [], 1: [], 2: [], 3:[], 4:[]}
  damage_data = list(zip(names, damages))
  for name, damage in damage_data:
    for key, value in reversed_damage_scale.items():
      if isinstance(damage, str):
        organized_scaled_data[0].append(name)
        continue
      elif damage >= value:
        organized_scaled_data[key].append(name)
    
  return organized_scaled_data
catagorized_damage = catagorize_damage(names, convert_data(damages))
print(catagorized_damage)