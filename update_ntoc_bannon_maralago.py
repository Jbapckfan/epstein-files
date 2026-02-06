#!/usr/bin/env python3
"""Update dashboard with NTOC complaints, Bannon meetings, Mar-a-Lago recruitment — v10.76"""
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
timeline_entries = """  {date:'2025-08-07',event:'FBI Child Exploitation Task Force circulates NTOC master complaint log listing 20+ Trump-related tips/allegations received during Epstein investigation. Document notes many are second-hand, several deemed not credible. Includes Alexander brothers follow-up interview request.',source:'EFTA01660679_v2'},
  {date:'2018-02-08',event:'Epstein emails from jeevacation@gmail.com: "we will have to delay eric. i have bannon on tucs at 1." Response: "OK on Eric...adding in Bannon! ;)" Confirms Epstein personally scheduling meeting with Steve Bannon for Feb 13, 2018.',source:'EFTA02237514'},
  {date:'2019-01-22',event:'Epstein assistant Lesley Groff emails Paris schedule. "People to See in Paris: Kifah, Pinto, Jack Lang, Raafat Terje, Sultan, Eduardo, Nicole, Tabor, Moritz, Bannon, Astrid, Annas." Bannon on Epstein contact list 6 months before arrest.',source:'EFTA02276212'},
  {date:'1992-01-01',event:'George Houraney (American Dream Enterprise) organizes "calendar girl" competition at Mar-a-Lago at Trump\\'s request. "I said Who\\'s coming tonight? I have 28 girls coming. It was him and Epstein." Trump and Epstein were the only men present with 28 women.',source:'EFTA00042963'},
  {date:'1998-06-01',event:'15-year-old girl working summer job at Mar-a-Lago allegedly recruited by Ghislaine Maxwell for Epstein. Maxwell invited her to "make good money by learning massage therapy." Victim claims 4 years as Epstein\\'s sex slave, pimped to wealthy friends.',source:'EFTA00065479'},
"""

