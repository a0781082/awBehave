run_parallel:
	make -j valid_case invalid_case add_item_case remove_item_case

valid_case:
	behave features/valid_login.feature

invalid_case:
	behave features/invalid_login.feature

add_item_case:
	behave features/add_item_to_cart.feature

remove_item_case:
	behave features/remove_item_from_cart.feature
