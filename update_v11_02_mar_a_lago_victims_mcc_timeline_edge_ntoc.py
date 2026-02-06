#!/usr/bin/env python3
"""Update dashboard with Mar-a-Lago victim recruitment, MCC death timeline, Edge Foundation, NTOC tips, Observer invite — v11.02"""
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

# Use simple search to find closing brackets
def find_close_simple(content, array_name):
    """Find the ]; that closes the array by searching for the pattern before the next const"""
    marker = f"const {array_name} = ["
    start = content.find(marker)
    if start == -1:
        return -1
    # Find the next 'const ' after this array starts
    next_const = content.find('\n    const ', start + len(marker))
    if next_const == -1:
        next_const = content.find('\n  const ', start + len(marker))
    if next_const == -1:
        next_const = len(content)
    # Search backwards from next_const for ];
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
timeline_entries = """  {date:'1998-06-01',event:'Jane Doe 102 civil complaint: "A vulnerable young girl, Plaintiff was working as a changing room assistant at The Mar-A-Lago Club in Palm Beach making approximately $9 an hour when she was first lured into Defendant\\'s sexually exploitative world. In or about the summer of 1998, when Plaintiff was merely fifteen years old while attending to her duties at Mar-A-Lago, Plaintiff was recruited by Ghislaine Maxwell."',source:'EFTA00210921'},
  {date:'2000-01-01',event:'FBI interview notes: Victim "knew that [REDACTED] had previously worked at Mar-A-Lago and thought she met MAXWELL there." Also: "[REDACTED] was approached by MAXWELL at Mar-A-Lago." Juan Alessi (Epstein employee) "confirms that Maxwell recruited [victim] from her job in Mar-a-Lago to massage Epstein." Maxwell trial 820 Series evidence: Mar-a-Lago Personnel Records (SEALED), HR Correspondence for Minor Victim-5, Mar-a-Lago Termination List.',source:'EFTA00097825'},
  {date:'2019-08-10',event:'MCC SUICIDE TIMELINE (minute-by-minute): Aug 9 8:00am: Cellmate Efrain Reyes departs for court, leaving Epstein ALONE in cell. 8:30am-6:45pm: Epstein in attorney conference. 7:00pm: "Epstein was in good spirits, nothing unusual." Aug 10 6:33am: Body alarm -- staff found Epstein unresponsive. CPR initiated. 6:45am: EMS arrives, no pulse found. 7:36am: Official time of death. 8:34am: FBI notified. 10:15pm: Computer Services Manager arrives to REMOVE HARD DRIVES from SHU, replaced with new ones.',source:'EFTA00138731'},
  {date:'2019-07-23',event:'MCC Psych Observation Log: "Inmate states this cellmate tried to kill him" at approximately 2:15am on July 23, 2019 (Epstein\\'s first incident). Placed on suicide watch. Regular 15-minute checks documented. Suicide watch logs: safety toothbrush, SW blanket and mattress, no regular linens. Epstein removed from suicide watch after only 6 days despite this claim.',source:'EFTA00138731'},
  {date:'2011-05-12',event:'John Brockman (Edge Foundation) emails "Edge Master Class" invitation at Spring Mountain Vineyard, Napa. CC list includes: Jeff Bezos, Sergey Brin, Bill Gates, Elon Musk, Larry Page, Mark Zuckerberg, Sean Parker, Paul Allen, Craig Venter, Daniel Kahneman, Pierre Omidyar, Evan Williams, Jimmy Wales, Dean Kamen, Ari Emanuel, Jean Pigozzi, Ricardo Salinas Pliego -- AND Jeffrey Epstein. Post-conviction Epstein on same distribution list as the world\\'s most powerful tech figures.',source:'EFTA00433872'},
  {date:'2013-03-14',event:'Jared Kushner\\'s New York Observer 25th Anniversary celebration at The Four Seasons. Invitation sent to "Mr. Jeffrey Epstein." Guest list includes: Donald Trump, Ivanka Trump, Mayor Bloomberg, Harvey Weinstein, Matt Lauer, Stephen Schwarzman, Woody Johnson (later Trump UK Ambassador), Ken Kurson (later Trump pardon), Cory Booker, Sean Parker, Katie Couric, Commissioner Ray Kelly, Ron Perelman, Katie Holmes, Blake Lively.',source:'EFTA00394771'},
  {date:'1992-11-01',event:'George Houraney confirms to NYT: Trump threw a party at Mar-a-Lago with "28 girls" -- NFL cheerleaders for a "calendar girl" competition. "He and Epstein were the only men there." NBC footage exists of Trump and Epstein speaking at this party. Trump later attributed his falling-out with Epstein (2004) to Epstein "stealing workers from Mar-a-Lago" -- including a victim who was later abused.',source:'EFTA00042963'},
  {date:'2025-08-06',event:'FBI Child Exploitation and Human Trafficking Task Force internal email compiling 15-20 NTOC (National Threat Operations Center) tips related to Trump and Epstein. Tips include: personal assistant to Epstein (1986-1992) naming Trump as guest; victim recruited at age 13-14 in NJ; orgy parties at Epstein\\'s NY residence naming Clinton and Trump. FBI disposition notes show many tips had "no contact information provided," "deemed not credible," or "no probative information." FBI agents described the most explosive tip as "the salacious piece."',source:'EFTA01660679'},
"""

