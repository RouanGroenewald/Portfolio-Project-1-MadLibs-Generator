""" 
Portfolio Project 1
Date: 04/07/2026
File Name: 01_MadLibs_Generator.py
Project Information: Create an interactive script that prompts users for various parts of speech (nouns, verbs, adjectives) and injects them into a pre-defined story template. 
This project focuses on mastering the inputs() and Print() functions, string concentration, and f-string formatting. 
By pushing this into GitHub, you establish your first commit and begin your journey of version-tracked development.
"""
print("Welcome to MadLibs Generator")
print("Answer the following questions")

#Word List
adjective1 = input("adjective: ")
verb1 = input("verb (ending in -ing): ") 
noun1 = input("noun: ")
adjective2 = input("adjective: ")
verb2 = input("verb (past tense): " )
noun2 = input("noun: ")

madlibs = f"Norman and Livvy were {adjective1}, naturally, since {verb1} a {noun1} is always a matter of last-minute delays, so they had to take the only {adjective2} seat in the coach. It was the one toward the front; the one with nothing before it but the seat that faced the wrong way, with its back hard against the front partition. While Norman {verb2} the {noun2} onto the rack, Livvy found herself chafing a little."

print(madlibs)

"""
Original Mad Libs: The Train Journey
Norman and Livvy were late, naturally, since catching a train is always a matter of last-minute delays, so they had to take the only available seat in the coach. 
It was the one toward the front; the one with nothing before it but the seat that faced the wrong way, with it's back hard against the front partition. 
While Norman heaved the suitcase onto the rack, Livvy found herself chafing a little.

Resources:
1. Wikipedia: https://en.wikipedia.org/wiki/Mad_Libs
2. Book: "Nightfall" is a 1941 science fiction short story by Isaac Asimov: https://s3.us-west-1.wasabisys.com/luminist/EB/A/Asimov%20-%20Nightfall.pdf

References:
Book: "Nightfall" is a 1941 science fiction short story by Isaac Asimov. page 197 
"""
