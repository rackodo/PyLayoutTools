import textwrap

class box:
	def __init__(self, title: str, *content: str):
		self.title = title
		self.items = list(content)
		self.maxwidth = 80

	def draw(self):
		titleSpans = textwrap.wrap(self.title, self.maxwidth) # Split title into spans if it exceeds the max width limit
		itemSpans = []
		for i in self.items: # Loop over items
			for j in textwrap.wrap(i, self.maxwidth): # Loop over spans in that item (if it exceeds the max width, it'll be split into spans under the limit. if it doesn't, it'll just return itself)
				itemSpans.append(j)

		highestWidth = max([len(i) for i in titleSpans + itemSpans]) # Get the length of the longest number in the total spans. Should be equal to or below the max width limit.

		bar = "+" + ("-" * (highestWidth + 2)) + "+" 

		boxOutput = []

		boxOutput.append(bar)

		for span in titleSpans:
			boxOutput.append(f"| {span}{" " * (highestWidth - len(span))} |")

		boxOutput.append(bar)

		for span in itemSpans:
			boxOutput.append(f"| {span}{" " * (highestWidth - len(span))} |")

		boxOutput.append(bar)

		return '\n'.join(boxOutput)

	def __call__(self):
		return self.draw()