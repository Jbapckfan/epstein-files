#!/usr/bin/env python3
"""Update dashboard with Giuffre sworn declaration, SDNY Wexner proffer, Gates/Nikolic bgC3, Mar-a-Lago subpoena — v10.84"""
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
timeline_entries = """  {date:'2013-02-27',event:'Epstein\\'s schedule: "Reminder: Bill Gates in NY" and "2:00pm Appt w/Bill Gates" -- five years after Epstein\\'s 2008 conviction. Same day: Lithuanian model Vaiva Martinonyte arriving JFK via Virgin Atlantic.',source:'EFTA00395096'},
  {date:'2013-04-13',event:'Epstein asks Richard Branson if he can bring "Bill Gates assistant, Boris Nikolic" to lunch on Branson\\'s island. Branson replies: "Of course."',source:'EFTA00392464'},
  {date:'2013-08-24',event:'Boris Nikolic (Gates\\'s science advisor) forwards to Epstein a draft separation agreement from Bill Gates\\'s bgC3 -- prepared by Epstein\\'s lawyer Larry Cohen. Epstein was directly involved in drafting employment terms between Gates and his own advisor.',source:'EFTA02730265'},
  {date:'2014-03-14',event:'Epstein calendar: "TBD Dinner w/Bill Gates" in NY. Same calendar page includes: "Reminder: NYS Sex Off Reg. requests updated photo be taken between March 26-May 5 in the VI."',source:'EFTA00373880'},
  {date:'2018-05-28',event:'Howard Lutnick coordinates with Epstein on opposing NYC building development near their properties. Lutnick: "I\\'m sending a lawyer." Epstein responds: "WILL DO!" Active collaboration one year before Epstein\\'s 2019 arrest.',source:'EFTA00474455'},
  {date:'2021-11-17',event:'SDNY prosecutors subpoena Mar-a-Lago for employment records of an Epstein victim who worked there circa 2000. Trump Organization compliance counsel struggles to locate records; HR Director "prior to 2007 is no longer with Mar a Lago."',source:'EFTA00078510'},
"""

