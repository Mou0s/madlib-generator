print("Welcome to Mad Libs!")
print("--------------------Please provide the following:------------")

# Get user input
name = input("Enter a **Noun** (name): ")
adjective1 = input("Enter an **Adjective** (e.g. happy, tall): ")
adjective2 = input("Enter another **Adjective** (e.g. silly, colorful): ")
adjective3 = input("Enter one more **Adjective** (e.g. big, fluffy): ")
noun1 = input("Enter a **Noun** (e.g. book, chair): ")
noun2 = input("Enter another **Noun** (e.g. car, tree): ")
animal = input("Enter an **Noun** (animal): ")
food = input("Enter a **Noun** (food): ")
verb1 = input("Enter a **Verb** (e.g. run, jump): ")
verb2 = input("Enter another **Verb** (e.g. read, dance): ")
adverb1 = input("Enter an **Adverb** (e.g. quickly, loudly): ")
place = input("Enter a **Noun** (place): ")

# Create the story
happystory = (
    f"One day, {name} was walking through the {place} when they came across a {adjective1} {noun1}. "
    f"They were surprised to see a {adjective2} {animal} sitting on top of it, eating a {food}. "
    f"{name} was so startled that they jumped into a nearby {noun2} and hid. "
    f"After a while, the {animal} finished its snack and wandered off, leaving {name} to emerge from the {noun2}, feeling a bit {adjective3}. "
    f"Then, {name} decided to {verb1} {adverb1} through the {place}, singing a happy song and {verb2} with joy. "
    f"As they {verb1} along, they met a friendly {animal} who offered them a {food} and a cold drink. "
    f"{name} gratefully accepted and sat down on a nearby {noun2} to rest and enjoy their snack. "
    f"After a while, they felt refreshed and decided to continue their journey through the {place}. "
    f"They walked for a while, taking in the beautiful sights and sounds of the {place}, until they came to a beautiful {adjective1} beach. "
    f"{name} was amazed by the {adjective2} sand and the {adjective3} water, and they spent the rest of the day {verb1} in the waves and {verb2} on the beach."
)

# Print the story
print("Here's your Mad Libs story:")
print(happystory)

