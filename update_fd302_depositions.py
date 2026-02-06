#!/usr/bin/env python3
"""Update dashboard with FD-302s, sworn depositions, court filings — v10.77"""
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
timeline_entries = """  {date:'2011-03-17',event:'FBI FD-302: Victim interviewed at US Consulate overseas (file 31E-MM-108062). Testifies Maxwell recruited her at Mar-a-Lago in Aug 1998-99 while working as locker room attendant age 15-16. Describes 50 surveillance cameras at Epstein Manhattan residence and witness tampering by attorney.',source:'EFTA00269967'},
  {date:'2009-05-01',event:'Jane Doe 102 federal complaint filed (Case 9:09-cv-80656). Alleges 15-year-old recruited by Maxwell at Mar-a-Lago while earning $9/hour. Epstein asked her to quit Mar-a-Lago and travel with him. Trafficked to "royalty, politicians, academicians, businessmen."',source:'EFTA00221614'},
  {date:'2015-02-11',event:'CVRA case filings reveal: Epstein invoked Fifth Amendment when asked under oath "Have you ever socialized with Donald Trump in the presence of females under the age of 18?" Edwards affidavit documents 14 phone numbers for Trump in Epstein\\'s computer directory.',source:'EFTA00188608'},
  {date:'1995-01-01',event:'FBI FD-302 of victim\\'s brother: sister told him she met Donald Trump at Mar-a-Lago in approximately 1995/1996 at age ~15. Same victim was groomed by Epstein starting at age 14 at Interlochen camp. Later disclosed: "I was raped by a pedophile for years."',source:'EFTA00173816'},
"""

