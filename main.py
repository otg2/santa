
import random
import copy

# TODO:
# Try out shuffled list and point to next item

#names = ["Ottar  ", "Magnus ", "Knutur ", "Vidar  ", "Atli   ", "Kriss  ", "David  ", "Hrodmar", "Gunnar ", "Petur  ", "Erling"]
names = ["Ottar  ", "Magnus ", "Knutur ", "Vidar  ", "Atli   ", "Gunnar ", "Petur  ", "Erling"]
"""
names = ["Alma",
"Arna",
"Arnar",
"Auður",
"Ágústa",
"Ásta",
"Baldur",
"Belinda",
"Birna",
"Daði",
"Einar",
"Elísabet",
"Erla",
"Erna",
"Guðrún",
"Hafdís",
"Helga",
"Herdís",
"Hólmfríður",
"Jóhanna",
"Malen",
"María",
"Matja",
"Nína",
"Ragnar",
"Sigrún",
"Sigurður",
"Sigþrúður",
"Valgerður"]
"""
#names = ["Auður", "Andrea", "Aðalheiður", "Anna Katrín", "Hildur","Inga"]
leynivin = copy.copy(names) 

random.shuffle(names)
random.shuffle(leynivin)

increment = 0 
isComplete = False


while isComplete == False:
  increment += 1
  random.shuffle(names)
  random.shuffle(leynivin)

  isComplete = True;
  
  for i in range(len(names)):
    if(names[i] == leynivin[i]):
      isComplete = False;
       
  for i in range(len(names)):
    firstLink = names[i]
    secondLink = leynivin[i]
    
    indexOfA = names.index(secondLink)
    if leynivin[indexOfA] == firstLink:
      isComplete = False;
	
for i in range(len(names)):  
  f = open("names/Jolavinur2022_"+names[i]+".txt", "a")
  f.write(leynivin[i])
  f.close()

print(increment)
print(names)
print(leynivin)