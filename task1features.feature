Feature: Shopping cart functionality

  Background:
    Given the user navigates to the shopping website

  Scenario: Add products to cart and checkout
    When the user logs in with valid credentials
    And searches for a product
    And selects some products to add to the cart
    And deletes one product from the cart
    And proceeds to checkout
    And enters payment information
    And confirms the payment
    Then the user should see the order invoice