#!/usr/bin/env python3
"""Update dashboard with victim naming names, Wexner mansion $20M, NPA defense/Ken Starr, Deutsche Bank/JPMorgan — v11.03"""
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
timeline_entries = """  {date:'2015-01-01',event:'VICTIM ACCUSATIONS COMPILATION: Victim alleges Epstein directed her to have sex with Bill Richardson (NM Governor), George Mitchell (Senate Majority Leader), Marvin Minsky (MIT scientist), Jean-Luc Brunel (modeling agent), an unnamed "prince," a "foreign president," and owner of "a French hotel chain." Another victim told she could become "a Victoria\\'s Secret model" as recruitment lure (age 16). Dershowitz specifically named -- victim alleges "sex with Dershowitz at least 6 times, aged 16-19."',source:'EFTA00022133'},
  {date:'2015-01-02',event:'VICTIM DIARY (CONFIDENTIAL FOR ATTORNEY\\'S EYES ONLY): First-person account states: "even old senators like George Mitchell who you think would be good like a grandpa are bad." Also names "Mr. Leonsis, Mr. Case, Mr. Snyder, the Gregorys, Mr. Colgan" and describes "flights of horror." This is a handwritten victim journal/scrapbook with personal reflections corroborating the accusations compilation.',source:'EFTA02731420'},
  {date:'1998-11-01',event:'WEXNER MANSION SALE: Purchase and Sale Agreement for 9 East 71st Street. Total price: $20,000,000 ($19.3M for shares/interest + $667,500 personal property including a $600,000 Louis XIV desk). Wexner FINANCED HALF via $10 million promissory note to NES, LLC at 4.5% interest. Epstein was SOLE MEMBER of NES, LLC and personally guaranteed the note. Property later valued at $77 million. Whether the note was ever repaid is unknown.',source:'EFTA00312957'},
  {date:'2005-01-01',event:'NPA DEFENSE SUMMARY: Epstein\\'s defense team narrative names FULL legal roster: Roy Black, Gerald Lefcourt, Alan Dershowitz, Nat Dershowitz, KEN STARR (Clinton impeachment prosecutor), Jay Lefkowitz, Jack Goldberger, Martin Weinberg, and 6 others. State sex crimes prosecutor (13 years experience) stated "there were no real victims in this case" and women were "causing trouble in hopes of getting money." Grand jury returned only single count of solicitation.',source:'EFTA00314859'},
  {date:'2007-12-04',event:'NPA DEFENSE SUMMARY: US Attorney Alex Acosta "expressly represented to Ken Starr" the NPA\\'s civil remedy provisions. Criminal Division Chief Matthew Menchel characterized AUSA Villafana as "unsupervisable." Defense memo contains Darren Indyke\\'s editing notes dated Oct 6, 2011 consulting "JEE" (Jeffrey E. Epstein himself) on narrative details: "DIDN\\'T JE LEARN THAT BRAD WAS NOT THE INFORMANT? IF SO, WHO IS THE INFORMANT?"',source:'EFTA00314859'},
  {date:'2016-05-25',event:'SECOND PASSPORT: Darren Indyke requests second valid US passport for Epstein via G3 Global Services on "Mission Critical" basis ($702.20 total). Epstein lists occupation as "BANKER" at "SOUTHERN TRUST COMPANY." Justification: planned travel to France June 13 and BELARUS June 20 for "business matters." Courier service form branded "GO TO RUSSIA." Epstein already had passport expiring June 2016; second passport maintained continuously since 2014.',source:'EFTA00316230'},
  {date:'2013-10-08',event:'Deutsche Bank Private Bank: Email from Paul Morris (Managing Director) and Amanda Kirby (Associate) coordinating meeting between "Jeffrey" and "Paul and the DB team who will be managing his accounts." Deutsche Bank actively managing Epstein\\'s accounts in October 2013 -- five years after his sex offense conviction.',source:'EFTA00382930'},
  {date:'2017-02-01',event:'JPMorgan Private Bank: Email from Justin Nelson (Managing Director, J.P. Morgan Private Bank, Greenwich CT) scheduling meeting with "Jeffrey" in NYC. JPMorgan maintained private banking relationship with Epstein through at least early 2017 -- nearly a DECADE after his conviction and sex offender registration.',source:'EFTA00444494'},
  {date:'2013-09-01',event:'Epstein schedule: "3:00pm Appt w/Governor Bill Richardson" alongside "6:30am Breakfast w/Josh Ramo and Ehud Barak." Multiple emails show Richardson\\'s office coordinating meetings with Epstein through 2016-2017. Senator George Mitchell: "10:30am Appt w/Senator George Mitchell." Both the Governor and the Senator named by victims continued meeting with Epstein years after his conviction.',source:'EFTA00382924'},
  {date:'2008-01-01',event:'CVRA MOTION (42 pages): Crime Victims\\' Rights Act filing documents how the US Attorney\\'s Office signed the NPA then agreed to a CONFIDENTIALITY PROVISION barring disclosure to victims. For 9 months, prosecutors "assiduously concealed" the NPA. Victims were sent FALSE notification letters stating "the case is currently under investigation" MONTHS AFTER the NPA was already signed. Filing calls it concealment of a "sweetheart plea deal with a politically-connected billionaire."',source:'EFTA00078993'},
"""

