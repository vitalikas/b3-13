from classes import HTML, TopLevelTag, LevelTag, Tag

with HTML("html") as html_:

	with TopLevelTag("head") as head:
		with Tag("title") as title:
			title.text = "hello"
			head += title

		html_ += head

	with TopLevelTag("body") as body:
		with Tag("h1", klass=("main-text",)) as h1:
			h1.text = "test"
			body += h1

		with LevelTag("div", class_=("container", "container-fluid"), id="lead") as div:
			with Tag("p") as p:
				p.text = "another test"
				div += p
			with Tag("img", is_single=True, scr="/icon.png", data_image="responsive") as img:
				div += img

			body += div

		html_ += body

print(str(html_))