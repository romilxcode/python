#Ask the user for their 3 favourite movies and store them in a list.

# movies= input ("Enter your 3 favourite movies: ")
# movie_list= movies.split(", ")
# print("Your favourite movies are: ", movie_list)
# print("Total number of movies you entered: ", len(movie_list))
# print("Second movie in your list: ", movie_list[1])
# print("Last movie in your list: ", movie_list[-1])
# print(movie_list)

#1st way:

# movies = input("Enter your 3 favourite movies: ")
# movie_list = movies.split(", ")

# print("Your favourite movies are:", movie_list)
# print("Total number of movies you entered:", len(movie_list))
# print("Second movie in your list:", movie_list[1])
# print("Last movie in your list:", movie_list[-1])
# print(movie_list)

#2nd way (using if else):

while True:
    movies = input("Enter your 3 favourite movies (separated by commas): ")
    movie_list = [m.strip() for m in movies.split(",")]

    if len(movie_list) == 3:
        break
    else:
        print("Please enter exactly 3 movies.\n")

print("Your favourite movies are:", movie_list)
print("Total number of movies you entered:", len(movie_list))
print("First movie in your list:", movie_list[0])
print("Second movie in your list:", movie_list[1])
print("Last movie in your list:", movie_list[-1])
print(movie_list)
