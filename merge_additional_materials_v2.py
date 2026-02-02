#!/usr/bin/env python3
"""
Merge additional_materials_findings.json into red_flag_expanded.json.

Maps each finding's "term" to the correct person, then increments
the appropriate category counts based on keyword matches in the
finding's context/matched_line. Recalculates composite scores using
the user-specified formula.
"""

import json
import re
import copy
from collections import defaultdict

# ── File paths ──────────────────────────────────────────────────────
ADDITIONAL = "/Users/jamesalford/epstein_jan30/outputs/additional_materials_findings.json"
RED_FLAG   = "/Users/jamesalford/epstein_jan30/outputs/red_flag_expanded.json"
# We first restore from the backup (original file before any modification)
# Since the script already ran once, we need to undo. Let's check if backup exists.
import os

BACKUP = RED_FLAG + ".bak"

# ── Score formula ───────────────────────────────────────────────────
def calc_scores(cats):
    criminal_conduct = (
        cats.get("rape_sexual_assault", 0) * 3 +
        cats.get("minors_underage", 0) * 3 +
        cats.get("trafficking", 0) * 3 +
        cats.get("recruitment_grooming", 0) * 2
    )
    blackmail_risk = (
        cats.get("blackmail_kompromat", 0) * 5 +
        cats.get("hidden_surveillance", 0) * 4 +
        cats.get("flight_logs_travel", 0) * 2 +
        cats.get("present_at_locations", 0) * 2 +
        cats.get("named_in_black_book", 0) * 2
    )
    direct_involvement = (
        cats.get("victim_named_them", 0) * 5 +
        cats.get("rape_sexual_assault", 0) * 2 +
        cats.get("minors_underage", 0) * 2 +
        cats.get("flight_logs_travel", 0) * 3 +
        cats.get("present_at_locations", 0) * 3
    )
    obstruction_coverup = (
        cats.get("legal_political_cover", 0) * 3 +
        cats.get("witness_tampering", 0) * 4 +
        cats.get("threats_intimidation", 0) * 3 +
        cats.get("murder_suspicious_death", 0) * 2
    )
    overall_severity = criminal_conduct + blackmail_risk + direct_involvement + obstruction_coverup
    return {
        "criminal_conduct": criminal_conduct,
        "blackmail_risk": blackmail_risk,
        "direct_involvement": direct_involvement,
        "obstruction_coverup": obstruction_coverup,
        "overall_severity": overall_severity,
    }


# ── 1. Load data ────────────────────────────────────────────────────
with open(ADDITIONAL) as f:
    add_data = json.load(f)
findings = add_data["findings"]
print(f"Loaded {len(findings)} findings from additional_materials_findings.json")

# If backup exists, restore from it first; otherwise create backup
if os.path.exists(BACKUP):
    with open(BACKUP) as f:
        red_flag = json.load(f)
    print(f"Restored original data from backup ({BACKUP})")
else:
    with open(RED_FLAG) as f:
        red_flag = json.load(f)
    # Save backup
    with open(BACKUP, "w") as f:
        json.dump(red_flag, f, indent=2)
    print(f"Created backup at {BACKUP}")

print(f"Loaded {len(red_flag)} people from red_flag_expanded.json\n")

# Save original scores (from the OLD formula) for comparison
original_scores = {}
for entry in red_flag:
    original_scores[entry["person"]] = entry["scores"]["overall_severity"]

# Also compute what the NEW formula gives on the ORIGINAL categories (before increments)
new_formula_before = {}
for entry in red_flag:
    new_formula_before[entry["person"]] = calc_scores(entry["categories"])["overall_severity"]

# Keep a deep copy of categories before incrementing
cats_before = {}
for entry in red_flag:
    cats_before[entry["person"]] = copy.deepcopy(entry["categories"])

# ── 2. Build term -> person mapping ─────────────────────────────────
TERM_TO_PERSON = {
    "trump":          "trump",
    "clinton":        "clinton",
    "bush":           "bush",
    "acosta":         "acosta",
    "barr":           None,         # Not in red_flag list
    "dershowitz":     "dershowitz",
    "ghislaine":      "ghislaine",
    "maxwell":        "maxwell",
    "prince andrew":  "prince andrew",
    "spacey":         "spacey",
    "mossad":         None,
    "fbi":            None,
    "blackmail":      None,
    "conspiracy":     None,
    "immunity":       None,
    "massage":        None,
    "minor":          None,
    "murder":         None,
    "plea deal":      None,
    "recording":      None,
    "recruit":        None,
    "suicide":        None,
    "victim":         None,
}

# Build person name -> index lookup
person_idx = {}
for i, entry in enumerate(red_flag):
    person_idx[entry["person"]] = i