# New FINDINGS entries
findings_entries = """  {id:'victims-name-richardson-mitchell-dershowitz-brunel-prince',dataset:'DS10-Official',pages:42,severity:10,keywords:['bill richardson','george mitchell','marvin minsky','jean-luc brunel','alan dershowitz','prince','foreign president','french hotel chain','victoria secret','model','recruitment','sex trafficking','aged 16','aged 16-19','six times','diary','journal','confidential','attorney eyes only','flights of horror','mr leonsis','mr case','mr snyder','like a grandpa are bad'],summary:'CRITICAL -- PRIMARY SOURCES: Victim accusations compilation (EFTA00022133) and victim diary (EFTA02731420, CONFIDENTIAL FOR ATTORNEY\\\\'S EYES ONLY, combined 42 pages). VICTIMS NAME POWERFUL FIGURES: (1) Victim alleges Epstein DIRECTED HER TO HAVE SEX WITH: Bill Richardson (NM Governor), George Mitchell (Senate Majority Leader), Marvin Minsky (MIT scientist), Jean-Luc Brunel (modeling agent), an unnamed \\\"prince,\\\" a \\\"foreign president,\\\" and owner of \\\"a French hotel chain\\\"; (2) DERSHOWITZ specifically named: victim alleges \\\"sex with Dershowitz at least 6 times, aged 16-19\\\"; (3) Another victim told she could become \\\"a Victoria\\\\'s Secret model\\\" as recruitment lure (age 16 in 2000) -- connecting to Les Wexner\\\\'s Victoria\\\\'s Secret brand; (4) VICTIM DIARY (EFTA02731420): First-person handwritten journal states: \\\"even old senators like George Mitchell who you think would be good like a grandpa are bad.\\\" Also names \\\"Mr. Leonsis, Mr. Case, Mr. Snyder, the Gregorys, Mr. Colgan\\\" and describes \\\"flights of horror\\\"; (5) Both Richardson and Mitchell documented maintaining meetings with Epstein through 2013-2017 despite being named by victims. Richardson and Mitchell have denied the allegations. [v11.03]',date:'2015-01-01',type:'victim-testimony'},
  {id:'wexner-mansion-20m-10m-note-npa-defense-starr-acosta',dataset:'DS11-Financial',pages:46,severity:10,keywords:['les wexner','9 east 71st street','$20 million','$10 million','promissory note','4.5 percent','nes llc','sole member','personal guaranty','birch wathen school','$77 million','louis xiv desk','$600000','ken starr','alexander acosta','alan dershowitz','roy black','jay lefkowitz','gerald lefcourt','jack goldberger','no real victims','unsupervisable','villafana','menchel','darren indyke','dki','jee','october 2011','non-prosecution agreement','npa','november 1998'],summary:'CRITICAL -- PRIMARY SOURCES: Purchase and Sale Agreement (EFTA00312957, 33 pages, November 1998) and NPA Defense Summary (EFTA00314859, 13 pages, October 2011). TWO FOUNDATIONAL DOCUMENTS: (1) WEXNER MANSION SALE: 9 East 71st Street purchased for $20 million total. WEXNER FINANCED HALF via $10 million promissory note to NES, LLC at 4.5% interest. Jeffrey Epstein was SOLE MEMBER of NES, LLC and personally guaranteed the note. Property included $600,000 Louis XIV desk. Property later valued at $77 MILLION. Whether the $10M note was ever repaid is unknown -- if forgiven, it would represent an extraordinary wealth transfer; (2) NPA DEFENSE SUMMARY: Full defense roster includes KEN STARR (Clinton impeachment prosecutor), Roy Black, Alan Dershowitz, Jay Lefkowitz, Gerald Lefcourt, Jack Goldberger, and 8 others. State sex crimes prosecutor stated \\\"no real victims\\\" and women were \\\"causing trouble in hopes of getting money.\\\" Grand jury returned only single count. US Attorney Acosta \\\"expressly represented to Ken Starr\\\" NPA terms. Criminal Division Chief characterized AUSA Villafana as \\\"unsupervisable.\\\" INTERNAL EDITING: Darren Indyke\\\\'s notes (Oct 6, 2011) consult \\\"JEE\\\" (Epstein himself) on narrative construction: \\\"DIDN\\\\'T JE LEARN THAT BRAD WAS NOT THE INFORMANT?\\\" [v11.03]',date:'1998-11-01',type:'financial-legal-evidence'},
  {id:'second-passport-belarus-deutsche-bank-jpmorgan-post-conviction',dataset:'DS9-Email',pages:28,severity:9,keywords:['second passport','mission critical','g3 global services','banker','southern trust company','usvi','belarus','france','darren indyke','go to russia','ds-82','deutsche bank','paul morris','managing director','private bank','jpmorgan','jp morgan','justin nelson','greenwich','private banking','post-conviction','sex offender','2013','2016','2017'],summary:'HIGH VALUE -- PRIMARY SOURCES: Passport application packet (EFTA00316230, 16 pages, May 2016), Deutsche Bank email (EFTA00382930, Oct 2013), JPMorgan email (EFTA00444494, Feb 2017). POST-CONVICTION INSTITUTIONAL ACCESS: (1) SECOND PASSPORT: Darren Indyke requests second valid US passport on \\\"Mission Critical\\\" basis ($702.20). Epstein lists occupation as \\\"BANKER\\\" at \\\"SOUTHERN TRUST COMPANY.\\\" Claims travel to France June 13 and BELARUS June 20 for \\\"business matters.\\\" Courier form branded \\\"GO TO RUSSIA.\\\" Epstein maintained two valid passports continuously since 2014; (2) DEUTSCHE BANK (Oct 2013): Paul Morris, Managing Director of Deutsche Bank Private Bank, coordinating \\\"the DB team who will be managing his accounts\\\" -- 5 years post-conviction; (3) JPMORGAN (Feb 2017): Justin Nelson, Managing Director of J.P. Morgan Private Bank (Greenwich CT), scheduling meeting with \\\"Jeffrey\\\" in NYC -- nearly a DECADE post-conviction. Both major banks actively managing a convicted sex offender\\\\'s private banking accounts years after registration. [v11.03]',date:'2016-05-25',type:'financial-institutional-evidence'},
  {id:'cvra-victims-rights-false-notification-sweetheart-deal',dataset:'DS10-Official',pages:42,severity:9,keywords:['cvra','crime victims rights act','jane doe','false notification','currently under investigation','assiduously concealed','confidentiality provision','sweetheart plea deal','politically-connected billionaire','9 months','barred disclosure','victims rights','non-prosecution agreement','npa','epstein','2008'],summary:'HIGH VALUE -- PRIMARY SOURCE: Crime Victims\\' Rights Act motion (EFTA00078993, 42 pages, ~2008). SYSTEMATIC CONCEALMENT FROM VICTIMS: (1) US Attorney\\\\'s Office signed the NPA then agreed to CONFIDENTIALITY PROVISION barring disclosure to anyone including victims; (2) For 9 MONTHS prosecutors \\\"assiduously concealed\\\" the NPA from victims; (3) Victims sent FALSE notification letters stating \\\"the case is currently under investigation\\\" MONTHS after NPA was already signed; (4) Filing characterizes this as concealment of a \\\"sweetheart plea deal with a politically-connected billionaire\\\"; (5) Victims were denied their statutory right to confer with prosecutors and be treated with fairness under the CVRA; (6) This concealment was later cited by Judge Marra as a violation of the Crime Victims\\' Rights Act. [v11.03]',date:'2008-01-01',type:'court-filing'},
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
count = content.count('v11.02')
print(f"Replacing {count} occurrences of 'v11.02' with 'v11.03'")
content = content.replace('v11.02', 'v11.03')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v11.03.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v11.02')
new_ver = verify.count('v11.03')
print(f"Remaining v11.02: {remaining}")
print(f"Total v11.03: {new_ver}")

for check_id in ['victims-name-richardson-mitchell-dershowitz-brunel-prince',
                  'wexner-mansion-20m-10m-note-npa-defense-starr-acosta',
                  'second-passport-belarus-deutsche-bank-jpmorgan-post-conviction',
                  'cvra-victims-rights-false-notification-sweetheart-deal']:
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
