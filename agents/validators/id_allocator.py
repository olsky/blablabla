import os
import glob
import re

def get_next_id(entity_type):
    """
    Git-safe Directory-Scan Sequential Allocation algorithm.
    Reads all files in project/{entity_type}/, calculates the max ID,
    and returns the next zero-padded ID.
    """
    prefixes = {
        'epics': 'EP',
        'stories': 'US',
        'overrides': 'OV'
    }
    
    prefix = prefixes.get(entity_type)
    if not prefix:
        raise ValueError("Invalid entity type for ID allocation")
        
    pattern = f"project/{entity_type}/{prefix}-*.yaml"
    files = glob.glob(pattern)
    
    max_id = 0
    regex = re.compile(rf"{prefix}-(\d+)\.yaml")
    
    for f in files:
        basename = os.path.basename(f)
        match = regex.match(basename)
        if match:
            num = int(match.group(1))
            if num > max_id:
                max_id = num
                
    next_id = max_id + 1
    return f"{prefix}-{next_id:04d}"

if __name__ == '__main__':
    # test dummy logic
    print("Next Epic ID:", get_next_id('epics'))
    print("Next Story ID:", get_next_id('stories'))
