#!/usr/bin/env python3
"""Update dashboard with Burns/Barr/Ruemmler/network findings — v10.73"""
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
timeline_entries = """  {date:'2014-09-02',event:'Epstein assistant emails Bob Kerrey (former Senator/9-11 Commission): "Jeffrey is having Peter Thiel and possibly Bill Burns for lunch at his home in NY on Sat Sept 13th...Jeffrey is asking if you might be available to join." Kerrey responds: "I think both work."',source:'EFTA00363688'},
  {date:'2014-09-21',event:'Epstein NY schedule master list: "People To See: Jagland, Terje, Thiel, Kathy, Cass, Woody, Ehud, Leon, Summers, Boris, Barbro, Bill Burns." Same day: Leon Black 11am, Peter Thiel lunch, Boris Nikolic 2pm.',source:'EFTA00362192'},
  {date:'2014-09-23',event:'Epstein schedule: 12pm Lunch with Ehud Barak. "1:00pm Kathy Ruemmler to join you and Ehud." Ruemmler was Obama White House Counsel, later Goldman Sachs General Counsel.',source:'EFTA00362192'},
  {date:'2014-09-24',event:'Epstein schedule: "5:00pm Appt w/Bill Burns" — standalone meeting. Burns was Deputy Secretary of State, later CIA Director (2021-2025). Note: "Kathy Ruemmler is in NY and would love to join" Jagland meeting.',source:'EFTA00362192'},
  {date:'2019-08-12',event:'AG William Barr announces "serious irregularities" at MCC after Epstein death. Guards placed on leave, warden reassigned. One guard wasnt a correctional officer. Epstein cellmate removed. 30-minute checks not performed.',source:'EFTA00092812'},
"""

# New FINDINGS entries
findings_entries = """  {id:'burns-thiel-kerrey-lunch-invite',dataset:'DS9-Email',pages:1,severity:9,keywords:['bill burns','peter thiel','bob kerrey','lunch','9-11 commission'],summary:'CRITICAL: Email from Epstein assistant to Bob Kerrey (former Senator, 9-11 Commission member), Sept 2, 2014. Subject: "Jeffrey Epstein." Text: "Jeffrey is having Peter Thiel and possibly Bill Burns for lunch at his home in NY on Sat. Sept 13th and Sun. Sept. 14th...Jeffrey is asking if you might be available to join." Kerrey responds: "I think both work but let me double check with Jen!" This documents Epstein hosting a power lunch bringing together Silicon Valley (Thiel), U.S. foreign policy (Burns, then Deputy SecState), and politics (Kerrey) at his home — all post-conviction. [v10.73]',date:'2014-09-02',type:'email-evidence'},
  {id:'burns-epstein-solo-sept24',dataset:'DS9-Schedule',pages:4,severity:8,keywords:['bill burns','cia','deputy secretary of state','leon black','thiel','ruemmler','summers'],summary:'HIGH VALUE: Epstein full week schedule Sept 21-26, 2014. Master "People To See" list: Jagland, Terje, Thiel, Kathy [Ruemmler], Woody, Ehud, Leon [Black], Summers, Boris [Nikolic], Bill Burns. Sept 21: Leon Black 11am, Peter Thiel lunch 12pm, Boris Nikolic 2pm. Sept 22: Larry Summers 3pm. Sept 23: Ehud Barak lunch, Kathy Ruemmler joins at 1pm. Sept 24: Bill Burns standalone 5pm meeting. Sept 25: Ehud Barak (Ruemmler joins). Shows Burns had MULTIPLE meetings with Epstein across one week, not just the Thiel joint meeting. [v10.73]',date:'2014-09-21',type:'schedule'},
  {id:'ruemmler-barak-epstein-meetings',dataset:'DS9-Schedule',pages:4,severity:7,keywords:['kathy ruemmler','ehud barak','obama','white house counsel','goldman sachs'],summary:'Kathy Ruemmler (Obama White House Counsel 2011-2014, later Goldman Sachs General Counsel) appears in 176 Epstein documents. Sept 23, 2014: "1:00pm Kathy Ruemmler to join you and Ehud [Barak]." Sept 24: "Kathy Ruemmler is in NY and would love to join" Jagland meeting. Sept 25: "Ehud Barak (Kathy Ruemmler is in NY and would love to join)." Oct 16, 2016: "3:30pm Appt w/Kathy Ruemmler." Nov 27, 2017: 1:30-2:30pm meeting. Continued personal relationship with convicted sex offender while serving as Goldman Sachs top lawyer. [v10.73]',date:'2014-09-23',type:'schedule'},
  {id:'barr-mcc-serious-irregularities',dataset:'DS9-DOJ',pages:2,severity:8,keywords:['william barr','mcc','epstein death','guards','irregularities','warden'],summary:'HIGH VALUE: WSJ reporting (Aug 13, 2019). AG William Barr cited "serious irregularities" at MCC Manhattan after Epstein death. Key facts: (1) Two guards placed on leave; (2) Warden Lamine N Diaye reassigned; (3) One guard wasnt a correctional officer (had transferred to different job); (4) Both guards working overtime; (5) Epstein cellmate removed — left alone and unsupervised; (6) 30-minute checks not performed as promised. Later: warden N Diaye being promoted to Fort Dix until Barr intervened. Guard Michael Thomas arrested. SDNY US Attorney Berman publicly asserted independence from Barr. [v10.73]',date:'2019-08-12',type:'news-reporting'},
  {id:'thiel-multi-day-sept2014',dataset:'DS9-Schedule',pages:5,severity:8,keywords:['peter thiel','leon black','boris nikolic','larry summers','bob kerrey','bill burns'],summary:'Sept 2014 shows Peter Thiel deeply embedded in Epstein social network. Sept 13: 2-4pm Thiel meeting (Burns joins at 3pm), dinner with Woody Allen (Thiel and Ruemmler invited). Sept 14: "TENTATIVE LUNCH w/Bob Kerrey (Maybe Peter Thiel)." Sept 21: Thiel lunch 12pm (same day as Leon Black 11am, Boris Nikolic 2pm). Feb 4, 2016: "9:30-11:30pm Appt w/Peter Thiel" then Leon Black at his office then Ehud Barak. Apr 8, 2016: Lunch at Thiel Capital Office. Aug 18, 2017: Lunch with Thiel. Pattern shows sustained multi-year relationship spanning 2014-2017. [v10.73]',date:'2014-09-13',type:'schedule'},
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
count = content.count('v10.72')
print(f"Replacing {count} occurrences of 'v10.72' with 'v10.73'")
content = content.replace('v10.72', 'v10.73')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.73 with Burns/Barr/network findings.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.72')
new_ver = verify.count('v10.73')
print(f"Remaining v10.72: {remaining}")
print(f"Total v10.73: {new_ver}")

for check_id in ['burns-thiel-kerrey-lunch-invite', 'burns-epstein-solo-sept24',
                  'ruemmler-barak-epstein-meetings', 'barr-mcc-serious-irregularities',
                  'thiel-multi-day-sept2014']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
