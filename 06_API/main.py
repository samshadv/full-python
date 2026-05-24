import requests 

base_url = "https://pokeapi.co/api/v2/"

def get_poke_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data  = response.json()
        print("Pokemon Name:", data["name"])
        print("Height:", data["height"])
        print("Weight:", data["weight"])
    else:
        print("fail to retreve data")

poki_name = "Pikachu"
get_poke_info(poki_name)