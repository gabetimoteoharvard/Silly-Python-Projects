import requests
from bs4 import BeautifulSoup

site = 'https://pokemondb.net/pokedex/all'
page = requests.get(site)
soup = BeautifulSoup(page.content, 'html.parser')

pokedex = soup.find(id='pokedex')

main_body = pokedex.find('tbody')
pokemon_data = main_body.find_all('tr')

pokemon_stats = {}

for name in pokemon_data:
    pokemon = name.find(class_='cell-name').find(class_='ent-name').text.strip()
    link = name.find(class_='cell-name').find(class_='ent-name')['href']
    mega = name.find(class_='cell-name').find(class_='text-muted')
    
    if mega:
        mega = mega.text.strip()
        pokemon = f'{pokemon} ({mega})'
    
    stats = name.find_all('td', class_='cell-num')
    stats = stats[1:]
    
    stats_map = {'HP':int(stats[0].text), 'Attack':int(stats[1].text), 'Defense':int(stats[2].text), 'Sp.Atk':int(stats[3].text), 'Sp.Def':int(stats[4].text), 'Speed':int(stats[5].text), 'Link':link}
    pokemon_stats[pokemon] = stats_map
    

print(f"Hello, welcome to ideal Pokemon finder.\nHere you can find which Pokemon fits within your needs.\nWe will show you a list of Pokemon (if there are any) that have stats greater than or equal to the ones that you input.\n\nIf you don't care about a particular stat, then you're free to leave it blank, otherwise put in a number\n")

hp = input('>Hp: ').strip()
attack = input('>Attack: ').strip()
defense = input('>Defense: ').strip()
spAtk = input('>Special Attack: ').strip()
spDef = input('>Special Defense: ').strip()
speed = input('>Speed: ').strip()

ideal_pokemon = []

for pok in pokemon_stats:
    if hp and int(hp) > pokemon_stats[pok]['HP']:
        continue
    if attack and int(attack) > pokemon_stats[pok]['Attack']:
        continue
    if defense and int(defense) > pokemon_stats[pok]['Defense']:
        continue
    if spAtk and int(spAtk) > pokemon_stats[pok]['Sp.Atk']:
        continue
    if spDef and int(spDef) > pokemon_stats[pok]['Sp.Def']:
        continue
    if speed and int(speed) > pokemon_stats[pok]['Speed']:
        continue
    
    ideal_pokemon.append(pok)

if not len(ideal_pokemon):
    print(f'Sorry, there are no pokemon which fit your criteria.')
elif len(ideal_pokemon) == 1:
    print(f'There is one pokemon which fits your criteria.\n')
    print(f"{ideal_pokemon[0]}, pokemondb.net{pokemon_stats[ideal_pokemon[0]]['Link']}")
else:
    print(f"There are {len(ideal_pokemon)} pokemon which fit your criteria.\n")
    for pokemon in ideal_pokemon:
        print(f"{pokemon}, pokemondb.net{pokemon_stats[pokemon]['Link']}", sep = '\n')
       





