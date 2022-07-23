class RenderList:
    def __init__(self, type_list: str):
        self.type_list = "ol" if type_list == "ol" else "ul"

    def __call__(self, *args, **kwargs):
        rendered_string = '\n'.join([f'<li>{i}</li>' for i in args[0]])
        return f"""<{self.type_list}>\n{rendered_string}\n</{self.type_list}>"""


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)