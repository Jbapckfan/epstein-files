#!/usr/bin/env python3
"""Update dashboard with Wyden Senate letter, Acosta/Dershowitz prosecution sabotage, Grand Jury testimony, OIG draft report — v11.00"""
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
timeline_entries = """  {date:'2023-07-24',event:'Senate Finance Committee Chairman Ron Wyden writes 16-page letter to Leon Black demanding answers about $158M payments to Epstein. Committee investigating whether Epstein\\'s tax advice constituted illegal tax evasion. Key: Epstein devised a scheme transferring ~$2 billion to Black\\'s children via 2006 GRATs while avoiding gift/estate taxes -- estimated $1 billion+ in tax savings. Black refused to answer key Committee questions. IRS has NEVER audited these transactions.',source:'EFTA02731023'},
  {date:'2012-12-20',event:'Email chain documenting Leon Black\\'s private jet (tail 6241) flying from Teterboro to St. Thomas carrying: Black, his wife and kids, Leon Botstein (Bard College president, described as "friend of Jeffrey\\'s"), and another unnamed "friend of Jeffrey\\'s." Destination: "Jeffrey\\'s island." Epstein\\'s staff coordinates pickup: "We will have Leon picked up and taken to Jeffrey\\'s island...all will be taken care of!" Leon Black\\'s plane ferrying Epstein\\'s friends to Little St. James.',source:'EFTA00399109'},
  {date:'2012-01-01',event:'Black-Epstein Indemnification Agreement signed (template dated "201_"). Southern Trust Company Inc. (St. Thomas, USVI) and Jeffrey Epstein fully indemnified and held harmless by Black Family Members. All communications routed through Carlyn McCaffrey / McDermott Will & Emery to create attorney-client privilege shield. Epstein disclaimed ALL warranties and fiduciary duties while Black assumed "full risk and responsibility." USVI jurisdiction selected.',source:'EFTA00301563'},
  {date:'2008-09-15',event:'U.S. Attorney R. Alexander Acosta personally signs letter to victim attorney Robert Josefsberg transmitting the Non-Prosecution Agreement. Requests copies of "signed Protective Order governing the disclosure of the Non-Prosecution Agreement." Acosta directly managing the NPA that immunized Epstein and all named/unnamed co-conspirators.',source:'EFTA00177459'},
  {date:'2006-02-01',event:'PALM BEACH PD REPORT: Grand Jury session requested to seek Epstein indictment. "Due to subsequent meetings with the State Attorney\\'s Office and Defense Attorney Alan Dershowitz the Grand Jury was postponed." Dershowitz provided a "package of material on the main victims" from MySpace showing "alcohol use and some marijuana use" to smear teenage victims. State Attorney wanted "time to review the material." Grand Jury effectively derailed.',source:'EFTA00177459'},
  {date:'2005-10-01',event:'PALM BEACH PD REPORT: Witness intimidation documented. Victim told: "Those who help him will be compensated and those who hurt him will be dealt with." Private investigators from Epstein\\'s defense team photographed victim families, ran vehicles off the road, and impersonated police officers. Defense attorney Roy Black directing PI operations.',source:'EFTA00177459'},
  {date:'2007-02-06',event:'FBI agent testifies before Federal Grand Jury (FGJ 05-02): "Our victims were 14 to 17." Documents pyramid recruitment scheme under oath: girls paid $200 just for "bringing another girl, so there starts the chain." Epstein assistant Kellen used her cell phone to "schedule the underage girls to come and work, perform the massages." Marcinkova identified as subject who "engaged in sexual activity with" minors.',source:'EFTA00226396'},
  {date:'2019-08-09',event:'OIG DRAFT REPORT: On his last night alive, staff allowed Epstein to make an "unrecorded, unmonitored telephone call" -- he claimed he was calling his mother, but "Epstein\\'s mother was deceased at the time." He actually called an individual with whom he "allegedly had a personal relationship." Cell contained excess blankets and linens ripped to create nooses. Only one SHU cell search that day -- not of Epstein\\'s cell.',source:'EFTA00172546'},
  {date:'2019-08-10',event:'OIG DRAFT REPORT: Medical Examiner determined cause of death was hanging, manner was suicide. "No evidence of defensive wounds...did not have marks on his hands, broken fingernails or debris under them." Video shows no one approached Epstein\\'s tier between 10:40pm and 6:30am. Three inmates with direct line of sight confirmed no one entered or exited his cell. Guards Noel and Thomas falsified count slips and round sheets. Camera system had been malfunctioning since July 29.',source:'EFTA00172546'},
"""

