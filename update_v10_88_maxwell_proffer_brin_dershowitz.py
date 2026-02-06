#!/usr/bin/env python3
"""Update dashboard with Maxwell proffer transcripts, Sergey Brin island witness, second Dershowitz victim — v10.88"""
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
timeline_entries = """  {date:'2025-07-24',event:'GHISLAINE MAXWELL PROFFER DAY 1 (263 pages): Maxwell cooperates with Deputy AG Todd Blanche and FBI. On Trump: "always very cordial and very kind to me," never observed inappropriate behavior, "absolutely never, in any context." On Dershowitz: confirmed as Epstein\\'s attorney who socialized with him, MARKED in Alfredo Rodriguez black book as "involved." On Bill Gates: confirms meeting, may have traveled with Epstein. On Bill Barr: "No" never met him. Mentions father Robert Maxwell\\'s intelligence background.',source:'PROFFER Day 1'},
  {date:'2025-07-25',event:'GHISLAINE MAXWELL PROFFER DAY 2 (156 pages): Maxwell confirms Bobby Kennedy (RFK Jr.) "knew" Epstein -- went on dinosaur bone hunting trip together in the Dakotas ~1993-94. Confirms meeting Elon Musk at Sergey Brin\\'s birthday party on Pigozzi\\'s Caribbean island ~2010, believes Epstein knew Musk. Tells Blanche: "some are in your cabinet" regarding men associated with Epstein. Admits: "He\\'s a disgusting guy who did terrible things to young kids." Clinton never went to the island.',source:'PROFFER Day 2'},
  {date:'2007-01-01',event:'Sergey Brin (Google co-founder) and Ann Wojcicki visit Epstein\\'s island St. Little James. A trafficking victim\\'s compensation claim states: "They observed that we did not speak and that we remained mute. They witnessed the trauma on our faces and in our eyes...They said nothing. They did nothing."',source:'EFTA00143433'},
"""

