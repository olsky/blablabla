import os
import glob
import re

epics_dir = "/Users/olsky/github/olsky/blablabla/project/epics"
reviews_dir = "/Users/olsky/github/olsky/blablabla/project/reviews"

epic_files = glob.glob(os.path.join(epics_dir, "EP-*.yaml"))
epics = []

for filepath in epic_files:
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            
            # Use regex to find score to avoid yaml dependency issues if any
            score_match = re.search(r'feasibility(?:_score)?:\s*([0-9.]+)(?:/10)?', content, re.IGNORECASE)
            id_match = re.search(r'id:\s*(EP-\d+)', content)
            title_match = re.search(r'title:\s*(.*?)\n', content)
            
            score = 0.0
            if score_match:
                score = float(score_match.group(1))
            
            epic_id = id_match.group(1) if id_match else os.path.basename(filepath).split('.')[0]
            title = title_match.group(1).strip() if title_match else ""
            
            # Simple extraction for ranking
            epics.append({
                'id': epic_id,
                'title': title,
                'score': score,
                'path': filepath
            })
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")

# Sort by score descending
epics.sort(key=lambda x: x['score'], reverse=True)

print("=== TOP 5 EPICS BY FEASIBILITY ===")
for e in epics[:5]:
    # Check existing reviews
    existing_reviews = glob.glob(os.path.join(reviews_dir, f"RV-{e['id']}-*.yaml"))
    next_num = len(existing_reviews) + 1
    
    print(f"{e['id']} | Score: {e['score']} | {e['title']}")
    print(f"  Next review file: RV-{e['id']}-{next_num:03d}.yaml")

