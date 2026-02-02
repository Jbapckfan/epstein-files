#!/usr/bin/env python3
"""
Merge additional_materials_findings.json into red_flag_expanded.json.

Maps each finding's "term" to the correct person, then increments
the appropriate category counts based on keyword matches in the
finding's context/matched_line. Recalculates composite scores.
"""

import json
import re
import copy
from collections import defaultdict

# ── File paths ──────────────────────────────────────────────────────
ADDITIONAL = "/Users/jamesalford/epstein_jan30/outputs/additional_materials_findings.json"
RED_FLAG   = "/Users/jamesalford/epstein_jan30/outputs/red_flag_expanded.json"

# ── 1. Load data ────────────────────────────────────────────────────
with open(ADDITIONAL) as f:
    add_data = json.load(f)
findings = add_data["findings"]
print(f"Loaded {len(findings)} findings from additional_materials_findings.json")

with open(RED_FLAG) as f:
    red_flag = json.load(f)
print(f"Loaded {len(red_flag)} people from red_flag_expanded.json\n")

# Keep a deep copy so we can show before/after
red_flag_before = copy.deepcopy(red_flag)

# ── 2. Build term → person mapping ─────────────────────────────────
# Some terms map directly to a person; others are generic keywords
# that apply globally (not to a specific person).
TERM_TO_PERSON = {
    "trump":          "trump",
    "clinton":        "clinton",
    "bush":           "bush",
    "acosta":         "acosta",
    "barr":           "barr",       # Bill Barr – not in red_flag list, skip
    "dershowitz":     "dershowitz",
    "ghislaine":      "ghislaine",
    "maxwell":        "maxwell",
    "prince andrew":  "prince andrew",
    "spacey":         "spacey",
    "mossad":         None,         # generic intelligence keyword
    "fbi":            None,         # generic keyword
    "blackmail":      None,         # generic keyword
    "conspiracy":     None,         # generic keyword
    "immunity":       None,         # generic keyword
    "massage":        None,         # generic keyword
    "minor":          None,         # generic keyword
    "murder":         None,         # generic keyword
    "plea deal":      None,         # generic keyword
    "recording":      None,         # generic keyword
    "recruit":        None,         # generic keyword
    "suicide":        None,         # generic keyword
    "victim":         None,         # generic keyword
}

# Build person name -> index lookup
person_idx = {}
for i, entry in enumerate(red_flag):
    person_idx[entry["person"]] = i

print("=" * 72)
print("TERM → PERSON MAPPING")
print("=" * 72)
for term, person in sorted(TERM_TO_PERSON.items()):
    status = person if person else "(generic keyword – applied by context only)"
    in_list = "  ✓ in red_flag" if person and person in person_idx else ""
    if person and person not in person_idx:
        in_list = "  ✗ NOT in red_flag (will skip)"
    print(f"  {term:20s} → {status}{in_list}")
print()

# ── 3. Keyword → category mapping ──────────────────────────────────
# Each rule: (compiled regex, category_name)
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

# ── 4. Process each finding ─────────────────────────────────────────
person_finding_counts = defaultdict(int)
person_category_increments = defaultdict(lambda: defaultdict(int))
unmapped_terms = defaultdict(int)
skipped_no_person = 0
skipped_not_in_list = 0