# New FINDINGS entries
findings_entries = """  {id:'fbi-ntoc-trump-complaint-master-log',dataset:'DS9-FBI',pages:6,severity:10,keywords:['ntoc','fbi','trump','complaints','allegations','child exploitation','task force','alexander brothers'],summary:'CRITICAL — PRIMARY SOURCE: FBI NTOC (National Threat Operations Center) master complaint log, circulated Aug 6-7, 2025 by Child Exploitation & Human Trafficking Task Force, FBI New York Field Office. Lists 20+ separate tips/complaints naming Donald Trump in connection with Epstein. IMPORTANT: Document notes "some of these individuals are reporting second-hand information." Several were "deemed not credible," had "no contact made," or "no contact information provided." Allegations range from party attendance to sexual assault of minors. One tip (Alexander brothers) being actively investigated with interview requested. Yellow highlighting added for "the salacious piece." This document was being shared internally as FBI reviewed Trump-related allegations per AG Bondi\\'s order to flag Trump-mentioning records. [v10.76]',date:'2025-08-07',type:'fbi-internal'},
  {id:'ntoc-mar-a-lago-party-invitations',dataset:'DS9-FBI',pages:6,severity:8,keywords:['mar-a-lago','trump','maxwell','epstein','party','prostitutes','bobby cox'],summary:'FBI NTOC log includes tip: complainant invited by "Lisa Villeneuve" (going by "Ghislaine Lisa Villeneuve") to party at Epstein\\'s Palm Beach residence where she met model scout "Bobby Cox" referred to as a pimp. Complainant states they were invited by Donald Trump to a party at Mar-a-Lago and was told by Villeneuve "it was for prostitutes." Separate tip: neighbor sought modeling gigs at Trump Modeling Agency in NYC (1998-2000), shown photo of recruiter who looked like Epstein, neighbor "allegedly raped several times." Note: These are UNVERIFIED tips in FBI intake system. [v10.76]',date:'2025-08-07',type:'fbi-internal'},
  {id:'bannon-epstein-scheduling-email',dataset:'DS11-Email',pages:1,severity:9,keywords:['steve bannon','epstein','email','scheduling','jeevacation','february 2018'],summary:'CRITICAL — PRIMARY SOURCE: Epstein email from jeevacation@gmail.com (Feb 8, 2018): "we will have to delay eric. i have bannon on tucs at 1. i forwarded it to you." Response: "OK on Eric...adding in Bannon! ;)" Confirms Epstein personally scheduling a meeting with Steve Bannon (then recently departed as Trump White House Chief Strategist, Aug 2017) for Tuesday Feb 13, 2018. Meeting scheduled at Epstein\\'s location after arriving NY-Islip. Bannon left White House less than 6 months prior. [v10.76]',date:'2018-02-08',type:'email-evidence'},
  {id:'bannon-paris-people-to-see-jan2019',dataset:'DS11-Schedule',pages:3,severity:8,keywords:['steve bannon','paris','people to see','lesley groff','january 2019','jack lang'],summary:'HIGH VALUE — PRIMARY SOURCE: Epstein assistant Lesley Groff email (Jan 22, 2019) lists "People to See in Paris" for Epstein\\'s trip: "Kifah, Pinto, Jack Lang, Raafat Terje, Sultan, Eduardo, Nicole, Tabor, Moritz, Bannon, Astrid, Annas." Schedule includes meetings Jan 23-31, 2019 in Paris. Steve Bannon on Epstein\\'s active contact list just 6 months before Epstein\\'s arrest (July 6, 2019). Also lists Maxim Churkin (Jan 24 at 4:30pm) and Joscha Bach (AI researcher traveling from Zurich). [v10.76]',date:'2019-01-22',type:'schedule'},
  {id:'houraney-28-girls-mar-a-lago-1992',dataset:'DS9-News',pages:84,severity:9,keywords:['george houraney','28 girls','calendar girl','mar-a-lago','1992','american dream enterprise','trump','epstein'],summary:'CRITICAL: NYT investigation (in FBI files). George Houraney (American Dream Enterprise) organized "calendar girl" competition at Mar-a-Lago at Trump\\'s request in 1992. Houraney: "At the very first party, I said Who\\'s coming tonight? I have 28 girls coming. It was him and Epstein." Trump and Epstein were the only men present. Houraney: "I said Donald, this is supposed to be a party with V.I.P.s. You\\'re telling me it\\'s you and Epstein?" Relationship ended after "failed business arrangement." Epstein "blamed Mr. Trump for his legal problems with Palm Beach County police." Epstein claimed he introduced Trump to Melania — neither Trump has confirmed. [v10.76]',date:'1992-01-01',type:'news-reporting'},
  {id:'mar-a-lago-victim-recruitment-1998',dataset:'DS9-News',pages:26,severity:9,keywords:['mar-a-lago','ghislaine maxwell','recruitment','15 year old','massage','sex slave','virginia roberts'],summary:'CRITICAL: FBI files contain reporting that a 15-year-old girl working a summer job at Mar-a-Lago was recruited by Ghislaine Maxwell for Epstein in 1998. Maxwell invited her to "make good money by learning massage therapy." Like other victims, she was sexually abused during massage sessions. Maxwell told her she had "lots of potential" and asked her to return the next day. Victim claims she spent 4 years as "Epstein\\'s sex slave and was pimped out to the wealth manager\\'s rich and powerful friends." This is the Virginia Roberts Giuffre recruitment narrative — directly connecting Trump\\'s property to Epstein\\'s trafficking pipeline. [v10.76]',date:'1998-06-01',type:'news-reporting'},
  {id:'apollo-epstein-kushner-sec-whistleblower',dataset:'DS9-Whistleblower',pages:13,severity:7,keywords:['apollo','leon black','kushner','sec','whistleblower','esww','money laundering','milken'],summary:'SEC whistleblower Chris Dilorio filed multiple complaints (April-Nov 2019-2020) with subject line "Apollo/Epstein/Kushner connection." Alleges: (1) Leon Black/Apollo controlled ESWW (Environmental Solutions Worldwide) — the ONLY SEC-disclosed Epstein investment vehicle; (2) SEC filed fraud complaint against ESWW in 2002 but let it operate 13 more years; (3) Apollo gave Kushner Companies $180M loan; (4) SEC dropped Apollo probe month after this loan; (5) Josh Harris (Apollo co-founder) considered for White House job after meetings with Kushner. Note: These are whistleblower allegations, not verified findings. [v10.76]',date:'2020-10-30',type:'whistleblower-complaint'},
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
count = content.count('v10.75')
print(f"Replacing {count} occurrences of 'v10.75' with 'v10.76'")
content = content.replace('v10.75', 'v10.76')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.76 with NTOC/Bannon/Mar-a-Lago findings.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.75')
new_ver = verify.count('v10.76')
print(f"Remaining v10.75: {remaining}")
print(f"Total v10.76: {new_ver}")

for check_id in ['fbi-ntoc-trump-complaint-master-log', 'ntoc-mar-a-lago-party-invitations',
                  'bannon-epstein-scheduling-email', 'bannon-paris-people-to-see-jan2019',
                  'houraney-28-girls-mar-a-lago-1992', 'mar-a-lago-victim-recruitment-1998',
                  'apollo-epstein-kushner-sec-whistleblower']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
