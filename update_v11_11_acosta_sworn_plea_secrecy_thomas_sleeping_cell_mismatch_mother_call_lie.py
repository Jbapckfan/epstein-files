#!/usr/bin/env python3
"""Update dashboard with Acosta sworn OPR interview, plea negotiation secrecy emails, Thomas sleeping admission, Noel cell mismatch (220 vs 206), mother call lie, grand jury Mar-a-Lago, warden camera admission — v11.11"""
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
timeline_entries = """  {date:'2019-10-18',event:'ACOSTA\\'S OWN SWORN OPR INTERVIEW (100 pages): Trump\\'s future Labor Secretary testifies under oath about the Epstein NPA. Admits he had "ultimate authority over the Epstein" case. On why he refused to share information with state prosecutors: "said no for fear it\\'ll be leaked straight to Epstein." Recused from case December 2008. The OPR found that while the NPA "constitutes poor judgment," they could not prove political motivation.',source:'EFTA00009229'},
  {date:'2007-09-01',event:'PLEA NEGOTIATION EMAILS -- NPA DESIGNED SECRET (289 pages): Internal emails between AUSA Villafaña and Epstein attorney Jay Lefkowitz (Kirkland & Ellis) reveal the mechanics of the deal. Defense explicitly BLOCKED victim notification: "object to your sending any letter whatsoever to the alleged victims in this matter." NPA secrecy by design: "A non-prosecution agreement would not be made public or filed with the Court." After plea: "the FBI and the U.S. Attorney\\'s Office will close their investigations." Defense fixated on "victim\\'s fund" as compensation workaround. Kenneth Starr also on defense team.',source:'EFTA00226107'},
  {date:'2007-02-06',event:'GRAND JURY TESTIMONY -- OPERATION LEAP YEAR (390 pages): Sworn testimony before federal grand jury. FBI agent: "2005 initiated an investigation on Mr. Epstein involving multiple underage females." Payment structure: "Mr. Epstein paid the underage females anywhere from 200 to $400." MAR-A-LAGO IN GRAND JURY RECORD: "Ghislaine Maxwell... Jane Doe Number One at Mar-a-Lago." Grand jury subpoenas issued to Epstein-linked aviation entities "Hyperion Air, Inc. and JEGE, Inc."',source:'EFTA00085291'},
  {date:'2021-06-17',event:'SWORN STATEMENT -- CO MICHAEL THOMAS (344 pages): The OTHER guard on duty Aug 9-10 testifies. ADMITS SLEEPING ON DUTY: "I recall dozing off from here." Cannot confirm rounds: "No, I can\\'t say that I did rounds every 30 minutes." Was on SHU shift "from 12:00 a.m. to 8:00 a.m." Does not recall being told about cellmate requirement: "No. I don\\'t recall anybody specifically talking about he needs a cellmate."',source:'EFTA00063613'},
  {date:'2021-06-22',event:'TOVA NOEL ADDITIONAL SWORN DETAILS (464 pages): CELL MISMATCH DISCOVERED: "So he was in cell 220. He was assigned to cell 206." Epstein was found dead in a DIFFERENT CELL than his official assignment. Phone call made from SHU shower area: "the shower to use the phone. And he called and told me to take the phone from him." Did not know cellmate removed: "He had a cellmate. I didn\\'t know that the cellmate was removed." Direct admission: "We didn\\'t do the rounds."',source:'EFTA00117759'},
  {date:'2021-10-27',event:'SWORN STATEMENT -- LAMINE N\\'DIAYE, MCC SUPERVISOR (114 pages): Quantifies camera outage: "two weeks of no cameras, and in the SHU, no cameras." July 23 incident detail: "1:27 a.m., Epstein found in fetal position in cell, breathing, but would not acknowledge." Confirms "mother" pretext for unmonitored call: "call, so that he - Epstein - could call his mother." Cellmate failure: "Inmate Epstein was not placed with a cellmate."',source:'EFTA00064311'},
  {date:'2023-06-22',event:'FULL OIG REPORT 23-085 -- NEW DETAIL: THE MOTHER CALL WAS A LIE (128 pages): Beyond the memorandum summary, the full report reveals: "purportedly to speak with his mother. In actuality, Epstein speaks with someone with" — the call was NOT to his mother. "Epstein\\'s mother was deceased at the time he asked to telephone her." Guards "created, certified, and submitted false documentation indicating that the counts and rounds had been done." "6:30 a.m. on August 10, no one was seen entering" Epstein\\'s tier.',source:'EFTA00039025'},
  {date:'2008-01-01',event:'JOINT STATEMENT OF UNDISPUTED FACTS -- 40+ VICTIMS (132 pages): Stipulated facts in CVRA litigation: Epstein "sexually-abused more-than-40 minor girls." NPA required DOJ to "not notify any of the victims of the existence of the non prosecution agreement." DOJ sent "misleading letter stating that the case was currently under investigation." FBI hand-delivered victim notification to Jane Doe #1 on June 7, 2007 — but concealed the NPA.',source:'EFTA00191264'},
  {date:'2019-08-12',event:'MCC WARDEN SWORN STATEMENT (144 pages): Warden confirms camera system unreliable: "They\\'re not good. We were just funded to get new cameras installed." On DVR equipment: "The ones that hold the recordings, they\\'re breaking down." Was told directly: "the cameras aren\\'t working." Confirmed psychology required cellmate: "required, he needs to have a cellmate at all times." Began tenure "May of 2018."',source:'EFTA00135369'},
  {date:'2009-08-07',event:'RODRIGUEZ AND ALESSI DEPOSITIONS -- MAXWELL\\'S OPERATIONAL ROLE: Alfredo Rodriguez (house manager) testifies Maxwell maintained "lists of names of girls to come and give massages" and kept "pictures of the young women on her laptop." References a "black book with all the names." Separately, Juan Alessi testifies Maxwell rejected an older woman: "Maxwell says to me, you have to find an excuse. We don\\'t want her." Age estimates for masseuses: "have been 16 or 20." Standard rate: "$100 an hour... for everybody."',source:'EFTA00310278'},
"""

