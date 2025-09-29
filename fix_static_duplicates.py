import os
from pathlib import Path

STATIC_DIR = Path("siteapp/static")

# Keep track of seen relative paths
seen = {}

for root, dirs, files in os.walk(STATIC_DIR):
    for f in files:
        full_path = Path(root) / f
        rel_path = full_path.relative_to(STATIC_DIR)

        # If we've already seen this relative path, rename it
        if rel_path in seen:
            counter = 1
            new_name = f"{full_path.stem}-{counter}{full_path.suffix}"
            new_full_path = full_path.with_name(new_name)

            # Keep incrementing until unique
            while new_full_path.relative_to(STATIC_DIR) in seen:
                counter += 1
                new_name = f"{full_path.stem}-{counter}{full_path.suffix}"
                new_full_path = full_path.with_name(new_name)

            full_path.rename(new_full_path)
            rel_path = new_full_path.relative_to(STATIC_DIR)
            print(f"Renamed duplicate: {full_path} -> {new_full_path}")

        seen[rel_path] = True

print("All duplicates processed!")
