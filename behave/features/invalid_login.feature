Feature: Invalid User

    Scenario: Login
        Given we visit the login page
	When we login as an invalid user
	Then we should see the error icon


