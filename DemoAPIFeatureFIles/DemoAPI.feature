Feature: Validate CoinDesk API response for current BPI
  # Automate a scenario to fetch API response and assert value

 Scenario: Verify response for the BPI endpoint
   Given   I send a GET request
   Then   The response status code should be 200
   And    I should get response for 3 BPIs and validate the Description

