==== What I Did ====

For this project I used urllib.request and json libraies.

Firstly I used urllib.request functionality to retrive the data from the given URL and store it inside a json variable.

I then initialised two list variables named allGenres and hiphopPacks for storing genre data and all packs within hip hop.

Next I looped through all of the packs in the JSON. One if statement checked weather the current genre was in the allGenres list appending it to the list if it wasnt, this was to avoid duplicate genres.
Another if statement was trigered any time the current genre was hip-hop and added the pack within that item to the hiphopPacks list.

Finally I looped through both lists printing out each element.

=== Compile Instructions ===

All libaries used come inbuilt with Python.
Version used -- Python 3.8.2
