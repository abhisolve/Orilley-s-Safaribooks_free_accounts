#!/bin/python3
"""
	Created By : llama | Sahil Shukla
	Website : https://llamasec.tk
	Twitter: https://twitter.com/iamllamma
	License : GNU General Public License v3 (GPL-3)
"""
import requests as r
import matplotlib.pyplot as plt 

COLLECTION = ['web', 'website', 'webapp', 'web app', 'develop',
		 'development', 'developer', 'work', 'company', 'design', 
		'logo design', 'logo', 'deployment', 'website design', 'website development', 
		'search engine optmization', 'seo', 'hosting', 'domain', 'packages', 'web hosting',
		'seo', 'sem', 'experience', 'beautiful', 'clients', 'process', 'steps', 'procedure',
		'php', 'mysql', 'droopal', 'wordpress', 'joomla', 'html5', 'html', 'css', 'consultation', 
		'chandigarh']


class KeywordAnalysis:
	def __init__(self):
		self.target_url = input("enter the target url ")
		self.target_text = r.get(self.target_url).text
		self.number_of = []
		self.of_what = []
		plt.show()
		self.analyize()

	def analyize(self):
		for i in range(len(COLLECTION)):
			print("checking for the word "+COLLECTION[i])
			print(self.target_text.count(COLLECTION[i]))
			self.number_of.append(self.target_text.count(COLLECTION[i]))
			self.of_what.append(COLLECTION[i])
		#print("done with the list")
		print("plotting graph")
		plt.bar(self.of_what, self.number_of)
		plt.xlabel("KEYWORDS")
		plt.xticks(self.of_what, fontsize=5, rotation=90)
		plt.ylabel("occurrence")
		plt.title = "MEHNAT"
		plt.show()

if __name__ == "__main__":
	a = KeywordAnalysis()
