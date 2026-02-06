#!/usr/bin/env python3
"""Update dashboard with Jane Doe complaint, FBI Assessment, FBI CHS intel report, Acosta intelligence claim, Lutnick donation — v10.80"""
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
timeline_entries = """  {date:'2020-01-16',event:'Jane Doe files federal complaint (SDNY) against Epstein Estate and Maxwell. Alleges meeting Epstein and Maxwell at Interlochen Arts Camp in Michigan in 1994 at age 13. Epstein took her to Mar-a-Lago and introduced her to Donald J. Trump. Epstein elbowed Trump: "This is a good one, right?" Trump smiled and nodded.',source:'EFTA00019101'},
  {date:'2016-07-04',event:'Attorney Tom Meagher contacts FBI Public Access Line to report sexual exploitation and rape of 13-year-old Jane Doe (alias "Katie Johnson") by Donald J. Trump and Jeffrey Epstein at parties in NYC summer 1994. FBI opens Assessment Zero File. Trump classified as "Main, Person" in FBI entity list.',source:'EFTA00129126'},
  {date:'2020-10-16',event:'FBI Los Angeles CHS (S-00099701) reports via encrypted messaging: Dershowitz told Acosta that Epstein "belonged to both U.S. and allied intelligence services." CHS states Kushner brothers were Dershowitz students. Claims Trump "compromised by Israel" and Chabad trying to "co-opt the Trump presidency."',source:'EFTA00090314'},
  {date:'2019-07-10',event:'SDNY AUSA internally circulates Daily Beast article reporting Acosta told Trump transition team: "I was told Epstein belonged to intelligence and to leave it alone." Transition team accepted this and hired Acosta as Labor Secretary anyway.',source:'EFTA00030182'},
  {date:'2017-11-09',event:'Jeffrey Epstein donates $50,000 (Platinum Page level) to UJA-Federation Wall Street Dinner honoring Howard W. Lutnick (now Commerce Secretary). Event organizers describe Epstein as "a close friend of the Lutnicks." Epstein agrees to be listed in Roll of Honor.',source:'EFTA00462693'},
"""

