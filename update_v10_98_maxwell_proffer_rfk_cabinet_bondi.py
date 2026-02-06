#!/usr/bin/env python3
"""Update dashboard with Maxwell proffer transcripts (cabinet, RFK Jr, Mar-a-Lago), AG Bondi FBI letter — v10.98"""
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
timeline_entries = """  {date:'2025-07-24',event:'MAXWELL PROFFER DAY 1: Ghislaine Maxwell interviewed under immunity by DAG Todd Blanche (Trump\\'s former personal attorney), Diego Pestana, and FBI SAC Spencer Horn. Maxwell tells Blanche: "some are in your cabinet, who you value as your coworkers" -- directly stating current Trump cabinet members were part of Epstein\\'s circle. On Trump: "The President was never inappropriate with anybody. He was a gentleman in all respects" and "I admire his extraordinary achievement."',source:'PROFFER_transcript_day1'},
  {date:'2025-07-24',event:'MAXWELL ON RFK JR: "Bobby Kennedy knew him. We went on a trip together -- dinosaur bone hunting in the Dakotas" circa 1993-94. Blanche asks specifically about "anything inappropriate with Mr. Kennedy and masseuses or young women." Maxwell: "I never saw anything inappropriate." Relationship "continued into the 2000s." Bobby Kennedy Jr. is now Trump\\'s HHS Secretary.',source:'PROFFER_transcript_day1'},
  {date:'2025-07-25',event:'MAXWELL PROFFER DAY 2: On Mar-a-Lago victim recruitment, Maxwell volunteers overnight: "the allegation at least is that I met [REDACTED] in Mar-a-Lago." DAG Blanche confirms: "[REDACTED] has said that she was working at Mar-a-Lago and that you recruited her to meet Mr. Epstein." Maxwell: "I don\\'t believe it\\'s true. But...in the realms of possibility, it could have."',source:'PROFFER_transcript_day2'},
  {date:'2025-07-25',event:'MAXWELL ON SUMMERS AND CLINTON: "to suggest that Larry Summers or Clinton would certainly go, oh my gosh...They\\'re men that went and had a massage and maybe did something sexual, they\\'re men, I wasn\\'t in the room. I cannot tell you if that happened." Then directly to Blanche: "some are in your cabinet." Also admits she recruited attractive masseuses: "if she was attractive, I did introduce her, yes."',source:'PROFFER_transcript_day2'},
  {date:'2025-07-24',event:'MAXWELL ON CLINTON: "I was with President Clinton. President Clinton was my friend, not Epstein\\'s friend." Confirms arranging Epstein\\'s plane for Clinton 26 times: "without me, I don\\'t think there would\\'ve been those flights." Denies Clinton went to island: "He never. Absolutely never went." Claims she was "very central" to starting the Clinton Global Initiative.',source:'PROFFER_transcript_day1'},
  {date:'2025-07-25',event:'MAXWELL ON ELON MUSK: "I believe they did [know each other]. The only reason I say that is...in discovery, they were communicating on email. And I believe his brother as well." Met Musk at Sergey Brin\\'s birthday party around 2010-2011.',source:'PROFFER_transcript_day2'},
  {date:'2025-07-24',event:'MAXWELL ON EPSTEIN\\'S DEATH: "I do not believe he died by suicide, no." On who killed him: "If it is indeed murder, I believe it was an internal situation." Dismisses theory powerful people had him killed: "if that is what they wanted, they would\\'ve had plenty of opportunity when he wasn\\'t in jail."',source:'PROFFER_transcript_day1'},
  {date:'2025-07-24',event:'MAXWELL ON INTELLIGENCE: Asked about Mossad: "Well, not deliberately." Calls spy theories "Bullshit." On her father Robert Maxwell: "once you\\'ve been an intelligence officer, you\\'re kind of -- always." On Black Book: "There is no list" -- attempts to discredit entire document as manufactured by Alfredo Rodriguez.',source:'PROFFER_transcript_day1'},
  {date:'2025-02-27',event:'AG Pam Bondi letter to FBI Director Kash Patel: FBI delivered only 200 pages despite repeated AG requests for full Epstein files. Bondi learned from "a source" that FBI NY Field Office had "thousands of pages" never disclosed. Orders full files delivered by 8:00 AM including "all records, documents, audio and video recordings related to Jeffrey Epstein and his clients." Orders investigation of FBI noncompliance.',source:'MEMO_2025.02.27_AG_Bondi_Letter'},
  {date:'2025-07-24',event:'MAXWELL ON PRINCE ANDREW: "I did not introduce him to Prince Andrew. That is a flat untruth." Calls Virginia Giuffre\\'s allegations: "What\\'s an even bigger word than bullshit?" Claims iconic photo of Andrew with Giuffre is "literally a fake photo." On Dershowitz: "Never" saw inappropriate behavior. On Les Wexner: "his closest friend."',source:'PROFFER_transcript_day1'},
"""

