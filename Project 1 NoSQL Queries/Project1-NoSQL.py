#!/usr/bin/env python
# coding: utf-8

# In[41]:


from unqlite import UnQLite
db = UnQLite('sample.db')
data = db.collection('data')


# In[45]:


import math
# Graded Cell, PartID: o1flK
def FindBusinessBasedOnCity(cityToSearch,saveLocation1,collection):
    d = collection.filter(lambda obj: obj['city'] == cityToSearch)
    f = open(saveLocation1, 'w')
    for bus in d: 
        txt = bus['name']+ "$" + bus['full_address']+"$" + bus['city'] + "$" + bus ['state']+ "\n"
        f.write(txt)
    f.close()
    

def FindBusinessBasedOnLocation(categoriesToSearch, myLocation, maxDistance, saveLocation2, collection):
    f = open(saveLocation2, 'w')
    for destination in collection:
        if(dist(myLocation[0], myLocation[1], destination['latitude'],destination['longitude']) < maxDistance):
            l = []
            for de in destination['categories']: 
                l.append(de)
            if categoriesToSearch[0] in l: 
                result = destination['name']
                f.write(result)
    f.close()
                
def dist(lat2, lon2, lat1, lon1): 
    R = 3959
    o1 = math.radians(lat1)
    o2 = math.radians(lat2)
    do = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    h = math.sin(do/2)*math.sin(do/2) + math.cos(o1) * math.cos(o2) * math.sin(dl/2) * math.sin(dl/2)
    c = 2* math.atan2(math.sqrt(h), math.sqrt(1-h))
    distance = R * c
    return distance


# In[46]:


true_results = ["VinciTorio's Restaurant$1835 E Elliot Rd, Ste C109, Tempe, AZ 85284$Tempe$AZ", "P.croissants$7520 S Rural Rd, Tempe, AZ 85283$Tempe$AZ", "Salt Creek Home$1725 W Ruby Dr, Tempe, AZ 85284$Tempe$AZ"]

try:
    FindBusinessBasedOnCity('Tempe', 'output_city.txt', data)
except NameError as e:
    print ('The FindBusinessBasedOnCity function is not defined! You must run the cell containing the function before running this evaluation cell.')
except TypeError as e:
    print ("The FindBusinessBasedOnCity function is supposed to accept three arguments. Yours does not!")
    
try:
    opf = open('output_city.txt', 'r')
except FileNotFoundError as e:
    print ("The FindBusinessBasedOnCity function does not write data to the correct location.")
    
lines = opf.readlines()
if len(lines) != 3:
    print ("The FindBusinessBasedOnCity function does not find the correct number of results, should be 3.")
    
lines = [line.strip() for line in lines]
if sorted(lines) == sorted(true_results):
    print ("Correct! You FindBusinessByCity function passes these test cases. This does not cover all possible test edge cases, however, so make sure that your function covers them before submitting!")


# In[47]:


true_results = ["VinciTorio's Restaurant"]

try:
    FindBusinessBasedOnLocation(['Buffets'], [33.3482589, -111.9088346], 10, 'output_loc.txt', data)
except NameError as e: 
    print ('The FindBusinessBasedOnLocation function is not defined! You must run the cell containing the function before running this evaluation cell.')
except TypeError as e:
    print ("The FindBusinessBasedOnLocation function is supposed to accept five arguments. Yours does not!")
    
try:
    opf = open('output_loc.txt','r')
except FileNotFoundError as e:
    print ("The FindBusinessBasedOnLocation function does not write data to the correct location.")

lines = opf.readlines()
if len(lines) != 1:
    print ("The FindBusinessBasedOnLocation function does not find the correct number of results, should be only 1.")

if lines[0].strip() == true_results[0]:
    print ("Correct! Your FindBusinessBasedOnLocation function passes these test cases. This does not cover all possible edge cases, so make sure your function does before submitting.")


# In[ ]:





# In[ ]:




