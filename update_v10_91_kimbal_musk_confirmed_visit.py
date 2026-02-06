#!/usr/bin/env python3
"""Update dashboard with Kimbal Musk confirmed visit to Epstein's home Oct 7, 2012 — v10.91"""
import sys

filepath = '/Users/jamesalford/epstein_jan30/github_update/dashboard_v10_latest.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

def find_array_closing(content, array_name):
    marker = f"const {array_name} = ["
    start = content.find(marker)
    if start == -1:
        return -1
    bracket_pos = start + len(marker) - 1
    depth = 1
    i = bracket_pos + 1
    in_string = False
    string_char = None
    while i < len(content) and depth > 0:
        ch = content[i]
        if in_string:
            if ch == '\\':
                i += 2
                continue
            if ch == string_char:
                in_string = False
        else:
            if ch in ('"', "'", '`'):
                in_string = True
                string_char = ch
            elif ch == '[':
                depth += 1
            elif ch == ']':
                depth -= 1
                if depth == 0:
                    return i
        i += 1
    return -1

findings_close = find_array_closing(content, 'FINDINGS_DATA')
timeline_close = find_array_closing(content, 'TIMELINE_DATA')

print(f"FINDINGS_DATA closing at: {findings_close}")
print(f"TIMELINE_DATA closing at: {timeline_close}")

if findings_close == -1 or timeline_close == -1:
    print("ERROR: Could not find arrays!")
    sys.exit(1)

# New TIMELINE entries
timeline_entries = """  {date:'2012-09-27',event:'Four days after Elon\\'s visit, Epstein\\'s call list includes "Kimbal" alongside Boris and Leon Black. Assistant emails Kimbal Musk directly: "Jeffrey would like to speak with you when you have a moment."',source:'EFTA00404016/EFTA00404030'},
  {date:'2012-10-03',event:'Epstein\\'s assistant emails Kimbal Musk with subject "Jeffrey Epstein (again!)" -- multiple scheduling attempts for coffee. Staff also requests Kimbal\\'s cell number for Epstein\\'s directory.',source:'EFTA00403662/EFTA00403663/EFTA00403555'},
  {date:'2012-10-07',event:'Kimbal Musk CONFIRMED visit to Epstein\\'s NYC home: "Kimbal is now confirmed to come to your house at 11:30 on Sunday." Schedule shows: "11:30 Lunch w/Kimbal Musk and MAYBE Boris." Boris Nikolic (Bill Gates\\' science advisor, later named backup executor in Epstein\\'s will) may have attended.',source:'EFTA00403173/EFTA00403207'},
"""

# New FINDINGS entries
findings_entries = """  {id:'kimbal-musk-confirmed-visit-epstein-home-oct2012',dataset:'DS9-Email',pages:14,severity:10,keywords:['kimbal musk','elon musk','epstein','boris nikolic','71st street','october 2012','coffee','snacks','lunch','musk boys','cell number','confirmed'],summary:'CRITICAL -- PRIMARY SOURCE: Email chain documenting Epstein actively pursuing Kimbal Musk after Elon\\'s September 23 visit, culminating in confirmed October 7, 2012 visit to Epstein\\'s home (EFTA00403173-404030, 14 pages combined across 9 documents). COMPLETE TIMELINE: (1) Sept 21: Epstein emails Pritzker "the musk boys told me you are in town" (already documented in v10.90); (2) Sept 23: Elon visits with Talulah Riley, Kimbal does not attend; (3) Sept 27: Epstein\\'s call list includes "Kimbal" alongside Boris Nikolic and Leon Black (EFTA00404016). Same day, assistant emails Kimbal directly: "Jeffrey would like to speak with you when you have a moment. Could you please give him a call" (EFTA00404030); (4) Oct 2: Epstein\\'s staff requests "Kimbal Musk\\'s cell number" for directory (EFTA00403555); (5) Oct 3: Subject line "Jeffrey Epstein (again!)" -- assistant emails Kimbal that "Jeffrey cannot keep the 10am coffee date this Friday" and tries to reschedule for Saturday after 6pm or Sunday. Same day: "Can JE do coffee w/Kimbal Musk at 10am on Fri Oct. 5th?" (EFTA00403652, 403662, 403663); (6) Oct 4-5: Schedule revised multiple times, meeting moved to Sunday Oct 7 at 11:30am (EFTA00403463, 403491); (7) Oct 5: CONFIRMED -- "Kimbal is now confirmed to come to your house at 11:30 on Sunday" (EFTA00403173); (8) Oct 7: Schedule shows "11:30 Lunch w/Kimbal Musk and MAYBE Boris" -- Boris Nikolic (Bill Gates\\' science advisor, later named as BACKUP EXECUTOR in Epstein\\'s will). This trail is devastating because: (A) Epstein was ACTIVELY pursuing the relationship with Kimbal, not the other way around; (B) The "Jeffrey Epstein (again!)" subject line shows persistent, repeated outreach; (C) Both Musk brothers visited Epstein\\'s home within two weeks of each other; (D) Boris Nikolic\\'s potential presence connects this to the Gates orbit; (E) All of this was FOUR YEARS after Epstein\\'s 2008 conviction. Kimbal Musk is not just Elon\\'s brother but a significant figure: co-founder of The Kitchen Restaurant Group, board member of Tesla and SpaceX. [v10.91]',date:'2012-10-07',type:'email-evidence'},
"""

# Insert TIMELINE entries (before closing ])
content = content[:timeline_close] + "\n" + timeline_entries + content[timeline_close:]

# Re-find FINDINGS closing bracket (shifted by timeline insertion)
findings_close = find_array_closing(content, 'FINDINGS_DATA')
if findings_close == -1:
    print("ERROR: Could not find FINDINGS_DATA after timeline insert!")
    sys.exit(1)

# Insert FINDINGS entries (before closing ])
content = content[:findings_close] + "\n" + findings_entries + content[findings_close:]

# Version bump
count = content.count('v10.90')
print(f"Replacing {count} occurrences of 'v10.90' with 'v10.91'")
content = content.replace('v10.90', 'v10.91')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.91.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.90')
new_ver = verify.count('v10.91')
print(f"Remaining v10.90: {remaining}")
print(f"Total v10.91: {new_ver}")

for check_id in ['kimbal-musk-confirmed-visit-epstein-home-oct2012']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
print(f"Arrays at different positions: {f_close2 != t_close2}")
