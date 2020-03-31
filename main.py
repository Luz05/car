class Car:
	def __init__(self, brand,model,color):
		self.brand = brand
		self.model = model
		self.color = color
		print ("auto nuevo creado")

	def set brand(Self, brand):
		self.brand = brand
		print ("la nueva marca es " + self.brand)

	def get_brand(self)
		print("la marca actual es " + self.brand)

def main():
	auto = Car("bwm","z3","black")
	auto.set_brand("audi")
	auto.get_brand()

if __name__ == "__main__":
	main() 