# New FINDINGS entries
findings_entries = """  {id:'maxwell-proffer-day1-trump-dershowitz-gates-july2025',dataset:'DS9-Legal',pages:263,severity:10,keywords:['ghislaine maxwell','proffer','todd blanche','trump','dershowitz','bill gates','bill barr','alfredo rodriguez','black book','fbi','deputy attorney general','massage','mar-a-lago','july 2025'],summary:'CRITICAL -- PRIMARY SOURCE: Ghislaine Maxwell Proffer Interview Day 1 (263 pages, July 24, 2025). Maxwell cooperates with Deputy AG Todd Blanche, FBI ASAC Spencer Horn, and Acting AAG Diego Pestana under recorded proffer agreement. KEY REVELATIONS: (1) TRUMP: Maxwell met Trump through her father Robert Maxwell ~1990, father "was friendly with him and liked him very much." "Trump was always very cordial and very kind to me." Asked if she ever observed Trump receive a massage: "Never." Asked if she ever heard Epstein say Trump did "anything inappropriate with masseuses or with anybody": "Absolutely never, in any context." Asked about Mar-a-Lago spa masseuses going to Epstein: "I don\\'t recall. Is it possible? Yes." Asked if she recruited masseuses from Mar-a-Lago for Epstein: "I\\'ve never recruited a masseuse from Mar-a-Lago for that, as far as I remember"; (2) DERSHOWITZ: Confirmed as Epstein\\'s attorney who also "socialized" with him. "Never" saw him do anything inappropriate. BUT -- in the Alfredo Rodriguez black book (Exhibit 52 at trial): "It includes Alan Dershowitz, for the record, who\\'s marked. I don\\'t remember what it does with Donald Trump"; (3) BILL GATES: Confirms meeting at TED conference, may have traveled with Epstein on his plane; (4) BILL BARR: "No" she never met him, never heard of Barr having role in Epstein plea deal; (5) Robert Maxwell\\'s intelligence: Maxwell discusses father\\'s WWII British intelligence background, "once you\\'ve been an intelligence officer, you\\'re kind of always." NOTE: Deputy AG Todd Blanche\\'s questioning pattern notably focuses on exonerating Trump while documenting other associates. This is the first time Maxwell has cooperated with DOJ. [v10.88]',date:'2025-07-24',type:'proffer-transcript'},
  {id:'maxwell-proffer-day2-rfk-musk-brin-cabinet-july2025',dataset:'DS9-Legal',pages:156,severity:10,keywords:['ghislaine maxwell','proffer','rfk jr','bobby kennedy','elon musk','sergey brin','pigozzi','cabinet','clinton','wexner','larry summers','young kids','dinosaur','dakotas','july 2025'],summary:'CRITICAL -- PRIMARY SOURCE: Ghislaine Maxwell Proffer Interview Day 2 (156 pages, July 25, 2025). KEY REVELATIONS: (1) RFK JR. (BOBBY KENNEDY): Maxwell confirms "Bobby knew Mr. Epstein." They went on a "dinosaur bone hunting" trip together in the Dakotas, approximately 1993-94. Maxwell knew Bobby\\'s wife Mary before they were married. When asked about "anything inappropriate with Mr. Kennedy and masseuses or young women on the trip," Maxwell says: "I never saw anything inappropriate with Mr. Kennedy." RFK Jr. is now HHS Secretary in Trump\\'s cabinet; (2) ELON MUSK: Maxwell confirms she met Musk at Sergey Brin\\'s birthday party on Mr. Pigozzi\\'s island in the Caribbean around 2010, stayed 3-4 days, "Mr. Musk was present for that." Asked if Epstein knew Musk: "I believe they did." Also mentions dinner with "Mr. Musk\\'s brother as well"; (3) CABINET BOMBSHELL: Maxwell tells Blanche directly: "some are in your cabinet, who you value as your coworkers" referring to powerful men who associated with Epstein. Adds: "They\\'re men that went and had a massage and maybe did something sexual"; (4) MAXWELL ADMITS: "He\\'s a disgusting guy who did terrible things to young kids" — Maxwell herself acknowledging Epstein abused children under oath; (5) WEXNER: Described as Epstein\\'s "closest friend in this time." Maxwell traveled with Wexner but Epstein said Wexner "didn\\'t want to be seen too much with me"; (6) CLINTON: Multiple trips, visited Chappaqua. Maxwell insists Clinton "never came to the island"; (7) LARRY SUMMERS mentioned alongside Clinton as attending. [v10.88]',date:'2025-07-25',type:'proffer-transcript'},
  {id:'victim-compensation-dershowitz-sergey-brin-island-oct2006-may2007',dataset:'DS9-Legal',pages:22,severity:10,keywords:['dershowitz','sergey brin','ann wojcicki','victim','compensation','island','trafficking','sexual assault','igor zinoviev','ghislaine maxwell','jean-luc brunel','lesley groff','blackberry','starvation','passport','jp morgan','2006','2007'],summary:'CRITICAL -- PRIMARY SOURCE: Victim Compensation Claim Form (EFTA00143433, 22 pages). A trafficking victim describes being trafficked by Epstein from October 2006 to May 2007. KEY REVELATIONS: (1) SECOND VICTIM NAMING DERSHOWITZ: "Epstein forced me to perform sexual acts with his lawyer friend, Alan Dershowitz" at Epstein\\'s mansion. Met Dershowitz on THREE occasions: at Epstein\\'s office in NY, a restaurant, and Epstein\\'s mansion. "Alan Dershowitz and [redacted] — I was sexually assaulted on one occasion." This is a SECOND victim (beyond Virginia Giuffre) independently naming Dershowitz as a sexual assailant; (2) SERGEY BRIN AND ANN WOJCICKI ON ISLAND: "I met Sergey and Anna when they came for the day to Epstein\\'s Island on 01/01/2007 to visit Epstein, Maxwell, and Jean-Luc Brunel." Victim states: "They observed that we did not speak and that we remained mute. They witnessed the trauma on our faces and in our eyes. Sergey and Anne witnessed our souls and bodies riddled with fear. They said nothing. They did nothing. They just continued to laugh and joke around us as if we were nothing"; (3) TRAFFICKING DETAILS: Passport confiscated on first plane trip. Raped daily, "sometimes up to thrice a day." Put on extreme starvation diet, forced to send nude weight-check photos to Lesley Groff. Tracked via Blackberry given by Epstein. Attempted to swim off island to escape -- bodyguard Igor Zinoviev confirmed her "attempt showed no greater level of distress than he\\'d seen in other girls throughout the years"; (4) JP MORGAN: "I\\'m assuming the payment made on my behalf came from Epstein\\'s JP Morgan account"; (5) WITNESS TAMPERING: $250,000 and $100,000 payments to witnesses during litigation. This document provides devastating corroboration of the Dershowitz allegations and places Google\\'s co-founder on Epstein\\'s island with visibly traumatized trafficking victims. [v10.88]',date:'2007-01-01',type:'victim-testimony'},
  {id:'maxwell-proffer-complete-analysis-v1088',dataset:'DS9-Combined',pages:0,severity:10,keywords:['maxwell','proffer','complete','trump','rfk','kennedy','musk','brin','dershowitz','gates','clinton','wexner','cabinet','blanche','cooperation','2025'],summary:'STRUCTURAL FINDING -- MAXWELL PROFFER COMPLETE ANALYSIS compiled from 419 pages of sworn cooperation testimony (July 24-25, 2025). Ghislaine Maxwell cooperated with Trump\\'s DOJ under a proffer agreement -- her first-ever cooperation with prosecutors. Interviewed by Deputy AG Todd Blanche (Trump\\'s former personal defense attorney), FBI ASAC Spencer Horn, and Acting AAG Diego Pestana. CRITICAL PATTERN: Blanche\\'s questioning systematically exonerates Trump (\"Did you ever observe President Trump receive a massage?\" \"Did you ever hear...anything inappropriate?\") while documenting other associates. Maxwell\\'s own responses nonetheless reveal: (A) RFK Jr. knew Epstein, traveled together on dinosaur hunting trip ~1993-94 -- RFK Jr. is now HHS Secretary; (B) Elon Musk met Maxwell at Sergey Brin\\'s birthday, Epstein knew Musk, Musk\\'s brother mentioned -- Musk heads DOGE; (C) \"Some are in your cabinet\" -- Maxwell directly tells Blanche that Trump cabinet members associated with Epstein; (D) Dershowitz marked as \"involved\" in Alfredo Rodriguez black book -- Dershowitz was Trump\\'s impeachment attorney; (E) Maxwell\\'s father Robert Maxwell had British intelligence background, \"once an intelligence officer, you\\'re kind of always\"; (F) Bill Gates may have traveled on Epstein\\'s plane; (G) Wexner was Epstein\\'s \"closest friend.\" CORROBORATION from EFTA00143433: A second trafficking victim (beyond Giuffre) independently names Dershowitz as sexual assailant AND places Sergey Brin/Ann Wojcicki on Epstein\\'s island with visibly traumatized victims on January 1, 2007. Combined with earlier dashboard findings: 8+ Trump flights on Epstein\\'s jet (SDNY), Bannon 9+ docs/flights/island/16hrs tape, Lutnick island visits/FBI money laundering, Thiel 6+ meetings/direct emails, Musk direct emails/dinner invitation, Burns-Thiel joint meeting. [v10.88]',date:'2025-07-25',type:'compiled-timeline'},
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
count = content.count('v10.87')
print(f"Replacing {count} occurrences of 'v10.87' with 'v10.88'")
content = content.replace('v10.87', 'v10.88')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.88.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.87')
new_ver = verify.count('v10.88')
print(f"Remaining v10.87: {remaining}")
print(f"Total v10.88: {new_ver}")

for check_id in ['maxwell-proffer-day1-trump-dershowitz-gates-july2025',
                  'maxwell-proffer-day2-rfk-musk-brin-cabinet-july2025',
                  'victim-compensation-dershowitz-sergey-brin-island-oct2006-may2007',
                  'maxwell-proffer-complete-analysis-v1088']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
