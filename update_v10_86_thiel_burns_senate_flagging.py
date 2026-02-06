#!/usr/bin/env python3
"""Update dashboard with Thiel-Burns-Epstein meeting, Senate letter re FBI flagging Trump mentions — v10.86"""
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
timeline_entries = """  {date:'2014-09-13',event:'Epstein schedule: "2-4:00pm Appt w/Peter Thiel. 3-4:00pm Bill Burns will join Jeffrey and Peter Thiel meeting. 4-5:00pm Meeting with Bill Burns alone." Staff instructed to drive Burns to airport. That evening: dinner with Woody Allen, JE to invite Kathy Ruemmler and Peter Thiel.',source:'EFTA00362678'},
  {date:'2025-07-18',event:'Senate Judiciary Ranking Member Durbin writes AG Bondi demanding answers on FBI review: "My office was told that these personnel were instructed to flag any records in which President Trump was mentioned." Also: ~1,000 FBI personnel on 24-hour shifts, modified surveillance video, no client list found.',source:'EFTA00173350'},
"""

# New FINDINGS entries
findings_entries = """  {id:'thiel-burns-epstein-joint-meeting-sept2014',dataset:'DS9-Email',pages:5,severity:10,keywords:['peter thiel','bill burns','cia director','epstein','meeting','kathy ruemmler','woody allen','bob kraft','september 2014'],summary:'CRITICAL -- PRIMARY SOURCE: Epstein\\'s detailed weekly schedule (EFTA00362678, 5 pages, September 11-30, 2014). Saturday September 13, 2014 in New York: "2-4:00pm Appt w/Peter Thiel" then "3-4:00pm Bill Burns will join Jeffrey and Peter Thiel meeting" then "4-5:00pm Meeting with Bill Burns alone." Staff instructed: "MVO YOU ARE TO TAKE BILL BURNS TO THE AIRPORT AFTER HIS MEETING WITH JEFFREY." That evening: "7:30pm DINNER w/Woody Allen (JE to invite Kathy Ruemmler and Peter Thiel to dinner)." Sunday Sept 14: "TBD TENTATIVE LUNCH w/Bob Kraft (Maybe Peter Thiel)." This documents: (1) PETER THIEL -- billionaire Trump ally, JD Vance\\'s political mentor and financial backer, co-founder of Palantir -- in a scheduled 2-hour meeting with Epstein; (2) BILL BURNS -- then-Deputy Secretary of State, later CIA Director (2021-2025) -- joining the Thiel-Epstein meeting for an hour, then meeting Epstein alone for another hour; (3) KATHY RUEMMLER -- former Obama White House Counsel -- invited to dinner same evening; (4) BOB KRAFT -- Patriots owner, close Trump friend -- tentative lunch next day. All at Epstein\\'s residence, SIX YEARS after Epstein\\'s 2008 conviction. [v10.86]',date:'2014-09-13',type:'email-evidence'},
  {id:'senate-judiciary-fbi-flagging-trump-mentions-1000-personnel',dataset:'DS11-Legal',pages:5,severity:10,keywords:['senate judiciary','durbin','bondi','fbi','flag','trump','1000 personnel','24-hour shifts','client list','modified video','surveillance'],summary:'CRITICAL -- PRIMARY SOURCE: Senate Judiciary Committee letter from Ranking Member Richard J. Durbin to AG Pam Bondi (EFTA00173350, 5 pages, July 18, 2025). Key findings: (1) "My office was told that these personnel were instructed to FLAG any records in which President Trump was mentioned" -- FBI reviewers were specifically flagging Trump\\'s name in Epstein files; (2) Bondi pressured FBI to put ~1,000 IMD personnel on 24-hour shifts to review ~100,000 Epstein records over two weeks in March 2025; (3) Hundreds of FBI NY Field Office personnel added who "lacked the expertise to identify statutorily-protected information regarding child victims"; (4) Surveillance footage from outside Epstein\\'s cell described by DOJ as "full raw" was actually MODIFIED per embedded metadata (Wired reporting); (5) Bondi publicly claimed "client list" was "sitting on my desk" on Feb 21, but DOJ found "no incriminating client list" on July 7; (6) 13 detailed questions demanding accountability including: "What happened to the records mentioning President Trump once they were flagged?" and "Is there a log of the records mentioning President Trump?" Letter signed by Durbin, cc\\'d to Chairman Grassley. Routed to DOJ Office of Legislative Affairs. [v10.86]',date:'2025-07-18',type:'senate-letter'},
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
count = content.count('v10.85')
print(f"Replacing {count} occurrences of 'v10.85' with 'v10.86'")
content = content.replace('v10.85', 'v10.86')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.86.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.85')
new_ver = verify.count('v10.86')
print(f"Remaining v10.85: {remaining}")
print(f"Total v10.86: {new_ver}")

for check_id in ['thiel-burns-epstein-joint-meeting-sept2014',
                  'senate-judiciary-fbi-flagging-trump-mentions-1000-personnel']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
