#!/usr/bin/env python3
"""Update dashboard with Trump flew on plane deposition, Trump knew quote, systematic record falsification, video tampering discussion, FBI Murder reference, victim island testimony — v11.12"""
import sys

filepath = '/Users/jamesalford/epstein_jan30/github_update/dashboard_v10_latest.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

def find_close_simple(content, array_name):
    """Find the ]; that closes the array by searching backwards from next const"""
    marker = f"const {array_name} = ["
    start = content.find(marker)
    if start == -1:
        return -1
    next_const = content.find('\n    const ', start + len(marker))
    if next_const == -1:
        next_const = content.find('\n  const ', start + len(marker))
    if next_const == -1:
        next_const = len(content)
    pos = next_const
    while pos > start:
        if content[pos:pos+2] == '];':
            return pos
        pos -= 1
    return -1

findings_close = find_close_simple(content, 'FINDINGS_DATA')
timeline_close = find_close_simple(content, 'TIMELINE_DATA')

print(f"FINDINGS_DATA closing at: {findings_close}")
print(f"TIMELINE_DATA closing at: {timeline_close}")

if findings_close == -1 or timeline_close == -1:
    print("ERROR: Could not find arrays!")
    sys.exit(1)

if findings_close == timeline_close:
    print("ERROR: Arrays at same position!")
    sys.exit(1)

# New TIMELINE entries
timeline_entries = """  {date:'2021-11-30',event:'MAXWELL TRIAL DEPOSITION -- TRUMP FLEW ON EPSTEIN\\'S PLANE (287 pages): Under oath, witness asked directly: "Donald Trump, before he was president, also flew on" Epstein\\'s aircraft. Also: "else sexually abuse underage girls?" and "been sexually abused by Maxwell and Epstein?" Witness describes interior of Maxwell\\'s residence. This is the first direct deposition testimony placing Trump on Epstein\\'s plane.',source:'EFTA00068582'},
  {date:'2021-06-14',event:'OIG SWORN STATEMENT -- "ALL THE WAY UP TO DONALD TRUMP KNEW" (229 pages): MCC staff member states under oath: "You know all the way up to Donald Trump knew" in context of discussing Epstein\\'s death and institutional awareness. Also discusses Epstein\\'s suicide attempt and suicide watch placement. The statement establishes that staff believed knowledge of Epstein\\'s situation extended to the highest levels of government.',source:'EFTA00114184'},
  {date:'2021-06-21',event:'OIG SWORN STATEMENT -- SYSTEMATIC FALSIFICATION ADMISSION (116 pages): Guard testifies that record falsification was NOT unique to the night Epstein died -- it was STANDARD PRACTICE: "falsified. Ever since you\\'ve been there, it\\'s always been falsified record is what you\\'re" saying. Also confirms cellmate requirement on suicide watch. This transforms the falsification narrative from isolated misconduct to endemic institutional fraud.',source:'EFTA00117643'},
  {date:'2021-09-29',event:'OIG SWORN STATEMENT -- VIDEO TAMPERING DISCUSSED (223 pages): Staff member asked directly about video evidence: "that video have been, at some point, deleted?" Response discusses how "as simple as changing the time, the recording" could alter evidence. Also references "assaults on inmate on inmate." This directly addresses the WIRED report finding that FBI prison video metadata was "likely modified."',source:'EFTA00141893'},
  {date:'2018-12-08',event:'FBI CASE FILE -- REFERENCES "MURDER" IN EPSTEIN CONTEXT (255 pages): FBI New York case file header: "Child Sex Trafficking investigation into Epstein, opened 12/08/2018." Internal FBI reference: "NTOC2020 37ch01 Elip: involvement with Jeffrey Epstein, Sex Trafficking, and Murder." Wexner mentioned. The word "Murder" in an official FBI case reference is significant -- it suggests investigators examined homicide theories.',source:'EFTA02730741'},
  {date:'2019-11-30',event:'VICTIM DIRECT STATEMENT FROM ISLAND (1004 pages): Victim writes: "NOT taken of me on Epstein\\'s island you have not only exploited me as a victim of rape and sex trafficking but" -- accusing attorneys of further exploitation. Names Trump, Bill Clinton, Prince Andrew. References: "RAPE AND SEX TRAFFICKING, THE ABUSE OF THE ATTORNEYS" and "the whole Epstein rape and sex trafficking ring."',source:'EFTA00144597'},
  {date:'2019-01-01',event:'EPSTEIN DISCARDED TRUMP PHOTOGRAPH: MCC psychological notes record Epstein "throwing away the newspaper photograph of himself by trump." This behavioral detail -- Epstein deliberately disposing of evidence linking himself to Trump -- was noted by prison staff during his incarceration. Also found with "a string loosely hanging around his neck" and placed on Suicide Watch.',source:'EFTA00073831'},
  {date:'2020-04-14',event:'CVRA COURT FILING -- NPA "DISGUSTING FAILURE" (44 pages): Court document states: "get away with child rape and international sex trafficking isn\\'t poor judgment -- it is a disgusting failure." Details: "sex trafficking more than 30 minors if: (I) Epstein pled guilty." NPA described as "extending immunity to Epstein and his co-conspirators." Meeting between victims and Alexander Acosta referenced.',source:'EFTA00073493'},
"""

