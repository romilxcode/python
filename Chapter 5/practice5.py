#Try to add both integer 9 and float 9.0 to a set and observe the result.

numberSet = set()
numberSet.add(9)
numberSet.add(9.0)
print("Set after adding 9 and 9.0:", numberSet)

# Observation: Both 9 and 9.0 are considered the same in a set, as sets do not allow duplicate values.