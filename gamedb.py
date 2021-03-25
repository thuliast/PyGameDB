"""
GameDB. A platform to manage video games and platforms

Author: Francesco Tattoli
Creation Date: 15-03-2021
"""
import sqlite3
import sys
from prettytable import PrettyTable
from prettytable import from_db_cursor

#Create SQLite3 connection and cursor
con = sqlite3.Connection(".\GamesDB.sqlite")


def gameinsert():
    #Choice #1 of the main menu. Inserting a new game into the library
    print("-" * 40)
    print(" INSERTING A NEW GAME ")
    print("-" * 40)
    #Gathering data to store in the Library
    gamename = input("Game Name: ")
    platform1 = input("First Platform Name: ")
    platform2 = input("Second Platform Name: ")
    platform3 = input("Third Platform Name: ")
    platform4 = input("Fourth Platform Name: ")
    platform5 = input("Fifth Platform Name: ")
    metascore = input("Metascore: ")
    #If user chooses not to input a Metascore a default of 0 is assigned
    if metascore == "":
        metascore = "0"
    #Prompt the user to select whether it's a DLC entry or not. For future printing
    isdlc = input("Is a DLC (Y/N) ? Default (N): ")
    #By default, if user doesn't type anything at the DLC prompt, default N is assumed
    if isdlc == "":
        isdlc = "N"

    #All done. Let's save data into db
    try:
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO GameLibrary(GameName, PlatformName1, PlatformName2, PlatformName3, PlatformName4, PlatformName5, Metascore,IsDLC) \
                        VALUES(?,?,?,?,?,?,?,?)", (gamename, platform1, platform2, platform3, platform4, platform5, metascore, isdlc))
            con.commit()
            print("All done.")
            print("Do you want to insert another game (y/Y) or exit to main menu (n/N)")
            choice = input("Y/N :")
            if choice == "Y" or choice == "y":
                gameinsert()
            else:
                main()
    except sqlite3.Error as e:
        print("Database Error. {}".format(e))
        main()


def platforminsert():
    #Choice #2 of the main menu. Inserting a new platform with details into the library
    #Pretty similar to function #1. NO PASSWORD WILL BE STORED (EVER).
    #This is just to recall which game on which platform user own games
    print("-" * 40)
    print(" INSERTING A NEW PLATFORM ")
    print("-" * 40)
    #Gathering data to store in the DB    
    platformname = input("Platform Name: ")
    platformaccount = input("Platform Account Name: ")
    
    #All done. Let's save data into db
    try:
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO PlatformDetails(PlatformName, PlatformAccount) \
                        VALUES(?,?)", (platformname, platformaccount))
            con.commit()
            print("All done.")
            print("Do you want to insert another platform (y/Y) or exit to main menu (n/N)")
            choice = input("Y/N :")
            if choice == "Y" or choice == "y":
                platforminsert()
            else:
                main()
    except sqlite3.Error as e:
        print("Database Error. {}".format(e))
        main()


def printgamesdb():
    #Choice #3 of the main menu. Printing games library ordered by Platform
    print("-" * 40)
    print(" PRINTING GAMES LIBRARY ")
    print(" Ordered by Platform Name")
    print("-" * 40)
    
    with con:
        cur = con.cursor()
        #Prompt the user whether wants to include DLCs in the report
        includedlc = input("Do you want to include DLCs in the report (Y/N)?: ")
        if includedlc == "y" or includedlc == "Y":
            stringsql = ("SELECT * FROM GameLibrary ORDER By PlatformName1")
            cur.execute(stringsql)
        elif includedlc == "n" or includedlc == "N":
            stringsql = ("SELECT * FROM GameLibrary WHERE IsDLC = 'n' or IsDLC = 'Y' ORDER BY PlatformName1")
            cur.execute(stringsql)
        else:
            print("Unrecognized choice.")
            printgamesdb()
        tb = from_db_cursor(cur)
    tb.field_names = ["Game ID","Game Name","Platform #1","Platform #2","Platform #3","Platform #4","Platform #5","Metascore", "DLC"]
    tb.align["Metascore"] = "r"
    print(tb.get_string(title="Your Games Library ordered by Platform"))
    _ = input("Press a key to exit")
    main()


