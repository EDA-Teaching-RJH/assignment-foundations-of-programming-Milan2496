n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0
    while loading < 5:
        print("Loading module " + str(loading))
        
        
        while True:
            print("\n--- MENU ---")
            print("1. View Crew")
            print("2. Add Crew")
            print("3. Remove Crew")
            print("4. Analyze Data")
            print("5. Exit")
        
            opt = input("Select option: ")
        
            if opt == "1":  
                print("Current Crew List:")
            
                for i in range(len(n)):
                    print(n[i] + " - " + r[i])
                
            elif opt == "2":
                new_name = input("Name: ")
                new_rank = input("Rank: ")
                new_div = input("Division: ")
            
           
                n.append(new_name)
                r.append(new_rank)
                d.append(new_div)

                print("Crew member added.")
            
            elif opt == "3":
                rem = input("Name to remove: ")

                if rem in n:
           
                    idx = n.index(rem)
                    n.pop(idx)
                    r.pop(idx)
                    d.pop(idx)
                    print("Removed.")
                else:
                    print("Name not found")
            
            elif opt == "4":
                print("Analyzing...")
                count = 0
            
                for rank in r:
                    if rank == "Captain" or rank == "Commander": 
                        count = count + 1
                print(f"High ranking officers: {count} ") 
            
            elif opt == "5":
                print("Shutting down.")
                return
            
            else:
                print("Invalid.")
            
        
            x = 10
            if x > 5:
                print("System Check OK")
            else:
                print("System Failure")
            
       
            if len(n) > 0:
                print("Database has entries.")
            if len(n) == 0:
                print("Database empty.")

        
        fuel = 100
        consumption = 0
        while fuel > 0:
            
            print("Idling...")
            break 
            
        print("End of cycle.")

run_system_monolith()

#10 distinct bugs
#add brackets to run_system_monolith
#change = to == in the if statement
#stop the infinte while loop and change break to return
#replace range(10) with range(len(n))
#add r.append and d.append to create a new crew member because otherwise the for loop will crash
#change print line to allow both integers and strings to be printed
#in an if statement with two options to be true then the code must be written as variable == (word) for both options
#add an if statement for removing name because the code will crash with the wrong name inputted