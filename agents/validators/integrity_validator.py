import glob
import yaml
import sys
import os

def check_integrity():
    epics = glob.glob('project/epics/*.yaml')
    stories = glob.glob('project/stories/*.yaml')
    
    existing_stories = set()
    for s in stories:
        basename = os.path.basename(s).replace('.yaml', '')
        existing_stories.add(basename)
        
    errors = 0
    
    for e in epics:
        with open(e, 'r') as fp:
            data = yaml.safe_load(fp)
            if not data:
                continue
                
            linked_stories = data.get('linked_stories', [])
            for ls in linked_stories:
                if ls not in existing_stories:
                    print(f"❌ Integrity Error in {e}: Linked story {ls} does not exist.")
                    errors += 1
                    
    # More checks can be added here (e.g., check if reviews reference existing epics)
    return errors

if __name__ == '__main__':
    errors = check_integrity()
    if errors > 0:
        sys.exit(1)
    else:
        print("Integrity checks passed.")
        sys.exit(0)
