FILENAME = "bars.txt"

def write_bars(bars):
    with open(FILENAME, "w") as file:
        for bar in bars:
            file.write(bar + "\n")

def read_bars():
    bars = []
    with open(FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            bars.append(line)
        return bars

def list_bars(bars):
    for i in range(len(bars)):
        bar = bars[i]
        print(str(i+1) + ". " + bar)
    print()

def add_bar(bars):
    bar = input("Bar Name: ")
    bars.append(bar)
    write_bars(bars)
    print(bar + " was added.\n")

def delete_bar(bars):
    index = int(input("Number: "))
    bar = bars.pop(index - 1)
    write_bars(bars)
    print(bar + " was deleted.\n")

def display_menu():
    print("The Bar List Program")
    print()
    print("COMMAND MENU")
    print("list - List all Bars")
    print("add  -  Add a Bar")
    print("del  - Delete a Bar")
    print("exit - Exit program")
    print()

def main():
    display_menu()
    bars = read_bars()
    while True:
        command = input("Command: ")
        if command == "list":
            list_bars(bars)
        elif command == "add":
            add_bar(bars)
        elif command == "del":
            delete_bar(bars)
        elif command == "exit":
            print("Later Jabroni!")
            break
        else:
            print("Not a valid command. Please try again jabroni.")

if __name__ == "__main__":
    main()
    
