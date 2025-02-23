from PIL import Image

# Open the PNG file
png_image = Image.open("image.png")

# Save as ICNS format
png_image.save("image.icns", format="ICNS")

print("Conversion completed: image.icns")