# New FINDINGS entries
findings_entries = """  {id:'acosta-sworn-opr-interview-plea-secrecy-emails-grand-jury-mar-a-lago-victim-deception',dataset:'DS10-Official',pages:1200,severity:10,keywords:['acosta','sworn','opr','interview','ultimate authority','leaked','straight to epstein','recused','plea negotiation','villafana','lefkowitz','kirkland ellis','object','victim notification','non-prosecution agreement','not made public','close their investigations','victims fund','kenneth starr','grand jury','operation leap year','2005','underage females','200 to 400','mar-a-lago','jane doe number one','hyperion air','jege','joint statement','40 minor girls','misleading letter','currently under investigation','rodriguez','alessi','maxwell','lists','laptop','black book','we dont want her','16 or 20'],summary:'CRITICAL -- PRIMARY SOURCES: Acosta OPR sworn interview (EFTA00009229, 100 pages), plea negotiation emails (EFTA00226107, 289 pages), grand jury transcript (EFTA00085291, 390 pages), Joint Statement of Undisputed Facts (EFTA00191264, 132 pages), Rodriguez/Alessi depositions (EFTA00310278/EFTA00101322). THE NPA MACHINERY EXPOSED: (1) ACOSTA UNDER OATH: Had \\\\\\\\\\\\\\\"ultimate authority over the Epstein\\\\\\\\\\\\\\\" case. Refused to share info with state: \\\\\\\\\\\\\\\"said no for fear it\\\\\\\\\\\\\\\\'ll be leaked straight to Epstein\\\\\\\\\\\\\\\"; (2) PLEA EMAILS: Defense blocked victims: \\\\\\\\\\\\\\\"object to your sending any letter whatsoever to the alleged victims.\\\\\\\\\\\\\\\" NPA secrecy by design: \\\\\\\\\\\\\\\"would not be made public or filed with the Court.\\\\\\\\\\\\\\\" After plea: \\\\\\\\\\\\\\\"FBI and U.S. Attorney\\\\\\\\\\\\\\\\'s Office will close their investigations\\\\\\\\\\\\\\\"; (3) GRAND JURY: \\\\\\\\\\\\\\\"Jane Doe Number One at Mar-a-Lago\\\\\\\\\\\\\\\" — victim recruitment at Trump\\\\\\\\\\\\\\\\'s club in sworn grand jury testimony; (4) STIPULATED FACTS: \\\\\\\\\\\\\\\"sexually-abused more-than-40 minor girls.\\\\\\\\\\\\\\\" Victims not notified; DOJ sent misleading letters; (5) MAXWELL OPERATIONS: Rodriguez confirms lists, photos on laptop, black book. Alessi: Maxwell rejected older women, \\\\\\\\\\\\\\\"We don\\\\\\\\\\\\\\\\'t want her.\\\\\\\\\\\\\\\" [v11.11]',date:'2007-09-01',type:'plea-negotiation'},
  {id:'thomas-sleeping-noel-cell-mismatch-220-vs-206-ndiaye-two-weeks-no-cameras-mother-call-lie-warden-cameras-breaking',dataset:'DS10-Official',pages:1300,severity:10,keywords:['michael thomas','sleeping','dozing off','rounds','every 30 minutes','tova noel','cell mismatch','cell 220','cell 206','assigned','different cell','shower','phone','didnt do the rounds','lamine ndiaye','two weeks','no cameras','fetal position','1:27 am','call his mother','mother','deceased','purportedly','in actuality','speaks with someone','false documentation','no one seen entering','warden','not good','new cameras','breaking down','cameras arent working','cellmate at all times'],summary:'CRITICAL -- PRIMARY SOURCES: Michael Thomas sworn statement (EFTA00063613, 344 pages), Tova Noel additional statement (EFTA00117759, 464 pages), Lamine N\\\\\\\\\\\\\\\\'Diaye sworn statement (EFTA00064311, 114 pages), Full OIG Report 23-085 (EFTA00039025, 128 pages), MCC Warden statement (EFTA00135369, 144 pages). EXPANDED GUARD FAILURES AND THE MOTHER CALL LIE: (1) THOMAS SLEEPING: \\\\\\\\\\\\\\\"I recall dozing off from here.\\\\\\\\\\\\\\\" \\\\\\\\\\\\\\\"No, I can\\\\\\\\\\\\\\\\'t say that I did rounds every 30 minutes\\\\\\\\\\\\\\\"; (2) NOEL CELL MISMATCH: \\\\\\\\\\\\\\\"So he was in cell 220. He was assigned to cell 206\\\\\\\\\\\\\\\" — Epstein found dead in a DIFFERENT CELL than his official assignment; (3) N\\\\\\\\\\\\\\\\'DIAYE: \\\\\\\\\\\\\\\"two weeks of no cameras, and in the SHU, no cameras.\\\\\\\\\\\\\\\" July 23: \\\\\\\\\\\\\\\"1:27 a.m., Epstein found in fetal position\\\\\\\\\\\\\\\"; (4) THE MOTHER CALL WAS A LIE: Full OIG reveals \\\\\\\\\\\\\\\"purportedly to speak with his mother. In actuality, Epstein speaks with someone with\\\\\\\\\\\\\\\" — call was NOT to his deceased mother. \\\\\\\\\\\\\\\"Epstein\\\\\\\\\\\\\\\\'s mother was deceased at the time\\\\\\\\\\\\\\\"; (5) WARDEN: \\\\\\\\\\\\\\\"They\\\\\\\\\\\\\\\\'re not good. We were just funded to get new cameras installed.\\\\\\\\\\\\\\\" \\\\\\\\\\\\\\\"The ones that hold the recordings, they\\\\\\\\\\\\\\\\'re breaking down.\\\\\\\\\\\\\\\" [v11.11]',date:'2021-06-17',type:'sworn-testimony'},
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
count = content.count('v11.10')
print(f"Replacing {count} occurrences of 'v11.10' with 'v11.11'")
content = content.replace('v11.10', 'v11.11')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v11.11.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v11.10')
new_ver = verify.count('v11.11')
print(f"Remaining v11.10: {remaining}")
print(f"Total v11.11: {new_ver}")

for check_id in ['acosta-sworn-opr-interview-plea-secrecy-emails-grand-jury-mar-a-lago-victim-deception',
                  'thomas-sleeping-noel-cell-mismatch-220-vs-206-ndiaye-two-weeks-no-cameras-mother-call-lie-warden-cameras-breaking']:
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
