import functools
import operator
import requests
import json
import os

class Earth:
    def __init__(self):
        self.population = 8000000000
        self.diameter = 12742
        self.density = self.population / self.diameter

class AtividadeCiclo2:
    def __init__(self):
        self.planets = []
        self.earth = Earth()

    def mappedPlanets(self, planet):
        population = 0
        if planet["population"] != "unknown":
            population = int(planet["population"])

        diameter = 0
        if planet["diameter"] != "unknown":
            diameter = int(planet["diameter"])

        density = 0
        if diameter != 0:
            density = round(population / diameter, 1)

        return [ planet["name"], population, diameter, density ]

    def requestPlanets(self, url = "http://swapi.dev/api/planets/"):
        resp = requests.get(url).json()
        results = map(self.mappedPlanets, resp["results"]) # map 1

        for planet in results:
            self.planets.append(planet)

        if resp["next"] != None:
            self.requestPlanets(resp["next"])

    def getDensityPlanets(self):
        return list(filter(lambda planet: self.earth.density > planet[3],  self.planets))

    def getPlanetsCount(self):
        return len(self.getPlanets())

    def getPlanets(self):
        return list(map(lambda planet: planet[0] , self.getDensityPlanets()))

    def getPopulationCount(self):
        return functools.reduce(lambda population, planet: population + planet[1], self.planets, 0)

atividadeCiclo2 = AtividadeCiclo2()
atividadeCiclo2.requestPlanets()
print("Quantos são os planetas mais densamente populados do que o planeta Terra: " + str(atividadeCiclo2.getPlanetsCount()) )
print("Quais são os planetas mais densamente populados do que o planeta Terra: " + str(atividadeCiclo2.getPlanets()) )
print("Total geral de habitantes: " + str(atividadeCiclo2.getPopulationCount()) )
