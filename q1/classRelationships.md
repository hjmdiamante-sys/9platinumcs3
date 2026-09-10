# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: Song 
Description: music that can be played in PROJECT SEKAI: COLORFUL STAGE! (rhythm game)
## New Related Class
Class: Chart
Description: The gameplay of the song in the game.
## Association
Relationship: The song contains a chart
Explanation: In the game, every song must have a chart so the players can play the rhythm game.
## Multiplicity

Multiplicity: Song 1 ---------------------- 1..* Chart 
Explanation: A Song can have multiple Chart objects because each song has a separate chart for each difficulty, such as Easy, Normal, Hard, Expert, Master, and sometimes Append. Each Chart belongs to only one Song, so the multiplicity can be shown as Song 1 — 5..6 Chart.
## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
### What multiplicity did you choose and why?
### How did you implement the relationship in Python?
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?
