Feature: Tests for Registration page

  Scenario: Verify Account Registration (Sign up) page title
    Given   Open Reelly sign up page
    Then    Verify Sign up page title


  Scenario: User can log in from sign up page
     Given  Open Reelly sign up page
     When   Click on Sign in
     When   Sign in page opens
     When   Enter a valid email and password combination
     And    Click on Continue
     Then   Verify user is logged in