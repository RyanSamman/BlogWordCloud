import json # Library for parsing JSON files
from os import path
from PIL import Image # Python Image Library

import numpy as np # Faster data structures 
import matplotlib.pyplot as plt # Used to display charts
from wordcloud import WordCloud, ImageColorGenerator

# Load Word/Frequency Data
with open("processedData.json", "r") as file:
    wordAndFrequencyData = json.load(file)

# Load Image which text will be superimposed onto
imageMask = np.array(Image.open(path.join("images", "FCITLogo.jpg")))

# Generate colors from Image
imageColors = ImageColorGenerator(imageMask)

# Create WordCloud object with image
wordCloudObject = WordCloud(scale=10, background_color="white", mask=imageMask) 

# Pass in Word: Frequency to be displayed
wordCloudObject.generate_from_frequencies(wordAndFrequencyData)

# Add the Color data to the Word Cloud
wordCloudObject.recolor(color_func=imageColors)

# Remove Axis markings
plt.axis("off")

# Display as Matplotlib Chart
plt.imshow(wordCloudObject, interpolation="bilinear")
plt.show()
