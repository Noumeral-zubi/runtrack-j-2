def print_fruits_or_veggies(type, season):
      if type == "fruits" and season == "hiver":
    print("orange, mandarine et kiwi")
  elif type == "fruits" and season == "été":
    print("Poire, fraise, cassis")
  elif type == "légume" and season == "hiver":
    print("carotte, topinambour, endive")
  elif type == "légume" and season == "été":
    print("artichaut, aubergine,navet")
  else:
    print("Type ou saison non reconnu")

# Appel de la fonction avec différents paramètres
print_fruits_or_veggies("fruits", "hiver")
print_fruits_or_veggies("fruits", "été")
print_fruits_or_veggies("légume", "hiver")
print_fruits_or_veggies("légume", "été")
print_fruits_or_veggies("fruits", "printemps")
