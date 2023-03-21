import requests

hakusana = "https://api.chucknorris.io/jokes/random"
vitsi = requests.get(hakusana).json()
print(vitsi['value'])

while True:
    vastaus = requests.get(hakusana).json()
    syote = input("Paina u, jos haluat toisen vitsin \nPaina s, jos haluat lopettaa \n")

    if syote == "u":
        print(vastaus['value'])
    elif syote == "s":
        break