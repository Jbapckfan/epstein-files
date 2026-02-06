#!/usr/bin/env python3
"""Update dashboard with Maxwell proffer transcripts + DOJ OPR Report — v10.78"""
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
timeline_entries = """  {date:'2025-07-24',event:'Ghislaine Maxwell proffer interview Day 1 with Deputy AG Todd Blanche (Trump\\'s former personal criminal defense attorney) and FBI ASAC Spencer Horn. Under immunity, Maxwell provides extensively exculpatory testimony about Trump: "The President was never inappropriate with anybody." Denies ever recruiting masseuses from Mar-a-Lago. Lists Epstein\\'s famous associates from the 1990s.',source:'PROFFER_transcript_day1'},
  {date:'2025-07-25',event:'Maxwell proffer Day 2. Addresses Mar-a-Lago recruitment: "I really don\\'t believe it\\'s true" but "it\\'s not impossible that I might have asked someone from there." Tells Blanche "some are in your cabinet" — Epstein associates in Trump\\'s cabinet. Admits Epstein "did terrible things to young kids."',source:'PROFFER_transcript_day2'},
  {date:'2020-11-01',event:'DOJ Office of Professional Responsibility releases 350-page report on Acosta\\'s handling of Epstein NPA. Finds Acosta exercised "poor judgment" but not "professional misconduct." 60-count indictment was drafted then abandoned. NPA gave immunity to ALL co-conspirators. CVRA violated by failing to consult victims.',source:'MEMO_2020.11_DOJ_OPR'},
  {date:'2025-07-24',event:'Maxwell proffer agreement signed at USAO Northern District of Florida. Blanche (DAG) grants Maxwell immunity for her statements. Agreement explicitly states "this is not a cooperation agreement" — DOJ makes no promises in exchange for Maxwell\\'s information.',source:'PROFFER_proffer_agreement'},
"""

