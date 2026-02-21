import os
from datetime import datetime

def generate_review(epic_id, review_class, summary, strengths, weaknesses, risks, recommendations, scores, weight, confidence, agent_name="reviewer-a", model="gpt-4o", provider="openai"):
    """
    Simulates a Review Agent evaluating an Epic and its linked Stories.
    """
    # Simple deterministic ID based on existing reviews for the epic
    review_dir = f"project/reviews/{epic_id}"
    os.makedirs(review_dir, exist_ok=True)
    
    existing = len([f for f in os.listdir(review_dir) if f.startswith('RV-') and f.endswith('.yaml')])
    review_id = f"RV-{epic_id}-{existing + 1:03d}"
    
    review_data = {
        "id": review_id,
        "epic": epic_id,
        "review_class": review_class,
        "summary": summary,
        "analysis": {
            "strengths": strengths,
            "weaknesses": weaknesses,
            "risks": risks,
            "recommendations": recommendations,
        },
        "scores": scores,
        "weight": weight,
        "confidence": confidence,
        "created_at": datetime.now().date().isoformat(),
        "created_by": {
            "agent": agent_name,
            "model": model,
            "provider": provider
        }
    }
    
    return review_data

if __name__ == '__main__':
    review = generate_review(
        epic_id="EP-0001",
        review_class="scoring",
        summary="Solid architectural approach but lacks UI alignment.",
        strengths=["Clear separation of concerns in the gateway."],
        weaknesses=["UI layer story is missing."],
        risks=["Potential latency increase due to double validation."],
        recommendations=["Add caching at the gateway layer."],
        scores={"security": 0.9, "performance": 0.6, "cross_layer_alignment": 0.4},
        weight=1.0,
        confidence=0.85
    )
    import yaml
    print(yaml.dump(review, sort_keys=False))
