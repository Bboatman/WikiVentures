'''
pages need to have a title, contents, summary, and links

we also want these test pages to mimic the wikipedia API so we need
the methd page(string) that returns a page based on the given string
'''

class APage(object):
	def __init__(self, title, links, text):
		self.title = title
		self.links = links
		self.summary = text
		self.contents = text

all_pages = {'Pickled Cucumber' : APage('Pickled Cucumber', ['United States', 'Mustard Seed', 'Polish Language', 'Dill', 'Brine'], 'A pickled cucumber (commonly known as a pickle in the United States and Canada or generically as gherkins in the United Kingdom) is a cucumber that has been pickled in a brine, vinegar, or other solution and left to ferment for a period of time, by either immersing the cucumbers in an acidic solution or through souring by lacto-fermentation.'),
			'United States' : APage('United States', ['Christianity', 'President Donald Trump', 'Republic', 'Native American'], "The United States of America (USA), commonly referred to as the United States (U.S.) or America, is a federal republic composed of 50 states, the federal district of Washington, D.C., five major territories, and various possessions. The 48 contiguous states and Washington, D.C., are in central North America between Canada and Mexico. The state of Alaska is in the northwestern part of North America and the state of Hawaii is an archipelago in the mid-Pacific. The territories are scattered about the Pacific Ocean and the Caribbean Sea. At 3.8 million square miles (9.9 million km2) and with over 320 million people, the country is the world's third largest by total area (fourth largest by land area) and the third most populous."),
			'Christianity' : APage('Christianity', ['Jesus', 'Cross', 'Cathedral', 'Rome'], "Christianity is an Abrahamic monotheistic[1] religion based on the life and teachings of Jesus Christ as presented in the New Testament. Christianity is the world's largest religion, with over 2.4 billion adherents, known as Christians. Christians believe that Jesus is the Son of God and the savior of humanity whose coming as Christ or the Messiah was prophesied in the Old Testament."), 
			'Jesus' : APage('Jesus', [], "Jesus; c. 4 BC to AD 30–33), also referred to as Jesus of Nazareth or Jesus Christ, is the central figure of Christianity, whom the teachings of most Christian denominations hold to be the Son of God. Christians believe Jesus is the awaited Messiah (or Christ, the Anointed One) of the Old Testament." ), 
			'Dead End' : APage('Dead End', [], 'A cul-de-sac /ˈkʌldəsæk/, dead end (British, Hong Kong, Canadian, American, South African English, and Australian English, Hiberno-English), closed, no through road, a close (British, Canadian, and Australian English), no exit (New Zealand English) or court (American, Australian English) is a street with only one inlet/outlet. While historically built for other reasons, one of its modern uses is to calm vehicle traffic.')}

def page(title):
	if title in all_pages:
		return all_pages[title]
	else:
		return APage(title, ['Dead End'], "Looks like you're off the beaten path!")


