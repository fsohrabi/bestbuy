import sys
from products import Product
from store import Store


def start(best_buy):
    store_menu = """
        Store Menu
        ----------
    1. List all products in store
    2. Show total amount in store
    3. Make an order
    4. Quit
    Enter choice (1-4): 
    """.strip()

    cmd_funcs = {
        "1": best_buy.get_all_products,
        "2": best_buy.get_total_quantity,
        "4": sys.exit
    }

    while True:
        print(store_menu)
        cmd = input()

        # Execute the corresponding function based on user input
        if cmd in cmd_funcs:
            if cmd == "4":
                print("Bye!")
            cmd_funcs[cmd]()
        else:
            print("Invalid choice")
            input("Press Enter to continue...")


class main():
    try:
        product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                        Product("Google Pixel 7", price=500, quantity=250),
                        ]

        best_buy = Store(product_list)
        start(best_buy)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
