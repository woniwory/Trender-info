from PIL import Image

src = r"C:\Users\user\.gemini\antigravity\brain\31a0c946-bf85-4574-9531-ab87d16a98ff\media__1773199909681.png"
dst = r"c:\Users\user\IdeaProjects\trender-intro\public\logo_white.png"

img = Image.open(src)
if img.mode != 'RGBA':
    img = img.convert('RGBA')

# Crop to non-transparent bbox
bbox = img.getbbox()
if bbox:
    img = img.crop(bbox)
    img.save(dst)
    print(f"Logo cropped and saved to {dst}. BBox: {bbox}")
else:
    print("Error: No content found in image.")
