def PVZ(zombies, plants):
  
    zombies_strength = sum(zombies)
    plants_strength = sum(plants)
    
   
    if zombies_strength > plants_strength:
        return False
    elif zombies_strength < plants_strength:
        return True
    else:
       
        if len(zombies) > len(plants):
            return False
        elif len(zombies) < len(plants):
            return True
        else:
            return True


zombies1 = [1, 3, 5, 7]
plants1 = [2, 4, 6, 8]
print(PVZ(zombies1, plants1)) 

zombies2 = [1, 3, 5, 7]
plants2 = [2, 4]
print(PVZ(zombies2, plants2))  

zombies3 = [1, 3, 5, 7]
plants3 = [2, 4, 0, 8]
print(PVZ(zombies3, plants3)) 

zombies4 = [2, 1, 1, 1]
plants4 = [1, 2, 1, 1]
print(PVZ(zombies4, plants4))  
