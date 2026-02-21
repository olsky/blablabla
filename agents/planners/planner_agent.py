from datetime import datetime
from validators.id_allocator import get_next_id

def plan_epic(title, description, user_input, model="gpt-4o", provider="openai"):
    """
    Simulates the Planner Agent.
    Takes user input and generates an Epic artifact (EP-XXXX).
    """
    epic_id = get_next_id('epics')
    
    epic = {
        "id": epic_id,
        "title": title,
        "description": f"{description}\n\nGenerated from: {user_input}",
        "created_at": datetime.now().date().isoformat(),
        "created_by": {
            "agent": "planner",
            "model": model,
            "provider": provider,
            "temperature": 0.2
        },
        "status": "draft",
        "linked_stories": [],
        "review_policy": {
            "min_reviews": 3,
            "approval_threshold": 0.75,
            "require_blocking_clearance": True
        }
    }
    
    return epic

if __name__ == '__main__':
    # usage example
    epic = plan_epic(
        title="Implement Auth Gateway", 
        description="A unified auth gateway intercepting all requests.",
        user_input="We need an API gateway that handles JWT auth before hitting backend services."
    )
    import yaml
    print(yaml.dump(epic, sort_keys=False))
