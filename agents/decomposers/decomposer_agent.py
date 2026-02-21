from datetime import datetime
from validators.id_allocator import get_next_id

def decompose_epic(epic_id, story_title, layer, acceptance_criteria, model="gpt-4o", provider="openai"):
    """
    Simulates the Decomposer Agent.
    Reads an Epic and breaks it down into User Stories (US-XXXX)
    stratified by architectural layer.
    """
    story_id = get_next_id('stories')
    
    story = {
        "id": story_id,
        "epic": epic_id,
        "title": story_title,
        "layer": layer,
        "stack": "TBD",
        "acceptance_criteria": acceptance_criteria,
        "created_at": datetime.now().date().isoformat(),
        "created_by": {
            "agent": "decomposer",
            "model": model,
            "provider": provider
        },
        "status": "draft"
    }
    
    return story

if __name__ == '__main__':
    story = decompose_epic(
        epic_id="EP-0001",
        story_title="JWT Validation Middleware",
        layer="gateway",
        acceptance_criteria=[
            "Must validate incoming JWT RS256 signatures",
            "Must extract tenant ID and attach to request headers",
            "Must return 401 Unauthorized on invalid tokens"
        ]
    )
    import yaml
    print(yaml.dump(story, sort_keys=False))
