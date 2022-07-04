Feature: Bank Manager Login

  Scenario: Add and Delete new customer
    Given I open XYZ Bank login page
    When I click on the "Bank Manager Login"
    When I add a new Customer
    And I search the customer on Customers list
    Then I assert that customer is added with correct info
    When I Delete customer
    Then I assert that customer is delete
    And close browser