import sys 
import json 
from datetime import datetime

def main():
    if len(sys.argv) < 2:
        print("usage: task [add|list|done|delete] [args]")
        return
    
    command = sys.argv[1]

    if command == "add":
        pass
    elif command == "list":
        pass
    elif command == "done":
        pass
    elif command == "delete":
        pass
    else:
        print("unkown command: ", command)



if __name__ == "__main__":
    main()

