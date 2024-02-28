Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Program name: Popular Movies by Year
# Program Author: Stephen Sutton
# Program Objective: Provide the most popular movie for a given year
# ----------------------------------------------------------------------

# Pseudocode:
# 1. Define the variable.
#    a. Request the year
#    b. Define the limits of the year
# 2. Define the most popular movie.
#    a. Define the movie based on the input year
# ----------------------------------------------------------------------

# Input: Year
# Output: Most popular movie

# Get the year input from the user
year = int(input('Year: '))

# Define the most popular movies for each year
popular_movies = {
    1964: "My Fair Lady",
    1965: "For a Few Dollars More",
    1966: "Balthazar",
    1967: "Cool Hand Luke",
    1968: "2001: A Space Odyssey",
    1969: "Midnight Cowboy",
    1970: "Patton",
    1971: "A Clockwork Orange",
    1972: "The Godfather",
    1973: "The Exorcist",  
    1974: "The Godfather Part II",  
    1975: "Monty Python and the Holy Grail",
    1976: "The Message",
    1977: "The Girl with the Red Scarf",
    1978: "Halloween",
    1979: "Alien",
    1980: "Star Wars: Episode V - The Empire Strikes Back",
    1981: "The Boat",
    1982: "The Thing",
    1983: "Star Wars: Episode VI - Return of the Jedi",
    1984: "The Terminator",
    1985: "Back to the Future",
    1986: "Aliens",
    1987: "The Princess Bride",
    1988: "Grave of the Fireflies",
    1989: "Dead Poets Society",
    1990: "The Godfather Part III",
    1991: "Terminator 2: Judgment Day",
    1992: "Unforgiven",
...     1993: "Schindler's List",
...     1994: "Forrest Gump",
...     1995: "Braveheart",
...     1996: "The Bandit",
...     1997: "Titanic",
...     1998: "The Truman Show",
...     1999: "The Matrix",
...     2000: "Gladiator",
...     2001: "The Lord of the Rings: The Fellowship of the Ring",
...     2002: "The Lord of the Rings: The Two Towers",
...     2003: "The Lord of the Rings: The Return of the King",
...     2004: "The Notebook",
...     2005: "My Father and My Son",
...     2006: "Pan's Labyrinth",
...     2007: "No Country for Old Men",
...     2008: "WALL·E",
...     2009: "Hachi: A Dog's Tale",
...     2010: "Inception",
...     2011: "The Help",
...     2012: "Django Unchained",
...     2013: "12 Years a Slave",
...     2014: "Interstellar",
...     2015: "Mad Max: Fury Road",
...     2016: "Your Name.",
...     2017: "Coco",
...     2018: "Avengers: Infinity War",
...     2019: "Avengers: Endgame",
...     2020: "Tenet",
...     2021: "Spider-Man: No Way Home",
...     2022: "Everything Everywhere All at Once",
...     2023: "Oppenheimer"
... }
... 
... # Check if the year is in the dictionary, and print the corresponding movie
... if year in popular_movies:
...     print(f"The most popular movie in {year} was: {popular_movies[year]}")
... else:
...     print("Movie data not available for the specified year.")
... 
