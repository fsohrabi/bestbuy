import sys
from products import Product
from store import Store


def show_all_products(store):
    """
    Displays all active products in the store.

    Args:
        store (Store): The store object containing products.
    """
    products = store.get_all_products()
    if not products:
        print("No products available.")
    else:
        print('----------')
        for i, product in enumerate(products, start=1):
            print(f"{i}. {product.show()}")
        print('----------')


def get_total_quantity(store):
    """
    Displays the total quantity of all active products in the store.

    Args:
        store (Store): The store object.
    """
    total_quantity = store.get_total_quantity()
    print(f"Total items in store: {total_quantity}")


def make_order(store):
    """
    Allows the user to place an order by selecting products and their quantities.

    Args:
        store (Store): The store object.
    """
    show_all_products(store)
    print("Enter the product number and quantity. Leave blank to finish ordering.")

    shopping_list = []
    while True:
        try:
            product_choice = input('Which product # do you want? ')
            if not product_choice:
                break
            quantity = input('Enter quantity: ')
            if not quantity:
                break

            product_list = store.get_all_products()
            product_index = int(product_choice) - 1

            if product_index < 0 or product_index >= len(product_list):
                print('Please choose a valid product.')
                continue

            shopping_list.append((product_list[product_index], int(quantity)))
            print('Product added to shopping list!')

        except ValueError:
            print('Invalid input. Please enter numbers only.')

    try:
        total_cost = store.order(shopping_list)
        print(f'Order successful! Total payment: ${total_cost:.2f}')
    except Exception as e:
        print(f"Order failed: {e}")


def start(store):
    """
    Displays the store menu and processes user input.

    Args:
        store (Store): The store object.
    """
    menu = """
    Store Menu
    ----------
    1. List all products in store
    2. Show total amount in store
    3. Make an order
    4. Quit
    """

    actions = {
        "1": show_all_products,
        "2": get_total_quantity,
        "3": make_order,
        "4": sys.exit
    }

    while True:
        print(menu)
        choice = input("Enter choice (1-4): ")

        if choice in actions:
            if choice == "4":
                print("Goodbye!")
                actions[choice]()
            actions[choice](store)
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    try:
        products = [
            Product("MacBook Air M2", price=1450, quantity=100),
            Product("Bose QuietComfort Earbuds", price=250, quantity=500),
            Product("Google Pixel 7", price=500, quantity=250),
        ]
        best_buy = Store(products)
        start(best_buy)
    except Exception as e:
        print(f"An error occurred: {e}")
