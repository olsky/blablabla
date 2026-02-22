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
            score_match = re.search(r'feasibility(?:_score)?:\s*([0-9.]+)(?:/10)?', content, re.IGNORECASE)
            id_match = re.search(r'id:\s*(EP-\d+)', content)
            title_match = re.search(r'title:\s*(.*?)\n', content)
            
            score = float(score_match.group(1)) if score_match else 0.0
            epic_id = id_match.group(1) if id_match else os.path.basename(filepath).split('.')[0]
            title = title_match.group(1).strip() if title_match else ""
            
            epics.append({
                'id': epic_id,
                'title': title,
                'score': score,
                'path': filepath
            })
    except Exception as e:
        pass

epics.sort(key=lambda x: x['score'], reverse=True)

unreviewed = []
for e in epics:
    existing_reviews = glob.glob(os.path.join(reviews_dir, f"RV-{e['id']}-*.yaml"))
    
    # We want epics with no reviews, or at least top scored overall.
    if not existing_reviews:
        unreviewed.append(e)

print("=== TOP UNREVIEWED EPICS ===")
for e in unreviewed[:10]:
    print(f"{e['id']} | Score: {e['score']} | {e['title']}")
