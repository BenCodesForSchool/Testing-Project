Feature: API login, account verification, account deletion functionality
  
  Background:
    Given the API endpoints for account creation, updating, verification, and deletion

  Scenario: Single account creation, verification
    When the user uses the API to create an account 
    Then the user should be able to use the API to verify account details

  Scenario: Account address change
    When the user attempts to change the address on the account
    Then the address should change on the account
  
  Scenario: Single account deletion
    When the user attempts to delete the account
    Then the account should be deleted

 """" Scenario: Multiple-account creation:
    When the user uses a CSV file to create multiple accounts
    Then every account should be created

  Scenario: Multiple-account deletion:
    When the user attempts to delete multiple accounts
    Then every one of those accounts should be deleted"""