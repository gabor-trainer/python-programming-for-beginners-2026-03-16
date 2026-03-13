import json
import msvcrt

user_input = None
top_n = None
root = {}
customers = []
input_file = "customers.json"
output_file = "top_customers.json"

while True:
    try:
        if not root:
            with open(input_file, "r", encoding="utf-8") as f:
                root = json.load(f)
                customers = root.get("customers", [])
        user_input = input(
            f"Enter a integer number for top n customers: (0-{len(customers)}): ")
        top_n = int(user_input)
        if top_n < 0 or top_n > len(customers):
            print(
                f"Number must be between 0 and {len(customers)} and you entered {top_n}")
            continue
        break
    except ValueError:
        print(f"Invalid number {user_input}")
    except FileNotFoundError:
        print(f"File not found: {input_file} from the current directory")
        # wait for the user to fix the problem and try again, press any key to continue
        print("Press any key to continue...")
        msvcrt.getch()
    # except IOError:
    #     print("File not found")

# business logig: woring with the number
print(f"Number was: {top_n}")
top_n_customers = customers[:top_n]
top_n_root = {
    "customers": top_n_customers
}

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(top_n_root, f, indent=4)
print(f"Top {top_n} customers were written to {output_file}")
