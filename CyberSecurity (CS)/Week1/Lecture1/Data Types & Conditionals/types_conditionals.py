"""
discount - to calculate the price after discount
tax      - to calculate the final price after tax

Enter either “discount” or “tax” from the menu above to proceed: discount

Enter the original price of the product: 100
Enter the discount percentage: 20

The price after a 20% discount is: 80.0

**EXTRA:
    - Colour the output in green for Discount
    - Colour the output in red for Tax
"""

BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"

BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"

# Menu
menu = "discount - to calculate the price after discount \
\ntax      - to calculate the final price after tax"
print(menu)

user_input = input("Enter either “discount” or “tax” from the menu above to proceed: ")
total = None

if user_input.casefold() == "tax":
    amount = int(input("What is the total amount?"))
    tax = int(input("Enter the tax amount in the form of a percentage (%): ")) 
    total = amount + (amount * tax/100)
    print(f"{BOLD}Your total after tax:{END} {RED}{total}{END}")

else:
    amount = int(input("What is the total amount? "))
    discount = int(input("Enter the discount to be applied in the form of a percentage (%): "))
    total = amount - (amount * discount/100)
    print(BOLD + "Your total after the discount: " + END + GREEN + str(total) + END)
