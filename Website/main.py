from taipy.gui import Gui

from taipy.gui import Html


text = "Original text"

html_page = Html("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>Alert Settings</title>
</head>
<body>
    <header>
        <h1>CleanCue Dashboard</h1>
    </header>
    <main>
        <div class="slider-container">
            <h2>Volume</h2>
            <div class="slider">
                <taipy:slider min="1" max="10">{value}</taipy:slider>
            </div>
        </div>
        <div class="slider-container">
            <h2>Duration before Alert (mins)</h2>
            <div class="slider">
               <taipy:slider min="0" max="120">{value}</taipy:slider>
            </div>
        </div>
        <div class="slider-container">
            <h2>Notifications</h2>
            <p>Plates/Bowls</p>
            <taipy:toggle lov="YES;NO">{value}</taipy:toggle>
            <p>Cutlery</p>
            <taipy:toggle lov="YES;NO">{value}</taipy:toggle>
            <p>Food</p>
           <taipy:toggle lov="YES;NO">{value}</taipy:toggle>
           
        </div>
    </main>
</body>
</html>


""")

my_theme = {
  "palette": {
    "background": {"default": "#556b2f"},
    "primary": {"main": "#8fbc8f"}
  }
}

:root{
    "padding": "30px",
}

Gui(html_page).run(theme=my_theme)


