Feature: Tests for main page

  Scenario: User can filter the Secondary deals by “Want to sell” criteria
     Given  Open Reelly sign in page
     When   Enter a valid email and password combination
     When   Click on Continue
     When   Main page opens
     When   Click on “Secondary” option at the left side menu
     When   Click on Filters button
     When   Filter the products by "Want to sell" criteria
     And    Click on Apply Filter button
     Then   Verify all deal cards display "For sale" tag



