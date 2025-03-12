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


  Scenario: User can filter Off-plan Sales status by Announced
     Given  Open Reelly sign in page
     When   Enter a valid email and password combination
     When   Click on Continue
     When   Main page opens
     When   Click on "Off-plan" at the left side menu
     When   Off-plan page opens
     When   Click on Sales status button
     And    Filter the sales status by "Announced" criteria
     Then   Verify each deal card contains the "Announced" tag


   Scenario: User can filter Off-plan Sales status by Presale
     Given  Open Reelly sign in page
     When   Enter a valid email and password combination
     When   Click on Continue
     When   Main page opens
     When   Click on "Off-plan" at the left side menu
     When   Off-plan page opens
     When   Click on Sales status button
     And    Filter the sales status by "Presale(EOI)" criteria
     Then   Verify each deal card contains the "Presale(EOI)" tag


   Scenario: User can filter Off-plan Sales status by Out of stock
     Given  Open Reelly sign in page
     When   Enter a valid email and password combination
     When   Click on Continue
     When   Main page opens
     When   Click on "Off-plan" at the left side menu
     When   Off-plan page opens
     When   Click on Sales status button
     And    Filter the sales status by "Out of stock" criteria
     Then   Verify each deal card contains the "Out of stock" tag


   Scenario: User can open Market tab and go to the view page template
     Given  Open Reelly sign in page
     When   Enter a valid email and password combination
     When   Click on Continue
     When   Main page opens
     When   Click on "Market" at the left side menu
     When   Market page opens
     When   Click on "Add company" button
     When   Add company page opens
     And    Scroll down and click on "View page template" button
     Then   Verify the button "Send my CV" button is available