# New FINDINGS entries
findings_entries = """  {id:'fd302-mar-a-lago-recruitment-50cameras',dataset:'DS9-FBI',pages:12,severity:10,keywords:['fbi','fd-302','mar-a-lago','maxwell','recruitment','surveillance','50 cameras','witness tampering','locker room'],summary:'CRITICAL — PRIMARY SOURCE: FBI FD-302 official interview record (March 17, 2011, file 31E-MM-108062). Victim (DOB Aug 9, 1983) interviewed at US Consulate overseas. Testifies: In Aug 1998-99, while working as locker room attendant at Trump\\'s Mar-a-Lago Club, was approached by Ghislaine Maxwell who offered $200/hour for massage work. Father drove her to Epstein\\'s El Brillo Way residence. Subsequently sexually abused by both Epstein and Maxwell. Trafficked to Glenn Dubin (age 16), Prince Andrew, Leslie Wexner, unnamed academic. Witnessed three 12-year-old French girls brought as Epstein "birthday gift." Describes surveillance room with "approximately 50 cameras" at Epstein Manhattan residence. "Eyeballs embedded into the wall" near massage room. Witness tampering: attorney told her "Epstein would take care of her if she did not talk to anyone." Given Xanax to "escape from reality." [v10.77]',date:'2011-03-17',type:'fbi-fd302'},
  {id:'epstein-fifth-amendment-trump-minors',dataset:'DS9-Court',pages:615,severity:10,keywords:['epstein','fifth amendment','trump','minors','deposition','under oath','socialized'],summary:'CRITICAL — PRIMARY SOURCE: CVRA court filings (Case 9:08-cv-80736-KAM, S.D. Florida). Epstein\\'s sworn deposition: "Q. Have you ever socialized with Donald Trump in the presence of females under the age of 18? A. Though I\\'d like to answer that question, at least today I\\'m going to have to assert my Fifth, Sixth and 14th Amendment Right, sir." Epstein invoked the Fifth rather than deny socializing with Trump around underage females. He also took the Fifth on same question regarding Dershowitz, Mottola, Copperfield, and Richardson. Also took the Fifth on: "Have you ever sexually abused children?" [v10.77]',date:'2015-02-11',type:'sworn-deposition'},
  {id:'edwards-14-phone-numbers-holy-grail',dataset:'DS9-Court',pages:615,severity:10,keywords:['edwards','14 phone numbers','trump','holy grail','rodriguez','message pads','epstein plane','mark epstein'],summary:'CRITICAL — PRIMARY SOURCE: Attorney Bradley Edwards affidavit (CVRA case). Basis for Trump deposition: (a) Message pads showed Trump called Epstein\\'s Palm Beach mansion "during the time period most relevant"; (b) Trump\\'s 2002 quote about Epstein and "younger" women; (c) Trump allegedly banned Epstein for assaulting underage girl at Mar-a-Lago; (d) Jane Doe 102 recruited at Mar-a-Lago by Maxwell; (e) Mark Epstein testified Trump flew on Epstein\\'s plane; (f) Trump visited Epstein\\'s Palm Beach home; (g) Epstein\\'s phone directory contained 14 phone numbers for Trump including emergency numbers, car numbers, security guard and houseman. Trump on page 85 of the "Holy Grail" journal (seized from housekeeper Rodriguez) which listed names alongside abused girls. [v10.77]',date:'2015-02-11',type:'court-affidavit'},
  {id:'rodriguez-deposition-trump-dinner-visits',dataset:'DS9-Court',pages:615,severity:8,keywords:['alfredo rodriguez','housekeeper','trump','dinner','palm beach','no massages','kitchen'],summary:'HIGH VALUE — PRIMARY SOURCE: Housekeeper Alfredo Rodriguez deposition (CVRA case). Q: "Trump had a home in Palm Beach, correct?" A: "Uh-huh." Q: "He would come for a meal?" A: "He would come, have dinner. He never sat at the table. He eat with me in the kitchen." Q: "Did he ever have massages while he was there?" A: "No. Because he\\'s got his own spa." Rodriguez confirmed Trump visited Epstein home for dinners but never stayed overnight and never had massages. Separately, Epstein\\'s driver testified he drove Maxwell to Mar-a-Lago where she got treatments: "that day I remember this girl..." Rodriguez was later arrested for trying to sell the "Holy Grail" journal for $50,000. [v10.77]',date:'2015-02-11',type:'sworn-deposition'},
  {id:'jane-doe-102-mar-a-lago-complaint',dataset:'DS9-Court',pages:20,severity:9,keywords:['jane doe 102','mar-a-lago','15 years old','ghislaine maxwell','massage therapy','9 dollars','sex slave'],summary:'CRITICAL — PRIMARY SOURCE: Federal civil complaint (Case 9:09-cv-80656-KAM, filed May 2009). Jane Doe 102 alleges: "A vulnerable young girl, Plaintiff was working as a changing room assistant at The Mar-A-Lago Club in Palm Beach making approximately $9 an hour when she was first lured into Defendant\\'s sexually exploitative world. In or about the summer of 1998, when Plaintiff was merely fifteen years old while attending to her duties at Mar-A-Lago, Plaintiff was recruited by Ghislaine Maxwell." Epstein asked her to quit Mar-a-Lago and travel with him. Trafficked to "Epstein\\'s adult male peers, including royalty, politicians, academicians, businessmen." [v10.77]',date:'2009-05-01',type:'court-complaint'},
  {id:'victim-brother-fd302-trump-meeting-age15',dataset:'DS9-FBI',pages:8,severity:8,keywords:['fbi','fd-302','victim brother','trump','mar-a-lago','1995','interlochen','grooming','swedish'],summary:'HIGH VALUE — PRIMARY SOURCE: FBI FD-302 interview of victim\\'s brother (Swedish-origin family, Palm Beach). Brother testifies sister told him she met Donald Trump at Mar-a-Lago in approximately 1995/1996 at age ~15. Same victim was groomed by Epstein starting at age 14 at Interlochen camp (1994) where Epstein approached her claiming he knew their late father. Epstein subsequently: purchased family a computer, called home to speak with sister, sent driver to pick her up, helped with pageant, gave "large amounts of cash," co-signed apartment lease, paid for Interlochen, flew her to NM ranch. Brother reports sister later disclosed: "How do you think I feel; I was raped by a pedophile for years." [v10.77]',date:'2011-01-01',type:'fbi-fd302'},
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
count = content.count('v10.76')
print(f"Replacing {count} occurrences of 'v10.76' with 'v10.77'")
content = content.replace('v10.76', 'v10.77')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.77 with FD-302s and sworn depositions.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.76')
new_ver = verify.count('v10.77')
print(f"Remaining v10.76: {remaining}")
print(f"Total v10.77: {new_ver}")

for check_id in ['fd302-mar-a-lago-recruitment-50cameras', 'epstein-fifth-amendment-trump-minors',
                  'edwards-14-phone-numbers-holy-grail', 'rodriguez-deposition-trump-dinner-visits',
                  'jane-doe-102-mar-a-lago-complaint', 'victim-brother-fd302-trump-meeting-age15']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
