Feature: Add Items to Cart

    Scenario: Add One Iten
        Given we visit the inventory page
	    When we add one item to the cart
	    Then we should see an item in the cart


