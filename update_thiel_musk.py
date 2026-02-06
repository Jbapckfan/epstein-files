#!/usr/bin/env python3
"""Update dashboard with Thiel/Musk/Lutnick findings — v10.72"""
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

# New TIMELINE entries — Thiel/Musk/Lutnick
timeline_entries = """  {date:'2011-07-17',event:'EDGE San Francisco Science Dinner: Epstein, Elon Musk, Talulah Musk, Sergey Brin, Larry Page, Sean Parker, Mark Zuckerberg, Daniel Kahneman on same guest list. John Brockman EDGE Foundation event.',source:'EFTA00430881'},
  {date:'2013-04-17',event:'Epstein email to Lesley Groff RE: Elon Musk. Musk assistant Mary Beth Brown declines NY dinner invite. Epstein: "see him at milken conference."',source:'EFTA00392060'},
  {date:'2014-06-05',event:'Direct email exchange: Peter Thiel to Epstein arranging dinner. Thiel: "maybe 8pm?" Epstein: "done, see you then." Dinner June 9 at 9 East 71st St (Epstein mansion).',source:'EFTA00368250'},
  {date:'2014-06-09',event:'Dinner at Epstein mansion: Peter Thiel and Ehud Barak. Thiel brought a guest. Talia Parnass (Thiel EA) confirmed arrangements.',source:'EFTA00368287'},
  {date:'2014-09-13',event:'Epstein schedule: 2-4pm Peter Thiel meeting. 3-4pm Bill Burns (future CIA Director) joins Thiel-Epstein meeting. 4-5pm Burns alone with Epstein. 7:30pm dinner with Woody Allen — Epstein to invite Kathy Ruemmler (Obama WH Counsel) and Thiel.',source:'EFTA00363098'},
  {date:'2016-04-08',event:'Epstein visits Thiel Capital Office, 1 Letterman Dr Suite 400, San Francisco. Lunch meeting. Email from Peter Thiel Admin confirming: "Lunch | Peter Thiel & Jeffrey Epstein."',source:'EFTA00326659'},
  {date:'2017-08-18',event:'Calendar alert: "1:00pm LUNCH w/Peter Thiel" — latest documented Epstein-Thiel meeting, during Trump presidency.',source:'EFTA02220083'},
  {date:'2020-10-19',event:'FBI NTOC intake: Caller reports Howard Lutnick (CEO Cantor Fitzgerald) was Epstein neighbor, suspicious financial activities at BGC Financial could be related to Epstein case. Caller has documentation.',source:'EFTA00020515'},
"""