def printplatformdb():
    #Choice #4 of the main menu. Printing platform details
    print("-" * 40)
    print(" PRINTING PLATFORM LIBRARY ")
    print("   AND ACCOUNT DETAILS   ")
    print("-" * 40)
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM PlatformDetails")
        tb = from_db_cursor(cur)
    tb.field_names = ["Platform", "Account Name"]
    print(tb.get_string(title="Your Platform Library with Account Details"))
    _ = input("Press a key to exit")
    main()


def searchgamebyname():
    print("-" * 40)
    print(" SEARCH GAME BY ITS NAME ")
    print("-" * 40)
    gamename = input("Type some character of the game you want to search: ")
    if gamename == "":  #Nothing typed. Showing the whole game library
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM GameLibrary")
            tb = from_db_cursor(cur)
        tb.field_names = ["Game ID","Game Name","Platform #1","Platform #2","Platform #3","Platform #4","Platform #5","Metascore", "DLC"]
        tb.align["Metascore"] = "r"
        print(tb.get_string(title="Games Found"))
        _ = input("Press a key to exit")
        main()
    else:
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM GameLibrary WHERE GameName LIKE ?", ('%{}%'.format(gamename),))
            tb = from_db_cursor(cur)
        tb.field_names = ["Game ID","Game Name","Platform #1","Platform #2","Platform #3","Platform #4","Platform #5","Metascore", "DLC"]
        tb.align["Metascore"] = "r"
        print(tb.get_string(title="Games Found"))
        _ = input("Press a key to exit")
        main()


def searchplatformbyname():
    print("-" * 40)
    print(" SEARCH PLATFORM BY ITS NAME ")
    print("-" * 40)
    platformname = input("Type some character of the platform you want to search: ")
    if platformname == "":  #Nothing typed. Showing the whole platform library
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM PlatformDetails")
            tb = from_db_cursor(cur)
        tb.field_names = ["Platform Name", "Platform Account"]
        print(tb.get_string(title="Match(es) Found"))
        _ = input("Press a key to exit")
        main()
    else:
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM PlatformDetails WHERE PlatformName LIKE ?", ('%{}%'.format(platformname),))
            tb = from_db_cursor(cur)
        tb.field_names = ["Platform Name", "Platform Account"]
        print(tb.get_string(title="Match(es) Found"))
        _ = input("Press a key to exit")
        main()


def main():
    print("-" * 40)
    print("     THE GAMES LIBRARY     ")
    print("-" * 40)
    mainchoice = ["1", "2", "3", "4", "5", "6", "9"]  #List containing all the valid menu entries
    print("SELECT FUNCTION:")
    print("1 - Insert a Game")
    print("2 - Insert a Platform/Account")
    print("3 - Print Games Library")
    print("4 - Print Platform Details")
    print("5 - Search Game by Name")
    print("6 - Search Platform by Name")
    print("9 - Exit")
    mychoice = input("Choose a function :")
    if mychoice in mainchoice:
        if mychoice == "1":
            #User chose to insert a new game into the library
            gameinsert()
        elif mychoice == "2":
            #User chose to insert a new platform and account details
            platforminsert()
        elif mychoice == "3":
            #User chose to print Games Library
            printgamesdb()
        elif mychoice == "4":
            #User chose to print Platform Library
            printplatformdb()
        elif mychoice == "5":
            #User chose to search a Game by its name
            searchgamebyname()
        elif mychoice == "6":
            #User chose to search a Platform and its details by Platform name
            searchplatformbyname()
        elif mychoice == "9":
            #User chose to exit the application
            sys.exit()    
        else:
            #Unidentified command. Sending user back to main menu
            print("Unrecognized function.")
            main()
        

if __name__ == "__main__":
    main()