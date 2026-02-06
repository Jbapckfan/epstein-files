#!/usr/bin/env python3
"""Update dashboard with complete Peter Thiel-Epstein relationship timeline — v10.87"""
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
timeline_entries = """  {date:'2014-06-09',event:'Peter Thiel dinner at Epstein\\'s 71st Street residence. Direct email: Thiel: "sorry for being so awol...are you planning on a dinner on the 9th?" Epstein: "Yes, what time good for you?" Thiel: "maybe 8pm?" Epstein: "done, see you then." Thiel\\'s assistant confirms "Peter is looking forward to this and has asked if he may bring a guest?" Schedule shows: "8:00pm DINNER w/Peter Thiel and Ehud Barak."',source:'EFTA00368250'},
  {date:'2016-04-08',event:'Lunch at Peter Thiel\\'s office in San Francisco. Email from "Peter Thiel Admin": "Lunch | Peter Thiel & Jeffrey Epstein" at Thiel Capital Office, 1 Letterman Drive, Suite 400, San Francisco. 12:00 PM PDT.',source:'EFTA00326659'},
  {date:'2017-08-18',event:'Epstein calendar: "1:00pm LUNCH w/Peter Thiel." Relationship continues three years after the Burns joint meeting.',source:'EFTA02220083'},
"""

# New FINDINGS entries
findings_entries = """  {id:'thiel-epstein-direct-email-dinner-june2014',dataset:'DS9-Email',pages:3,severity:10,keywords:['peter thiel','epstein','email','dinner','ehud barak','71st street','june 2014','talia','guest'],summary:'CRITICAL -- PRIMARY SOURCE: Direct email chain between Peter Thiel and Jeffrey Epstein (EFTA00368250, 3 pages, June 5-6, 2014). Full exchange: Thiel: "sorry for being so awol. hope you are well. are you planning on a dinner on the 9th?" Epstein: "Yes, what time good for you?" Thiel: "maybe 8pm?" Epstein: "done, see you then." Thiel\\'s assistant Talia then emails Groff: "Peter is looking forward to this and has asked if he may bring a guest?" Dinner at 9 East 71st Street. Confirmed by schedule (EFTA00368287): "8:00pm DINNER w/Peter Thiel and Ehud Barak." This proves DIRECT personal email communication between Thiel and Epstein, with a casual tone suggesting routine social contact. The dinner included Ehud Barak (former Israeli PM). All SIX YEARS after Epstein\\'s 2008 conviction. [v10.87]',date:'2014-06-09',type:'email-evidence'},
  {id:'thiel-epstein-lunch-thiel-capital-sf-april2016',dataset:'DS9-Email',pages:1,severity:10,keywords:['peter thiel','epstein','lunch','thiel capital','san francisco','letterman drive','april 2016'],summary:'CRITICAL -- PRIMARY SOURCE: Email from Peter Thiel Admin (EFTA00326659, 1 page, April 7-8, 2016). Subject: "Lunch | Peter Thiel & Jeffrey Epstein." Location: Thiel Capital Office, 1 Letterman Drive, Suite 400, San Francisco, CA. Date: April 8, 2016, 12:00 PM PDT. This is significant because: (1) Epstein traveled to SAN FRANCISCO specifically to meet Thiel -- not a casual encounter; (2) Meeting at Thiel\\'s own corporate office, not a neutral venue; (3) Thiel\\'s staff organized the meeting -- institutional, not purely personal; (4) EIGHT YEARS after Epstein\\'s 2008 conviction. Thiel Capital is Peter Thiel\\'s personal investment firm. [v10.87]',date:'2016-04-08',type:'email-evidence'},
  {id:'thiel-epstein-lunch-august2017',dataset:'DS9-Email',pages:1,severity:9,keywords:['peter thiel','epstein','lunch','august 2017','calendar'],summary:'HIGH VALUE -- PRIMARY SOURCE: Epstein calendar entry (EFTA02220083, 1 page, August 18, 2017). Entry reads: "1:00pm LUNCH w/Peter Thiel." This establishes continued contact as late as August 2017 -- NINE YEARS after Epstein\\'s 2008 conviction and less than two years before Epstein\\'s July 2019 arrest. The relationship persisted across at least 4 years of documented meetings. [v10.87]',date:'2017-08-18',type:'email-evidence'},
  {id:'thiel-epstein-complete-relationship-v1087',dataset:'DS9-Combined',pages:0,severity:10,keywords:['peter thiel','epstein','complete','relationship','burns','cia','barak','thiel capital','palantir','jd vance','dinner','lunch','2014','2016','2017'],summary:'STRUCTURAL FINDING -- PETER THIEL-EPSTEIN COMPLETE RELATIONSHIP compiled from 6+ primary source documents spanning June 2014 through August 2017: (1) June 9, 2014: Direct email exchange -- Thiel: "sorry for being so awol...dinner on the 9th?" Epstein: "done, see you then." Dinner with Ehud Barak at 71st Street (EFTA00368250, EFTA00368287); (2) September 13, 2014: TWO-HOUR scheduled meeting at Epstein\\'s NYC residence, then CIA Deputy Secretary Bill Burns joins for one hour, then Burns meets Epstein alone for another hour. That evening: dinner with Woody Allen, Thiel invited (EFTA00362678); (3) September 14, 2014: Tentative lunch with Bob Kraft, "Maybe Peter Thiel" (EFTA00362678); (4) April 8, 2016: Lunch at THIEL CAPITAL OFFICE, 1 Letterman Drive, San Francisco -- Epstein traveled to Thiel\\'s corporate HQ (EFTA00326659); (5) August 18, 2017: "1:00pm LUNCH w/Peter Thiel" -- contact continues less than 2 years before arrest (EFTA02220083). KEY CONTEXT: Peter Thiel is co-founder of Palantir (major government surveillance contractor), was JD Vance\\'s political mentor and primary financial backer for his Senate campaign, and is one of the most influential figures in Trump\\'s political orbit. The Burns joint meeting is especially significant as Burns later served as CIA Director (2021-2025). All meetings occurred AFTER Epstein\\'s 2008 conviction and sex offender registration. The casual tone of emails ("sorry for being so awol") and meetings at Thiel\\'s own corporate office indicate a substantive, ongoing relationship -- not casual acquaintance. [v10.87]',date:'2017-08-18',type:'compiled-timeline'},
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
count = content.count('v10.86')
print(f"Replacing {count} occurrences of 'v10.86' with 'v10.87'")
content = content.replace('v10.86', 'v10.87')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.87.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.86')
new_ver = verify.count('v10.87')
print(f"Remaining v10.86: {remaining}")
print(f"Total v10.87: {new_ver}")

for check_id in ['thiel-epstein-direct-email-dinner-june2014',
                  'thiel-epstein-lunch-thiel-capital-sf-april2016',
                  'thiel-epstein-lunch-august2017',
                  'thiel-epstein-complete-relationship-v1087']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
