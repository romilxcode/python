food= {"paneer", "chole bathure", "sandwitch", "golgappe"} # ✅
# food= {"paneer", "chole bathure", "sandwitch", "golgappe", "paneer"} ❌
print(type(food))
print(food)
food.add("Kunafa")
print(food)
food.remove("chole bathure")
print(food)
#sets do not allow duplicate values.

emptySet= set()
print(type(emptySet))