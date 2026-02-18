# Created by alexandrabugaeva at 2/14/26
Feature: Tests for property search

  @smoke
  Scenario: User can filter by status Out Of Stock
    Given Open Reelly main page
    When Log in to the account
    And Click on “off plan” in the left side menu
    Then Verify the correct page opened
    When Filter by status of “Out of Stocks”
    Then Verify each product contains the Out of Stocks tag