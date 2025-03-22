# main.py

## based on excel table like this
![excel table look](excel_look.png)
## from a template image
![template image](10.png)
## it generates image like this
![reference image](ref.png)
## and sends it to corresponding email


# config.py

##### configurations
* for image generation: fonts, colors, points/coordinates(where to draw text)
* SMTP(email) server login credentials
* mappings of excel columns to data types

# get_config.py

Was supposed to be a helper to get colors, drawing points and font sizes based of a reference image. (i don't rember... and don't know if it works properly.....)  
To run it, it needs an argument - reference image: ```python get_config.py ref.png```
