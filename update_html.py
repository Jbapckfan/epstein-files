import json
import re
import sys

# Load JSON data
with open('/Users/jamesalford/epstein_jan30/outputs/red_flag_expanded.json', 'r') as f:
    data = json.load(f)

# Load HTML
with open('/tmp/epstein-files-update/red_flag_deepdive.html', 'r') as f:
    html = f.read()

# Sort by overall_severity descending
data.sort(key=lambda x: x['scores']['overall_severity'], reverse=True)

# Name mapping from JSON lowercase to display name
name_display = {
    'maxwell': 'Maxwell',
    'ghislaine': 'Ghislaine',
    'acosta': 'Acosta',
    'trump': 'Trump',
    'prince andrew': 'Prince Andrew',
    'brunel': 'Brunel',
    'dershowitz': 'Dershowitz',
    'clinton': 'Clinton',
    'sarah kellen': 'Sarah Kellen',
    'wexner': 'Wexner',
    'jes staley': 'Jes Staley',
    'bill richardson': 'Bill Richardson',
    'gates': 'Gates',
    'leon black': 'Leon Black',
    'spacey': 'Spacey',
    'george mitchell': 'George Mitchell',
    'woody allen': 'Woody Allen',
    'kushner': 'Kushner',
    'ehud barak': 'Ehud Barak',
    'obama': 'Obama',
    'biden': 'Biden',
    'bush': 'Bush',
    'musk': 'Musk',
    'chris tucker': 'Chris Tucker',
    'pence': 'Pence',
    'naomi campbell': 'Naomi Campbell',
    'tom hanks': 'Tom Hanks',
    'spielberg': 'Spielberg',
}

# Category mapping: JSON key -> HTML key
cat_map = {
    'rape_sexual_assault': 'rape',
    'minors_underage': 'minors',
    'trafficking': 'trafficking',
    'recruitment_grooming': 'grooming',
    'blackmail_kompromat': 'blackmail',
    'hidden_surveillance': 'surveillance',
    'murder_suspicious_death': 'murder',
    'threats_intimidation': 'threats',
    'witness_tampering': 'witness',
    'victim_named_them': 'victim_named',
    'flight_logs_travel': 'flight',
    'present_at_locations': 'locations',
    'named_in_black_book': 'black_book',
    'legal_political_cover': 'legal_cover',
    'financial_entanglement': 'financial',
    'intelligence_connection': 'intel',
}

# Exclude maxwell and ghislaine from the people array (as per existing pattern)
excluded = {'maxwell', 'ghislaine'}
people_for_array = [p for p in data if p['person'] not in excluded]

# Build the new var people array
lines = []
for p in people_for_array:
    name = name_display.get(p['person'], p['person'].title())
    s = p['scores']
    c = p['categories']
    
    cat_parts = []
    for json_key, html_key in cat_map.items():
        cat_parts.append(f'{html_key}:{c[json_key]}')
    cats_str = ','.join(cat_parts)
    
    line = (f'  {{ name:"{name}", overall:{s["overall_severity"]}, '
            f'crim:{s["criminal_conduct"]}, blkml:{s["blackmail_risk"]}, '
            f'invlv:{s["direct_involvement"]}, obstr:{s["obstruction_coverup"]},\n'
            f'    cats:{{{cats_str}}} }}')
    lines.append(line)

new_people_block = 'var people = [\n' + ',\n'.join(lines) + '\n];'

# Replace the var people block
pattern = r'var people = \[.*?\];'
html_new = re.sub(pattern, new_people_block, html, flags=re.DOTALL)

# Verify replacement happened
if 'var people = [' not in html_new:
    print("ERROR: var people block not found after replacement!")
    sys.exit(1)

