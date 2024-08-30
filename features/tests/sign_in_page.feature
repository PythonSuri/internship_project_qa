Feature: Tests for Sign In functionality

    Scenario: User can log in when enters valid credentials
     Given  Open Reelly sign in page
     When   Enter a valid email and password combination
     And    Click on Continue
     Then   Verify user is logged in