# New FINDINGS entries
findings_entries = """  {id:'jane-doe-interlochen-mar-a-lago-trump-good-one',dataset:'DS9-DOJ',pages:10,severity:10,keywords:['jane doe','interlochen','mar-a-lago','trump','this is a good one','epstein','maxwell','13 years old','guinea pig','michigan','palm beach','71st street','new mexico'],summary:'CRITICAL — PRIMARY SOURCE: Federal civil complaint (SDNY, Jan 16, 2020, 10 pages). Jane Doe alleges she met Epstein and Maxwell at Interlochen Arts Camp in Michigan in summer 1994 at age 13. Epstein and Maxwell groomed her over months, acting as "godfather" and "older sister." CRITICAL PASSAGE (Paragraph 17): "During one of Doe\\\\'s encounters with Epstein, he took her to Mar-a-Lago where he introduced her to its owner, Donald J. Trump. Introducing 14-year-old Doe to Donald J. Trump, Epstein elbowed Trump playfully asking him, referring to Doe, \\\\'This is a good one, right?\\\\' Trump smiled and nodded in agreement. They both chuckled and Doe felt uncomfortable, but, at the time, was too young to understand why." Abuse escalated to rape at 71st Street townhouse, Palm Beach, and New Mexico ranch. Epstein moved Doe to NYC at 16, co-signed her lease, paid for private school. Complaint describes Doe as Epstein and Maxwell\\\\'s "first known victim" and "guinea pig." Filed under Child Victims Act. NOTE: This is a civil complaint — allegations are sworn but unproven. Trump is named as a witness/participant, not a defendant. [v10.80]',date:'2020-01-16',type:'federal-complaint'},
  {id:'fbi-assessment-katie-johnson-trump-epstein-rape',dataset:'DS9-DOJ',pages:4,severity:10,keywords:['fbi','fd-71','assessment','katie johnson','jane doe','trump','epstein','rape','13 years old','sexual exploitation','minor','parties','tiffany doe','tom meagher'],summary:'CRITICAL — PRIMARY SOURCE: FBI FD-71 Complaint Form (Assessment Zero File, Nov 23, 2016, 4 pages). Attorney Tom Meagher reports to FBI Public Access Line (July 4, 2016) the "sexual exploitation and rape of a minor child of 13 years of age by Donald J Trump and Jeffrey E Epstein." Specific allegations over four parties in NYC summer 1994: (1) First party: Doe forced to massage Trump\\\\'s penis; (2) Second party: Doe performed oral sex on Trump; (3) Third party: Doe performed oral sex on Trump with another girl; (4) Fourth party: "Doe was raped by Trump vaginally penetrating Doe with his penis. Epstein was angry that Trump was the one to take Doe\\\\'s virginity and then went on to rape Doe." Both men struck Doe and threatened: "We\\\\'ll make you disappear like [REDACTED]." Trump listed in FBI Entities as "Donald Trump (Main, Person)." FBI ran Sentinel query for cases involving Epstein and Trump regarding exploitation of minors. CRITICAL CONTEXT: This corresponds to the "Katie Johnson" civil lawsuit (filed April 26, 2016, refiled June 20, 2016, later withdrawn). These are UNVERIFIED allegations from a civil proceeding that was ultimately withdrawn before trial. The FBI assessed the complaint but investigative follow-up is unclear from this document alone. [v10.80]',date:'2016-11-23',type:'fbi-assessment'},
  {id:'fbi-chs-dershowitz-mossad-epstein-intelligence-kushner',dataset:'DS9-DOJ',pages:3,severity:10,keywords:['fbi','fd-1023','chs','dershowitz','mossad','epstein','intelligence','kushner','jared kushner','josh kushner','acosta','chabad','trump','ivanka','israel','leon black','apollo','tillerson','broidy','cadre'],summary:'CRITICAL — PRIMARY SOURCE: FBI FD-1023 CHS Reporting Document (Oct 19, 2020, 3 pages, Source S-00099701, LA Field Office Squad 101). Synopsis: "Foreign influence on U.S. officials by Israel, Russia, and UAE." Key claims from Confidential Human Source: (1) Dershowitz told CHS "if he were young again, he would be holding a stun gun as an Israeli Intelligence (Mossad) agent" — CHS believed Dershowitz "was co-opted by Mossad"; (2) CHS "remembered Dershowitz tell Alex [Acosta] that Epstein belonged to both U.S. and allied intelligence services"; (3) After Dershowitz-Epstein phone calls, "Mossad would then call Dershowitz to debrief"; (4) Epstein "trained as a spy" under Ehud Barak; (5) "Josh Kushner and Jared Kushner were both [Dershowitz\\\\'s] students"; (6) "Chabad is doing everything they can to co-opt the Trump presidency"; (7) Ivanka and Jared visited Rabbi Schneerson\\\\'s gravesite on election day; (8) "Trump has been compromised by Israel, and Kushner is the real brains behind his organization and his Presidency"; (9) Leon Black gave Epstein $50M, Apollo lent Kushners $184M; (10) Rex Tillerson told CHS that Jared was "running a rival State Department operation." NOTE: CHS reporting reflects one source\\\\'s claims/opinions and is not independently verified by the FBI in this document. [v10.80]',date:'2020-10-19',type:'fbi-chs-report'},
  {id:'acosta-belonged-to-intelligence-sdny-circulation',dataset:'DS9-DOJ',pages:1,severity:9,keywords:['acosta','belonged to intelligence','trump transition','leave it alone','labor secretary','sdny','ausa','daily beast','above his pay grade'],summary:'HIGH VALUE — PRIMARY SOURCE: Internal SDNY email (July 10, 2019, 1 page). An Assistant U.S. Attorney from the Southern District of New York circulates article containing explosive claim. Key passage: "I was told Epstein \\\\'belonged to intelligence\\\\' and to leave it alone," [Acosta] told his interviewers in the Trump transition, who evidently thought that was a sufficient answer and went ahead and hired Acosta." Also: Acosta "had cut the non-prosecution deal with one of Epstein\\\\'s attorneys because he had \\\\'been told\\\\' to back off, that Epstein was above his pay grade." CRITICAL CONTEXT: (1) This was circulated internally by SDNY prosecutors 4 days after Epstein\\\\'s July 6, 2019 arrest; (2) Trump appointed Acosta as Labor Secretary despite this explanation; (3) Acosta resigned July 12, 2019 after renewed scrutiny; (4) This corroborates the FBI CHS report (EFTA00090314) where Dershowitz told Acosta that Epstein "belonged to both U.S. and allied intelligence services." [v10.80]',date:'2019-07-10',type:'internal-doj-email'},
  {id:'lutnick-epstein-50k-donation-close-friend-2017',dataset:'DS11-Email',pages:2,severity:9,keywords:['howard lutnick','epstein','donation','50000','uја','cantor fitzgerald','close friend','roll of honor','commerce secretary','2017'],summary:'HIGH VALUE — PRIMARY SOURCE: Email chain (Nov 9, 2017, 2 pages). Jeffrey Epstein (jeevacation@gmail.com) donates $50,000 to UJA-Federation Wall Street Dinner honoring Howard W. Lutnick, Chairman/CEO of Cantor Fitzgerald. At the Platinum Page level ($50,000), Epstein received a table for 10 and commemorative journal page. Epstein declined to use the table himself: "no, tell lutnik he can fill them." Epstein agreed to be listed in the "Roll of Honor." Event organizers describe Epstein as "a close friend of the Lutnicks" (plural — implying family friendship). Epstein is listed under "JEE" (Jeffrey E. Epstein enterprises) confidentiality notice claiming attorney-client privilege. CRITICAL CONTEXT: (1) This donation occurred in November 2017 — during Trump\\\\'s first year in office and 9 years after Epstein\\\\'s 2008 conviction; (2) Lutnick is now (2025) the U.S. Secretary of Commerce; (3) Combined with previous findings of phone calls between Epstein and Lutnick, this establishes a continuing financial and personal relationship with a convicted sex offender well into the Trump era. [v10.80]',date:'2017-11-09',type:'email-evidence'},
  {id:'trump-admin-epstein-connections-structural-v1080',dataset:'DS9-Combined',pages:0,severity:10,keywords:['trump','administration','epstein','connections','structural','acosta','lutnick','dershowitz','kushner','bannon','blanche','intelligence','conflict of interest'],summary:'STRUCTURAL FINDING — TRUMP ADMINISTRATION EPSTEIN CONNECTIONS MAP compiled from primary sources across v10.74-v10.80: (1) TODD BLANCHE (Deputy AG): Trump\\\\'s personal defense attorney now conducting Maxwell proffer, eliciting exculpatory testimony under immunity [v10.78]; (2) ALEXANDER ACOSTA (former Labor Sec): Told Trump transition Epstein "belonged to intelligence," hired anyway; drafted 60-count indictment then gave NPA with blanket co-conspirator immunity [v10.78, v10.80]; (3) HOWARD LUTNICK (Commerce Sec): $50,000 Epstein donation to his UJA honor dinner 2017; described as "close friend" [v10.80]; (4) ALAN DERSHOWITZ (Trump advisor/attorney): Told Acosta Epstein belonged to intelligence; CHS claims co-opted by Mossad; debriefed by Mossad after Epstein calls; Kushner brothers were his students [v10.80]; (5) STEVE BANNON (former Chief Strategist): 16 hours videotaped interviews with Epstein; Dropbox file sharing April 2019; active relationship through arrest [v10.76, v10.79]; (6) JARED KUSHNER (former Senior Advisor): Dershowitz student; Apollo/Leon Black $184M loan connection; CHS claims "real brains behind Trump\\\\'s Presidency" [v10.80]; (7) PAM BONDI (AG): First Trump FL AG endorsement aligned with $25K donation timing [v10.74]. Seven current or former Trump administration officials with documented Epstein connections across sworn testimony, FBI reports, emails, and court filings. [v10.80]',date:'2025-02-06',type:'structural-analysis'},
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
count = content.count('v10.79')
print(f"Replacing {count} occurrences of 'v10.79' with 'v10.80'")
content = content.replace('v10.79', 'v10.80')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.80 with Jane Doe complaint + FBI Assessment + FBI CHS intel + Acosta intelligence + Lutnick donation.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.79')
new_ver = verify.count('v10.80')
print(f"Remaining v10.79: {remaining}")
print(f"Total v10.80: {new_ver}")

for check_id in ['jane-doe-interlochen-mar-a-lago-trump-good-one', 'fbi-assessment-katie-johnson-trump-epstein-rape',
                  'fbi-chs-dershowitz-mossad-epstein-intelligence-kushner', 'acosta-belonged-to-intelligence-sdny-circulation',
                  'lutnick-epstein-50k-donation-close-friend-2017', 'trump-admin-epstein-connections-structural-v1080']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
