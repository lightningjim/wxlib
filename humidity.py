import conversion
class humidity(object):
	s_rh_only = 0
	s_td_only = 1
	s_gkg = 2

	def __init__(self, humid, air, htype):
		if htype == s_rh_only:
			self.relative = humid
			#self.absolute = dp_from_rh(self.relative, air.toC())
		elif htype == s_td_only:
			self.absolute == humid
			self.relative = rh_from_dp(self.absolute.toC(), air.toC())
		elif htype == s_gkg:
			#self.absolute == gkg_to_dp(humid)
			self.none = None


	def __init__(self, absolute, relative):
		self.absolute = absolute
		self.relative = relative

	def __str__(self):
		return "Dewpoint: " + str(self.absolute.toF()) + "F | RH: " + str(self.relative) + "%"

# Also need version for g/kg