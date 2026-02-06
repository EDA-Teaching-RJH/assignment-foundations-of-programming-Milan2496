n = ["Picard", "Riker", "Data", "Worf", "La Forge"]
r = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Lieutenant Commander"]
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
    opt = int(input("\nSelect option: "))
    return opt

def add_member(n, r, d, id):
    rank = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant"]
    new_name = input("Name: ")
    new_rank = input("Rank: ")
    new_rank = new_rank.title()
    while new_rank not in rank:
        new_rank = input("This is not a valid TNG Rank. Please enter a valid Rank: ")
        new_rank = new_rank.title()
    new_div = input("Division: ")   
    new_id = input("ID: ")      
    while new_id in id:
        new_id = input("This is not a unique ID. Please enter a unique ID: ")
    n.append(new_name)
    r.append(new_rank)
    d.append(new_div)
    id.append(new_id)
    print("\nUpdated Crew List:")
    for i in range(len(n)):
            print( n[i] + " - " + r[i] + " - " + d[i] + " - " + id[i])
    return n, r, d, id


def remove_members(n, r, d, id):
    rem = input("Name to remove: ")
    if rem in n:           
        idx = n.index(rem)
        n.pop(idx)
        r.pop(idx)
        d.pop(idx)
        id.pop(idx)
        print("Crew member removed")
    else:
        print("Name not found")
    print("\nUpdated Crew List:")
    for i in range(len(n)):
            print( n[i] + " - " + r[i] + " - " + d[i] + " - " + id[i])
    return n, r, d, id


def main():
    init_database()
    opt = display_menu()

    if opt == 1:
        add_member(n, r, d, id)

    elif opt == 2:
        remove_members(n, r, d, id)
        
        


        


main()