# New FINDINGS entries
findings_entries = """  {id:'giuffre-sworn-declaration-dershowitz-6x-prince-andrew-3x',dataset:'DS9-Legal',pages:14,severity:10,keywords:['virginia giuffre','dershowitz','prince andrew','sworn','declaration','blackmail','brunel','acosta','sex trafficking','six times'],summary:'CRITICAL -- PRIMARY SOURCE: Virginia Giuffre sworn declarations under penalty of perjury (EFTA00098456, 14 pages, January-February 2015, Case No. 08-80736-CIV-MARRA, SDFL). Key sworn testimony: (1) Para 24-31: Sexual intercourse with Alan Dershowitz "at least six times" starting at age 16 -- locations include New York, Palm Beach, Zorro Ranch NM, Little Saint James Island, and Epstein\\'s airplane; (2) Para 32-46: Sex with Prince Andrew three times -- London (age 17), New York (age 17), and orgy on Little Saint James (age 18). Andrew "guessed her age as 17." Epstein paid $15,000 for Andrew encounter; (3) Para 19: Epstein told her the purpose was so powerful people would "owe him" and he would "have something on them"; (4) Para 11: "Epstein maintained videos in some rooms where I had sex with other powerful people"; (5) Para 55-56: "federal prosecutors likely possess videotapes and photographic images of me as an underage girl having sex with Epstein and some of his powerful friends"; (6) Para 53: Explicitly states she did NOT have sex with Bill Clinton. Document also includes Sept 3, 2008 FBI victim notification letter signed by R. Alexander Acosta confirming her status as identified victim. Dershowitz served as Trump\\'s impeachment defense lawyer and remains a close ally. [v10.84]',date:'2015-01-01',type:'sworn-declaration'},
  {id:'sdny-mar-a-lago-subpoena-victim-employment-records',dataset:'DS9-Legal',pages:4,severity:10,keywords:['mar-a-lago','subpoena','sdny','trump organization','employment records','victim','maxwell trial','2021'],summary:'CRITICAL -- PRIMARY SOURCE: Email chain between SDNY prosecutors and Trump Organization compliance counsel Patricia Anne Pileggi (EFTA00078510, 4 pages, September-November 2021, during Maxwell trial preparation). SDNY served trial subpoena on Mar-a-Lago for employment records of an Epstein victim who worked there circa 2000. Key exchanges: (1) Pileggi: "I have been speaking with Compliance Counsel for the Trump Organization who informs me that Mar a Lago does not have in house counsel"; (2) "I have not been able to locate anyone who recalls working at Mar a Lago in 2000"; (3) "The Director of Human Resources prior to 2007 is no longer with Mar a Lago." This establishes: federal prosecutors investigating a direct Epstein victim-to-Mar-a-Lago employment nexus during the Maxwell trial. Trump Organization struggled or failed to produce responsive records. [v10.84]',date:'2021-11-17',type:'legal-evidence'},
  {id:'sdny-wexner-proffer-epstein-wealth-power-of-attorney',dataset:'DS9-Legal',pages:3,severity:10,keywords:['wexner','sdny','prosecution','power of attorney','several hundred million','wealth','mansion','71st street','victoria secret'],summary:'CRITICAL -- PRIMARY SOURCE: SDNY prosecution memo "Investigation into Potential Co-Conspirators of Jeffrey Epstein" addressed to U.S. Attorney Geoffrey Berman (EFTA02731082, Dec 19, 2019). Documents Wexner\\'s attorney proffer of July 25, 2019: (1) "Over his years handling Wexner\\'s finances, Epstein stole or otherwise misappropriated several hundred million dollars from Wexner"; (2) "That misconduct, together with fees that Epstein paid himself for his services to Wexner, appears to account for VIRTUALLY ALL OF EPSTEIN\\'S WEALTH"; (3) By 1991, Epstein had unrestricted power of attorney over Wexner; (4) In 1998, Epstein transferred himself Wexner\\'s NYC mansion (9 East 71st Street) at a discounted price of $20M (bought for $13M in 1989); (5) Epstein may have been "holding himself out as connected to Victoria\\'s Secret" to recruit; (6) In 2007, Epstein warned Wexner of "legal problems involving an overly aggressive police chief"; (7) Wexner\\'s wife discovered the misappropriation; Epstein returned $100M in Jan 2008. This document explains the ENTIRE financial foundation of Epstein\\'s operation. [v10.84]',date:'2019-12-19',type:'prosecution-memo'},
  {id:'gates-epstein-bgc3-nikolic-separation-agreement',dataset:'DS9-Email',pages:2,severity:9,keywords:['bill gates','boris nikolic','bgc3','epstein','separation agreement','larry cohen','employment','2013'],summary:'HIGH VALUE -- PRIMARY SOURCE: Email chain (EFTA02730265, 2 pages, August 24, 2013). Boris Nikolic (Bill Gates\\'s personal science advisor and right-hand man at bgC3/Gates Ventures) forwards to Jeffrey Epstein a DRAFT SEPARATION AGREEMENT from Bill Gates, prepared by Epstein\\'s lawyer Larry Cohen. The draft includes: "We won\\'t disparage each other privately or publically"; "You agree that you have no legal claims against me, my family or any of my related entities, such as the foundation and bgC3." Nikolic tells Epstein he needs changes re "helping me find a job." This reveals Epstein was DIRECTLY INVOLVED in drafting employment separation terms between Gates and his own advisor -- a level of involvement in Gates\\'s affairs far deeper than Gates has publicly acknowledged. Nikolic was later named in Epstein\\'s final will as a successor executor. [v10.84]',date:'2013-08-24',type:'email-evidence'},
  {id:'gates-epstein-post-conviction-meetings-2013-2014',dataset:'DS9-Email',pages:4,severity:9,keywords:['bill gates','epstein','appointment','dinner','boris nikolic','post-conviction','2013','2014','sex offender'],summary:'HIGH VALUE -- PRIMARY SOURCE: Multiple scheduling documents (EFTA00395096, EFTA00373880, EFTA00392464, EFTA00425730, 4 pages combined, 2011-2014). Pattern of post-conviction Gates-Epstein contact: (1) Oct 2011: Groff describes Boris Nikolic as "Bill Gates right hand man...very interesting and smart" when arranging Woody Allen dinner (EFTA00425730); (2) Feb 2013: "Reminder: Bill Gates in NY" and "2:00pm Appt w/Bill Gates" -- same day Lithuanian model arrives JFK (EFTA00395096); (3) Apr 2013: Epstein brings "Bill Gates assistant, Boris Nikolic" to lunch on Richard Branson\\'s island (EFTA00392464); (4) Mar 2014: "TBD Dinner w/Bill Gates" -- same calendar page notes "NYS Sex Off Reg. requests updated photo" for Epstein\\'s sex offender registration (EFTA00373880). All meetings occurred AFTER Epstein\\'s 2008 conviction and sex offender registration. [v10.84]',date:'2014-03-14',type:'email-evidence'},
  {id:'lutnick-epstein-2018-zoning-collaboration-will-do',dataset:'DS11-Email',pages:2,severity:8,keywords:['howard lutnick','epstein','2018','zoning','real estate','neighbors','frick','will do','may 2018'],summary:'NOTABLE -- PRIMARY SOURCE: Email chain (EFTA00474455, 2 pages, May 25-28, 2018). Howard Lutnick\\'s attorney Babak Yaghmaie (Cooley LLP) tries to reach Epstein about opposing a building development. Lutnick forwards and urges action: "I\\'m sending a lawyer. Don\\'t ignore this. They will build exactly across from you." An intermediary reports: "Jeffrey has responded: WILL DO!" This confirms Lutnick and Epstein were Upper East Side neighbors who actively collaborated as recently as May 2018 -- one year before Epstein\\'s arrest. Supplements Lutnick-Epstein relationship evidence from v10.83. [v10.84]',date:'2018-05-28',type:'email-evidence'},
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
count = content.count('v10.83')
print(f"Replacing {count} occurrences of 'v10.83' with 'v10.84'")
content = content.replace('v10.83', 'v10.84')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.84.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.83')
new_ver = verify.count('v10.84')
print(f"Remaining v10.83: {remaining}")
print(f"Total v10.84: {new_ver}")

for check_id in ['giuffre-sworn-declaration-dershowitz-6x-prince-andrew-3x',
                  'sdny-mar-a-lago-subpoena-victim-employment-records',
                  'sdny-wexner-proffer-epstein-wealth-power-of-attorney',
                  'gates-epstein-bgc3-nikolic-separation-agreement',
                  'gates-epstein-post-conviction-meetings-2013-2014',
                  'lutnick-epstein-2018-zoning-collaboration-will-do']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
