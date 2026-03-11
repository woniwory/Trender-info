from PIL import Image
import numpy as np

img = Image.open(r"c:\Users\user\IdeaProjects\trender-intro\public\logo_nav_wide.png")
data = np.array(img)

# Check if there are non-transparent pixels on the right half
mid = img.width // 2
right_half = data[:, mid:, 3]
non_zero = np.count_nonzero(right_half)

print(f"Non-zero pixels in right half: {non_zero}")

# If non-zero is small, then it's just the icon.
# Let's check the original image `media__1773199331128.png` which had text BELOW.
# horizontal logo usually has text to the RIGHT.
