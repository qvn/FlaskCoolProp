import CoolProp
import CoolProp.CoolProp as CP
from CoolProp import *



class CoolProp_State():
	"""Get States from Properties Entered"""
	def __init__(self, flash, fluid, prop1, prop2):
		self.prop1 = prop1
		self.prop2 = prop2
		self.fluid = fluid
		self.flash = flash

		self.d = dict()
		a=flash[0]
		b=flash[1]
		self.d[a] = prop1
		self.d[b] = prop2
		
		self.state = CoolProp.State(str(self.fluid),self.d)

	def construct_dict(self):
		f = self.flash
		d = dict()


	def get_cv(self):
		return self.state.get_cv()

	def get_cp(self):
		return self.state.get_cp()

	def get_rho(self):
		return self.state.get_rho()

	def get_p(self):
		return self.state.get_p()

	def get_t(self):
		return self.state.get_T()

	def get_s(self):
		return self.state.get_s()

	def get_h(self):
		return self.state.get_h()

	def get_all(self):
		fluid = self.fluid
		t = self.get_t()
		p = self.get_p()
		cv = self.get_cv()
		cp = self.get_cp()
		rho = self.get_rho()
		s = self.get_s()
		h = self.get_h()
		return {'fluid':fluid,'t':t,'p':p,'cv':cv, 'cp':cp, 'rho':rho, 's':s, 'h':h}

		
		