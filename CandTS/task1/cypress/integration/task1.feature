Feature: Shopping cart functionality

  Background:
    Given the user navigates to the shopping website

  Scenario: Add products to cart and checkout
    When the user logs in with valid credentials
    And searches for a product
    And selects some products to add to the cart
    And deletes one product from the cart
    And proceeds to checkout
    And confirms address and reviews order
    And enters payment information
    And confirms the payment
    And downloads the invoice
    Then the invoice file should be downloaded

  /*
  Scenario: User fails to login using invalid credentials
    When the user attempts to log in with invalid credentials
    Then the login should fail*/