# New FINDINGS entries
findings_entries = """  {id:'maxwell-proffer-day1-trump-exculpatory',dataset:'DS9-DOJ',pages:215,severity:10,keywords:['ghislaine maxwell','proffer','todd blanche','deputy attorney general','trump','immunity','mar-a-lago','masseuse','gentleman','inappropriate'],summary:'CRITICAL — PRIMARY SOURCE: Recorded proffer interview of Ghislaine Maxwell (July 24, 2025, 215 pages). Conducted by Deputy AG Todd Blanche — who was Trump\\'s PERSONAL criminal defense attorney in People v. Trump (Manhattan DA) and the federal classified documents case before being appointed DAG. Under immunity, Maxwell testifies: (1) She may have met Trump in 1990 through her father Robert Maxwell before meeting Epstein; (2) Trump was \"always very cordial and very kind to me\"; (3) \"I admire his extraordinary achievement in becoming the President now. And I like him\"; (4) She only saw Trump and Epstein in \"social settings,\" \"I don\\'t think they were close friends\"; (5) \"I actually never saw the President in any type of massage setting. I never witnessed the President in any inappropriate setting in any way. The President was never inappropriate with anybody. In the times that I was with him, he was a gentleman in all respects\"; (6) Never heard anyone say Trump did anything inappropriate; (7) \"I\\'ve never recruited a masseuse from Mar-a-Lago for that.\" CRITICAL CONTEXT: This testimony directly contradicts multiple victims\\' sworn statements about Mar-a-Lago recruitment, Epstein\\'s own Fifth Amendment invocation about Trump and minors, and 14 phone numbers in Epstein\\'s directory. Maxwell had every incentive to provide exculpatory testimony to Trump\\'s own former lawyer. [v10.78]',date:'2025-07-24',type:'proffer-transcript'},
  {id:'maxwell-proffer-blanche-conflict-of-interest',dataset:'DS9-DOJ',pages:215,severity:10,keywords:['todd blanche','conflict of interest','deputy attorney general','trump defense attorney','proffer','maxwell','immunity','people v trump'],summary:'CRITICAL — STRUCTURAL FINDING: Todd Blanche served as Donald Trump\\'s LEAD criminal defense attorney in two cases: People of the State of New York v. Donald J. Trump (Manhattan DA, convicted on 34 felony counts) and United States v. Trump (classified documents, dismissed). Trump then appointed Blanche as Deputy Attorney General — the #2 position at DOJ. In that role, Blanche PERSONALLY conducted the Maxwell proffer interview, specifically asking about Trump, and elicited extensively exculpatory testimony. The proffer agreement was signed at USAO Northern District of Florida (where the classified documents case originated). This represents an extraordinary conflict of interest: Trump\\'s personal lawyer, now running DOJ, interviews the key co-conspirator about his client/boss under immunity. No special counsel or recusal was sought. [v10.78]',date:'2025-07-24',type:'structural-analysis'},
  {id:'maxwell-proffer-day2-mar-a-lago-cabinet',dataset:'DS9-DOJ',pages:120,severity:10,keywords:['ghislaine maxwell','proffer','day 2','mar-a-lago','cabinet','p diddy','clinton','recruitment','impossible'],summary:'CRITICAL — PRIMARY SOURCE: Maxwell proffer Day 2 (July 25, 2025, 120 pages). Maxwell addresses Mar-a-Lago recruitment allegation: overnight she \"realized that I was — the allegation at least is that I met [REDACTED] in Mar-a-Lago and so I felt that I needed to address that.\" Says \"I really don\\'t believe it\\'s true\" but \"it\\'s not impossible that I might have asked someone from there.\" Admits she went to spas and asked people about massage work. Tells Blanche directly: \"some are in your cabinet\" — meaning Epstein\\'s associates are in Trump\\'s cabinet. Compares case to \"P. Diddy in Redux on TV with Clintons and Trump.\" Calls Epstein \"a disgusting guy who did terrible things to young kids\" but dismisses scope of conspiracy: \"He\\'s not some — they\\'ve made him into this — he\\'s not that interesting.\" [v10.78]',date:'2025-07-25',type:'proffer-transcript'},
  {id:'maxwell-proffer-black-book-no-blackmail',dataset:'DS9-DOJ',pages:215,severity:9,keywords:['black book','rodriguez','alfredo rodriguez','blackmail','brad edwards','exhibit 52','names','list'],summary:'HIGH VALUE — PRIMARY SOURCE: Maxwell proffer Day 1. On the Rodriguez \"black book\" (Exhibit 52 from her trial): \"I don\\'t remember what it does with Donald Trump. I don\\'t know. You\\'d have to look.\" Claims she doesn\\'t know what the book actually is: \"That book is some type of a compilation, but what it is, is it\\'s just pieces of paper with type.\" Says Brad Edwards \"has a list of 25 men that he got money off.\" Denies any knowledge of blackmail operation: \"There is no list. There is no — I\\'m not aware of any blackmail. I never heard that. I never saw it.\" Discusses Rothstein Adler law firm scheme involving placing \"prostitutes\" as fake secretaries. Note: Rodriguez was arrested for trying to sell the book for $50,000 and died in prison in 2015. [v10.78]',date:'2025-07-24',type:'proffer-transcript'},
  {id:'doj-opr-acosta-poor-judgment-60count',dataset:'DS9-DOJ',pages:350,severity:9,keywords:['doj','opr','acosta','poor judgment','60-count indictment','npa','co-conspirators','immunity','cvra','victims'],summary:'CRITICAL — PRIMARY SOURCE: DOJ Office of Professional Responsibility Report (November 2020, 350 pages). Full investigation into Acosta\\'s handling of Epstein case. Key findings: (1) AUSA drafted 60-count federal indictment that was abandoned; (2) Acosta exercised \"poor judgment\" but not \"professional misconduct\" (high threshold); (3) NPA was \"a flawed mechanism\"; (4) Acosta\\'s federalism rationale was \"too expansive\" and federal interest view \"too narrow\"; (5) NPA gave immunity to Epstein, four NAMED co-conspirators, AND \"any potential co-conspirators\"; (6) Government violated CVRA by not consulting victims; (7) Letters to victims after NPA \"risked misleading\" them; (8) OPR found no evidence Acosta\\'s decision was based on \"corruption or other impermissible considerations, such as Epstein\\'s wealth, status, or associations.\" Note: Trump later appointed Acosta as Secretary of Labor despite this; Acosta resigned July 2019 after Miami Herald reporting. [v10.78]',date:'2020-11-01',type:'doj-investigation'},
  {id:'maxwell-proffer-epstein-associates-90s-massages',dataset:'DS9-DOJ',pages:215,severity:8,keywords:['henry rosovsky','harvard','minsky','massages','joe pagano','jerry goldsmith','tom pritzker','jimmy cayne','prince andrew'],summary:'HIGH VALUE — PRIMARY SOURCE: Maxwell proffer Day 1. When asked which famous associates received massages, Maxwell names: Henry Rosovsky (Harvard provost, \"in his 80s,\" saw him in bathrobe at 71st Street); Marvin Minsky (MIT AI pioneer). Denies Clinton received massage: \"The time that Epstein and President Clinton spent together... I don\\'t believe there was ever a massage on the plane.\" On Prince Andrew: says Epstein \"didn\\'t know\" him in the 1990s. Lists Epstein\\'s 1990s circle: Congressman McMillen, Joe Pagano, Jerry Goldsmith, Joe Roberts, Kenny Lipper, Dan Abramson, Tom Pritzker, Jimmy Cayne, Lou Ranieri. Also documents Epstein paid Maxwell approximately $30 million total; she was on salary starting at $25,000 rising to $250,000/year. [v10.78]',date:'2025-07-24',type:'proffer-transcript'},
  {id:'maxwell-proffer-agreement-immunity-terms',dataset:'DS9-DOJ',pages:2,severity:8,keywords:['proffer agreement','immunity','todd blanche','maxwell','northern district florida','cooperation','false statements'],summary:'PRIMARY SOURCE: Proffer agreement between DOJ and Ghislaine Maxwell, signed by DAG Todd Blanche. Key terms: (1) \"THIS IS NOT A COOPERATION AGREEMENT\"; (2) Government cannot use Maxwell\\'s statements against her in case-in-chief; (3) Exception: if Maxwell lies, she can be prosecuted for false statements; (4) Government CAN use statements for cross-examination if she later testifies differently; (5) Government CAN use leads derived from proffer; (6) Held at USAO Northern District of Florida (Tallahassee) — same district where Trump classified documents case originated. Signed July 24, 2025 by Blanche, Maxwell, and David Oscar Markus (Maxwell\\'s attorney). [v10.78]',date:'2025-07-24',type:'legal-agreement'},
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
count = content.count('v10.77')
print(f"Replacing {count} occurrences of 'v10.77' with 'v10.78'")
content = content.replace('v10.77', 'v10.78')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.78 with Maxwell proffer transcripts + DOJ OPR Report.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.77')
new_ver = verify.count('v10.78')
print(f"Remaining v10.77: {remaining}")
print(f"Total v10.78: {new_ver}")

for check_id in ['maxwell-proffer-day1-trump-exculpatory', 'maxwell-proffer-blanche-conflict-of-interest',
                  'maxwell-proffer-day2-mar-a-lago-cabinet', 'maxwell-proffer-black-book-no-blackmail',
                  'doj-opr-acosta-poor-judgment-60count', 'maxwell-proffer-epstein-associates-90s-massages',
                  'maxwell-proffer-agreement-immunity-terms']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
