import imageio

# Read the PNG file
png_image = imageio.imread("image.png")

# Save as ICO format
imageio.imwrite("image.ico", png_image)


# imageio is a library that provides an easy interface to read and write images in various formats.
# The imread function reads an image from a file and returns it as a NumPy array.
# The imwrite function writes a NumPy array to a file in the specified format.
# In this case, we read a PNG image and write it as an ICO image.
