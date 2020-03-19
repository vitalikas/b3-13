class HTML:
	def __init__(self, html_tag, output="screen"):
		self.html_tag = html_tag
		self.children = []
		
		self.output = output
		self.file = None

	def __enter__(self):
		if self.output != "screen":
			self.file = open(self.output, "w")
		return self

	def __exit__(self, type, value, traceback):
		if self.file:
			self.file.write(str(self))
			self.file.close()

	def __iadd__(self, other):
		self.children.append(other)
		return self

	def __str__(self):
		opening = "<%s>\n" % self.html_tag
		internal = ""
		closing = "</%s>" % self.html_tag

		if self.children:
			for child in self.children:
				internal += str(child)

		html_element = opening + internal + closing

		return html_element


class TopLevelTag:
	def __init__(self, top_level_tag):
		self.top_level_tag = top_level_tag
		self.children = []

	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback): pass

	def __iadd__(self, other):
		self.children.append(other)
		return self

	def __str__(self):
		opening = "<%s>\n" % self.top_level_tag
		internal = ""
		closing = "</%s>\n" % self.top_level_tag

		if self.children:
			for child in self.children:
				internal += str(child)

		top_level_element = opening + internal + closing

		return top_level_element


class LevelTag:
	def __init__(self, level_tag, **kwargs):
		self.level_tag = level_tag
		self.children = []
		self.attributes = {}

		for attr, value in kwargs.items():
			if attr == "class_":
				attr = "class"
				value = " ".join(value)
			self.attributes[attr] = value

	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback): pass

	def __iadd__(self, other):
		self.children.append(other)
		return self

	def __str__(self):
		opening = "  <%s" % self.level_tag

		if self.attributes:
			for attr, value in self.attributes.items():
				opening += ' %s="%s"' % (attr, value)
		opening += '>\n'
		
		internal = ""
		closing = "  </%s>\n" % self.level_tag

		if self.children:
			for child in self.children:
				internal += str(child)

		level_element = opening + internal + closing

		return level_element


class Tag:
	def __init__(self, tag, is_single=False, **kwargs):
		self.tag = tag
		self.is_single = is_single
		self.children = []
		self.text = ""
		self.attributes = {}

		for attr, value in kwargs.items():
			if "_" in attr:
				attr = attr.replace("_","-")
			if attr == "klass":
				attr = "class"
				value = " ".join(value)
			self.attributes[attr] = value

	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback): pass

	def __iadd__(self, other):
		self.children.append(other)
		return self

	def __str__(self):
		opening = "  <%s" % self.tag
		if self.attributes:
			for attr, value in self.attributes.items():
				opening += ' %s="%s"' % (attr, value)
		opening += '>'
		
		internal = self.text

		closing = "</%s>\n" % self.tag

		if self.is_single: return opening + "\n"

		if self.children:
			for child in self.children:
				internal += str(child)

		_element = opening + internal + closing

		return _element