print("=" * 72)
print("TERM -> PERSON MAPPING")
print("=" * 72)
for term, person in sorted(TERM_TO_PERSON.items()):
    if person:
        in_list = "in red_flag" if person in person_idx else "NOT in red_flag (skip)"
        print(f"  {term:20s} -> {person} ({in_list})")
    else:
        print(f"  {term:20s} -> (generic keyword - applied by context)")
print()

# ── 3. Keyword -> category mapping ─────────────────────────────────
CATEGORY_RULES = [
    (re.compile(r'\b(rap[ei]|sexual\s*assault|molest|abus[ei])', re.I),        "rape_sexual_assault"),
    (re.compile(r'\b(minor|underage|under-age|child|girl|teen|young\s*wom)', re.I), "minors_underage"),
    (re.compile(r'\b(traffick)', re.I),                                         "trafficking"),
    (re.compile(r'\b(recruit|groom)', re.I),                                    "recruitment_grooming"),
    (re.compile(r'\b(blackmail|kompromat|leverage)', re.I),                     "blackmail_kompromat"),
    (re.compile(r'\b(recording|video|tape[sd]?\b|camera|surveillance)', re.I),  "hidden_surveillance"),
    (re.compile(r'\b(murder|kill[ei]|(?<!suicide\s)death|homicid)', re.I),      "murder_suspicious_death"),
    (re.compile(r'\b(threat|intimidat)', re.I),                                 "threats_intimidation"),
    (re.compile(r'\b(witness|tamper|obstruct)', re.I),                          "witness_tampering"),
    (re.compile(r'\b(plea|immunity|non-?prosecution|NPA\b|cover[\s-]*up)', re.I), "legal_political_cover"),
    (re.compile(r'\b(intelligen|mossad|cia\b|mi[56]\b|spy|espionag)', re.I),   "intelligence_connection"),
]

# Fallback: if no regex matched but the search term itself implies a category
TERM_FALLBACK_CAT = {
    "blackmail":  "blackmail_kompromat",
    "murder":     "murder_suspicious_death",
    "suicide":    "murder_suspicious_death",
    "minor":      "minors_underage",
    "recruit":    "recruitment_grooming",
    "recording":  "hidden_surveillance",
    "massage":    "rape_sexual_assault",
    "victim":     "rape_sexual_assault",
    "plea deal":  "legal_political_cover",
    "immunity":   "legal_political_cover",
    "mossad":     "intelligence_connection",
    "conspiracy": "legal_political_cover",
}

# Alias map for detecting persons in context text
ALIAS_MAP = {
    "ghislaine": "ghislaine", "maxwell": "maxwell",
    "prince andrew": "prince andrew", "dershowitz": "dershowitz",
    "acosta": "acosta", "trump": "trump", "clinton": "clinton",
    "bill clinton": "clinton", "hillary": "clinton",
    "obama": "obama", "bush": "bush", "spacey": "spacey",
    "kevin spacey": "spacey", "wexner": "wexner",
    "les wexner": "wexner", "gates": "gates", "bill gates": "gates",
    "brunel": "brunel", "jean-luc brunel": "brunel",
    "ehud barak": "ehud barak", "barak": "ehud barak",
    "leon black": "leon black", "richardson": "bill richardson",
    "bill richardson": "bill richardson",
    "george mitchell": "george mitchell", "mitchell": "george mitchell",
    "jes staley": "jes staley", "staley": "jes staley",
    "kellen": "sarah kellen", "sarah kellen": "sarah kellen",
    "kushner": "kushner", "musk": "musk",
    "naomi campbell": "naomi campbell", "campbell": "naomi campbell",
    "pence": "pence", "spielberg": "spielberg",
    "tom hanks": "tom hanks", "hanks": "tom hanks",
    "woody allen": "woody allen", "biden": "biden",
    "chris tucker": "chris tucker",
}

# ── 4. Process each finding ─────────────────────────────────────────
person_finding_counts = defaultdict(int)
person_category_increments = defaultdict(lambda: defaultdict(int))
skipped_no_person = 0
skipped_not_in_list = 0

def apply_finding_to_person(person, term, text):
    """Determine category increments for this finding and person."""
    global skipped_not_in_list
    if person not in person_idx:
        skipped_not_in_list += 1
        return

    person_finding_counts[person] += 1

    cats_matched = set()
    for regex, cat in CATEGORY_RULES:
        if regex.search(text):
            cats_matched.add(cat)

    # Fallback: if no category matched, use term-based fallback
    if not cats_matched and term in TERM_FALLBACK_CAT:
        cats_matched.add(TERM_FALLBACK_CAT[term])

    for cat in cats_matched:
        person_category_increments[person][cat] += 1


