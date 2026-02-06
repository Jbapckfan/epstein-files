#!/usr/bin/env python3
"""Update dashboard with Bondi-Patel letter, proffer agreement details, Maxwell intelligence/Clinton admissions — v10.89"""
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
timeline_entries = """  {date:'2025-02-27',event:'AG Pam Bondi letter to FBI Director Kash Patel: "I repeatedly questioned whether this was the full set of documents...and was repeatedly assured by the FBI that we had received the full set." Learned FBI NY Field Office had "thousands of pages" hidden. Orders delivery by 8:00 AM next day and investigation into why order was not followed.',source:'Bondi-Patel Letter'},
  {date:'2025-07-24',event:'Maxwell proffer agreement signed at Office of U.S. Attorney, Northern District of Florida. "THIS IS NOT A COOPERATION AGREEMENT." Maxwell agrees to provide information and respond to questions under use restrictions. Signed by Deputy AG Todd Blanche and defense attorney David Oscar Markus.',source:'Proffer Agreement'},
"""

# New FINDINGS entries
findings_entries = """  {id:'bondi-patel-letter-fbi-hiding-epstein-files-feb2025',dataset:'DS9-Legal',pages:1,severity:10,keywords:['pam bondi','kash patel','fbi','epstein files','hiding','thousands of pages','flight logs','contact list','victims','investigation','february 2025'],summary:'CRITICAL -- PRIMARY SOURCE: Letter from Attorney General Pam Bondi to FBI Director Kash Patel (1 page, February 27, 2025). Bondi writes: "I repeatedly questioned whether this was the full set of documents responsive to my request and was repeatedly assured by the FBI that we had received the full set of documents." Bondi received only "approximately 200 pages" consisting of "flight logs, Epstein\\'s list of contacts, and a list of victims\\' names and phone numbers." She then learned from a source that "the FBI Field Office in New York was in possession of thousands of pages of documents related to the investigation and indictment of Epstein." Orders: (1) By 8:00 AM February 28, FBI must deliver "the full and complete Epstein files...including all records, documents, audio and video recordings, and materials related to Jeffrey Epstein and his clients"; (2) "There will be no withholdings or limitations"; (3) Immediate investigation into why her order was not followed; (4) Comprehensive report with "proposed personnel action within 14 days." This letter triggered the massive FBI review described in the Senate Judiciary Committee letter (EFTA00173350): ~1,000 personnel on 24-hour shifts, flagging Trump mentions, modified surveillance video. [v10.89]',date:'2025-02-27',type:'ag-letter'},
  {id:'maxwell-proffer-clinton-flights-mossad-intelligence-details',dataset:'DS9-Legal',pages:419,severity:9,keywords:['maxwell','proffer','clinton','plane','flights','mossad','intelligence','ehud barak','african warlords','robert maxwell','british intelligence','council foreign relations','doug band','cheryl mills','latin america'],summary:'HIGH VALUE -- SUPPLEMENTARY PROFFER DETAILS from Maxwell proffer Days 1-2 (419 pages combined). ADDITIONAL KEY ADMISSIONS: (1) CLINTON FLIGHTS: Maxwell explicitly states "I was the one who asked Epstein to provide the plane" for Clinton trips. On the Clinton-Epstein relationship: "they met because of me and the plane was because of me." Confirms multiple Clinton trips including Latin America with Doug Band and Cheryl Mills, Davos (once or twice), and Africa. Insists Clinton "absolutely never" went to the island: "I don\\'t believe he had an independent friendship with Epstein"; (2) MOSSAD: When Blanche asks "Have you ever had any contact with...Mossad, the Israeli intelligence agency?" Maxwell responds: "Not deliberately." Asked if Epstein got money from intelligence agencies including Mossad: "I don\\'t believe so, but I wouldn\\'t know"; (3) INTELLIGENCE: When asked about CIA/DIA connections, Maxwell calls it "bullshit" BUT acknowledges Epstein showed her "a photograph that he had with some African warlords" suggesting "covert" connections, and in his early money-finding career "he may have suggested that there was some people who helped him"; (4) ROBERT MAXWELL: Confirms father had "a background in intelligence during...the second World War. He was a British intelligence officer." Adds: "once you\\'ve been an intelligence officer, you\\'re kind of always." Family has "ties to Israel" because father "loved Israel"; (5) EHUD BARAK: Maxwell names Barak as international politician close to Epstein, relationship in "later 2000s." When asked nature of relationship: "I don\\'t" know; (6) PROFFER CONTEXT: Held at Northern District of Florida (not SDNY). Agreement explicitly states "THIS IS NOT A COOPERATION AGREEMENT." Maxwell represented by David Oscar Markus. [v10.89]',date:'2025-07-24',type:'proffer-supplementary'},
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
count = content.count('v10.88')
print(f"Replacing {count} occurrences of 'v10.88' with 'v10.89'")
content = content.replace('v10.88', 'v10.89')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.89.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.88')
new_ver = verify.count('v10.89')
print(f"Remaining v10.88: {remaining}")
print(f"Total v10.89: {new_ver}")

for check_id in ['bondi-patel-letter-fbi-hiding-epstein-files-feb2025',
                  'maxwell-proffer-clinton-flights-mossad-intelligence-details']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
