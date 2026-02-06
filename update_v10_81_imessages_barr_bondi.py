#!/usr/bin/env python3
"""Update dashboard with Epstein iMessages, Barr recusal, Bondi-Patel about-face, Bannon scheduling, hidden cameras — v10.81"""
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
timeline_entries = """  {date:'2019-02-20',event:'Epstein iMessages (law enforcement extraction): Texts about Mueller report next week, Michael Cohen prison delayed to testify before Congress, asks contact about "Macron scandal-- is that Erik Prince company???" Texts Woody Allen comparing his situation to Jussie Smollett.',source:'EFTA00509312'},
  {date:'2019-07-09',event:'Senator Kamala Harris sends letter to AG William Barr and DAG Rosen demanding full recusal from Epstein case due to Kirkland & Ellis ties. Barr only recuses from old Florida case, NOT the SDNY case where Epstein later dies.',source:'EFTA00175169'},
  {date:'2025-07-08',event:'DOJ releases memo concluding "no incriminating client list" after reviewing 300+ GB of data. AG Bondi walks back earlier promises of "a lot of names." Director Patel had previously claimed Congress blocking list "because of who\\'s on that list." Bongino promoted Epstein intelligence asset theory. Trump says "Are you still talking about Jeffrey Epstein?"',source:'EFTA00163550'},
  {date:'2018-02-12',event:'Epstein weekly schedule confirms: "1:00pm Appt w/Steve Bannon (Regency? 71st?)" — direct meeting at either Regency Hotel or Epstein\\'s 71st Street townhouse, 6 months after Bannon left White House.',source:'EFTA00469208'},
"""

