Feature: Verify Item Can Be Added to Cart on eBay
#  Automate a scenario to ensure a user can add an item to the cart on the eBay website.
#  The test verifies that the cart updates correctly after adding an item.

Scenario: Add an item to the cart and verify cart updates
    Given I open the browser and navigate to ebay
    When  I search for book in the search bar
    And   I click on the first item in the search results
    And   I click on Add to cart on the item listing page
    Then  I should see the cart updated with correct number of items.
