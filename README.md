# Simple Store Management System

This project is a simple store management system implemented in Python. It allows users to manage a list of products, view available stock, and place orders. The store keeps track of the inventory and adjusts the stock based on customer orders.

## Features
- **List Products**: View all available products in the store.
- **Total Quantity**: Check the total quantity of all active products.
- **Order Products**: Customers can select products and specify quantities to create an order. Only products with sufficient stock can be ordered.
- **Error Handling**: Input validation and error messages for invalid choices or insufficient stock.

## Project Structure
- **`main.py`**: The main file that contains the store's menu system and interaction logic.
- **`products.py`**: Contains the `Product` class, which represents individual products in the store.
- **`store.py`**: Contains the `Store` class, which manages the collection of products, their availability, and the order process.

## How to Run

1. Ensure you have Python 3 installed on your machine.
2. Clone or download the project.
3. Navigate to the project directory in your terminal.
4. Run the following command:

    ```bash
    python main.py
    ```

## Example Usage
1. **List Products**: Displays all available products in the store, showing their price and quantity.
2. **Show Total Quantity**: Outputs the total quantity of all available products.
3. **Make an Order**: Allows the user to select products by number, specify the quantity, and finalize the order. Only products with enough stock are added to the shopping list.

## Classes and Methods

### `Product`
- **Attributes**: `name`, `price`, `quantity`, `active`
- **Methods**:
  - `get_quantity()`: Returns the quantity of the product.
  - `set_quantity()`: Updates the quantity of the product.
  - `is_active()`: Checks if the product is active.
  - `buy(quantity)`: Processes the purchase of a product and updates its quantity.
  - `show()`: Displays the product details.

### `Store`
- **Attributes**: `products`
- **Methods**:
  - `add_product(product)`: Adds a new product to the store.
  - `remove_product(product)`: Removes a product from the store.
  - `get_total_quantity()`: Returns the total quantity of active products.
  - `get_all_products()`: Returns a list of active products.
  - `order(shopping_list)`: Processes the order of products and calculates the total price.

## Future Enhancements
- Add a database to persist product information.
- Implement a user interface for better interaction.
- Add more detailed product categories and descriptions.

## License
This project is licensed under the MIT License.
