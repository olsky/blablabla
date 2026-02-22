#!/usr/bin/env python3
import yaml
import glob
import math
import re
import json
from pathlib import Path

epics_data = []
for path in sorted(glob.glob('project/epics/EP-*.yaml')):
    try:
        d = yaml.safe_load(Path(path).read_text())
        if not isinstance(d, dict) or 'id' not in d:
            continue
        bc = d.get('business_case', {})
        feas = d.get('feasibility_score', 5)
        rev = bc.get('first_year_revenue_usd', 0)
        roi = bc.get('roi_time_in_months', 12)
        users = bc.get('target_users_estimate', 10)
        
        timeline = str(d.get('implementation_timeline', '')).lower()
        mvp_w = 8
        m = re.search(r'mvp:\s*(\d+)\s*week', timeline)
        if m: 
            mvp_w = int(m.group(1))
        
        score = (feas*10) + (100/max(roi,0.5)) + (50/max(mvp_w,1)) + math.log10(max(rev,1))*5
        
        arpu = bc.get('average_customer_value_usd_per_month', 0)
        desc = str(d.get('description', ''))
        approach = str(d.get('solution', {}).get('approach', ''))
        tech = str(d.get('solution', {}).get('technical_stack', ''))
        problem = str(d.get('problem_statement', ''))
        revenue_model = str(d.get('solution', {}).get('revenue_model', ''))
        
        epics_data.append({
            'id': d['id'],
            'title': d.get('title',''),
            'score': round(score, 1),
            'feas': feas,
            'rev': int(rev),
            'roi': roi,
            'mvp': mvp_w,
            'users': users,
            'arpu': int(arpu),
            'description': desc,
            'approach': approach,
            'tech': tech,
            'problem': problem,
            'revenue_model': revenue_model
        })
    except Exception as e:
        pass

epics_data.sort(key=lambda x: x['score'], reverse=True)

# Print top 20
print("\n" + "="*150)
print("TOP 20 - STARTUP VIABLE EPICS (1 Dev + AI Coders)")
print("="*150)
print(f"{'Rank':<4} {'ID':<10} {'Score':<7} {'Feas':<5} {'MVP':<5} {'ROI':<6} {'Y1 Rev':<11} {'Users':<5} {'ARPU':<7} Title")
print("-"*150)

for i, e in enumerate(epics_data[:20], 1):
    title_short = e['title'][:45]
    print(f"{i:<4} {e['id']:<10} {e['score']:<7.1f} {e['feas']:<5.1f} {e['mvp']:<5}w {e['roi']:<6.1f}m ${e['rev']:<10,} {e['users']:<5} ${e['arpu']:<6} {title_short}")

print("\n" + "="*150)
print("DETAILED ANALYSIS: TOP 5")
print("="*150)

for rank, e in enumerate(epics_data[:5], 1):
    print(f"\n[#{rank}] {e['id']}: {e['title']}")
    print("-" * 150)
    print(f"\nSTARTUP VIABILITY SCORE: {e['score']:.1f}/100\n")
    
    print(f"METRICS:")
    print(f"  • Feasibility: {e['feas']}/10 | MVP: {e['mvp']} weeks | ROI: {e['roi']} months")
    print(f"  • Y1 Revenue: ${e['rev']:,} | Target Users: {e['users']} | ARPU: ${e['arpu']}/mo")
    print(f"  • Revenue per user (avg): ${e['rev'] // max(e['users'], 1) / 12:.0f}/mo/user")
    
    print(f"\nPROBLEM:")
    print(f"  {e['problem'][:200]}")
    
    print(f"\nSOLUTION APPROACH:")
    print(f"  {e['approach'][:200]}")
    
    print(f"\nTECH STACK:")
    print(f"  {e['tech'][:200]}")
    
    print(f"\nREVENUE MODEL:")
    print(f"  {e['revenue_model'][:200]}")

# Export top 10 for reference
top_10_ids = [e['id'] for e in epics_data[:10]]
with open('TOP_10_STARTUP_VIABLE.txt', 'w') as f:
    f.write("TOP 10 STARTUP-VIABLE EPICS:\n")
    for i, e in enumerate(epics_data[:10], 1):
        f.write(f"{i}. {e['id']}: {e['title']}\n")
        f.write(f"   Score: {e['score']} | Feas: {e['feas']}/10 | MVP: {e['mvp']}w | ROI: {e['roi']}m | Rev: ${e['rev']:,}\n\n")

print(f"\n✓ Saved top 10 list to TOP_10_STARTUP_VIABLE.txt")
