import functools
import operator
import requests
import json
import os

os.system('cls' if os.name == 'nt' else 'clear') # apaga a tela

earth_population = 8000000000
earth_diameter = 12742
earth_density = earth_population / earth_diameter

listaPlanetas = []

def getPlanetas(url = "http://swapi.dev/api/planets/", listaPlanetas = []):
    resposta = requests.get(url)
    if resposta.status_code == 200:
        planetas = resposta.json()

        def planets_mapping(atual):
            population = 0
            if atual["population"] != 'unknown':
                population = int(atual["population"])

            diameter = 0
            if atual["diameter"] != 'unknown':
                diameter = int(atual["diameter"])

            density = 0
            if diameter != 0:
                density = round(population / diameter, 1)

            return ([ atual["name"], population, diameter,  density  ])

        mapped_planets = list(map( planets_mapping, planetas["results"]))

        def planets_reducing(e_d, planet):
            if planet[3] != None and  planet[3] > e_d:
                listaPlanetas.append(planet)

        functools.reduce(planets_reducing, mapped_planets, earth_density)
        
        if planetas["next"] != None:
            getPlanetas(planetas["next"])
        
        return listaPlanetas
    else:
        print("API indisponível!", resposta.status_code)
        return []

print("Aguarde enquanto a lista de planetas é obtida")
print("------------------------------")
print()

planetas = getPlanetas()
print(planetas)

reduce(sum_population, planetas)
