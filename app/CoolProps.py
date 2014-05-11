import CoolProp
import CoolProp.CoolProp as CP

class CoolPropsDensity():
	"""Take Pressure and Temperature and spit out Density for now"""
	def Density(self,P,T):
		rho = CP.Props('D','P',P,'T',T,'Water')
		return rho
		pass
		