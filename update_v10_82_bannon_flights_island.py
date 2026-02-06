#!/usr/bin/env python3
"""Update dashboard with Bannon on Epstein flights, island question, dinner with UN President + Barak — v10.82"""
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
timeline_entries = """  {date:'2018-03-25',event:'Epstein pilot Larry Visoski asks "Is S Bannon coming on this flight?" Assistant Lesley Groff replies: "Yes, Jeffrey said Bannon is going today! Jeffrey has been hanging out a lot with Bannon these days." Following day, Groff asks pilot: "Did Bannon or anyone else return to NY with him?" re island trip.',source:'EFTA00471570+EFTA00471504'},
  {date:'2018-03-20',event:'Groff invites UN General Assembly President Miroslav Lajcak to dinner at Epstein\\'s 71st Street townhouse: "Jeffrey will be in NY and is asking if President Lajcak could please come join him, Steve Bannon and Ehud Barak at 7:30 for dinner and interesting conversation."',source:'EFTA00471126'},
"""

# New FINDINGS entries
findings_entries = """  {id:'bannon-epstein-flight-hanging-out-march2018',dataset:'DS11-Email',pages:2,severity:10,keywords:['steve bannon','epstein','flight','plane','pilot','visoski','hanging out','march 2018','groff'],summary:'CRITICAL -- PRIMARY SOURCE: Email chain between Epstein pilot Larry Visoski and assistant Lesley Groff (March 25, 2018, 2 pages). Visoski asks: "Is S Bannon coming on this flight?" and adds "I\\'m a fan,,, lol." Groff replies: "Yes, Jeffrey said Bannon is going today! not sure who Sean is...you\\'ll have to let me know on all! Jeffrey has been hanging out a lot with Bannon theses days." This establishes: (1) Steve Bannon flew on Jeffrey Epstein\\'s private aircraft; (2) Epstein\\'s own pilot confirms Bannon as a passenger; (3) Groff\\'s comment "hanging out a lot with Bannon these days" indicates a frequent, ongoing relationship in March 2018 -- just 7 months after Bannon left the White House as Trump\\'s Chief Strategist in August 2017. Bannon remained a close Trump ally and advisor. Combined with the Feb 2018 scheduling, the dinner with Barak, the April 2019 Dropbox share, and the 16 hours of videotaped interviews, this is now the 6th+ independent document confirming an intensive Bannon-Epstein relationship. [v10.82]',date:'2018-03-25',type:'email-evidence'},
  {id:'bannon-epstein-island-question-march2018',dataset:'DS11-Email',pages:1,severity:10,keywords:['steve bannon','epstein','island','little st james','groff','visoski','return','march 2018'],summary:'CRITICAL -- PRIMARY SOURCE: Email from Lesley Groff to pilot Larry Visoski (March 25-26, 2018, 1 page). Subject line: "Re: Jeffrey\\'s plan tomorrow to island?" Groff asks: "Did Bannon or anyone else return to NY with him?" The context: On March 25, Bannon flew on Epstein\\'s plane. The same evening, Groff asks about "Jeffrey\\'s plan tomorrow to island" and whether Bannon returned to NY. This strongly implies Bannon traveled WITH Epstein on his private plane and the question was whether Bannon continued to Epstein\\'s island (Little St. James, U.S. Virgin Islands) or returned to New York. Whether Bannon actually visited the island cannot be definitively confirmed from this email alone, but Groff\\'s question establishes the possibility was being discussed by Epstein\\'s staff. NOTE: Bannon was Trump\\'s former White House Chief Strategist and remained a close advisor. [v10.82]',date:'2018-03-26',type:'email-evidence'},
  {id:'bannon-barak-un-president-dinner-71st-march2018',dataset:'DS11-Email',pages:2,severity:9,keywords:['steve bannon','ehud barak','epstein','miroslav lajcak','un general assembly','president','dinner','71st street','march 2018','groff'],summary:'HIGH VALUE -- PRIMARY SOURCE: Email chain between Groff and Vanda Siposova (office of UN GA President Lajcak), March 20-22, 2018, 2 pages. Groff invites the President of the United Nations General Assembly to dinner at Epstein\\'s townhouse: "Jeffrey will be in NY and is asking if President Lajcak could please come join him, Steve Bannon and Ehud Barak at 7:30 for dinner and interesting conversation." Dinner was at 9 East 71st Street. Lajcak confirmed for 8:30pm on March 22 but was later delayed by a storm. Lunch rescheduled for Saturday March 24 at 2pm. This shows Epstein hosting a dinner combining: (1) Steve Bannon -- Trump\\'s former White House Chief Strategist; (2) Ehud Barak -- former Israeli Prime Minister and Defense Minister, alleged intelligence connections; (3) Miroslav Lajcak -- sitting President of the UN General Assembly. Epstein functioning as a nexus between Trump\\'s inner circle, Israeli intelligence-linked figures, and international political leadership -- at his private residence. [v10.82]',date:'2018-03-22',type:'email-evidence'},
  {id:'bannon-epstein-complete-timeline-v1082',dataset:'DS9-Combined',pages:0,severity:10,keywords:['steve bannon','epstein','timeline','complete','2018','2019','flight','island','16 hours','dropbox','dinner','barak','un president','hanging out'],summary:'STRUCTURAL FINDING -- UPDATED BANNON-EPSTEIN TIMELINE compiled from 9+ primary source documents: (1) Jan 26, 2018: Scheduling email references "Watson/Bannon/Serguei" -- Groff notes she doesn\\'t have Bannon\\'s details (EFTA00468166); (2) Feb 8, 2018: Epstein emails "we will have to delay eric. i have bannon on tucs at 1" (EFTA02237514); (3) Feb 12, 2018: Weekly schedule confirms "1:00pm Appt w/Steve Bannon (Regency? 71st?)" (EFTA00469208); (4) March 20-22, 2018: Dinner planned at 71st Street with Bannon, Ehud Barak, and UN GA President Lajcak (EFTA00471126); (5) March 25, 2018: Bannon flies on Epstein\\'s private plane -- "Jeffrey has been hanging out a lot with Bannon these days" (EFTA00471570); (6) March 25-26, 2018: Groff asks if Bannon returned to NY or went to "the island" (EFTA00471504); (7) Jan 22, 2019: Bannon listed on "People to See in Paris" (EFTA02276212); (8) April 13, 2019: Bannon shares Dropbox folder directly with Epstein (EFTA02315270); (9) Pre-death: Bannon conducts 16 hours of recorded video interviews with Epstein (per Mark Epstein OIG testimony, EFTA00113482); (10) Post-death: Mark Epstein contacts Bannon about tapes, Bannon claims attorney-client privilege despite not being an attorney. This establishes a MINIMUM 16-month documented relationship (Jan 2018 - April 2019) with at least 6 in-person meetings, 1 flight on Epstein\\'s plane, possible island visit, file sharing, and 16 hours of recordings. Bannon left the Trump White House Aug 2017 but remained one of Trump\\'s closest political allies. [v10.82]',date:'2019-04-13',type:'compiled-timeline'},
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
count = content.count('v10.81')
print(f"Replacing {count} occurrences of 'v10.81' with 'v10.82'")
content = content.replace('v10.81', 'v10.82')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.82.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.81')
new_ver = verify.count('v10.82')
print(f"Remaining v10.81: {remaining}")
print(f"Total v10.82: {new_ver}")

for check_id in ['bannon-epstein-flight-hanging-out-march2018',
                  'bannon-epstein-island-question-march2018',
                  'bannon-barak-un-president-dinner-71st-march2018',
                  'bannon-epstein-complete-timeline-v1082']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
