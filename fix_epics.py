import os
import yaml

epics_dir = "project/epics"
for i in range(21, 41):
    filename = f"EP-{i:04d}.yaml"
    filepath = os.path.join(epics_dir, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r') as f:
        content = f.read()
        
    # Find start of description
    desc_start = content.find("description: |")
    if desc_start == -1:
        continue
        
    # Split into lines
    lines = content.splitlines()
    new_lines = []
    metadata = {}
    in_description = False
    
    for line in lines:
        if line.startswith("description: |"):
            in_description = True
            new_lines.append(line)
            continue
            
        if in_description:
            # Check for metadata keys indented inside description
            stripped = line.strip()
            if stripped.startswith("**Created At:**"):
                date_val = stripped.split(":**")[1].strip().strip('"')
                metadata['created_at'] = date_val
                continue
            elif stripped.startswith("**Created By:**") or stripped.startswith("created_by:"):
                # We'll re-generate created_by or parse it
                # For simplicity, since I know what they are:
                metadata['created_by'] = {
                    "agent": "planner",
                    "model": "gpt-4o",
                    "provider": "openai"
                }
                in_description = False # Stop adding to description
                continue
            elif in_description and not line.startswith("  ") and line.strip() != "":
                # We hit a top-level key like status:
                in_description = False
                new_lines.append(line)
            elif in_description:
                new_lines.append(line)
        else:
            # We are outside description now
            # Skip lines that are part of the old indented created_by
            if "agent:" in line or "model:" in line or "provider:" in line or "temperature:" in line:
                continue
            new_lines.append(line)
            
    # Clean up empty lines at end of description
    while new_lines and new_lines[-1].strip() == "" and "description: |" not in new_lines[-1]:
        new_lines.pop()
        
    # Reconstruct with metadata at top level
    # Find where to insert metadata (before status or after description)
    status_idx = -1
    for idx, l in enumerate(new_lines):
        if l.startswith("status:"):
            status_idx = idx
            break
            
    if status_idx != -1:
        # Insert before status
        if 'created_at' in metadata:
            new_lines.insert(status_idx, f"created_at: \"{metadata['created_at']}\"")
            status_idx += 1
        if 'created_by' in metadata:
            new_lines.insert(status_idx, "created_by:")
            new_lines.insert(status_idx + 1, f"  agent: {metadata['created_by']['agent']}")
            new_lines.insert(status_idx + 2, f"  model: {metadata['created_by']['model']}")
            new_lines.insert(status_idx + 3, f"  provider: {metadata['created_by']['provider']}")
            
    final_content = "\n".join(new_lines) + "\n"
    with open(filepath, 'w') as f:
        f.write(final_content)

print("Fixed EPICs 0021-0040")
