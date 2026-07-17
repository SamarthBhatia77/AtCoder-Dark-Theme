import os
import sys

# Ensure pillow is installed
try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Pillow library not found. Installing pillow...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image, ImageDraw

def create_icon(size):
    # Create high-quality transparent RGBA canvas
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Scale factor based on standard 128px coordinates
    scale = size / 128.0
    
    # Background rounded rectangle: deep slate color with blue border
    r = int(24 * scale)
    draw.rounded_rectangle(
        [(int(4 * scale), int(4 * scale)), (int(124 * scale), int(124 * scale))],
        radius=r,
        fill=(15, 23, 42, 255), # #0f172a
        outline=(59, 130, 246, 255), # #3b82f6
        width=max(1, int(5 * scale))
    )
    
    # Draw letter 'A' in white
    a_left = (int(30 * scale), int(90 * scale))
    a_top = (int(50 * scale), int(38 * scale))
    a_right = (int(70 * scale), int(90 * scale))
    a_bar_l = (int(38 * scale), int(72 * scale))
    a_bar_r = (int(62 * scale), int(72 * scale))
    
    w = max(1, int(8 * scale))
    draw.line([a_left, a_top], fill=(248, 250, 252, 255), width=w, joint="round")
    draw.line([a_top, a_right], fill=(248, 250, 252, 255), width=w, joint="round")
    draw.line([a_bar_l, a_bar_r], fill=(248, 250, 252, 255), width=w, joint="round")
    
    # Draw letter 'C' in bright blue using arc
    c_box = [int(78 * scale), int(38 * scale), int(112 * scale), int(90 * scale)]
    # Pillow draw.arc starts from 0 degrees (east) and goes clockwise.
    # To draw a "C", we draw an arc from 45 degrees (bottom-rightish) to 315 degrees (top-rightish) clockwise.
    # Note: Pillow's arc behaves differently based on version. To make sure C is highly visible,
    # we can draw it as a thick arc.
    draw.arc(c_box, start=45, end=315, fill=(59, 130, 246, 255), width=w)
    
    return img

def main():
    # Change working directory to the directory of this script to avoid permission issues when run from elsewhere
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Ensure icons folder exists in the project root
    os.makedirs("icons", exist_ok=True)
    
    # Generate 16x16, 48x48, 128x128 versions
    for size in [16, 48, 128]:
        img = create_icon(size)
        img.save(f"icons/icon{size}.png")
        print(f"Successfully generated: icons/icon{size}.png")

if __name__ == "__main__":
    main()
