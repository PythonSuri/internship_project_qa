Feature: Tests for main page

  Scenario: User can filter the Secondary deals by “want to sell” option
     Given  Open Reelly sign in page
     When   Enter a valid email and password combination
     When   Click on Continue
     When   Main page opens
     When   Click on “Secondary” option at the left side menu
     When   Click on Filters
     When   Filter the products by "Want to sell"
     And    Click on Apply Filter
     Then   Verify all cards have "For sale" tag



