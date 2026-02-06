#!/usr/bin/env python3
"""Update dashboard with Trump Org indictment advice, Tom Barrack, Gates Foundation Jan 2019, Cohen/RONA testimony, pro-Acosta media strategy — v10.95"""
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
timeline_entries = """  {date:'2019-01-18',event:'Epstein iMessages contact about Trump Organization: "If they indict trump org. You will have some decisions to make quickly" and "Two stools won\\'t work. Either all in or all out" then "You are on the cusp. The movement has gigantic potential.. as do you. dems are crazed and dangerous." Sends detailed RICO statute text. Also: "Cruel irony, but it was Rudy that first understood the power of the rico laws." Contact replies: "The mob, then Milken."',source:'EFTA00509050'},
  {date:'2019-01-15',event:'Epstein iMessage: "Barrack said wacko. Also If trump runs Cuomo definitely not." Contact: "Barrack said djt Waco?" Tom Barrack -- Trump\\'s close friend, inaugural committee chair, and Colony Capital founder -- referenced in political discussion. Same conversation: "Brock coming to see me tonight in palm" (David Brock, Media Matters founder).',source:'EFTA00509032'},
  {date:'2019-01-13',event:'Epstein iMessages contact: "you devoted full time to trump for months. great results.. now you are spread over us europe movement brazil. uae, too many fronts." Implies Epstein was connected to someone who worked full-time on Trump\\'s political operation and was now building an international populist "movement."',source:'EFTA00509032'},
  {date:'2019-01-18',event:'Terje Roed-Larsen iMessages Epstein about Bill Gates: "Gates didn\\'t answer email. However I had a good conversation with Chris Elias, head of the foundation on the phone. He is setting up a meeting with the head of Gates Foundation in London when I\\'m back from Davos. Would still be good to see Gates in Davos." Earlier: "Was the mail to Bill ok? The mail to Chris Elias on the Gates Foundation worked."',source:'EFTA00509032'},
  {date:'2019-02-27',event:'During Michael Cohen\\'s Congressional testimony, contact iMessages Epstein: "Cohen brought up RONA - keeper of the secrets" -- referring to Rhona Graff, Trump\\'s longtime executive assistant. Epstein: "what do you think so far of cohen. are you back in fighting form?" Contact monitoring testimony in real time.',source:'EFTA00509347'},
  {date:'2019-02-28',event:'Epstein iMessage: "Who would write a pro Acosta story." Outlines strategy: "The idea is to get into the public realm the story that the girls used the agreement to get money from them and their attorneys and only after receiving it they moved to overturn it." Seeking favorable media coverage for Trump\\'s Labor Secretary Alexander Acosta.',source:'EFTA00509347'},
  {date:'2019-01-20',event:'Epstein iMessages contact comparing Trump and Weinstein: "Harvey Weinstein, like Donald can\\'t find anyone to be his lawyer." Then: "Yes but like djt. He told ben how to fight it and made some horrific mistakes. Ie instead of letting the girl that was a proven fake wait until trial. That would have damaged all, he wanted it out in the press that she was untruthful. Amateur bully." Also: "Davos west will be at my apt in Paris."',source:'EFTA00509050'},
  {date:'2019-01-16',event:'Epstein iMessages an unnamed governor: "Good morning governor. If you are free to speak, either today, tomorrow just send a time. Thx J. Epstein." Governor responds: "Ok. Will call you." Epstein maintaining direct communication with a sitting governor six months before arrest.',source:'EFTA00509032'},
"""

