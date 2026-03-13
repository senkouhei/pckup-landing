import os
import shutil
import glob

dest_dir = r"c:\Users\admin\Documents\kouhei\pckup-landing\v7\images"
os.makedirs(dest_dir, exist_ok=True)

src_dir = r"C:\Users\admin\.gemini\antigravity\brain\86617e3e-c3ce-4e5f-9de7-445b2648d587"

files = {
    "hero_background": "hero_background.png",
    "who_we_are": "who_we_are.png",
    "services_isometric": "services_isometric.png",
    "why_us_command": "why_us_command.png"
}

for prefix, out_name in files.items():
    matches = glob.glob(os.path.join(src_dir, f"{prefix}_*.png"))
    if matches:
        shutil.copy(matches[0], os.path.join(dest_dir, out_name))
        print(f"Copied {matches[0]} to {out_name}")
