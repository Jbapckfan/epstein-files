#!/usr/bin/env python3
"""Update dashboard with Bondi/Patel/DOJ oversight + FBI Maxwell intel — v10.74"""
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
timeline_entries = """  {date:'2025-02-21',event:'AG Pam Bondi tells Fox News "It\\'s sitting on my desk right now to review" when asked if DOJ would release Epstein client list. Later found to be false — DOJ found "no incriminating client list" after reviewing 300+ GB.',source:'EFTA00173350'},
  {date:'2025-02-27',event:'AG Bondi letter to FBI Director Patel: "I learned from a source that the FBI Field Office in New York was in possession of thousands of pages" of Epstein documents. Orders full delivery by 8am Feb 28. Demands investigation into why FBI didnt comply with earlier orders.',source:'MEMO_2025.02.27'},
  {date:'2025-03-14',event:'AG Bondi pressures FBI to put ~1,000 IMD personnel on 24-hour shifts to review ~100,000 Epstein records. Personnel instructed to "flag" any records mentioning President Trump. NY Field Office personnel lacking expertise in child victim protections also deployed.',source:'EFTA00173350'},
  {date:'2025-07-07',event:'DOJ/FBI release unsigned memo: "no incriminating client list" found. Confirms Epstein suicide finding. Released surveillance video described as "full raw" — but Wired reports metadata shows 3 minutes cut, footage "likely modified."',source:'EFTA00163550'},
  {date:'2025-07-18',event:'Senate Judiciary RM Durbin sends 13-question letter to AG Bondi. Reveals Trump birthday letter to Epstein (2003) with "hand-drawn outline of a naked woman." Questions why personnel flagged Trump-mentioning records. Demands answers by Aug 1.',source:'EFTA00173350'},
  {date:'2019-10-18',event:'FBI NY Tactical Intelligence Report (LES) on Ghislaine Maxwell. Documents $200M+ suspicious transactions, Maxwell pistol permit (Glock 19), Silent Hit for travel, and Vanity Fair reporting on Maxwell-Epstein-Trump social circle in 1990s.',source:'EFTA00174138'},
  {date:'2011-01-01',event:'Manhattan DA Cy Vance\\'s ADA asks to downgrade Jeffrey Epstein\\'s sex offender status — judge denies it. Same ADA later negotiated lenient deal for another sex predator (Dr. Hadden). Pattern of Vance office going easy on powerful men.',source:'EFTA00020535'},
"""

