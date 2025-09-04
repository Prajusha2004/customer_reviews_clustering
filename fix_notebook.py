import os

file_path = "clusteringreviews.ipynb"
fixed_path = "clusteringreviews_fixed.ipynb"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

cleaned = []
for line in lines:
    if line.strip().startswith("<<<<<<<") or line.strip().startswith("=======") or line.strip().startswith(">>>>>>>"):
        continue
    cleaned.append(line)

with open(fixed_path, "w", encoding="utf-8") as f:
    f.writelines(cleaned)

print("✅ Fixed notebook saved to:", os.path.abspath(fixed_path))
