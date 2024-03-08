# ShoppingCart System

This Python system allows for the management of a basic shopping cart, including product handling, user management, and a shopping cart interface. Transactions are simulated with basic balance checks without any real monetary exchange.

## Features

- Add and manage products.
- User account management with login and balance tracking.
- A ShoppingCart class that allows users to add and remove products, check out, and print a receipt.

## Classes

### Product

- Attributes:
  - name: The name of the product.
  - price: The price of the product.

### User

- Attributes:
  - login: The user's login name.
  - balance: The user's current balance, default is 0.
- Methods:
  - deposit(val): Add money to the user's balance.
  - is_money_enough(val): Check if the user has enough balance for a purchase.
  - payment(val): Deduct money from the user's balance for a purchase.

### Cart

- Attributes:
  - user: The User associated with the cart.
  - goods: A collection of products in the cart.
  - total: The total price of all products in the cart.
- Methods:
  - add(product, col=1): Add a product to the cart.
  - remove(product, col=1): Remove a product from the cart.
  - order(): Attempt to pay for the cart. Prints a message indicating success or failure.
  - print_check(): Prints a detailed list of the cart contents and the total price.

## How to Use

1. Initialize a User object with a login name and an optional balance.
2. Create Product objects with a name and price.
3. Initialize a Cart object with a User.
4. Use the add() method to add products to the cart.
5. Call print_check() to show the cart's contents and total price.
6. Use order() to attempt to pay for the cart. Ensure the user has enough balance.
