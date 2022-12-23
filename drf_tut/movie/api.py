import requests

url = "https://the-cocktail-db.p.rapidapi.com/search.php"

querystring = {"i":"vodka"}

headers = {
    'x-rapidapi-key': "69eeecd026mshdbabc319184b5aap160565jsn34fa6e8190d2",
    'x-rapidapi-host': "the-cocktail-db.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)