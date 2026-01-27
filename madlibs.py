#This is a Madibs mini project made for fun while learning

print("-----------------------------------------")
print(" Welcome to the Adult Comedy Mad Libs ")
print("Answer honestly… or lie creatively.\n")

print("-----------------------------------------")

name = input("Enter a name: ")
adjective = input("Enter an adjective: ")
place = input("Enter a place: ")
verb = input("Enter a verb (ending with -ing): ")
body_part = input("Enter a body part (non-NSFW ): ")
celebrity = input("Enter a celebrity name: ")
emotion = input("Enter an emotion: ")
weird_item = input("Enter a weird object: ")

print("\n Your Story \n")

story = f"""
Last night, {name} was feeling extremely {adjective}.
So he decided to go to {place} and he was {verb} like nobody was watching.

Suddenly, {celebrity} appeared out of nowhere and stared directly at
{name}'s {body_part}. The silence was loud. Awkwardly loud.

Everyone was in {emotion}, but no one said a word.
To make things worse, someone dropped a {weird_item} on the floor.

At that moment, {name} realized one thing:
"I should never make decisions after midnight."

THE END.
"""

print(story)