# New FINDINGS entries
findings_entries = """  {id:'mar-a-lago-victim-recruitment-maxwell-820-series-trial-evidence',dataset:'DS10-Official',pages:92,severity:10,keywords:['mar-a-lago','ghislaine maxwell','recruited','victim','changing room assistant','$9 an hour','fifteen years old','juan alessi','palm beach','spa','masseuse','820 series','trial evidence','sealed','personnel records','hr correspondence','minor victim-5','termination list','jane doe 102','civil complaint','fbi interview','prosecution memo','1998','2000'],summary:'CRITICAL -- PRIMARY SOURCES: Multiple independent corroborating documents (EFTA00210921, EFTA00097825, EFTA00173816, EFTA02731226, EFTA02731082, EFTA00022133, combined 92+ pages). MAR-A-LAGO AS EPSTEIN VICTIM RECRUITMENT SITE: (1) JANE DOE 102 CIVIL COMPLAINT (EFTA00210921): \\\"A vulnerable young girl, Plaintiff was working as a changing room assistant at The Mar-A-Lago Club in Palm Beach making approximately $9 an hour when she was first lured into Defendant\\\\'s sexually exploitative world. In or about the summer of 1998, when Plaintiff was merely fifteen years old while attending to her duties at Mar-A-Lago, Plaintiff was recruited by Ghislaine Maxwell\\\"; (2) FBI INTERVIEW NOTES (EFTA00097825): Victim \\\"knew that [REDACTED] had previously worked at Mar-A-Lago and thought she met MAXWELL there.\\\" \\\"[REDACTED] was approached by MAXWELL at Mar-A-Lago\\\"; (3) PROSECUTION MEMO (EFTA02731226): \\\"Juan Alessi, who worked for Epstein...confirms that Maxwell recruited [victim] from her job in Mar-a-Lago to massage Epstein\\\"; (4) VICTIM IMPACT STATEMENT (EFTA00019994): \\\"When I was recruited by Ghislaine Maxwell at Mar-a-Lago, just before I was 17, I thought I was given a big break\\\"; (5) MAXWELL TRIAL 820 SERIES EVIDENCE: Entire evidence category dedicated to Mar-a-Lago records including GX-821 (HR Correspondence Regarding Minor Victim-5\\\\'s Records), GX-822 (Mar-A-Lago Termination List), GX-823 (Mar-A-Lago Personnel Records -- SEALED). This is documented across civil complaints, FBI interviews, prosecution memos, victim statements, and trial evidence -- the most extensively corroborated aspect of the entire Epstein case. [v11.02]',date:'1998-06-01',type:'multi-source-evidence'},
  {id:'mcc-death-timeline-hard-drives-removed-cellmate-claim-aug2019',dataset:'DS10-Official',pages:58,severity:10,keywords:['mcc','metropolitan correctional center','suicide','death','timeline','minute by minute','body alarm','cpr','epinephrine','no pulse','hard drives','removed','computer services','shu','efrain reyes','cellmate','alone','good spirits','suicide watch','tried to kill him','psych observation','safety toothbrush','judge berman','fbi','mark epstein','warden ndiaye','august 2019'],summary:'CRITICAL -- PRIMARY SOURCE: Official MCC New York medical, psychological, and operational records (EFTA00138731, 58+ pages, July-August 2019). MINUTE-BY-MINUTE DEATH TIMELINE: Aug 9: 8:00am -- Cellmate Efrain Reyes (85993-054) departs for court, leaving Epstein ALONE; 8:30am-6:45pm -- Epstein in attorney conference all day; 7:00pm -- \\\"Epstein was in good spirits, nothing unusual\\\"; Aug 10: 6:33am -- Body alarm activated, staff found Epstein unresponsive, CPR initiated; 6:35am -- Medical staff, AED applied; 6:45am -- EMS arrives, intubated, three rounds Epinephrine, NO PULSE FOUND; 7:36am -- OFFICIAL TIME OF DEATH; 8:34am -- FBI notified; 10:00am -- Fingerprints and photographs at hospital; 10:15pm -- HARD DRIVES REMOVED: \\\"Computer Services Manager arrives at institution to remove hard drives (Computers) from SHU. And replaced with new ones\\\" -- hard drives removed 15 HOURS after death; 11:15am next day -- OIG departs with two computers. PRIOR INCIDENT (July 23): Psych observation log: \\\"Inmate states this cellmate tried to kill him\\\" at ~2:15am. Placed on suicide watch but REMOVED after only 6 days. Excess linens allowed to accumulate. No cell search of Epstein\\\\'s cell documented on Aug 9. [v11.02]',date:'2019-08-10',type:'official-records'},
  {id:'edge-foundation-tech-billionaire-list-observer-invite-2011-2013',dataset:'DS9-Email',pages:8,severity:9,keywords:['john brockman','edge foundation','edge master class','jeff bezos','sergey brin','bill gates','elon musk','larry page','mark zuckerberg','sean parker','paul allen','craig venter','daniel kahneman','pierre omidyar','evan williams','jimmy wales','dean kamen','ari emanuel','jared kushner','new york observer','25th anniversary','four seasons','donald trump','ivanka trump','harvey weinstein','matt lauer','woody johnson','ken kurson','stephen schwarzman','cory booker','commissioner ray kelly','ron perelman','2011','2013','post-conviction'],summary:'HIGH VALUE -- PRIMARY SOURCES: Edge Foundation email (EFTA00433872, May 2011) and NY Observer invitation (EFTA00394771, March 2013). POST-CONVICTION ELITE ACCESS: (1) EDGE MASTER CLASS CC LIST (2011): John Brockman emails invitation with CC list including Jeff Bezos, Sergey Brin, Bill Gates, Elon Musk, Larry Page, Mark Zuckerberg, Sean Parker, Paul Allen, Craig Venter, Daniel Kahneman, Pierre Omidyar, Evan Williams, Jimmy Wales, Dean Kamen, Ari Emanuel, Jean Pigozzi, Ricardo Salinas Pliego -- AND Jeffrey Epstein. Three years after his conviction, Epstein remained on the same distribution list as the world\\\\'s most powerful tech figures; (2) KUSHNER NY OBSERVER 25TH ANNIVERSARY (March 14, 2013 -- EFTA00394771): Invitation to \\\"Mr. Jeffrey Epstein\\\" for Jared Kushner\\\\'s celebration at The Four Seasons. Guest list: Donald Trump, Ivanka Trump, Mayor Bloomberg, Harvey Weinstein, Matt Lauer, Stephen Schwarzman (Blackstone CEO), Woody Johnson (later Trump UK Ambassador), Ken Kurson (later pardoned by Trump), Cory Booker, Commissioner Ray Kelly, Ron Perelman, Katie Couric, Sean Parker, Katie Holmes, Blake Lively. Multiple future Trump administration figures on same guest list as convicted sex offender. [v11.02]',date:'2013-03-14',type:'email-evidence'},
  {id:'fbi-ntoc-tip-compilation-trump-epstein-aug2025',dataset:'DS10-Official',pages:35,severity:8,keywords:['fbi','ntoc','national threat operations center','child exploitation','human trafficking','task force','tips','complaints','calendar girls','28 girls','nfl cheerleaders','george houraney','1992','personal assistant','1986','orgy parties','salacious','not credible','no contact information','mar-a-lago','trump','clinton','dershowitz','august 2025'],summary:'NOTABLE -- PRIMARY SOURCE: FBI Child Exploitation and Human Trafficking Task Force internal email chain (EFTA01660679, ~35 pages, August 6-7, 2025). FBI NTOC TIP COMPILATION: Internal FBI compilation of 15-20 NTOC tips related to Trump and Epstein. Tips include: (1) Former Epstein personal assistant (1986-1992) naming Trump as guest; (2) Victim recruited age 13-14 in NJ; (3) \\\"Big orgy parties\\\" at Epstein\\\\'s NY residence naming Clinton and Trump (age 16 complainant attended 8 parties); (4) \\\"Calendar girls\\\" party at Mar-a-Lago (naming Trump family, Musk, Dershowitz -- NO contact information provided); (5) Films of prominent men including Epstein, Clinton, Trump; (6) George Houraney\\\\'s CONFIRMED account of 1992 party with \\\"28 girls\\\" -- Trump and Epstein the only men, NFL cheerleaders for calendar girl competition. FBI DISPOSITION: Many tips resulted in \\\"no contact made,\\\" \\\"deemed not credible,\\\" \\\"no probative information.\\\" FBI agents described the most explosive tip as \\\"the salacious piece.\\\" The compilation itself is significant as an institutional record, but most individual tips lack corroboration. The Houraney account is independently confirmed by NBC footage. SEVERITY REDUCED because most tips are unverified. [v11.02]',date:'2025-08-06',type:'law-enforcement-compilation'},
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
count = content.count('v11.01')
print(f"Replacing {count} occurrences of 'v11.01' with 'v11.02'")
content = content.replace('v11.01', 'v11.02')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v11.02.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v11.01')
new_ver = verify.count('v11.02')
print(f"Remaining v11.01: {remaining}")
print(f"Total v11.02: {new_ver}")

for check_id in ['mar-a-lago-victim-recruitment-maxwell-820-series-trial-evidence',
                  'mcc-death-timeline-hard-drives-removed-cellmate-claim-aug2019',
                  'edge-foundation-tech-billionaire-list-observer-invite-2011-2013',
                  'fbi-ntoc-tip-compilation-trump-epstein-aug2025']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

# Verify structure
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
