#!/usr/bin/env python3
"""Update dashboard with Trump/Administration nexus findings — v10.71"""
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

# New TIMELINE entries — Trump/Administration connections
timeline_entries = """  {date:'1997-01-05',event:'Flight 934: EPSTEIN, MAXWELL, DONALD TRUMP, MARK EPSTEIN, DIDIER on Epstein aircraft per pilot David Rodgers flight logs (FBI FD-302).',source:'EFTA00159180'},
  {date:'1998-06-01',event:'Virginia Roberts (age 15) recruited by Maxwell at Trump Mar-a-Lago Club while working as $9/hr changing room assistant. Father was maintenance manager.',source:'EFTA00269967'},
  {date:'1995-01-01',event:'Victim (age ~15) taken to Mar-a-Lago by Epstein to meet Trump. Epstein told Trump "This is a good one, huh." Before sexual abuse started.',source:'EFTA00158473'},
  {date:'2007-06-26',event:'Dershowitz, Roy Black, Lefcourt, Sanchez present legal arguments against indictment to AUSA Acosta. NPA negotiations begin.',source:'EFTA00190318'},
  {date:'2016-07-04',event:'Katie Johnson FBI complaint filed: alleges Trump and Epstein sexually assaulted 13-year-old at Epstein NYC parties in summer 1994. Civil suit later voluntarily dismissed Nov 2016.',source:'EFTA00129126'},
  {date:'2019-12-13',event:'FBI/NYPD discover Epstein sex offender registration phone linked to Wexner The Limited company. MC2 model housing at 301 E 66th — thousands of foreign passport holders.',source:'EFTA00152144'},
  {date:'2020-01-17',event:'SDNY actively investigating victim who claims introduction to Trump at age 14. FBI scheduling interviews with family members. Media coverage of suit.',source:'EFTA00074344'},
  {date:'2020-06-08',event:'FBI pre-arrest planning for Maxwell: 6-count indictment drafted. Active surveillance — mail cover, pen register, physical surveillance. Prince Andrew MLAT request sent.',source:'EFTA00149560'},
  {date:'2020-10-16',event:'FBI FD-1023 CHS report: Dershowitz told Acosta "Epstein belonged to both US and allied intelligence services." CHS claims Chabad co-opting Trump presidency via Kushner.',source:'EFTA00090314'},
  {date:'2025-03-01',event:'AG Bondi directs ~1,000 FBI personnel on 24-hour shifts to review ~100K Epstein records. Personnel instructed to FLAG records mentioning President Trump.',source:'EFTA00173350'},
  {date:'2025-07-22',event:'FBI internal "Names in JE file" — Trump listed with note: "one identified victim claimed abuse by Trump but ultimately refused to cooperate."',source:'EFTA00161528'},
  {date:'2011-04-04',event:'Epstein staff email: "Howard Lutnick returned your call." Direct phone relationship between Epstein and current Commerce Secretary.',source:'EFTA00436148'},
"""

