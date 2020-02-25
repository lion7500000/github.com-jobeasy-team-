# Created by 16468 at 2/21/2020
Feature:  System rejects wrong login and password
  # Enter feature description here

  Scenario: check login and password
    # Enter steps here
    Given Go to login page
    When Input wrong login "WrongPassword1234!@gmail.com".
    And Input wrong password "WrongPassword1234!".
    Then Click on login button
    And Verify Invalid username or password pop-up is here.

