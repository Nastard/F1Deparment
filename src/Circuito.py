# Ejemplo, circuitos 2020: https://ergast.com/api/f1/2020.json

class Circuito:
	def __init__(self, circuit_id, url, circuit_name, lat, long, locality,
					country):
		self.circuit_id = circuit_id
		self.url = url
		self.circuit_name = circuit_name
		self.lat = lat
		self.long = long
		self.locality = locality
		self.country = country