# New FINDINGS entries — Trump/Administration nexus
findings_entries = """  {id:'trump-admin-nexus-flight-934',dataset:'DS9-FD302',pages:17,severity:10,keywords:['trump','maxwell','mark epstein','flight logs','rodgers'],summary:'CRITICAL: FBI FD-302 of David Rodgers, Epstein chief pilot 29 years. Flight 934 (Jan 5, 1997): EPSTEIN, MAXWELL, DONALD TRUMP, MARK EPSTEIN, DIDIER on aircraft together. "AP" on other flights confirmed as Adam Perry Lang, NOT Prince Andrew. Rodgers stopped recording passenger names Feb 2007. Cessna N908GM registered to Ghislaine Maxwell. [v10.71]',date:'2020-02-07',type:'fbi-interview'},
  {id:'trump-admin-nexus-mar-a-lago-recruitment',dataset:'DS9-FD302',pages:12,severity:10,keywords:['trump','mar-a-lago','maxwell','victim','recruitment','giuffre'],summary:'CRITICAL: FBI FD-302 of Virginia Roberts Giuffre (Mar 17, 2011, Case 31E-MM-108062). Recruited by Maxwell at Trumps Mar-a-Lago Club while working as $9/hr changing room assistant at age 15. Father was maintenance manager. First taken to Epstein residence at El Brillo Way same day. Maxwell demonstrated sexual acts. Giuffre later traveled worldwide with Epstein. Met Prince Andrew, Clinton, Gore. Epstein sent 3 twelve-year-old French girls as birthday gift. 50 surveillance cameras in NYC mansion. [v10.71]',date:'2011-03-17',type:'fbi-interview'},
  {id:'trump-admin-nexus-good-one-huh',dataset:'DS9-FD302',pages:7,severity:10,keywords:['trump','mar-a-lago','victim','minor','massage'],summary:'CRITICAL: FBI FD-302 victim interview — "EPSTEIN took [victim] in a dark green car to Mar-A-Lago to meet DONALD TRUMP. EPSTEIN told TRUMP, This is a good one, huh." Introduction occurred BEFORE sexual abuse started. Same victim: ~100 massage incidents, hidden cameras in clocks in massage room, Weinstein fondled victim while masturbating. Victim later DENIES separate allegation that she was "a victim of TRUMP but this was not true." [v10.71]',date:'2019-09-19',type:'fbi-interview'},
  {id:'trump-admin-nexus-sdny-active-investigation',dataset:'DS9-DOJ',pages:5,severity:9,keywords:['trump','sdny','victim','age 14','investigation'],summary:'HIGH VALUE: SDNY internal email chain (Dec 2019 - Feb 2020) showing FBI/SDNY actively investigating victim who claimed to be "introduced to Trump at age 14" and "molested at 13." FBI scheduling interviews with victim family members (siblings, mother) and witnesses. Attorney at Panish Shea & Boyle representing victim. Multiple media outlets covering lawsuit filing. [v10.71]',date:'2020-02-06',type:'doj-internal'},
  {id:'trump-admin-nexus-fbi-names-list',dataset:'DS9-FBI',pages:1,severity:10,keywords:['trump','prince andrew','staley','black','weinstein','clinton','dershowitz','wexner'],summary:'EXTREMELY SIGNIFICANT: FBI internal email (Jul 22, 2025) titled "Names in JE file" listing ALL high-profile persons with positive case hits in 50D-NY-3027571. Trump entry: "one identified victim claimed abuse by Trump but ultimately refused to cooperate." Also lists: Prince Andrew, Jes Staley, Leon Black, Glen Dubin, Harvey Weinstein, Bill Clinton, Alan Dershowitz, David Copperfield, Les Wexner, Jean Luc Brunel, Naomi Campbell, Chris Tucker, Larry Summers, Kevin Spacey, Bill Gates. [v10.71]',date:'2025-07-22',type:'fbi-internal'},
  {id:'trump-admin-nexus-bondi-flag-trump',dataset:'DS9-Senate',pages:5,severity:10,keywords:['bondi','trump','fbi','surveillance','modified','durbin'],summary:'CRITICAL: Senate Judiciary Committee letter from Sen. Durbin to AG Bondi (Jul 18, 2025). Reveals: (1) ~1,000 FBI personnel on 24-hour shifts reviewing Epstein records; (2) Personnel instructed to FLAG records mentioning President Trump; (3) Released MCC surveillance footage labeled "full raw" was actually MODIFIED per WIRED metadata analysis (~3 min cut); (4) Trump birthday letter to Epstein contained "outline of naked woman" with signature below her waist; (5) Bondi claimed client list "sitting on my desk" — DOJ later found "no incriminating client list." [v10.71]',date:'2025-07-18',type:'congressional'},
  {id:'trump-admin-nexus-acosta-intelligence',dataset:'DS9-FBI',pages:3,severity:10,keywords:['acosta','intelligence','mossad','dershowitz','kushner','chabad'],summary:'CRITICAL: FBI FD-1023 CHS Report (Oct 2020). CHS states Dershowitz told Acosta that "Epstein belonged to both U.S. and allied intelligence services." Mossad debriefed Dershowitz after Epstein calls. Epstein "trained as a spy under" Ehud Barak. CHS claims: "Trump has been compromised by Israel, and Kushner is the real brains behind his organization." Apollo/Leon Black lent Kushners $184M. Jared and Josh Kushner both Dershowitz students at Harvard. [v10.71]',date:'2020-10-16',type:'fbi-intelligence'},
  {id:'trump-admin-nexus-lutnick-epstein',dataset:'DS9-Email',pages:1,severity:8,keywords:['lutnick','cantor fitzgerald','bgc','island','epstein'],summary:'HIGH VALUE: (1) EFTA00436148 — Epstein staff email (Apr 2011): "Howard Lutnick returned your call" — direct phone relationship between Epstein and current Commerce Secretary; (2) FBI intelligence report on alleged money laundering via BGC Financial/Cantor Fitzgerald; (3) Allison Lutnick emails (Dec 2012) coordinating family visit to Epstein island area with 2 families and 8 children ages 7-16; (4) Epstein staff informed "JE asked me to provide him this" regarding Lutnick presence near St. Thomas. 54 documents mention Lutnick. [v10.71]',date:'2011-04-04',type:'email-evidence'},
  {id:'trump-admin-nexus-kushner-financial',dataset:'DS9-FBI',pages:3,severity:8,keywords:['kushner','apollo','leon black','chabad','money laundering','hapoalim'],summary:'HIGH VALUE: FBI FD-1023 CHS claims: "Kushner has moved a lot of Russian investment money around. The FBI should investigate Kushner family charities to find evidence of corruption and money laundering. Chabad routinely uses charities to launder money." Apollo/Leon Black $184M loan to Kushner during 666 5th Ave crisis. Ivanka Trump board member of Signature Bank (SBNY), "go to lender" for Trump/Kushner. Bank Hapoalim whistleblower filings link Putin/Rakishev/Trump/Kushner. [v10.71]',date:'2020-10-16',type:'fbi-intelligence'},
  {id:'trump-admin-nexus-cvra-14-phones',dataset:'DS9-Legal',pages:389,severity:9,keywords:['trump','mar-a-lago','phone numbers','mark epstein','flight'],summary:'HIGH VALUE: CVRA Case Compilation (389pg). Contains: (a) 14 Trump phone numbers found in Epstein computer; (b) Mark Epstein testified Trump flew on plane; (c) Jane Doe 102 recruited at Mar-a-Lago; (d) Epstein took Fifth Amendment on questions about Trump; (e) Giuffre declarations: Epstein maintained videos for blackmail, slept with 1000+ Brunel girls; (f) Rodriguez deposition: met Clinton on Epstein plane; (g) Sen. Mitchell, Prince Andrew, Dershowitz named. [v10.71]',date:'2014-12-30',type:'legal-filing'},
  {id:'trump-admin-nexus-katie-johnson',dataset:'DS9-FBI',pages:4,severity:7,keywords:['trump','epstein','13 year old','sexual assault','complaint'],summary:'FBI FD-71 complaint form (Jul 4, 2016): "Katie Johnson" sexual assault allegations against Trump and Epstein involving a 13-year-old at Epstein NYC parties in summer 1994. Filed through FBI Public Access Line. Underlying civil suit voluntarily dismissed Nov 2016. CAVEAT: Unverified complaint; civil case never went to trial. [v10.71]',date:'2016-07-04',type:'fbi-complaint'},
  {id:'trump-admin-nexus-employee-trump-org',dataset:'DS9-FD302',pages:3,severity:7,keywords:['trump','maxwell','employee','massage rooms'],summary:'FBI/NYPD Child Exploitation Task Force interview (Jul 29, 2019, 11 days before death). Chief Engineer (18 years service): "applied for job with Trump organization, was referred to EPSTEIN." Hired through Maxwell. Confirmed massage rooms in ALL locations. Another employee worked at Wexner address before Epstein took residence. [v10.71]',date:'2019-07-29',type:'fbi-interview'},
"""

# Insert TIMELINE entries (before closing ])
content = content[:timeline_close] + "\n" + timeline_entries + content[timeline_close:]

# Insert FINDINGS entries (before closing ])
content = content[:findings_close] + "\n" + findings_entries + content[findings_close:]

# Version bump
count = content.count('v10.70')
print(f"Replacing {count} occurrences of 'v10.70' with 'v10.71'")
content = content.replace('v10.70', 'v10.71')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.71 with Trump/Administration nexus findings.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.70')
new_ver = verify.count('v10.71')
print(f"Remaining v10.70: {remaining}")
print(f"Total v10.71: {new_ver}")

for check_id in ['trump-admin-nexus-flight-934', 'trump-admin-nexus-mar-a-lago-recruitment',
                  'trump-admin-nexus-good-one-huh', 'trump-admin-nexus-fbi-names-list',
                  'trump-admin-nexus-bondi-flag-trump', 'trump-admin-nexus-lutnick-epstein',
                  'trump-admin-nexus-kushner-financial', 'trump-admin-nexus-acosta-intelligence']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