# New FINDINGS entries
findings_entries = """  {id:'maxwell-proffer-cabinet-trump-exoneration-jul2025',dataset:'DS10-Proffer',pages:207,severity:10,keywords:['ghislaine maxwell','proffer','immunity','todd blanche','dag','deputy attorney general','cabinet','trump','president','gentleman','inappropriate','mar-a-lago','rfk','bobby kennedy','hhs secretary','dinosaur','dakotas','elon musk','sergey brin','discovery','email','brother','prince andrew','virginia giuffre','fake photo','dershowitz','les wexner','closest friend','mossad','intelligence','black book','alfredo rodriguez','suicide','murder','internal','july 2025'],summary:'CRITICAL -- PRIMARY SOURCE: Full transcript of Ghislaine Maxwell\\'s recorded proffer interview (Day 1: 207 pages, July 24, 2025, Tallahassee). Maxwell interviewed under immunity by DAG Todd Blanche (Trump\\'s former personal attorney), Acting Associate DAG Diego Pestana, and FBI SAC Spencer Horn. THE MOST SIGNIFICANT TESTIMONY: (1) \"SOME ARE IN YOUR CABINET\": Maxwell directly tells Blanche: \"this cast of characters, of which it\\'s extraordinary, and some are in your cabinet, who you value as your coworkers...would be with him if he was a creep\" -- EXPLICITLY STATING CURRENT TRUMP CABINET MEMBERS WERE PART OF EPSTEIN\\'S CIRCLE; (2) STRATEGIC TRUMP EXONERATION: Maxwell volunteers unprompted flattery: \"I admire his extraordinary achievement in becoming the President now. And I like him\" then \"The President was never inappropriate with anybody. He was a gentleman in all respects\" and \"Absolutely never, in any context\" -- all said to Trump\\'s own appointee in a transparently strategic bid for clemency; (3) RFK JR / BOBBY KENNEDY: \"Bobby Kennedy knew him. We went on a trip together -- dinosaur bone hunting in the Dakotas\" circa 1993-94. Blanche specifically asks about Kennedy and \"masseuses or young women.\" Relationship \"continued into the 2000s.\" Kennedy is now Trump\\'s HHS Secretary; (4) ELON MUSK: \"I believe they did know each other...in discovery, they were communicating on email. And his brother as well\" -- met Musk at Sergey Brin\\'s birthday ~2010-11; (5) TRUMP / MAR-A-LAGO: Confirms both she and Epstein went to Mar-a-Lago; she went \"mostly alone\"; Epstein \"possibly\" went to the spa; last saw Trump in person \"mid-2000s\"; (6) CLINTON: Was \"very central\" to starting Clinton Global Initiative; arranged Epstein\\'s plane for Clinton\\'s Africa trip; denies Clinton went to island: \"He never. Absolutely never went\"; (7) PRINCE ANDREW: \"I did not introduce him to Prince Andrew. That is a flat untruth.\" Giuffre allegations: \"What\\'s an even bigger word than bullshit?\" Claims photo is fake; (8) EPSTEIN\\'s DEATH: \"I do not believe he died by suicide.\" If murder: \"an internal situation\" not powerful people; (9) BLACK BOOK: \"There is no list\" -- attempts to discredit foundational evidence; (10) INTELLIGENCE: On Mossad contact: \"Well, not deliberately.\" Father Robert Maxwell: \"once you\\'ve been an intelligence officer, you\\'re kind of -- always.\" [v10.98]',date:'2025-07-24',type:'proffer-transcript'},
  {id:'maxwell-proffer-day2-summers-clinton-sexual-mar-a-lago-victim',dataset:'DS10-Proffer',pages:182,severity:10,keywords:['ghislaine maxwell','proffer','day 2','larry summers','clinton','massage','sexual','cabinet','mar-a-lago','victim','recruited','spa','masseuse','attractive','bobby kennedy','elon musk','george soros','les wexner','closest friend','sarah ferguson','naomi campbell','kevin spacey','chris tucker','normalized','blowjob','p diddy','clintons and trump','july 2025'],summary:'CRITICAL -- PRIMARY SOURCE: Full transcript of Maxwell\\'s proffer (Day 2: 182 pages, July 25, 2025). EXPLOSIVE ADMISSIONS: (1) SUMMERS/CLINTON SEXUAL MASSAGES: Maxwell states: \"Larry Summers or Clinton...They\\'re men that went and had a massage and maybe did something sexual, they\\'re men, I wasn\\'t in the room. I cannot tell you if that happened.\" Immediately follows with: \"some are in your cabinet\" -- naming current Trump cabinet members as Epstein associates; (2) MAR-A-LAGO VICTIM RECRUITMENT: Maxwell volunteers overnight clarification on Mar-a-Lago. DAG Blanche confirms: \"[REDACTED] has said that she was working at Mar-a-Lago and that you recruited her to meet Mr. Epstein.\" Maxwell: \"I don\\'t believe it\\'s true. But...in the realms of possibility, it could have\"; (3) RECRUITED ATTRACTIVE MASSEUSES: \"I did look for masseuses...if she was attractive, I did introduce her, yes\"; (4) NORMALIZED BEHAVIOR: \"the people around him, myself included, normalized his behavior\"; (5) RFK JR CONTINUED: Confirms Bobby Kennedy\\'s relationship with Epstein \"continued into the 2000s\"; (6) ELON MUSK: Epstein and Musk communicated by email per discovery, plus Musk\\'s brother; (7) GEORGE SOROS: \"I don\\'t think he knew him. I did, but I don\\'t think he did\"; (8) LES WEXNER: \"his closest friend\" from 1991 onward; (9) SARAH FERGUSON: implied romantic interest in Epstein; (10) P. DIDDY COMPARISON: \"it\\'s like P. Diddy in Redux on TV with Clintons and Trump. I mean, it\\'s bananas\"; (11) CLINTON ISLAND: \"He never. Absolutely never went\" -- emphatic denial; (12) CLINTON GLOBAL INITIATIVE: \"I would say very central to that, yes\" -- Maxwell claims credit for starting CGI. [v10.98]',date:'2025-07-25',type:'proffer-transcript'},
  {id:'ag-bondi-fbi-withheld-epstein-files-feb2025',dataset:'DS10-Official',pages:2,severity:9,keywords:['pam bondi','attorney general','kash patel','fbi director','fbi','withheld','thousands of pages','new york field office','full and complete','audio video recordings','clients','investigation','noncompliance','personnel action','transparency','february 2025'],summary:'HIGH VALUE -- PRIMARY SOURCE: Letter from Attorney General Pam Bondi to FBI Director Kash Patel (February 27, 2025, 2 pages). FBI CONCEALED EPSTEIN FILES FROM THE AG: (1) Bondi had repeatedly requested \"full and complete files related to Jeffrey Epstein\" -- FBI delivered only approximately 200 pages (flight logs, contact list, victim names); (2) Bondi learned from \"a source\" that FBI\\'s New York Field Office possessed \"thousands of pages of documents related to the investigation and indictment of Epstein\" that were never disclosed; (3) FBI Director Patel was \"just as surprised\" to learn of the hidden files; (4) Bondi orders delivery of ALL files by 8:00 AM the next day including \"all records, documents, audio and video recordings, and materials related to Jeffrey Epstein and his clients\" -- the phrase \"his clients\" implies investigation of associates; (5) Orders \"immediate investigation\" into FBI noncompliance with \"proposed personnel action\" within 14 days; (6) Demonstrates FBI institutional resistance to disclosure even when ordered by the sitting Attorney General. This document positions the Trump administration as fighting for Epstein transparency against FBI obstruction. [v10.98]',date:'2025-02-27',type:'official-correspondence'},
  {id:'opr-report-acosta-poor-judgment-60-count-indictment-2020',dataset:'DS10-Official',pages:12,severity:9,keywords:['alexander acosta','labor secretary','non-prosecution agreement','npa','poor judgment','60 count indictment','professional responsibility','opr','ben sasse','miami herald','perversion of justice','co-conspirators','immunity','cvra','crime victims rights','ron desantis','november 2020'],summary:'HIGH VALUE -- PRIMARY SOURCE: DOJ Office of Professional Responsibility Executive Summary (November 2020, 12 pages). OFFICIAL FINDING ON ACOSTA\\'S EPSTEIN DEAL: (1) An AUSA prepared a 60-count draft federal indictment in May 2007 against Epstein that was ABANDONED; (2) Instead, US Attorney Alexander Acosta negotiated a Non-Prosecution Agreement (Sept 24, 2007) giving Epstein a state plea to lesser charges, 18 months county jail, and sex offender registration; (3) The NPA immunized not just Epstein but \"four named co-conspirators\" and \"any potential co-conspirators\" -- blanket immunity for Epstein\\'s entire network; (4) OPR found Acosta exercised \"poor judgment\" but NOT professional misconduct: \"his view of the federal interest in prosecuting Epstein was too narrow\"; (5) OPR found \"no evidence that his decision was based on corruption or other impermissible considerations, such as Epstein\\'s wealth, status, or associations\"; (6) Victims were NOT informed of the NPA before it was signed -- letters sent after described the case as still \"under investigation\"; (7) Trump nominated Acosta as Labor Secretary in 2017; Acosta resigned July 12, 2019 under pressure; (8) Investigation triggered by Senator Ben Sasse\\'s December 2018 letter following Miami Herald\\'s \"Perversion of Justice\" series. [v10.98]',date:'2020-11-01',type:'official-report'},
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
count = content.count('v10.97')
print(f"Replacing {count} occurrences of 'v10.97' with 'v10.98'")
content = content.replace('v10.97', 'v10.98')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.98.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.97')
new_ver = verify.count('v10.98')
print(f"Remaining v10.97: {remaining}")
print(f"Total v10.98: {new_ver}")

for check_id in ['maxwell-proffer-cabinet-trump-exoneration-jul2025',
                  'maxwell-proffer-day2-summers-clinton-sexual-mar-a-lago-victim',
                  'ag-bondi-fbi-withheld-epstein-files-feb2025',
                  'opr-report-acosta-poor-judgment-60-count-indictment-2020']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
print(f"Arrays at different positions: {f_close2 != t_close2}")