for finding in findings:
    term = finding["term"]
    person = TERM_TO_PERSON.get(term)

    # For generic keywords, try to find person mentions in context
    text = (finding.get("context", "") + " " + finding.get("matched_line", "")).lower()

    if person is None:
        # Try to detect a person mentioned in the context
        matched_persons = []
        for pname in person_idx:
            # Use word boundary or partial match for multi-word names
            if pname in text:
                matched_persons.append(pname)
        # Also check common aliases
        alias_map = {
            "ghislaine": "ghislaine",
            "maxwell": "maxwell",
            "prince andrew": "prince andrew",
            "andrew": "prince andrew",
            "dershowitz": "dershowitz",
            "acosta": "acosta",
            "trump": "trump",
            "clinton": "clinton",
            "bill clinton": "clinton",
            "hillary": "clinton",
            "obama": "obama",
            "bush": "bush",
            "spacey": "spacey",
            "kevin spacey": "spacey",
            "wexner": "wexner",
            "les wexner": "wexner",
            "gates": "gates",
            "bill gates": "gates",
            "brunel": "brunel",
            "jean-luc brunel": "brunel",
            "ehud barak": "ehud barak",
            "barak": "ehud barak",
            "leon black": "leon black",
            "richardson": "bill richardson",
            "bill richardson": "bill richardson",
            "george mitchell": "george mitchell",
            "mitchell": "george mitchell",
            "jes staley": "jes staley",
            "staley": "jes staley",
            "kellen": "sarah kellen",
            "sarah kellen": "sarah kellen",
            "kushner": "kushner",
            "musk": "musk",
            "naomi campbell": "naomi campbell",
            "campbell": "naomi campbell",
            "pence": "pence",
            "spielberg": "spielberg",
            "tom hanks": "tom hanks",
            "hanks": "tom hanks",
            "woody allen": "woody allen",
            "biden": "biden",
            "chris tucker": "chris tucker",
        }
        for alias, pname in alias_map.items():
            if alias in text and pname not in matched_persons:
                matched_persons.append(pname)

        if not matched_persons:
            skipped_no_person += 1
            continue

        # Apply finding to all matched persons
        for mp in matched_persons:
            if mp not in person_idx:
                skipped_not_in_list += 1
                continue
            person_finding_counts[mp] += 1
            # Determine categories
            cats_matched = set()
            for regex, cat in CATEGORY_RULES:
                if regex.search(text):
                    cats_matched.add(cat)
            if not cats_matched:
                # If severity >= 10 and no specific category, give a general bump
                # based on the generic term itself
                term_cat_map = {
                    "blackmail": "blackmail_kompromat",
                    "murder": "murder_suspicious_death",
                    "suicide": "murder_suspicious_death",
                    "minor": "minors_underage",
                    "recruit": "recruitment_grooming",
                    "recording": "hidden_surveillance",
                    "massage": "rape_sexual_assault",
                    "victim": "rape_sexual_assault",
                    "plea deal": "legal_political_cover",
                    "immunity": "legal_political_cover",
                    "mossad": "intelligence_connection",
                    "conspiracy": "legal_political_cover",
                }
                if term in term_cat_map:
                    cats_matched.add(term_cat_map[term])

            for cat in cats_matched:
                person_category_increments[mp][cat] += 1
    else:
        # Direct person-term mapping
        if person not in person_idx:
            skipped_not_in_list += 1
            continue

        person_finding_counts[person] += 1

        # Determine which categories to increment
        cats_matched = set()
        for regex, cat in CATEGORY_RULES:
            if regex.search(text):
                cats_matched.add(cat)

        # If no specific category matched, still count it as a mention
        # but don't arbitrarily increment. The finding is tracked for count purposes.
        if not cats_matched:
            # Default: if the term itself hints at a category, use that
            pass

        for cat in cats_matched:
            person_category_increments[person][cat] += 1

# ── 5. Apply increments to red_flag_expanded ────────────────────────
print("=" * 72)
print("FINDINGS MAPPED PER PERSON")
print("=" * 72)
for person in sorted(person_finding_counts, key=person_finding_counts.get, reverse=True):
    cats = person_category_increments[person]
    cat_str = ", ".join(f"{c}: +{v}" for c, v in sorted(cats.items(), key=lambda x: -x[1]) if v > 0)
    print(f"  {person:20s}  {person_finding_counts[person]:5d} findings   [{cat_str}]")

print(f"\n  Skipped (no person in context):   {skipped_no_person}")
print(f"  Skipped (person not in list):     {skipped_not_in_list}")
print()

# Apply the increments
for person, cats in person_category_increments.items():
    idx = person_idx[person]
    for cat, incr in cats.items():
        if cat in red_flag[idx]["categories"]:
            red_flag[idx]["categories"][cat] += incr

# ── 6. Recalculate composite scores ────────────────────────────────
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

for entry in red_flag:
    entry["scores"] = calc_scores(entry["categories"])

# ── 7. Save updated file ───────────────────────────────────────────
with open(RED_FLAG, "w") as f:
    json.dump(red_flag, f, indent=2)
print(f"Saved updated red_flag_expanded.json ({len(red_flag)} people)\n")

# ── 8. Before/after summary for top 10 ─────────────────────────────
# Build before scores
before_scores = {}
for entry in red_flag_before:
    before_scores[entry["person"]] = entry["scores"]["overall_severity"]

after_scores = {}
for entry in red_flag:
    after_scores[entry["person"]] = entry["scores"]["overall_severity"]

# Sort by after score
ranked = sorted(after_scores.items(), key=lambda x: -x[1])

print("=" * 72)
print("TOP 10 — BEFORE vs AFTER overall_severity")
print("=" * 72)
print(f"  {'#':>3}  {'Person':<20s}  {'Before':>10s}  {'After':>10s}  {'Change':>10s}  {'%':>7s}")
print(f"  {'---':>3}  {'--------------------':<20s}  {'----------':>10s}  {'----------':>10s}  {'----------':>10s}  {'-------':>7s}")
for i, (person, after) in enumerate(ranked[:10], 1):
    before = before_scores[person]
    change = after - before
    pct = (change / before * 100) if before > 0 else float('inf')
    sign = "+" if change > 0 else ""
    print(f"  {i:>3}  {person:<20s}  {before:>10,d}  {after:>10,d}  {sign}{change:>9,d}  {pct:>6.1f}%")

print()

# Also show everyone who changed
print("=" * 72)
print("ALL PEOPLE WITH CHANGES")
print("=" * 72)
changed = [(p, before_scores[p], after_scores[p]) for p in after_scores if after_scores[p] != before_scores[p]]
changed.sort(key=lambda x: -(x[2] - x[1]))
for person, before, after in changed:
    change = after - before
    pct = (change / before * 100) if before > 0 else float('inf')
    print(f"  {person:<20s}  {before:>10,d} → {after:>10,d}  (+{change:,d}, {pct:.1f}%)")

if not changed:
    print("  (no changes)")
print()
