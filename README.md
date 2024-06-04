# Customer and Product Management Application

## Overview
The **Customer and Product Management Application** is a Python-based program designed to manage customers, products, and transactions for a retail environment. It supports regular and reward program customers, allows adding new products, and handles transactions, including calculating total costs.

## Features
- **Customer Management**: Add regular and reward program customers.
- **Product Management**: Add new products with details such as SKU, name, price, and quantity in stock.
- **Transactions**: Conduct transactions by adding products to a customer's purchase and calculating the total cost.
- **Data Persistence**: Save and load customer and product data using pickle.

## Code Structure

### Classes

#### Product
Represents a product in the store.
- `product_SKU`: Unique identifier for the product.
- `product_name`: Name of the product.
- `price`: Price of the product.

#### Customer
Represents a regular customer.
- `customer_id`: Unique identifier for the customer.
- `customer_name`: Name of the customer.
- `email`: Email address of the customer.

#### RewardCustomer (inherits from Customer)
Represents a customer enrolled in the reward program.
- `reward_points`: Points earned by the customer.
- `reward_level`: Level of the reward program (e.g., Silver, Gold).

#### Transaction
Represents a transaction.
- `transaction_id`: Unique identifier for the transaction.
- `customer_id`: ID of the customer who made the transaction.
- `products_purchased`: List of products purchased in the transaction.
- `transaction_date`: Date of the transaction.
- `add_product(product)`: Adds a product to the transaction.
- `calculate_total_cost()`: Calculates the total cost of the transaction.

### Functions

#### add_customer()
Prompts the user to input customer details and adds a new regular customer to the list.

#### add_reward_customer()
Prompts the user to input customer details and adds a new reward program customer to the list.

#### add_product()
Prompts the user to input product details and adds a new product to the list.

#### run_transaction()
Handles a transaction by prompting the user to input transaction details and add products to the transaction. Calculates and displays the total cost.

### Main Program Loop
Provides a menu for the user to select options to add customers, add products, run transactions, save data, load data, and exit the program.

## Getting Started

### Prerequisites
- Python 3.x

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/CustomerProductManagementApp.git
    ```
2. Navigate to the project directory:
    ```sh
    cd CustomerProductManagementApp
    ```
3. Run the program:
    ```sh
    python main.py
    ```

### Usage
1. Select an option from the menu:
    - `1. Add a new customer`
    - `2. Add a new reward program customer`
    - `3. Add a new product`
    - `4. Run a transaction`
    - `5. Save data to file`
    - `6. Load data from file`
    - `7. Exit`
2. Follow the prompts to perform the desired action.
3. To save data, select option 5. Data will be saved to `data.pickle`.
4. To load data, select option 6. Data will be loaded from `data.pickle`.

### Example
```sh
Options:
1. Add a new customer
2. Add a new reward program customer
3. Add a new product
4. Run a transaction
5. Save data to file
6. Load data from file
7. Exit
Select an option: 1
Enter customer ID: C001
Enter customer name: John Doe
Enter customer email: john.doe@example.com
Customer added successfully.
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Author
- Leslie

Feel free to reach out for any questions or contributions. Happy coding!
