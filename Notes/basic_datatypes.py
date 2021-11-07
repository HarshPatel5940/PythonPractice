# LIST

List = \
"""
Methods:
    list(my_list)                       is also used to copy original list
    .append                             to add item in the list at the end of the list
    .extend                             to add multiple values
    .insert(1, "chocolate")             to add a value at a specific position
    .pop(INX)                           to remove value using index value
    .remove("anything")                 to remove a value using value itself
    .clear()                            to clear list
    .sort()                             to sort the list
    .reverse()                          to copy original list to new list
    .del()                              to delete whole list
    .copy()                             to copy whole list
    .count("anything")                  to count the number of times a value is present in the list
    .index("anything")                  to get the index of a value
    .join(my_list)                      to join all the values in the list
    .split(my_list)                     to split a string into a list
    
"""

# TUPLES

Tuples = \
"""
Methods:
    tuple(list)     to convert list to tuple
    .count()        to count the value in the tuple
    .index()        to give the index of the value
    .sort()         to sort the tuple
    .reverse()      to copy original tuple to new tuple
    .del()          to delete whole tuple
    .copy()         to copy whole tuple


--> Note :  We can concatenate tuples other operations are not allowed

    tuple is an immutable object...it takes less space than list and also less time to run.
    tuple helps us when handling large data bases by python
"""
# Dictionary

Dictionary = \
"""
Methods:
    dict(my_dict)                          Function to create dictionaries, also Used for copying
    my_dict["email"] = "ABc@xYZ.com"       to add new values to dictionary and also to overwrite existing values
    del my_dict["name"]                    to delete existing values
    my_dict.pop("age")                     to delete existing values too
    dic1.update(dic2)                      to Concatenate 2 dictionaries
    .keys()                                to get all the keys in dictionary
    .values()                              to get all the Values in dictionary
    .items()                               to get all the Items in dictionary
    .copy()                                to copy dictionaries
    .update                                to add dictionaries dictionaries
    .clear()                               to clear dictionary
    .get()                                 to get value from dictionary
    .setdefault()                          to add value to dictionary if not present
    .pop()                                 to remove value from dictionary
    .popitem()                             to remove random value from dictionary
    .fromkeys()                            to create dictionary from list

    --> Note :  We can concatenate dictionaries other operations are not allowed
    for values in my_dict.values():                  |  values are stored
        print(values)                                |  
    for keys in my_dict.keys():                      |  looping values in dictionaries
        print(keys)                                  |  keys are the object in which values are stored
    for key, values in my_dict.items():              |  
        print(key, ":", values)                      |  key and values are used with .items to loop
    -------------------------------------------------|  
    ____________________________________________________________________________________________________________
    try:                              |
        if statement                  |  to check whether the value is stored in dictionary or not
    except:                           | 
        else statement                |
    __________________________________|_________________________________________________________________________
"""

# SETS

Sets = \
"""
    {}                                to make sets no repeating of characters is allowed here.
    set(["hello"])                    is also used to make null sets
    .add()                            to add something
    .discard()                        to remove something
    .clear()                          to clear the set characters
    set1.union(set2)                  to combine two sets
    set1.intersection(set2)           to get the common between two sets
    set1.difference(set2)             to get difference between the sets 
    set1.issuperset(set2)             to check it is a super set or not 
    set1.issubset(set2)               to check it is a sub set or not
    set1.symmetric_difference(set2)   to get the symmetric difference between two sets
    set1.copy()                       to copy the set
    set1.update()                     to update the set
    set1.pop()                        to remove random value from set
    set1.remove()                     to remove value from set
    set1.intersection_update()        to update the set with common values
    set1.difference_update()          to update the set with difference values
    set1.symmetric_difference_update()to update the set with symmetric difference values
    set1.issuperset()                 to check it is a super set or not
    set1.issubset()                   to check it is a sub set or not
    set1.isdisjoint()                 to check it is a disjoint set or not
    set1.union()                      to combine two sets
    set1.intersection()               to get the common between two sets
    set1.difference()                 to get difference between the sets
    set1.symmetric_difference()       to get the symmetric difference between two sets
    
"""

print(List, "\n\n =================================================================\n\n")
print(Tuples, "\n\n =================================================================\n\n")
print(Dictionary, "\n\n =================================================================\n\n")
print(Sets, "\n\n =================================================================\n\n")