# Predefined favorite foods for the hypothetical classmate
classmate_favorites = {"pizza", "sushi", "tacos", "pasta", "fries"}

# Ask the user to input their 2 or 3 favorite foods
user_favorites = set()

# Input from the user
food1 = input("Enter your first favorite food: ").lower()
food2 = input("Enter your second favorite food: ").lower()
food3 = input("Enter your third favorite food (optional, press enter to skip): ").lower()

# Add foods to user favorites set
user_favorites.add(food1)
user_favorites.add(food2)

if food3:
    user_favorites.add(food3)

# Compare both sets and find the common favorite foods
common_favorites = user_favorites & classmate_favorites

# Output the results
if common_favorites:
    print(f"Our common favorite food(s): {', '.join(common_favorites)}")
else:
    print("We have no common favorite foods.")
