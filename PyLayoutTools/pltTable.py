class pltTable:
	def __init__(self, title: str, headers: list[str], *data: list[str]):
		self.title = title
		self.headers = headers
		self.data = list(data)

	def _column(self, i):
		return [self.headers[i]] + [row[i] for row in self.data]

	def draw(self):
		columnwidths = []

		for i in range(0, len(self.headers)):
			columnwidths.append(max([len(j) for j in self._column(i)]))

		bar = "+" + ("-" * (sum(columnwidths) + (3*len(self.headers)) - 1)) + "+"

		output = []

		output.append(bar)
		output.append(f"| {' | '.join([item + (' ' * (columnwidths[idx] - len(item))) for idx, item in enumerate(self.headers)])} |")
		output.append(bar)
		for row in self.data:
			output.append(f"| {' | '.join([item + (' ' * (columnwidths[idx] - len(item))) for idx, item in enumerate(row)])} |")
		output.append(bar)

		return '\n'.join(output)

	def __call__(self):
		return self.draw()
		# return max([len(i) for i in ([self.headers[1]] + [item[1] for item in self.data])])
		# return ([self.headers[1]] + [item[1] for item in self.data])