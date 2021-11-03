import pandas as pd

class Predictor:
	def __init__(self, df=pd.DataFrame(columns=[]), model_race=0, model_pole=0):
		self.df = df
		self.model_race = model_race
		self.model_pole = model_pole

	def get_df(self):
		return self.df

	def set_df(self, df):
		self.df = df

	def get_model_race(self):
		return self.model_race

	def set_model_race(self, model_race):
		self.model_race = model_race

	def get_model_pole(self):
		return self.model_pole

	def set_model_pole(self, model_pole):
		self.model_pole = model_pole

	def load_csv(self, path):
		self.df = pd.read_csv(path)

	def train_race_prediction(self): # train race
		model = 0
		self.model_race = model

	def train_pole_prediction(self): # train pole
		model = 1
		self.model_pole = model

	def test_race_prediction(self, driver, circuit): # test race
		# print(driver+" "+circuit+" "+str(self.model_race))

		prediction = 0
		return prediction

	def test_pole_prediction(self, driver, circuit):  # test pole
		# print(driver+" "+circuit+" "+str(self.model_pole))

		prediction = 0
		return prediction

# p = Predictor()
# print(p)
# print(p.get_df().head())
# p.set_df(pd.DataFrame(columns=[]))
# print(p.get_df())
#
# p.set_model_race(1)
# print(p.get_model_race())
# p.set_model_pole(2)
# print(p.get_model_pole())
#
# p.load_csv("./data/dataF1.csv")
# print(p.get_df().head())
#
# p.train_race_prediction()
# print(p.get_model_race())
# p.train_pole_prediction()
# print(p.get_model_pole())
#
# p.test_race_prediction("alonso", "catalunya")
# p.test_pole_prediction("sainz", "monza")
