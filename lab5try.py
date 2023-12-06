"""
This module defines classes related to planetary systems and provides
methods to perform various operations on them.
"""
from enum import Enum


class Planet:
    """
    Represents a celestial body in a planetary system.
    """
    def __init__(self, name, mass, orbital_velocity, mean_temperature,
                length_of_day, distance_from_sun, planet_type):
        self.name = name
        self.mass = mass
        self.orbital_velocity = orbital_velocity
        self.mean_temperature = mean_temperature
        self.length_of_day = length_of_day
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type

    def justmethod_1(self):
        """ 
        I created this useless method just for pylint
        """
        print("Thats not important")

    def justmethod_2(self):
        """ 
        I created this useless method just for pylint
        """
        print("Thats not important too")


class PlanetType(Enum):
    """
    Enumerates the types of planets - Terrestrial or Jovian
    """
    TERRESTRIAL = "Terrestrial"
    JOVIAN = "Jovian"


class Planetary:
    """
    Represents a collection of planets in a planetary system
    """
    def __init__(self, planets=None):
        self.planets = planets

    def add_planet(self, planet):
        """
        Adds a planet to the planetary system 
        """
        self.planets.append(planet)

    def sort_by_day_length(self):
        """ 
        Sorts the planets in the planetary system by their day length
        """
        self.planets.sort(key=lambda x: x.length_of_day)
        for planet in self.planets:
            print(planet.name)

    def find_distance_between(self, planet_a, planet_b):
        """
        Finds the distance between two planets in the planetary system
        """
        for planet in self.planets:
            if planet.name == planet_a:
                planet_a = planet
            elif planet.name == planet_b:
                planet_b = planet
        return abs(planet_a.distance_from_sun - planet_b.distance_from_sun)

    def find_average_mass(self):
        """
        Calculates the average mass of planets in the planetary system 
        """
        total_mass = sum(planet.mass for planet in self.planets)
        return total_mass / len(self.planets)


earth = Planet("Earth", 5.972e24, 29.78, 15.0, 24, 149.6e6, PlanetType.TERRESTRIAL)
mars = Planet("Mars", 6.4171e23, 24.077, -80.0, 24.6, 227.9e6, PlanetType.TERRESTRIAL)
jupiter = Planet("Jupiter", 1.898e27, 13.07, -145.0, 9.9, 778.5e6, PlanetType.JOVIAN)


solar_system = Planetary([earth, mars, jupiter])

solar_system.sort_by_day_length()

distance = solar_system.find_distance_between("Earth", "Mars")

average_mass = solar_system.find_average_mass()

print(f"Distance between Earth and Mars: {distance} km")
print(f"Average mass of planets: {average_mass} kg")
