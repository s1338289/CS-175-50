repeat = False
while repeat == True:
    vegetarian=input("Is anyone in your party a vegetarian?")

if vegetarian == "yes" or vegetarian == "no":
    vegan= input("Is anyone in your party a vegan?")

    if vegan== "yes" or vegan == "no":
            gluten_free = input("is anyone in your party gluten-free?")

print("Here are your restaurant choices.")

if vegetarian =="no" and vegan == "no" and gluten_free == "no":
    print("Mamas Fine Italian","Corners Cafe","Main Street Pizza Company","The Chefs Kitchen","Joes Gourmet Burgers")
                                
if vegetarian == "yes" and vegan== "no" and gluten_free=="no":
 print("Mamas Fine Italian","Corners Cafe","Main Street Pizza Company","The Chefs Kitchen")

if vegetarian == "yes" and vegan == "yes" and gluten_free=="no":
       print ("Corners Cafe","Chefs Kitchen")

if vegetarian == "yes" and vegan=="yes" and gluten_free=="yes":
       print ("Corners Cafe","Chefs Kitchen")

if vegan == "yes" and vegetarian == "no" and gluten_free=="no":
       print("Corners Cafe","Chefs Kitchen")

if vegan == "yes" and gluten_free=="yes" and vegetarian =="no":
       print ("Corners Cafe","Chefs Kitchen")

if gluten_free=="yes" and vegetarian=="no" and vegan=="no":
       print("Main Street Pizza Company","Corners Cafe","Chefs Kitchen")

if gluten_free == "yes" and vegetarian =="yes" and gluten_free=="no":
       print ("Main Street Pizza Company","Corners Cafe","Chefs Kitchen")
repeat=False
print("I'm done with this loop")
       
             
           
        




