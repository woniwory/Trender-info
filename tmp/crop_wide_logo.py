from PIL import Image

src = r"C:\Users\user\.gemini\antigravity\brain\31a0c946-bf85-4574-9531-ab87d16a98ff\media__1773199909681.png"
dst = r"c:\Users\user\IdeaProjects\trender-intro\public\logo_nav_wide.png"

img = Image.open(src)
if img.mode != 'RGBA':
    img = img.convert('RGBA')

# Find bbox of non-transparent areas
bbox = img.getbbox()
if bbox:
    # Crop ONLY top and bottom
    # bbox = (left, top, right, bottom)
    # We want full width: left=0, right=img.width
    # We want tight vertical: top=bbox[1], bottom=bbox[3]
    top = bbox[1]
    bottom = bbox[3]
    
    # Add a tiny bit of padding to top/bottom for comfort
    pad = 10
    top = max(0, top - pad)
    bottom = min(img.height, bottom + pad)
    
    img_cropped = img.crop((0, top, img.width, bottom))
    img_cropped.save(dst)
    print(f"Wide logo cropped vertically and saved to {dst}. New size: {img_cropped.size}")
else:
    print("Error: No content found in image.")
