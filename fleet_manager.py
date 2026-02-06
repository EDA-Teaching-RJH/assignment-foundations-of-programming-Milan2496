n = ["Picard", "Riker", "Data", "Worf", "La Forge"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant Commander"]
d = ["Command", "Command", "Operations", "Security", "Engineering"]
id = ["SF-1701-A", "SF-1701-B", "SF-1701-C", "SF-1701-D", "SF-1701-E" ]


def init_database():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")

    print("\nCurrent Crew List:")           
    for i in range(len(n)):
        print( n[i] + " - " + r[i] + " - " + d[i] + " - " + id[i])





def main():
    init_database()



main()


