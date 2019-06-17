'''
FINAL PROJECT: HUB OF GRUB by Caroline Wang
5/4/2019
Description: A restaurant-finding application.
Goal is to find restaurants nearby that are open and match food preferences
'''


#import datetime library
from datetime import datetime, time

#import restaurant data
from restaurant_database import restaurants
 

class hubGrubOrder:
    
    def __init__(self,location,foodPref):
        #initialize as private attributes
        self.location = location
        self.food_pref = foodPref
        
        #Current time of the order
        self.current_time = datetime.now().time()
        self.current_day = datetime.today().weekday()
    
   
       
    def restaurants_open(self): 
        """Definition: returns a list of restaurants that are open at the time of order"""
        
        #create empty set to store open restaurants
        open_restaurants = set()
        
        #check each restaurant in restaurants dictionary
        for key in restaurants:
            #if today is in the list of days open
            if self.current_day in restaurants[key]['Days of Week Open']:   
                if restaurants[key]['Open Time'] < restaurants[key]['Close Time'] == True:
                    #if current time is during open hours
                    if self.current_time >= restaurants[key]['Open Time'] and self.current_time <= restaurants[key]['Close Time'] == True:
                        open_restaurants.add(key)
                else:
                    #Below executes if the time frame spans across midnight
                    if self.current_time >= restaurants[key]['Open Time'] or self.current_time <= restaurants[key]['Close Time'] == True:
                        open_restaurants.add(key)
                        
        return open_restaurants
    
    
    
    def restaurants_food_pref(self):
        """Definition: Returns list of restaurants that match food preference selection"""
        
        food_pref_restaurants = set()
        
        for key in restaurants:
            if self.food_pref in restaurants[key]['Food Categories']:
                food_pref_restaurants.add(key)
                
        return food_pref_restaurants
    
    
    def restaurants_close_by(self):
        """Definition: Returns list of restaurants that match neighborhood selected"""
        
        local_restaurants = set()
        
        for key in restaurants:
            if self.location in restaurants[key]['Location']:
                local_restaurants.add(key)
                
        return local_restaurants
                
    
        
#create an empty set for all possible food categories and food locations      
all_food_categories = set()

all_food_locations = set()



#add food categories to the set to use for the 1st user prompt 
for key in restaurants:
    for category in restaurants[key]['Food Categories']:
        all_food_categories.add(category)

#add location categories to the set to use for the 2nd user prompt
for key in restaurants:
    all_food_locations.add(restaurants[key]['Location'])


while True:
    
    print("Welcome to Hub of Grub! Please select what kind of food you're interested in:")
    
    num = 1 
    
    #print all food categories for user to select
    for x in all_food_categories:
        print("{0} - {1}".format(num,x))
        num += 1
        
    #if user inputs a non-digit or a number that isn't in the menu they will return 
    try:
        val1 = int(input("Enter selected number here:"))
    except Exception:
        print("That is not a valid number. Please try again.\n")
        continue

    if val1 > num-1 or val1 < 1:
        print("\n{} is not available in the menu. Please try again.".format(val1))
        continue
    
    break




while True:
    print("Please select where you are located:")
    
    count = 1
    
    for x in all_food_locations:
        print("{0} - {1}".format(count,x))
        count += 1
    
    #if user inputs a non-digit or a number that isn't in the menu they will return
    try:
        val2 = int(input("Enter selected number here:"))
    except Exception:
        print("That is not a valid number. Please try again.\n")
        continue
    
    if val2 > count-1 or val2 < 1:
        print("\n{} is not available in the menu. Please try again.".format(val2))
        continue

    break





#convert the sets to list so you can index them using the prompt values
foodpref = list(all_food_categories)

locations = list(all_food_locations)


order = hubGrubOrder(locations[val2-1],foodpref[val1-1])

#intersection of sets for restaurants close by, matching food pref and are open
results = order.restaurants_close_by().intersection(order.restaurants_food_pref(),order.restaurants_open())

print("\nBased on your location and food preferences, the following restaurants are open and ready to order from:\
       \n","-"*40)

#prints recommended restaurants or apologizes if no restaurant is returned
if len(results) == 0:
    print("I'm sorry! We could not find a restaurant currently open for your food preference and location.")
else:
    for x in results:
        print("\n{0} : {1}".format(x,restaurants[x]['Desc']))

