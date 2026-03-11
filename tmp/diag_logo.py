from PIL import Image
import sys

img = Image.open(r"C:\Users\user\.gemini\antigravity\brain\31a0c946-bf85-4574-9531-ab87d16a98ff\media__1773199909681.png")
if img.mode != 'RGBA':
    img = img.convert('RGBA')

# Get bbox of all non-transparent pixels
bbox = img.getbbox()
print(f"BBox: {bbox}")

# Sample a few pixels
data = img.getdata()
print(f"Sample 0: {data[0]}") # Top left
# Find some non-transparent pixels
for i in range(len(data)):
    if data[i][3] > 0:
        print(f"First non-transparent found at index {i}: {data[i]}")
        break
