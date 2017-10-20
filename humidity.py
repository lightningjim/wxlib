import conversion
import temp
class humidity(object):
	s_rh_only = 0
	s_td_only = 1
	s_gkg = 2

	def __init__(self, *args):
		# Absolute and Relative Direct
		if len(args) == 2:
			self.absolute = args[0]
			self.relative = args[1]
		# Only has RH or Absolute
		elif len(args) == 3:
			# If only has Relative
			if args[2] == s_rh_only:
				self.relative = args[0]
				self.absolute = dp_from_rh(args[1], args[2].toC())
			# If only has Absolute as Dewpoint
			elif args[2] == s_td_only:
				self.absolute = args[1]
				self.relative = rh_from_dp(args[1].toC(), args[2].toC())
			elif args[2] == s_gkg:
				self.absolute = gkg_to_dp(args[1])
				self.relative = rh_from_dp(self.absolute.toC(),args[2].toC())
		else:
				self.relative = -1
				self.absolute = temp(0, conversion.s_kelvin)

	def __init__(self, absolute, relative):
		self.absolute = absolute
		self.relative = relative

	def __str__(self):
		return "Dewpoint: " + str(self.absolute.toF()) + "F | RH: " + str(self.relative) + "%"

# Also need version for g/kg