# --- Update hero stats ---
# Compute total findings
total_findings = sum(sum(p['categories'].values()) for p in data)
# Round to nearest thousand for display
total_findings_display = (total_findings // 1000) * 1000
if total_findings_display == 0:
    total_findings_display = total_findings

# Get Maxwell and Ghislaine scores for the note
maxwell_sev = next(p['scores']['overall_severity'] for p in data if p['person'] == 'maxwell')
ghislaine_sev = next(p['scores']['overall_severity'] for p in data if p['person'] == 'ghislaine')

# Update hero stat data-count for findings
# Old: data-count="75000"  -> new value
html_new = re.sub(
    r'(<div class="stat-num" data-count=")75000(")',
    f'\\g<1>{total_findings_display}\\2',
    html_new
)

# Update the subtitle text about findings
html_new = re.sub(
    r'17 categories of analysis across 75,000\+ findings',
    f'17 categories of analysis across {total_findings_display:,}+ findings',
    html_new
)

# Update the footer/note with total findings 
html_new = re.sub(
    r'75,000\+ findings',
    f'{total_findings_display:,}+ findings',
    html_new
)

# Update Maxwell exclusion note - the note in the chart section
html_new = re.sub(
    r'Ghislaine Maxwell \(63,004\) and Maxwell \[combined references\] \(16,030\)',
    f'Ghislaine Maxwell ({maxwell_sev:,}) and Ghislaine [separate references] ({ghislaine_sev:,})',
    html_new
)

# Update the footer data line
html_new = re.sub(
    r'Maxwell \(63,004\) and Ghislaine \(16,030\)',
    f'Maxwell ({maxwell_sev:,}) and Ghislaine ({ghislaine_sev:,})',
    html_new
)

# --- Update Obama & Biden context section ---
obama_data = next((p for p in data if p['person'] == 'obama'), None)
biden_data = next((p for p in data if p['person'] == 'biden'), None)

if obama_data:
    s = obama_data['scores']
    c = obama_data['categories']
    
    # Update Obama score big
    html_new = re.sub(
        r'(<h4>Barack Obama</h4>\s*<div class="score-big" data-count=")11(")',
        f'\\g<1>{s["overall_severity"]}\\2',
        html_new
    )
    
    # Update Obama mentions
    html_new = re.sub(
        r'(Overall Severity &mdash; )517( raw mentions in corpus)',
        f'\\g<1>{obama_data["total_mentions"]:,}\\2',
        html_new,
        count=1
    )
    
    # Update Obama composite scores
    html_new = re.sub(
        r'(Criminal: <strong>)6(</strong> &bull; Blackmail: <strong>)2(</strong> &bull; Involvement: <strong>)0(</strong> &bull; Obstruction: <strong>)3(</strong>\s*</div>\s*<div class="context-cats">\s*<span class="cat-item">1 minors)',
        f'\\g<1>{s["criminal_conduct"]}\\g<2>{s["blackmail_risk"]}\\g<3>{s["direct_involvement"]}\\g<4>{s["obstruction_coverup"]}\\5',
        html_new,
        flags=re.DOTALL
    )

if biden_data:
    s = biden_data['scores']
    c = biden_data['categories']
    
    # Update Biden score big
    html_new = re.sub(
        r'(<h4>Joe Biden</h4>\s*<div class="score-big" data-count=")7(")',
        f'\\g<1>{s["overall_severity"]}\\2',
        html_new
    )
    
    # Update Biden mentions
    html_new = re.sub(
        r'(Overall Severity &mdash; )496( raw mentions in corpus)',
        f'\\g<1>{biden_data["total_mentions"]:,}\\2',
        html_new,
        count=1
    )

# --- Update excerpts section with new top_examples from JSON ---
# Build new excerpts object for people that have excerpts in the HTML
# Map JSON category names to display category names
cat_display = {
    'rape_sexual_assault': 'Rape / Sexual Assault',
    'minors_underage': 'Minors / Underage',
    'trafficking': 'Trafficking',
    'recruitment_grooming': 'Recruitment / Grooming',
    'blackmail_kompromat': 'Blackmail / Kompromat',
    'hidden_surveillance': 'Hidden Surveillance',
    'murder_suspicious_death': 'Murder / Suspicious Death',
    'threats_intimidation': 'Threats / Intimidation',
    'witness_tampering': 'Witness Tampering',
    'victim_named_them': 'Victim Named Them',
    'flight_logs_travel': 'Flight Logs / Travel',
    'present_at_locations': 'Present at Locations',
    'named_in_black_book': 'Named in Black Book',
    'legal_political_cover': 'Legal / Political Cover',
    'financial_entanglement': 'Financial Entanglement',
    'intelligence_connection': 'Intelligence Connection',
}

# The excerpt section shows top 6 associates (excluding Maxwell/Ghislaine)
# Priority categories: rape, minors, trafficking, blackmail, victim_named
priority_cats = ['rape_sexual_assault', 'minors_underage', 'trafficking', 'blackmail_kompromat', 'victim_named_them', 'recruitment_grooming']

excerpt_people = [p for p in people_for_array[:6]]  # Top 6 by severity

def build_excerpts_js(people_list):
    """Build the JavaScript excerpts object from JSON data."""
    parts = []
    for person in people_list:
        name = name_display.get(person['person'], person['person'].title())
        examples = person.get('top_examples', {})
        
        # Collect top examples from priority categories first, then others
        selected = []
        seen_docs = set()
        
        for cat in priority_cats:
            if cat in examples:
                for ex in examples[cat][:2]:  # Up to 2 per priority category
                    doc_key = (ex.get('doc_id', ''), ex.get('page', ''), cat)
                    if doc_key not in seen_docs:
                        seen_docs.add(doc_key)
                        selected.append((cat, ex))
                        if len(selected) >= 4:
                            break
            if len(selected) >= 4:
                break
        
        # If we don't have 4 yet, fill from remaining categories
        if len(selected) < 4:
            for cat, exs in examples.items():
                if cat not in priority_cats:
                    for ex in exs[:1]:
                        doc_key = (ex.get('doc_id', ''), ex.get('page', ''), cat)
                        if doc_key not in seen_docs:
                            seen_docs.add(doc_key)
                            selected.append((cat, ex))
                            if len(selected) >= 4:
                                break
                if len(selected) >= 4:
                    break
        
        # Build JS entries
        entries = []
        for cat, ex in selected[:4]:
            doc_id = ex.get('doc_id', 'unknown')
            page = str(ex.get('page', '?'))
            sev = ex.get('severity', 0)
            cat_name = cat_display.get(cat, cat)
            # Escape the excerpt text for JS
            text = ex.get('excerpt', '')
            # Truncate to reasonable length
            if len(text) > 300:
                text = text[:297] + '...'
            # Escape quotes and backslashes
            text = text.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ').replace('\r', '')
            text = text.replace('\u2019', '\u2019').replace('\u201c', '\u201c').replace('\u201d', '\u201d')
            
            entries.append(f'      {{ doc:"{doc_id}", page:"{page}", sev:{sev}, cat:"{cat_name}",\n        text:"{text}" }}')
        
        entries_str = ',\n'.join(entries)
        parts.append(f'    "{name}": [\n{entries_str}\n    ]')
    
    return '  var excerpts = {\n' + ',\n'.join(parts) + '\n  };'

new_excerpts = build_excerpts_js(excerpt_people)

# Replace the excerpts block
pattern_excerpts = r'  var excerpts = \{.*?\};'
html_new = re.sub(pattern_excerpts, new_excerpts, html_new, flags=re.DOTALL, count=1)

# Write updated HTML
with open('/tmp/epstein-files-update/red_flag_deepdive.html', 'w') as f:
    f.write(html_new)

print("SUCCESS: HTML file updated.")
print(f"\nTotal people in array: {len(people_for_array)}")
print(f"Total findings: {total_findings}")
print(f"Maxwell severity: {maxwell_sev}")
print(f"Ghislaine severity: {ghislaine_sev}")

# Print stats for verification
print("\n--- VERIFICATION: Top 5 people in updated array ---")
for p in people_for_array[:5]:
    name = name_display.get(p['person'], p['person'].title())
    s = p['scores']
    print(f"  {name}: overall={s['overall_severity']} crim={s['criminal_conduct']} blkml={s['blackmail_risk']} invlv={s['direct_involvement']} obstr={s['obstruction_coverup']}")
