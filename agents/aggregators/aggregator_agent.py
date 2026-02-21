import glob
import yaml
import os

def aggregate_reviews(epic_id):
    """
    Simulates the Aggregator Agent.
    Reads all RV-XXXX.yaml files for a given EP-XXXX and produces the SUMMARY.yaml
    and decides on the State Transition.
    """
    review_files = glob.glob(f"project/reviews/{epic_id}/RV-*.yaml")
    
    total_score = 0
    total_weight = 0
    blocking = False
    advisories = 0
    
    for rf in review_files:
        with open(rf, 'r') as f:
            data = yaml.safe_load(f)
            
            if data['review_class'] == 'blocking':
                blocking = True
            elif data['review_class'] == 'advisory':
                advisories += 1
                
            if 'scores' in data and data.get('weight', 0) > 0:
                # average the scores in the review
                avg_score = sum(data['scores'].values()) / len(data['scores'])
                total_score += avg_score * data['weight']
                total_weight += data['weight']
                
    aggregated = 0
    if total_weight > 0:
        aggregated = total_score / total_weight
        
    summary = {
        "aggregated_score": round(aggregated, 2),
        "blocking_issues": blocking,
        "advisory_count": advisories,
        "reviews_processed": len(review_files)
    }
    
    return summary

if __name__ == '__main__':
    # Needs valid files on disk to run, dummy run:
    print(aggregate_reviews("EP-0001"))
