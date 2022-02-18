Feature: Remove Items from Cart

    Scenario: Remove One Iten
        Given we visit the inventory page
	    When we add one item to the cart
        When we remove one item from the cart
	    Then we should not see an item in the cart