# New FINDINGS entries
findings_entries = """  {id:'epstein-imessages-feb2019-cohen-mueller-prince-kraft',dataset:'DS9-DOJ',pages:18,severity:9,keywords:['imessage','epstein','michael cohen','mueller','erik prince','macron','woody allen','robert kraft','trump','february 2019'],summary:'HIGH VALUE -- PRIMARY SOURCE: Epstein iMessages extracted from device NYC024328.aff4 by law enforcement (Feb 20-24, 2019, 18 pages). Key texts from jeeitunes@gmail.com: (1) "Cnn reports mueller next week.. surprise surprise" -- monitoring Mueller investigation; (2) "Don\\'t know. Michalel Cohen prison delayed so he can testify in front of congress" -- tracking Trump\\'s lawyer; (3) Contact asks "Macron scandal-- is that Erik Prince company???" -- awareness of Erik Prince operations; (4) Texts Woody Allen: "It would be nice if someone would write an article comparing Woodys issue with Smollett. Exactly the same. Total bullshit." Allen replies: "That\\'s a very good idea but no one is brave enough. They\\'re all cowards"; (5) "Jack" (attorney) texts about handling Robert Kraft prostitution case strategy via Quinn Emanuel; (6) "MICHAEL and reid at my house Monday 830 morning trying to strategize pr re my craziness" -- PR strategy for Epstein\\'s own legal exposure; (7) "I fear nothing to do but stay quiet. especially as I believe the next few weeks will be filled with trumping." These texts show Epstein actively monitoring Trump-world legal developments 4.5 months before his July 6 arrest. [v10.81]',date:'2019-02-20',type:'phone-extraction'},
  {id:'barr-kirkland-ellis-recusal-harris-demand',dataset:'DS9-DOJ',pages:7,severity:9,keywords:['william barr','kirkland ellis','recusal','kamala harris','epstein','jeffrey rosen','dag','conflict of interest','acosta','plea deal','sdny'],summary:'HIGH VALUE -- PRIMARY SOURCE: Senator Kamala Harris letter to AG Barr and DAG Rosen (July 9, 2019, 7 pages with DOJ ExecSec control sheet). Demands both officials recuse from Epstein case due to Kirkland and Ellis ties. Key facts: (1) Kirkland and Ellis negotiated Epstein\\'s 2008 plea deal through attorney Jay Lefkowitz; (2) Barr was Of Counsel at Kirkland and Ellis at the time of his nomination and in 2009; (3) DAG Rosen was a partner at Kirkland and Ellis 1988-2003 and again 2009-2017; (4) At confirmation hearing, Barr acknowledged: "Senator, I have to recuse myself from Kirkland and Ellis matters I am told, and I think Kirkland and Ellis was maybe involved in that case"; (5) CRITICAL: Barr recused only from the old Florida case, NOT the SDNY case. Epstein died at MCC New York (SDNY jurisdiction) one month later on August 10, 2019. Harris writes: "No one -- no matter how powerful or well-connected -- is above the law." DOJ assigned the letter to JMD/Ethics. [v10.81]',date:'2019-07-09',type:'congressional-correspondence'},
  {id:'bondi-patel-about-face-no-client-list-july2025',dataset:'DS9-DOJ',pages:4,severity:10,keywords:['bondi','patel','bongino','client list','no list','about-face','300 gigabytes','child porn','videos','intelligence asset','trump','epstein files','tom fitton','bannon'],summary:'CRITICAL -- PRIMARY SOURCE: FBI Daily News Briefing (July 9, 2025, compiled from Reuters, Forbes, ABC, NYT, WaPo, Fox, and 18+ outlets). Documents the Trump DOJ\\'s dramatic reversal on Epstein file promises. Key revelations: (1) DOJ memo concluded "no incriminating client list" after reviewing 300+ GB of data; (2) AG Bondi had previously promised to reveal "a lot of names" and "a lot of flight logs" -- walked this back saying she meant the entire "file"; (3) FBI Director Patel had told Benny Johnson podcast in Dec 2023: Congress was blocking the list "because of who\\'s on that list" and "put on your big boy pants and let us know who the pedophiles are"; (4) Deputy Director Bongino promoted conspiracy theory that Epstein was "an intelligence asset for people in the Middle East"; (5) AG Bondi said videos "turned out to be child porn" that will "never be released. Never going to see the light of day"; (6) Trump defended Bondi/Patel as "greatest law enforcement professionals" then said "Are you still talking about Jeffrey Epstein?"; (7) Judicial Watch\\'s Tom Fitton told Steve Bannon: "I don\\'t even think the Biden administration would have written anything like this." FBI confirmed Epstein died by suicide. STRUCTURAL NOTE: The same administration that promised to release the Epstein files concluded there was nothing significant to release. [v10.81]',date:'2025-07-09',type:'fbi-news-briefing'},
  {id:'bannon-epstein-feb2018-schedule-regency-71st',dataset:'DS11-Email',pages:3,severity:8,keywords:['steve bannon','epstein','schedule','february 2018','regency','71st street','appointment','weekly schedule','david grosof','francis pedraza'],summary:'CORROBORATING -- PRIMARY SOURCE: Epstein weekly schedule email (Feb 12, 2018, 3 pages). Confirms direct Bannon-Epstein meeting: "1:00pm Appt w/Steve Bannon (Regency? 71st?)" on Tuesday Feb 13, 2018. The parenthetical suggests choosing between the Regency Hotel or Epstein\\'s 71st Street townhouse as venue. Same schedule includes appointments with Leon Black and MIT researchers (George Church, Joscha Bach, Joi Ito, Hugh Herr, Ed Boyden, Digital Currency Initiative). Corroborates EFTA02237514 ("we will have to delay eric. i have bannon on tucs at 1") and adds venue detail. Combined with Jan 2019 Paris "People to See" list, April 2019 Dropbox share, and Mark Epstein\\'s testimony about 16 hours of tape, this is the 5th independent document confirming an active Bannon-Epstein relationship. [v10.81]',date:'2018-02-12',type:'email-evidence'},
  {id:'palm-beach-hidden-cameras-police-confirmed',dataset:'DS9-DOJ',pages:1,severity:8,keywords:['hidden camera','palm beach','police','video disks','computer crime unit','surveillance','epstein','el brillo'],summary:'CORROBORATING -- PRIMARY SOURCE: Palm Beach Police Department investigation report (2005-2006, within comprehensive case file). Police confirmation of hidden cameras at Epstein\\'s Palm Beach residence: "A review of the video disks which was extracted at the Palm Beach County Sheriff\\'s Office Computer Crime Unit revealed that only one hidden camera was functional at the time. Several images of Epstein working at his desk were seen." Same investigation conducted extensive physical surveillance of 358 El Brillo Way including video monitoring, trash pulls, and identification of young females visiting the property. CONTEXT: Maxwell denied any "inappropriate surveillance" in her July 2025 proffer, but police physically recovered hidden camera equipment. DOJ\\'s July 2025 memo concluded there was no evidence of blackmail, but much of the video evidence is classified as CSAM. [v10.81]',date:'2005-09-21',type:'police-investigation'},
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
count = content.count('v10.80')
print(f"Replacing {count} occurrences of 'v10.80' with 'v10.81'")
content = content.replace('v10.80', 'v10.81')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.81.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.80')
new_ver = verify.count('v10.81')
print(f"Remaining v10.80: {remaining}")
print(f"Total v10.81: {new_ver}")

for check_id in ['epstein-imessages-feb2019-cohen-mueller-prince-kraft',
                  'barr-kirkland-ellis-recusal-harris-demand',
                  'bondi-patel-about-face-no-client-list-july2025',
                  'bannon-epstein-feb2018-schedule-regency-71st',
                  'palm-beach-hidden-cameras-police-confirmed']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