# New FINDINGS entries
findings_entries = """  {id:'bondi-client-list-false-claim',dataset:'DS9-Senate',pages:5,severity:10,keywords:['pam bondi','attorney general','client list','epstein files','fox news','trump'],summary:'CRITICAL — PRIMARY SOURCE: Senate Judiciary Committee letter (July 18, 2025) from Ranking Member Durbin to AG Bondi. Documents that Bondi told Fox News on Feb 21, 2025: "It\\'s sitting on my desk right now to review" regarding Epstein client list. DOJ later found "no incriminating client list" after reviewing 300+ GB. Bondi then claimed she meant the entire Epstein "file" plus JFK/MLK files. Letter asks 13 detailed questions about veracity of her public statements and the handling of Epstein records under Trump Administration. [v10.74]',date:'2025-07-18',type:'senate-oversight'},
  {id:'bondi-flag-trump-records',dataset:'DS9-Senate',pages:5,severity:10,keywords:['pam bondi','trump','fbi','flag records','1000 personnel','24-hour shifts'],summary:'CRITICAL — PRIMARY SOURCE: Same Senate letter reveals AG Bondi pressured FBI to put ~1,000 Information Management Division personnel on 24-hour shifts (March 14-31, 2025) to review ~100,000 Epstein records. Personnel were instructed to "FLAG" any records in which President Trump was mentioned. Hundreds of NY Field Office personnel also deployed, many lacking expertise to identify child victim protections or handle FOIA requests properly. Raises serious questions about political interference in Epstein file review. [v10.74]',date:'2025-03-14',type:'senate-oversight'},
  {id:'trump-epstein-birthday-letter-naked-drawing',dataset:'DS9-Senate',pages:5,severity:10,keywords:['trump','epstein','birthday letter','naked woman','leather-bound album','ghislaine maxwell','2003'],summary:'CRITICAL — PRIMARY SOURCE: Senate letter cites WSJ reporting (July 17, 2025) that DOJ reviewed a "leather-bound album" of birthday letters to Epstein for his 50th birthday (2003), collected by Ghislaine Maxwell. One letter from President Trump "contains several lines of typewritten text framed by the outline of a naked woman, which appears to be hand-drawn with a heavy marker...and the future president\\'s signature is a squiggly Donald below her waist." Same letter quotes Trump\\'s 2002 statement: "I\\'ve known Jeff for 15 years. Terrific guy. He likes beautiful women as much as I do, and many of them are on the younger side." [v10.74]',date:'2003-01-20',type:'physical-evidence'},
  {id:'bondi-letter-to-patel-fbi-obstruction',dataset:'DS9-DOJ',pages:1,severity:9,keywords:['pam bondi','kash patel','fbi director','epstein files','obstruction','sdny'],summary:'HIGH VALUE — PRIMARY SOURCE: AG Bondi letter to FBI Director Patel (Feb 27, 2025). Bondi states she initially received only ~200 pages (flight logs, contacts, victim names). Despite "repeated requests," FBI assured her this was the full set. Then learned from source that FBI NY Field Office had "thousands of pages" of Epstein investigation/indictment documents. Orders full delivery by 8am Feb 28. Demands investigation into why FBI didnt comply. Reveals internal friction between DOJ leadership and FBI over Epstein file disclosure. [v10.74]',date:'2025-02-27',type:'doj-correspondence'},
  {id:'patel-bongino-epstein-list-claims',dataset:'DS9-FBI',pages:16,severity:9,keywords:['kash patel','dan bongino','fbi director','deputy director','bill gates','client list','conspiracy'],summary:'HIGH VALUE: FBI Daily News Briefing (July 9, 2025) documents pre-appointment statements by FBI Director Patel and Deputy Director Bongino. Patel told Benny Johnson (Dec 2023): Congress blocking Epstein list "because of who\\'s on that list" and "you don\\'t think that Bill Gates is lobbying Congress night and day to prevent the disclosure of that list?" Told audience to "put on your big boy pants and let us know who the pedophiles are." Nov 2024: said Trump would "maybe" release list. Bongino (2023): promoted theory Epstein was "an intelligence asset for people in the Middle East." Both now lead FBI that found "no incriminating client list." Conservative influencers including Elon Musk criticized them. [v10.74]',date:'2025-07-09',type:'fbi-internal'},
  {id:'epstein-video-modified-3min-cut',dataset:'DS9-DOJ',pages:5,severity:9,keywords:['surveillance video','modified','metadata','mcc','wired','3 minutes','raw footage'],summary:'HIGH VALUE: DOJ released MCC surveillance video as "full raw" footage in July 7, 2025 memo. Wired magazine (July 11 & 15, 2025) analysis of embedded metadata showed footage was "likely modified" — nearly 3 minutes had been cut out. This directly contradicts DOJs characterization of the footage as complete and unaltered. Senate Judiciary letter demands explanation of "all modifications made to the full raw surveillance footage before its publication." [v10.74]',date:'2025-07-15',type:'forensic-evidence'},
  {id:'fbi-maxwell-tactical-intel-report',dataset:'DS9-FBI',pages:10,severity:8,keywords:['ghislaine maxwell','fbi','tactical intelligence','financial records','200 million','pistol permit','silent hit','trump'],summary:'FBI NY Tactical Intelligence Report (Oct 18, 2019, LES classification). Maxwell financial records: $200M+ in 469 transactions (2003-2019); $56.9M in 543 transactions. Maxwell had NYC pistol permit (Glock 19 semi-auto), cancelled when moved to Florida. FBI placed "Silent Hit" on Maxwell for international travel monitoring. Report embeds Vanity Fair article documenting Trump-Epstein social relationship in 1990s: Trump party at Plaza Hotel, Trump calling Epstein for model\\'s number, Epstein claiming he had to "drop off food for Donald — he was at home crying under the covers." Also documents Acosta plea deal giving immunity to "others implicated." [v10.74]',date:'2019-10-18',type:'fbi-intelligence'},
  {id:'cy-vance-epstein-sex-offender-downgrade',dataset:'DS9-News',pages:4,severity:7,keywords:['cy vance','manhattan da','sex offender status','downgrade','2011','weinstein','hadden'],summary:'Manhattan DA Cy Vance\\'s ADA asked to downgrade Jeffrey Epstein\\'s sex offender status in 2011 — a judge denied the request. Vance later called it a "mistake." Same ADA negotiated lenient plea deal for Dr. Robert Hadden (sexual assault of 18+ patients) that kept Hadden off publicly accessible sex offender database. Article documents pattern of Vance office prioritizing powerful mens reputational interests over victims. Circulated within SDNY US Attorney office. Note: Cy Vance, not VP JD Vance. [v10.74]',date:'2020-03-06',type:'news-reporting'},
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
count = content.count('v10.73')
print(f"Replacing {count} occurrences of 'v10.73' with 'v10.74'")
content = content.replace('v10.73', 'v10.74')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.74 with Bondi/Patel/DOJ oversight findings.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.73')
new_ver = verify.count('v10.74')
print(f"Remaining v10.73: {remaining}")
print(f"Total v10.74: {new_ver}")

for check_id in ['bondi-client-list-false-claim', 'bondi-flag-trump-records',
                  'trump-epstein-birthday-letter-naked-drawing', 'bondi-letter-to-patel-fbi-obstruction',
                  'patel-bongino-epstein-list-claims', 'epstein-video-modified-3min-cut',
                  'fbi-maxwell-tactical-intel-report', 'cy-vance-epstein-sex-offender-downgrade']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
