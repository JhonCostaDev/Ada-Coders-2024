games_favoritos = {
    'Call of Duty': {
    "Call of Duty": 2003,
    "Call of Duty: United Offensive": 2004,
    "Call of Duty: Finest Hour": 2004,
    "Call of Duty 2": 2005,
    "Call of Duty 2: Big Red One": 2005,
    "Call of Duty 3": 2006,
    "Call of Duty 4: Modern Warfare": 2007,
    "Call of Duty: World at War": 2008,
    "Call of Duty: Modern Warfare 2": 2009,
    "Call of Duty: Black Ops": 2010,
    "Call of Duty: Modern Warfare 3": 2011,
    "Call of Duty: Black Ops II": 2012,
    "Call of Duty: Ghosts": 2013,
    "Call of Duty: Advanced Warfare": 2014,
    "Call of Duty: Black Ops III": 2015,
    "Call of Duty: Infinite Warfare": 2016,
    "Call of Duty: WWII": 2017,
    "Call of Duty: Black Ops 4": 2018,
    "Call of Duty: Modern Warfare": 2019,
    "Call of Duty: Warzone": 2020,
    "Call of Duty: Black Ops Cold War": 2020,
    "Call of Duty: Vanguard": 2021,
    "Call of Duty: Modern Warfare II": 2022,
    "Call of Duty: Warzone 2": 2022,
    "Call of Duty: Modern Warfare III": 2023,
    "Call of Duty: Black Ops 6": 2024
                    },
    "Assassin's Creed": {
    "Assassin's Creed": 2007,
    "Assassin's Creed: Altaïr's Chronicles": 2008,
    "Assassin's Creed II": 2009,
    "Assassin's Creed: Bloodlines": 2009,
    "Assassin's Creed II: Discovery": 2009,
    "Assassin's Creed: Brotherhood": 2010,
    "Assassin's Creed: Revelations": 2011,
    "Assassin's Creed III": 2012,
    "Assassin's Creed III: Liberation": 2012,
    "Assassin's Creed IV: Black Flag": 2013,
    "Assassin's Creed: Freedom Cry": 2013,
    "Assassin's Creed: Rogue": 2014,
    "Assassin's Creed: Unity": 2014,
    "Assassin's Creed: Syndicate": 2015,
    "Assassin's Creed: Chronicles": 2015,
    "Assassin's Creed: Identity": 2016,
    "Assassin's Creed: Origins": 2017,
    "Assassin's Creed: Odyssey": 2018,
    "Assassin's Creed: Valhalla": 2020,
    "Assassin's Creed: Mirage": 2023,
    "Assassin's Creed: Nexus VR": 2023,
    "Assassin's Creed: Shadows": 2024
}
    }

games_favoritos['God of war'] =  {
    "God of War": "20 de março de 2005",
    "God of War II": "13 de março de 2007",
    "God of War III": "16 de março de 2010",
    "God of War: Ascension": "12 de março de 2013",
    "God of War (2018)": "20 de abril de 2018",
    "God of War Ragnarök": "9 de novembro de 2022"
}

games_favoritos['Medal of Honor'] =  {
    "Medal of Honor": "12 de outubro de 1999",
    "Medal of Honor: Underground": "1 de novembro de 2000",
    "Medal of Honor: Frontline": "17 de junho de 2002",
    "Medal of Honor: Rising Sun": "11 de novembro de 2003",
    "Medal of Honor: Pacific Assault": "2 de novembro de 2004",
    "Medal of Honor: European Assault": "7 de junho de 2005",
    "Medal of Honor: Airborne": "4 de setembro de 2007",
    "Medal of Honor (2010)": "12 de outubro de 2010",
    "Medal of Honor: Warfighter": "23 de outubro de 2012",
    "Medal of Honor: Above and Beyond": "11 de dezembro de 2020"
}

games_favoritos['Bonce'] = {
    '1':1999,
    '2':2000,
    '3':2001,
    }

# print(f'Jogos no dicionário:')
# print(', '.join(games_favoritos.keys())) 

# Como existe um dicionário como valor para cada chave do dicionário principal. para buscar os valores do dicionário interno, eu atribuí a saída da chave a uma variável e então iterando por esse sub-dicionário eu extraí o par chave-valor com o método items().
assassins = games_favoritos["Assassin's Creed"]

for jogo, data in assassins.items():
    print(f'O jogo {jogo}, foi lançado em {data}')
    
