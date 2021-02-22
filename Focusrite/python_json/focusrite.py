
import urllib.request, json 


with urllib.request.urlopen("https://api.ampifymusic.com/packs") as url:
    data = json.loads(url.read().decode())

allGenres = []
hiphopPacks = []


size = (len(data['packs']))

print("==== genes ====")

for x in range(size):

    currentGenre = (data['packs'][x]['genres'])

    # if statement to make sure no duplicate genres are added
    
    if(currentGenre not in allGenres):
        allGenres.append(currentGenre)


    if(currentGenre == ['hip-hop']):

        hiphopPacks.append(data['packs'][x]['name'])

print("==== all genres ====")

for x in range(len(allGenres)):
    print(allGenres[x])


print("==== hip-hop packs ====")

for x in range(len(hiphopPacks)):
    print(hiphopPacks[x])