# New FINDINGS entries — Thiel/Musk/Lutnick
findings_entries = """  {id:'thiel-epstein-direct-emails',dataset:'DS9-Email',pages:4,severity:9,keywords:['peter thiel','ehud barak','dinner','east 71st','talia parnass'],summary:'HIGH VALUE: Direct email chain between Jeffrey Epstein (jeevacation@gmail.com) and Peter Thiel, June 5-6, 2014. Thiel: "are you planning on a dinner on the 9th? I think that should work." Epstein: "Yes, what time good for you?" Thiel: "maybe 8pm?" Epstein: "done, see you then." Talia Parnass (Executive Assistant to Peter Thiel) confirmed dinner at 9 East 71st St (Epstein NYC mansion) June 9, 2014. Thiel asked to bring a guest. This is a PERSONAL email exchange, not through assistants. [v10.72]',date:'2014-06-06',type:'email-evidence'},
  {id:'thiel-epstein-barak-dinner',dataset:'DS9-Schedule',pages:2,severity:8,keywords:['peter thiel','ehud barak','dinner','barak'],summary:'Epstein daily schedule June 9, 2014: "8:00pm DINNER w/Peter Thiel and Ehud Barak." Thiel bringing a guest. Same day includes meetings with Peter Diamandis, Austin Hall, Eileen Alexanderson. Shows Thiel-Barak-Epstein triangle — former Israeli PM dining with Silicon Valley billionaire at convicted sex offenders home. [v10.72]',date:'2014-06-09',type:'schedule'},
  {id:'thiel-burns-epstein-meeting',dataset:'DS9-Schedule',pages:5,severity:9,keywords:['peter thiel','bill burns','cia','woody allen','kathy ruemmler','obama'],summary:'CRITICAL: Epstein schedule Sept 13, 2014. (a) "2-4:00pm Appt w/Peter Thiel"; (b) "3-4:00pm Bill Burns will join Jeffrey and Peter Thiel meeting"; (c) "4-5:00pm Meeting with Bill Burns alone"; (d) "JOJO YOU ARE TO TAKE BILL BURNS TO THE AIRPORT"; (e) "7:30pm DINNER w/Woody Allen (JE to invite Kathy Ruemmler and Peter Thiel to dinner)." Bill Burns later became CIA Director (2021-2025). Kathy Ruemmler was Obama White House Counsel. Leon Black met Epstein Sept 11. [v10.72]',date:'2014-09-13',type:'schedule'},
  {id:'thiel-capital-lunch',dataset:'DS9-Email',pages:2,severity:8,keywords:['peter thiel','thiel capital','san francisco','lunch'],summary:'HIGH VALUE: Email from "Peter Thiel Admin" to Epstein, April 7, 2016. Subject: "Lunch | Peter Thiel & Jeffrey Epstein." Meeting at Thiel Capital Office, 1 Letterman Drive, Building C, Suite 400, San Francisco, April 8 at 12:00 PM PDT. Detailed arrival instructions including parking, security check-in, photo ID. Epstein traveled to Thiels corporate HQ — not a casual encounter. [v10.72]',date:'2016-04-08',type:'email-evidence'},
  {id:'thiel-2017-lunch',dataset:'DS11-Schedule',pages:1,severity:9,keywords:['peter thiel','lunch','2017','trump presidency'],summary:'CRITICAL TIMING: Calendar alert dated August 18, 2017: "1:00pm LUNCH w/Peter Thiel." This is the LATEST documented Epstein-Thiel meeting — during the Trump presidency, after Thiel served on Trump transition team and was major donor. Thiel maintained relationship with convicted sex offender while serving as key Trump ally. [v10.72]',date:'2017-08-18',type:'schedule'},
  {id:'musk-epstein-email',dataset:'DS9-Email',pages:1,severity:7,keywords:['elon musk','milken conference','dinner','mary beth brown'],summary:'Email chain April 16-17, 2013. Subject: "Elon Musk." Epstein assistant Lesley Groff invited Musk to dinner party April 23. Musk assistant Mary Beth Brown declined: "I dont think Elon is going to make it to NY next week." Epstein replied to Groff: "see him at milken conference." Shows Epstein actively pursuing relationship with Musk, planning to intercept him at Milken Institute conference. [v10.72]',date:'2013-04-17',type:'email-evidence'},
  {id:'musk-edge-dinner-guest-list',dataset:'DS9-Email',pages:4,severity:6,keywords:['elon musk','talulah musk','sergey brin','larry page','sean parker','zuckerberg','edge'],summary:'EDGE San Francisco Science Dinner, July 17, 2011. John Brockman invitation list includes: Jeffrey Epstein, Elon Musk, Talulah Musk (then-wife), Sergey Brin, Larry Page, Sean Parker, Daniel Kahneman, Mark Zuckerberg, Anne Wojcicki, Evan Williams, Martin Nowak, and others. Helmand Palace restaurant, 2424 Van Ness Ave, SF. Epstein embedded in Silicon Valley elite circles via Brockman EDGE network. [v10.72]',date:'2011-07-17',type:'guest-list'},
  {id:'lutnick-fbi-ntoc-tip',dataset:'DS9-FBI',pages:2,severity:8,keywords:['howard lutnick','cantor fitzgerald','bgc financial','fbi','ntoc','neighbor'],summary:'HIGH VALUE: FBI National Threat Operations Center (NTOC) intake, Oct 19, 2020, Case 50D-NY-3027571. Caller from UK reported "Howard Lutnick, CEO of [Cantor Fitzgerald], who could be connected to Jeffrey Epstein." Caller worked in NY 2015-2017 for BGC Financial, witnessed financial irregularities. States "Cantor Fitzgerald, Howard Lutnick, was Jeffrey Epsteins neighbor and he believes some of the suspicious financial activities could be related to Epsteins case." Caller has documentation for FBI. Charity day alleged fraudulent. [v10.72]',date:'2020-10-19',type:'fbi-intake'},
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
count = content.count('v10.71')
print(f"Replacing {count} occurrences of 'v10.71' with 'v10.72'")
content = content.replace('v10.71', 'v10.72')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.72 with Thiel/Musk/Lutnick findings.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.71')
new_ver = verify.count('v10.72')
print(f"Remaining v10.71: {remaining}")
print(f"Total v10.72: {new_ver}")

for check_id in ['thiel-epstein-direct-emails', 'thiel-burns-epstein-meeting',
                  'thiel-capital-lunch', 'thiel-2017-lunch',
                  'musk-epstein-email', 'musk-edge-dinner-guest-list',
                  'lutnick-fbi-ntoc-tip']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