# New FINDINGS entries
findings_entries = """  {id:'wyden-senate-letter-black-2b-tax-avoidance-jul2023',dataset:'DS11-Financial',pages:16,severity:10,keywords:['ron wyden','senate finance committee','leon black','$158 million','$2 billion','tax avoidance','grat','grantor retained annuity trust','remainder trust','gift tax','estate tax','step-up basis','$600 million','irs','no audit','sixty cent dollars','no written agreement','epstein','southern trust','elysium management','apollo','dechert','paul weiss','brownstein hyatt','july 2023'],summary:'CRITICAL -- PRIMARY SOURCE: 16-page letter from Senate Finance Committee Chairman Ron Wyden to Leon Black (EFTA02731023, July 24, 2023). CONGRESSIONAL INVESTIGATION OF $158M PAYMENTS AND $2B TAX AVOIDANCE: (1) Epstein devised scheme transferring approximately $2 BILLION to Black\\\\'s children via 2006 Grantor Retained Annuity Trusts (GRATs) funded with ~$585M in Apollo partnership interests -- estimated tax liability avoidance OVER $1 BILLION; (2) Epstein\\\\'s "proprietary solution" involved a mutual release of claims that extinguished Black\\\\'s income rights while preventing clawback of excess distributions; (3) Separate step-up-basis transaction saved Black an additional $600 MILLION in taxes -- Epstein demanded $60M for this, Black paid $20M; (4) $158M paid WITHOUT WRITTEN SERVICE AGREEMENTS: "you were willing to pay Epstein over $100 million without a written services agreement or contract"; (5) Epstein\\\\'s compensation "far exceeded any amounts Black paid to his other professional advisors" and exceeded median Fortune 500 CEO pay ($15.9M); (6) BLACK REFUSED TO ANSWER key Committee questions about: over-distributed income amounts, consideration exchanged, voting control of Apollo shares, how compensation was calculated, whether payments characterized as gifts; (7) IRS HAS NEVER AUDITED the 2006 GRATs, remainder trust, or mutual release scheme; (8) Committee investigating whether transactions constituted illegal tax evasion, not just avoidance. [v11.00]',date:'2023-07-24',type:'congressional-investigation'},
  {id:'acosta-dershowitz-prosecution-sabotage-palm-beach-pd',dataset:'DS10-Official',pages:98,severity:10,keywords:['alexander acosta','alan dershowitz','palm beach police','grand jury','non-prosecution agreement','npa','victim smearing','myspace','witness intimidation','roy black','private investigators','ghislaine maxwell','el brillo way','palm beach','arrest warrant','unlawful sexual activity','lewd and lascivious','robert josefsberg','guy fronstin','jack goldberger','les wexner','gulfstream','state attorney','detective','2005','2006','2008'],summary:'CRITICAL -- PRIMARY SOURCE: Complete Palm Beach Police Department incident report and U.S. Attorney Acosta\\\\'s NPA correspondence (EFTA00177459, 98+ pages, 2005-2008). PROSECUTION SABOTAGE DOCUMENTED: (1) DERSHOWITZ DERAILS GRAND JURY: In February 2006, a Grand Jury session was requested to seek Epstein\\\\'s indictment. \\\"Due to subsequent meetings with the State Attorney\\\\'s Office and Defense Attorney Alan Dershowitz the Grand Jury was postponed.\\\" Dershowitz provided a \\\"package of material on the main victims\\\" from MySpace showing \\\"alcohol use and some marijuana use\\\" -- SMEARING TEENAGE VICTIMS to delay prosecution; (2) WITNESS INTIMIDATION: Victim told \\\"Those who help him will be compensated and those who hurt him will be dealt with.\\\" Private investigators photographed victim families, ran vehicles off the road, and impersonated police officers. Defense attorney Roy Black directing PI operations; (3) ACOSTA PERSONALLY SIGNED NPA letter (September 15, 2008) managing disclosure of the agreement that immunized Epstein and ALL co-conspirators; (4) State plea deal offered WITHOUT CONSULTING the lead detective: one count aggravated assault with probation and adjudication withheld -- detective documented his \\\"disapproval\\\"; (5) MAXWELL IDENTIFIED: Cross-reference of 358 El Brillo Way revealed \\\"Maxwell, uk/f\\\" -- Maxwell\\\\'s notepaper with names and phone numbers found in trash pulls; Maxwell documented recruiting victims; (6) Arrest warrant requested for 4 counts unlawful sexual activity with minors plus lewd/lascivious molestation; (7) Wexner\\\\'s Gulfstream 4 tracked by police arriving at West Palm Beach. Acosta later became Trump\\\\'s Labor Secretary (2017-2019). [v11.00]',date:'2006-02-01',type:'law-enforcement-report'},
  {id:'fbi-grand-jury-testimony-pyramid-recruitment-feb2007',dataset:'DS10-Official',pages:56,severity:10,keywords:['fbi','grand jury','testimony','sworn','victims','14 to 17','pyramid recruitment','$200','kellen','marcinkova','scheduling','underage girls','massage','cell phone','adrian ross','fifth amendment','immunity','david rogers','pilot','subpoena','southern district florida','february 2007'],summary:'CRITICAL -- PRIMARY SOURCE: FBI agent\\\\'s sworn Grand Jury testimony and federal subpoena documents (EFTA00226396, 56+ pages, November 2006 - February 2007, Grand Jury FGJ 05-02(WPB)). UNDER-OATH DOCUMENTATION OF THE TRAFFICKING OPERATION: (1) FBI agent testifies: \\\"Our victims were 14 to 17, but we have girls that are 18, we have girls that are 20, we have girls that are in their early 20s\\\"; (2) PYRAMID RECRUITMENT SCHEME: \\\"if she brought another girl she would be paid $200 for just bringing another girl, so there starts the chain\\\"; (3) KELLEN\\\\'S ROLE: \\\"Ms. Kellen would contact many of our underage victims either prior to coming into Palm Beach, the day of, the day before, even the day after\\\" and \\\"would schedule the underage girls to come and work, perform the massages for Mr. Epstein\\\"; (4) MARCINKOVA as subject who \\\"engaged in sexual activity with\\\" minors -- described as Epstein\\\\'s \\\"companion, girlfriend, personal assistant\\\"; (5) Employee Adrian Ross invoked Fifth Amendment and demanded immunity through attorney Bruce Lyons; (6) Pilot David Rogers subpoenaed; (7) Grand jury subpoenas targeted employment records, massage appointment records, and all Epstein correspondence; (8) Federal prosecution guidelines (USAM 9-27.000) included in file state it is NOT in public interest to grant immunity to \\\"a high-ranking member of a criminal enterprise\\\" -- yet the NPA did exactly that. [v11.00]',date:'2007-02-06',type:'grand-jury-testimony'},
  {id:'oig-draft-report-epstein-death-camera-failure-falsified-records',dataset:'DS10-Official',pages:120,severity:9,keywords:['oig','office of inspector general','draft report','limited official use','metropolitan correctional center','mcc','bop','bureau of prisons','suicide','hanging','autopsy','medical examiner','no defensive wounds','camera failure','dvr malfunction','july 29','falsified records','count slips','noel','thomas','deferred prosecution','unmonitored call','deceased mother','excess linens','nooses','whitey bulger','staffing','24 hours straight','august 2019'],summary:'HIGH VALUE -- PRIMARY SOURCE: Complete DRAFT DOJ OIG investigation report marked LIMITED OFFICIAL USE (EFTA00172546, ~120 pages, March 2023). THE DEFINITIVE INVESTIGATION INTO EPSTEIN\\\\'S DEATH: (1) CAUSE OF DEATH: Medical Examiner determined hanging/suicide. \\\"No evidence of defensive wounds...did not have marks on his hands, broken fingernails or debris under them\\\"; (2) NO FOUL PLAY: Video showed \\\"no staff or other individuals approaching Epstein\\\\'s SHU tier\\\" between 10:40pm and 6:30am. Three inmates with direct line of sight confirmed no one entered cell; (3) CAMERA FAILURE: Video from only ONE camera available due to DVR malfunction starting July 29 -- discovered August 8 but not repaired before death; (4) FALSIFIED RECORDS: Guards Noel and Thomas \\\"charged criminally with falsifying BOP records\\\" -- charges dismissed after deferred prosecution agreements; (5) LAST PHONE CALL: Staff allowed \\\"unrecorded, unmonitored telephone call\\\" -- Epstein claimed he was calling his mother but \\\"Epstein\\\\'s mother was deceased at the time\\\"; (6) EXCESS LINENS: Cell contained excess blankets \\\"ripped to create nooses\\\" -- no cell search of Epstein\\\\'s cell documented on August 9; (7) STAFFING: Material Handler worked 24 hours straight, admitted \\\"no one did the 10:00 p.m. SHU inmate count because they were tired\\\"; (8) OIG concludes: failures \\\"depriving his numerous victims, many of whom were underage girls, of their ability to seek justice through the criminal justice process.\\\" [v11.00]',date:'2019-08-10',type:'official-investigation'},
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
count = content.count('v10.99')
print(f"Replacing {count} occurrences of 'v10.99' with 'v11.00'")
content = content.replace('v10.99', 'v11.00')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v11.00.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.99')
new_ver = verify.count('v11.00')
print(f"Remaining v10.99: {remaining}")
print(f"Total v11.00: {new_ver}")

for check_id in ['wyden-senate-letter-black-2b-tax-avoidance-jul2023',
                  'acosta-dershowitz-prosecution-sabotage-palm-beach-pd',
                  'fbi-grand-jury-testimony-pyramid-recruitment-feb2007',
                  'oig-draft-report-epstein-death-camera-failure-falsified-records']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
print(f"Arrays at different positions: {f_close2 != t_close2}")
