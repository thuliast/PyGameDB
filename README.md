# PyGameDB

A simple Videogames Database in Python

1. Installation and setup.
Requirements: Python 3.8+ 32/64 bit
From pip install prettytable

2. Usage
From terminal/command prompt/powershell, type:
python gamedb.py

The script consist in a main menu with 7 voices, which are:
1. Inserting a new game into the library
2. Inserting a new platform for games (eg. Steam, Origin, etc.)
3. Printing the whole games library (With option to include/exclude DLCs)
4. Printing the whole platform library
5. Searching a Game by its name
6. Searching a Platform by its name
9. Exiting to prompt

1. Inserting a new game into the library
This option prompts the user to insert a new video game in the library by typing its name, and up to 5 Platform where user
owns the game (eg. Platform #1: Steam, Platform #2: Epic, etc) and after typing the platforms user has the ability to flag
the entry as DLC or not, and to assing a Metascore

2. Insertin a new platform into the library
This option prompts the user to insert a new platform in the library by typing its name and username. NO PASSWORD IS REQUIRED
AND EVEN IN FUTURE UPDATES PASSWORD WILL BE CYPHERED AND NEVER SHARED ON THE INTERNET

3. Printing the whole games library
This option prints the whole games library with the option to include or exclude DLCs from the list. The list is ordered by
the first platform entered

4. Printing platform details
This option print the whole platforms library. Future updates will prompt the user to choose whether to show passwords or not

5. Searching a game by its name
This option prompts the user to type the game (or some part of it) to search and print on screen the results

6. Searching a platform by its name
This option prompts the user to type the platform name (eg. Steam) and the program will print on screen the corresponding platform
details. Future updates will prompr the user whether to show passwords or not

9. Exiting
This option quits the program and exits back to the command prompt