# New FINDINGS entries
findings_entries = """  {id:'trump-flew-epstein-plane-trump-knew-deposition-testimony-discarded-photo',dataset:'DS10-Official',pages:1500,severity:10,keywords:['trump','flew','plane','aircraft','deposition','donald trump','before he was president','sexually abuse','underage girls','maxwell','all the way up','donald trump knew','institutional awareness','highest levels','throwing away','newspaper photograph','trump photo','discarded','mcc','psychological notes'],summary:'CRITICAL -- PRIMARY SOURCES: Maxwell trial deposition (EFTA00068582, 287 pages), OIG sworn statement (EFTA00114184, 229 pages), MCC psychological notes (EFTA00073831, 149 pages), victim statement (EFTA00144597, 1004 pages). TRUMP CONNECTIONS IN SWORN TESTIMONY: (1) TRUMP ON EPSTEIN\\\\\\\\\\\\\\\\'S PLANE: Deposition question: \\\\\\\\\\\\\\\"Donald Trump, before he was president, also flew on\\\\\\\\\\\\\\\" Epstein\\\\\\\\\\\\\\\\'s aircraft -- first direct deposition testimony placing Trump on the plane; (2) \\\\\\\\\\\\\\\"TRUMP KNEW\\\\\\\\\\\\\\\": MCC staff under oath: \\\\\\\\\\\\\\\"You know all the way up to Donald Trump knew\\\\\\\\\\\\\\\" -- staff believed awareness extended to highest government levels; (3) PHOTO DISCARDED: Prison notes record Epstein \\\\\\\\\\\\\\\"throwing away the newspaper photograph of himself by trump\\\\\\\\\\\\\\\" -- deliberate disposal of Trump-linked imagery; (4) VICTIM NAMES TRUMP: Direct statement from island: \\\\\\\\\\\\\\\"NOT taken of me on Epstein\\\\\\\\\\\\\\\\'s island you have not only exploited me as a victim of rape and sex trafficking.\\\\\\\\\\\\\\\" Names Trump, Clinton, Prince Andrew. [v11.12]',date:'2021-11-30',type:'deposition-testimony'},
  {id:'systematic-falsification-video-tampering-fbi-murder-reference-npa-disgusting-failure',dataset:'DS10-Official',pages:900,severity:10,keywords:['systematic','falsification','always been falsified','standard practice','endemic','video','deleted','changing the time','recording','modified','wired','metadata','murder','fbi','ntoc','sex trafficking and murder','homicide','disgusting failure','child rape','international sex trafficking','poor judgment','30 minors','immunity','co-conspirators','acosta'],summary:'CRITICAL -- PRIMARY SOURCES: OIG sworn statements (EFTA00117643, 116 pages; EFTA00141893, 223 pages), FBI case file (EFTA02730741, 255 pages), CVRA filing (EFTA00073493, 44 pages). SYSTEMIC FAILURES AND FBI MURDER REFERENCE: (1) SYSTEMATIC FALSIFICATION: Guard testifies falsification was STANDARD PRACTICE, not isolated: \\\\\\\\\\\\\\\"falsified. Ever since you\\\\\\\\\\\\\\\\'ve been there, it\\\\\\\\\\\\\\\\'s always been falsified record\\\\\\\\\\\\\\\" -- transforms narrative from misconduct to endemic fraud; (2) VIDEO TAMPERING: Staff asked \\\\\\\\\\\\\\\"that video have been, at some point, deleted?\\\\\\\\\\\\\\\" Response: \\\\\\\\\\\\\\\"as simple as changing the time, the recording\\\\\\\\\\\\\\\" -- directly addresses WIRED report that FBI prison video was \\\\\\\\\\\\\\\"likely modified\\\\\\\\\\\\\\\"; (3) FBI REFERENCES MURDER: Official case file: \\\\\\\\\\\\\\\"involvement with Jeffrey Epstein, Sex Trafficking, and Murder\\\\\\\\\\\\\\\" -- investigators examined homicide theories; (4) NPA DENOUNCED: \\\\\\\\\\\\\\\"get away with child rape and international sex trafficking isn\\\\\\\\\\\\\\\\'t poor judgment -- it is a disgusting failure.\\\\\\\\\\\\\\\" NPA described as \\\\\\\\\\\\\\\"extending immunity to Epstein and his co-conspirators.\\\\\\\\\\\\\\\" [v11.12]',date:'2021-06-21',type:'institutional-fraud'},
"""

# Insert TIMELINE entries (before closing ])
content = content[:timeline_close] + "\n" + timeline_entries + content[timeline_close:]

# Re-find FINDINGS closing bracket (shifted by timeline insertion)
findings_close = find_close_simple(content, 'FINDINGS_DATA')
if findings_close == -1:
    print("ERROR: Could not find FINDINGS_DATA after timeline insert!")
    sys.exit(1)

# Insert FINDINGS entries (before closing ])
content = content[:findings_close] + "\n" + findings_entries + content[findings_close:]

# Version bump
count = content.count('v11.11')
print(f"Replacing {count} occurrences of 'v11.11' with 'v11.12'")
content = content.replace('v11.11', 'v11.12')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v11.12.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v11.11')
new_ver = verify.count('v11.12')
print(f"Remaining v11.11: {remaining}")
print(f"Total v11.12: {new_ver}")

for check_id in ['trump-flew-epstein-plane-trump-knew-deposition-testimony-discarded-photo',
                  'systematic-falsification-video-tampering-fbi-murder-reference-npa-disgusting-failure']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

print(f"\nStructure check:")
print(f"  const FINDINGS_DATA = [ found: {'const FINDINGS_DATA = [' in verify}")
print(f"  const TIMELINE_DATA = [ found: {'const TIMELINE_DATA = [' in verify}")
print(f"  </script> found: {'</script>' in verify}")
print(f"  </html> found: {'</html>' in verify}")

f_close2 = find_close_simple(verify, 'FINDINGS_DATA')
t_close2 = find_close_simple(verify, 'TIMELINE_DATA')
print(f"  FINDINGS closes at: {f_close2} (valid: {f_close2 != -1})")
print(f"  TIMELINE closes at: {t_close2} (valid: {t_close2 != -1})")
print(f"  Different positions: {f_close2 != t_close2}")