# New FINDINGS entries
findings_entries = """  {id:'epstein-trump-org-indictment-rico-advice-jan2019',dataset:'DS9-Digital',pages:17,severity:10,keywords:['trump organization','indictment','rico','rudy giuliani','two stools','movement','dems','weinstein','alex spiro','milken','january 2019','six months before arrest','chomsky'],summary:'CRITICAL -- PRIMARY SOURCE: Forensic iMessage extraction from Epstein\\'s Mac (NYC024328.aff4, EFTA00509050-509066, 17 pages, January 18-20, 2019 -- six months before arrest). EXPLOSIVE POLITICAL ADVISORY: (1) TRUMP ORG INDICTMENT: Epstein texts contact: "If they indict trump org. You will have some decisions to make quickly" then "Two stools won\\'t work. Either all in or all out" -- advising someone to pick a side before a potential Trump Organization indictment; (2) THE MOVEMENT: "You are on the cusp. The movement has gigantic potential.. as do you. dems are crazed and dangerous" -- referencing an international populist "movement"; (3) RICO ANALYSIS: Epstein sends full text of RICO statute after discussion. "Cruel irony, but it was Rudy that first understood the power of the rico laws." Contact replies: "The mob, then Milken"; (4) TRUMP-WEINSTEIN COMPARISON: "Harvey Weinstein, like Donald can\\'t find anyone to be his lawyer" then analyzing both their legal mistakes: "Yes but like djt. He told ben how to fight it and made some horrific mistakes"; (5) Alex Spiro (now Elon Musk\\'s attorney) mentioned: "alex spiro and burck both have worked with Ben and say Harvey can\\'t handle that he is going away for 20 years"; (6) CHOMSKY: "Chomsky not getting younger" -- casual reference; (7) DAVOS: "Davos west will be at my apt in Paris. Busy week. Mongolians included." This document shows Epstein providing real-time political strategy advice about Trump Organization legal exposure to someone embedded in the political sphere. [v10.95]',date:'2019-01-18',type:'digital-forensics'},
  {id:'tom-barrack-brock-gates-foundation-governor-jan2019',dataset:'DS9-Digital',pages:18,severity:10,keywords:['tom barrack','david brock','bill gates','gates foundation','chris elias','terje','governor','january 2019','davos','abu dhabi','wef','trump','cuomo','six months before arrest'],summary:'CRITICAL -- PRIMARY SOURCE: Forensic iMessage extraction (EFTA00509032-509049, 18 pages, January 12 - February 2, 2019 -- six months before arrest). MULTIPLE HIGH-LEVEL CONNECTIONS: (1) TOM BARRACK: "Barrack said wacko. Also If trump runs Cuomo definitely not" / "Barrack said djt Waco?" -- Trump\\'s close personal friend, inaugural committee chair, and Colony Capital founder referenced in political discussions. Barrack was later indicted (2021) for illegal foreign lobbying on behalf of UAE; (2) "DEVOTED FULL TIME TO TRUMP": Epstein tells contact: "you devoted full time to trump for months. great results.. now you are spread over us europe movement brazil. uae, too many fronts" -- connecting someone who worked on Trump\\'s campaign to an international populist movement; (3) DAVID BROCK: "Brock coming to see me tonight in palm" / "I think brock is broke again" -- founder of Media Matters for America visiting Epstein in Palm Beach; (4) GATES FOUNDATION VIA TERJE: Terje Roed-Larsen reports to Epstein: "Was the mail to Bill ok? The mail to Chris Elias on the Gates Foundation worked. He is going to call me tomorrow" then later: "Gates didn\\'t answer email. However I had a good conversation with Chris Elias, head of the foundation...setting up a meeting with the head of Gates Foundation in London." Epstein serving as connector to Gates Foundation in January 2019; (5) UNNAMED GOVERNOR: "Good morning governor. If you are free to speak, either today, tomorrow just send a time. Thx J. Epstein" -- direct text to a sitting governor; (6) TRUMP BORDER POLITICS: "Trump canceled rest of us delegation"; "Lol canceling pelosi trip"; government shutdown strategy discussion. [v10.95]',date:'2019-01-15',type:'digital-forensics'},
  {id:'cohen-rona-testimony-pro-acosta-media-feb2019',dataset:'DS9-Digital',pages:18,severity:9,keywords:['michael cohen','rhona graff','rona','congressional testimony','alexander acosta','pro acosta story','trump org','henchmen','republicans','jagland','osce','qatar','february 2019','four months before arrest'],summary:'HIGH VALUE -- PRIMARY SOURCE: Forensic iMessage extraction (EFTA00509347-509364, 18 pages, February 26-28, 2019 -- four months before arrest). TESTIMONY MONITORING AND MEDIA STRATEGY: (1) RHONA GRAFF: During Michael Cohen\\'s live Congressional testimony Feb 27, contact texts Epstein: "Cohen brought up RONA - keeper of the secrets." Rhona Graff was Trump\\'s longtime executive assistant and gatekeeper who was mentioned in testimony; (2) COHEN ANALYSIS: "what do you think so far of cohen. are you back in fighting form?" Contact: "Bad. but republicans stood strong, Cohen pretty detailed"; (3) TRUMP ORG HENCHMEN: "Hes opened the door to questions re who are the other henchmen at trump org" -- analyzing testimony implications; (4) PRO-ACOSTA MEDIA: Epstein: "Who would write a pro Acosta story." Strategy: "The idea is to get into the public realm the story that the girls used the agreement to get money from them and their attorneys and only after receiving it they moved to overturn it" -- actively seeking favorable coverage for Trump\\'s Labor Secretary; (5) "Trump had a bad day, did you watch?"; (6) JAGLAND/OSCE: Contact was "with Jagland in Strasbourg today" -- visiting the Nobel Committee chair; (7) QATARI BANKING: Epstein texting Khalid in Qatar (+974) about QNB Paris accommodations; (8) Woody Allen shared article defending Dershowitz\\'s right to represent clients. [v10.95]',date:'2019-02-27',type:'digital-forensics'},
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
count = content.count('v10.94')
print(f"Replacing {count} occurrences of 'v10.94' with 'v10.95'")
content = content.replace('v10.94', 'v10.95')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.95.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.94')
new_ver = verify.count('v10.95')
print(f"Remaining v10.94: {remaining}")
print(f"Total v10.95: {new_ver}")

for check_id in ['epstein-trump-org-indictment-rico-advice-jan2019',
                  'tom-barrack-brock-gates-foundation-governor-jan2019',
                  'cohen-rona-testimony-pro-acosta-media-feb2019']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
print(f"Arrays at different positions: {f_close2 != t_close2}")
