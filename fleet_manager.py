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

def display_menu():
    name = input("\nWhat is your full name? ")
    print("USER " + name + " HAS LOGGED IN...")

    print("\n--- MENU ---")
    print("1. Add Member")
    print("2. Remove Member")
    print("3. Update Rank")
    print("4. Display Roster")
    print("5. Search Crew")
    print("6. Filter by Division")
    print("7. Calculate Payroll")
    print("8. Count Officers")

    opt = int(input("Select option: "))
    return opt





def main():
    init_database()
    opt = display_menu()

    if opt == 1:
        print("hello")




main()


