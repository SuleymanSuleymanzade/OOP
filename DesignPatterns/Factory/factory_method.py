import abc 

#========================= factory method =======================

class Section(metaclass = abc.ABCMeta):
	@abc.abstractmethod
	def describe(self):
		pass

class PersonalSection(Section):
	def describe(self):
		print('Personal Section')

class WallSection(Section):
	def describe(self):
		print('Wall Section')

class GroupsSection(Section):
	def describe(self):
		print('Groups Section')

class PictureSection(Section):
	def describe(self):
		print('Picture Section')


class SocialNetworkProfile(metaclass = abc.ABCMeta):
	def __init__(self):
		self.sections = []
		self.create_profile()

	def describe(self):
		for section in self.sections:
			section.describe()

	@abc.abstractmethod
	def create_profile(self):
		pass

	def get_sections(self):
		return self.sections 

	def add_section(self, section):
		self.sections.append(section)

class Facebook(SocialNetworkProfile):
	def create_profile(self):
		self.add_section(PersonalSection())
		self.add_section(PictureSection())
		self.add_section(GroupsSection())

class Twitter(SocialNetworkProfile):
	def create_profile(self):
		self.add_section(WallSection())

#================================= Client Part =============================

facebook = Facebook()
twitter = Twitter()


twitter.describe()
facebook.describe()



