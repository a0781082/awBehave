Feature: Valid User

    Scenario: Login
        Given we visit the login page
	When we login as a standard user
	Then we should see the shopping cart
