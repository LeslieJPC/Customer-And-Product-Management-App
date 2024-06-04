import pickle

# Define empty lists to store customers and products
customers = []
products = []

# Class for Product
class Product:
    def __init__(self, product_SKU, product_name, price):
        """
        Initializes a Product object.

        Args:
            product_id (str): A unique identifier for the product.
            product_name (str): The name of the product.
            price (float): The price of the product.
        """
        self.product_SKU = product_SKU
        self.product_name = product_name
        self.price = price


# Class for Customer
class Customer:
    def __init__(self, customer_id, customer_name, email):
        """
        Initializes a Customer object.

        Args:
            customer_id (str): A unique identifier for the customer.
            customer_name (str): The name of the customer.
            email (str): The email address of the customer.
        """
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.email = email

# Class for RewardCustomer (Inherits from Customer)
class RewardCustomer(Customer):
    def __init__(self, customer_id, customer_name, email):
        """
        Initializes a RewardCustomer object, inheriting from Customer.

        Args:
            customer_id (str): A unique identifier for the customer.
            customer_name (str): The name of the customer.
            email (str): The email address of the customer.
        """
        super().__init__(customer_id, customer_name, email)
        self.reward_points = 0
        self.reward_level = "Silver"

    def earn_reward_points(self, points_earned):
        """
        Updates the reward points earned by the customer.

        Args:
            points_earned (int): The number of reward points earned.
        """
        self.reward_points += points_earned
        if self.reward_points >= 100:
            self.reward_level = "Gold"

# Class for Transaction
class Transaction:
    def __init__(self, transaction_id, customer_id):
        """
        Initializes a Transaction object.

        Args:
            transaction_id (str): A unique identifier for the transaction.
            customer_id (str): The ID of the customer who made the transaction.
        """
        self.transaction_id = transaction_id
        self.customer_id = customer_id
        self.products_purchased = []
        self.transaction_date = None  # Will be set during transaction completion

    def add_product(self, product):
        """
        Adds a product to the list of products purchased in the transaction.

        Args:
            product (Product): The product to be added to the transaction.
        """
        self.products_purchased.append(product)

    def calculate_total_cost(self):
        """
        Calculates the total cost of the products in the transaction.

        Returns:
            float: The total cost of the products.
        """
        total_cost = sum(product.price for product in self.products_purchased)
        return total_cost

# Function to add a new customer
def add_customer():
    customer_id = input("Enter customer ID: ")
    customer_name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    customer = Customer(customer_id, customer_name, email)
    customers.append(customer)
    print("Customer added successfully.")

# Function to add a new reward program customer
def add_reward_customer():
    customer_id = input("Enter customer ID: ")
    customer_name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    reward_customer = RewardCustomer(customer_id, customer_name, email)
    customers.append(reward_customer)
    print("Reward program customer added successfully.")

# Function to add a new product
def add_product():
    product_id = input("Enter product ID: ")
    product_name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity_in_stock = int(input("Enter quantity in stock: "))
    product = Product(product_id, product_name, price, quantity_in_stock)
    products.append(product)
    print("Product added successfully.")

# Function to run a transaction
def run_transaction():
    transaction_id = input("Enter transaction ID: ")
    customer_id = input("Enter customer ID: ")
    transaction = Transaction(transaction_id, customer_id)
    
    while True:
        product_id = input("Enter product ID (or 'done' to finish): ")
        if product_id == 'done':
            break
        for product in products:
            if product.product_id == product_id:
                transaction.add_product(product)
                print("Product added to transaction.")
                break
        else:
            print("Product not found.")

    total_cost = transaction.calculate_total_cost()
    transaction.transaction_date = input("Enter transaction date: ")
    print("\nTransaction Details:")
    print("Transaction ID:", transaction.transaction_id)
    print("Customer ID:", transaction.customer_id)
    print("Transaction Date:", transaction.transaction_date)
    print("Products Purchased:")
    for product in transaction.products_purchased:
        print("- Product:", product.product_name)
        print("  Price:", product.price)
    print("Total Cost:", total_cost)

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a new customer")
    print("2. Add a new reward program customer")
    print("3. Add a new product")
    print("4. Run a transaction")
    print("5. Save data to file")
    print("6. Load data from file")
    print("7. Exit")
    choice = input("Select an option: ")

    if choice == '1':
        add_customer()
    elif choice == '2':
        add_reward_customer()
    elif choice == '3':
        add_product()
    elif choice == '4':
        run_transaction()
    elif choice == '5':
        with open("data.pickle", "wb") as file:
            pickle.dump((customers, products), file)
        print("Data saved successfully.")
    elif choice == '6':
        try:
            with open("data.pickle", "rb") as file:
                customers, products = pickle.load(file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No data file found.")
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please select a valid option.")
