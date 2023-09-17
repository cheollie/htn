from taipy import Gui

Gui(

page = """
# Getting started with Taipy GUI

My text: <|{text}|>

<|{text}|input|>

<|{variable}|slider|min=min_value|max=max_value|>
"""





).run() # use_reloader=True





