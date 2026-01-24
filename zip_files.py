import zipfile
import os
import sys

# Ensure UTF-8 output for print statements
sys.stdout.reconfigure(encoding='utf-8')

try:
    files = ['index.html', 'style.css', 'script.js', 'รูปบัณฑิต.jpg']
    with zipfile.ZipFile('UPLOAD_TO_GITHUB.zip', 'w') as z:
        for f in files:
            if os.path.exists(f):
                print(f"Adding {f}")
                # Write file with explicit archive name to avoid encoding headers issue if possible, 
                # though modern zipfile handles utf-8 fine usually.
                z.write(f, arcname=f)
            else:
                print(f"Skipping {f} (Not found)")
    print("Zip created successfully.")
except Exception as e:
    print(f"Error: {e}")