for finding in findings:
    term = finding["term"]
    person = TERM_TO_PERSON.get(term)
    text = (finding.get("context", "") + " " + finding.get("matched_line", "")).lower()

    if person is not None:
        # Direct person-term mapping
        apply_finding_to_person(person, term, text)
    else:
        # Generic keyword: find persons mentioned in context
        matched_persons = set()
        for alias, pname in ALIAS_MAP.items():
            if alias in text:
                matched_persons.add(pname)

        if not matched_persons:
            skipped_no_person += 1
            continue

        for mp in matched_persons:
            apply_finding_to_person(mp, term, text)

# ── 5. Apply increments to categories ──────────────────────────────
print("=" * 72)
print("FINDINGS MAPPED PER PERSON")
print("=" * 72)
for person in sorted(person_finding_counts, key=person_finding_counts.get, reverse=True):
    cats = person_category_increments[person]
    cat_str = ", ".join(f"{c}: +{v}" for c, v in sorted(cats.items(), key=lambda x: -x[1]) if v > 0)
    print(f"  {person:<20s}  {person_finding_counts[person]:>5d} findings   [{cat_str}]")

print(f"\n  Skipped (no person detected in context): {skipped_no_person}")
print(f"  Skipped (person not in red_flag list):   {skipped_not_in_list}")
total_mapped = sum(person_finding_counts.values())
print(f"  Total findings mapped:                   {total_mapped}")
print()

# Apply increments
for person, cats in person_category_increments.items():
    idx = person_idx[person]
    for cat, incr in cats.items():
        if cat in red_flag[idx]["categories"]:
            red_flag[idx]["categories"][cat] += incr

# ── 6. Recalculate composite scores ────────────────────────────────
for entry in red_flag:
    entry["scores"] = calc_scores(entry["categories"])

# ── 7. Save updated file ───────────────────────────────────────────
with open(RED_FLAG, "w") as f:
    json.dump(red_flag, f, indent=2)
print(f"Saved updated red_flag_expanded.json ({len(red_flag)} people)\n")

# ── 8. Before/after summary ────────────────────────────────────────
# For a fair comparison, we compare using the SAME formula on old vs new categories
after_scores = {}
for entry in red_flag:
    after_scores[entry["person"]] = entry["scores"]["overall_severity"]

# Sort by after score
ranked = sorted(after_scores.items(), key=lambda x: -x[1])

print("=" * 72)
print("TOP 10 — BEFORE vs AFTER overall_severity (same formula)")
print("  (Before = new formula on original categories)")
print("  (After  = new formula on incremented categories)")
print("=" * 72)
print(f"  {'#':>3}  {'Person':<20s}  {'Before':>10s}  {'After':>10s}  {'Change':>10s}  {'%':>7s}")
print(f"  {'---':>3}  {'-'*20:<20s}  {'-'*10:>10s}  {'-'*10:>10s}  {'-'*10:>10s}  {'-'*7:>7s}")
for i, (person, after) in enumerate(ranked[:10], 1):
    before = new_formula_before[person]
    change = after - before
    pct = (change / before * 100) if before > 0 else 0.0
    sign = "+" if change >= 0 else ""
    print(f"  {i:>3}  {person:<20s}  {before:>10,d}  {after:>10,d}  {sign}{change:>9,d}  {sign}{pct:.1f}%")

print()

# ── 9. Detailed category changes for top 5 ─────────────────────────
print("=" * 72)
print("CATEGORY INCREMENTS — TOP 5 CHANGED PEOPLE")
print("=" * 72)
changed_list = []
for person in after_scores:
    before = new_formula_before[person]
    after = after_scores[person]
    if after != before:
        changed_list.append((person, before, after, after - before))

changed_list.sort(key=lambda x: -x[3])

for person, before, after, change in changed_list[:5]:
    idx = person_idx[person]
    print(f"\n  {person.upper()} (overall: {before:,d} -> {after:,d}, +{change:,d})")
    cats_now = red_flag[idx]["categories"]
    cats_orig = cats_before[person]
    for cat in sorted(cats_now.keys()):
        diff = cats_now[cat] - cats_orig[cat]
        if diff > 0:
            print(f"    {cat:<30s}  {cats_orig[cat]:>6,d} -> {cats_now[cat]:>6,d}  (+{diff})")

print()

# ── 10. Full ranking change summary ────────────────────────────────
print("=" * 72)
print("ALL PEOPLE — SCORE CHANGES (sorted by overall_severity)")
print("=" * 72)
print(f"  {'#':>3}  {'Person':<20s}  {'Old Score':>10s}  {'New Score':>10s}  {'Delta':>10s}")
print(f"  {'---':>3}  {'-'*20:<20s}  {'-'*10:>10s}  {'-'*10:>10s}  {'-'*10:>10s}")
for i, (person, after) in enumerate(ranked, 1):
    before = new_formula_before[person]
    change = after - before
    sign = "+" if change > 0 else (" " if change == 0 else "")
    print(f"  {i:>3}  {person:<20s}  {before:>10,d}  {after:>10,d}  {sign}{change:>9,d}")
print()
