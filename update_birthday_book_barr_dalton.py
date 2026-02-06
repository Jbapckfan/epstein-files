#!/usr/bin/env python3
"""Update dashboard with birthday book details, Johnson FBI claim, Barr-Dalton — v10.75"""
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
timeline_entries = """  {date:'2025-09-08',event:'Epstein estate lawyers turn over birthday book to House Oversight Committee via subpoena. WSJ reports Trump\\'s letter ended with "may every day be another wonderful secret" signed "Donald" in style mimicking pubic hair. Separate letter by Joel Pashcow included mock $22,500 check suggesting Epstein "sold" a woman to Trump.',source:'EFTA00163802'},
  {date:'2025-09-08',event:'House Speaker Mike Johnson claims at Capitol that Trump had been "an FBI informant to try and take this stuff down" regarding Epstein. Later retreats — his office clarifies he was referring to attorney Brad Edwards comments. Trump now calls matter "Democrat Epstein Hoax."',source:'EFTA00163802'},
  {date:'2003-02-01',event:'Ghislaine Maxwell assembles "leather-bound album" of birthday letters for Epstein\\'s 50th birthday. Table of contents lists Trump and Clinton under "Friends" section with ~20 associates. Also: Leon Black ("Love and kisses, Leon"), Dershowitz (mock "Vanity Unfair" cover), Peter Mandelson (10-page letter calling Epstein "my best pal"), Les Wexner.',source:'EFTA00163802'},
  {date:'1974-01-01',event:'Donald Barr (father of future AG William Barr) hires Jeffrey Epstein to teach math and physics at Dalton School, the elite private Manhattan school, despite Epstein having no college degree.',source:'EFTA00069870'},
  {date:'2019-08-23',event:'NYT reports: AG Barr personally overseeing 4 federal inquiries into Epstein death, briefed multiple times daily. Barr\\'s old law firm Kirkland & Ellis worked with Epstein on 2008 Miami plea deal. 15 MCC employees subpoenaed. Barr hired Kathleen Hawk Sawyer to run BOP.',source:'EFTA00069870'},
"""

# New FINDINGS entries
findings_entries = """  {id:'birthday-book-trump-signature-revealed',dataset:'DS9-FBI',pages:16,severity:10,keywords:['trump','epstein','birthday book','signature','pubic hair','naked woman','house oversight','subpoena','joel pashcow'],summary:'CRITICAL — PRIMARY SOURCE: FBI Daily News Briefing (Sept 9, 2025) reports WSJ story that Epstein estate lawyers turned over the professionally bound birthday book to House Oversight Committee via congressional subpoena. Trump\\'s letter ended with "Happy Birthday — and may every day be another wonderful secret" with "Donald" signed in a style described as "mimicking pubic hair." Separate letter from Joel Pashcow included mock $22,500 check suggesting Epstein "sold" a woman to Trump. Table of contents listed Trump and Clinton under "Friends" section. Trump has denied writing it, calling it "a fake thing," and sued WSJ for defamation. WSJ signature analysis found similarities with known Trump letters from 2000 and 2006 — same typeface, hand-drawn doodles, familiar word choices. [v10.75]',date:'2025-09-08',type:'fbi-internal'},
  {id:'birthday-book-full-contributors',dataset:'DS9-FBI',pages:16,severity:8,keywords:['leon black','alan dershowitz','peter mandelson','les wexner','ghislaine maxwell','bill clinton','vera wang','nathan myhrvold','mort zuckerman'],summary:'HIGH VALUE: Same FBI briefing details full birthday book contents. Contributors included: Bill Clinton (single handwritten paragraph — spokesman says he cut ties before 2019 arrest), Leon Black (rhymed poem signed "Love and kisses, Leon"), Alan Dershowitz (mock "Vanity Unfair" magazine cover), Les Wexner (brief note with "suggestive drawing"), Peter Mandelson (10-PAGE letter calling Epstein "my best pal"), Vera Wang (joke about The Bachelor), Nathan Myhrvold (7-page wildlife photo submission), Mort Zuckerman (satirical note). Ghislaine Maxwell wrote prologue and closing note. Sections: Friends, Science, Brooklyn, Family. Concluded with "Next 50 Years" and "Lots of love, Ghislaine." [v10.75]',date:'2003-02-01',type:'physical-evidence'},
  {id:'johnson-trump-fbi-informant-claim',dataset:'DS9-FBI',pages:16,severity:9,keywords:['mike johnson','house speaker','fbi informant','trump','brad edwards','democrat epstein hoax'],summary:'CRITICAL: FBI Daily Briefing (Sept 9, 2025) reports House Speaker Mike Johnson claimed at the Capitol that Trump had been "an FBI informant to try and take this stuff down" regarding Epstein. Johnson later retreated — office clarified he was referring to comments by Brad Edwards (attorney for Epstein victims) who said Trump helped him investigate Epstein but did NOT confirm law enforcement cooperation. Trump now calls entire matter the "Democrat Epstein Hoax." Bipartisan legislation being pushed to force DOJ to release all Epstein files. [v10.75]',date:'2025-09-08',type:'political-statement'},
  {id:'barr-dalton-kirkland-connections',dataset:'DS9-SDNY',pages:26,severity:9,keywords:['william barr','donald barr','dalton school','kirkland ellis','alexander acosta','miami deal','epstein death'],summary:'CRITICAL — PRIMARY SOURCE: SDNY News Clips (Aug 23, 2019). NYT reports AG William Barr has "chance ties" to Epstein: (1) Barr\\'s FATHER Donald Barr hired Epstein to teach at Dalton School (elite Manhattan private school) decades earlier despite Epstein having no college degree; (2) Barr\\'s "old law firm" Kirkland & Ellis worked with Epstein on the 2008 Miami plea deal (brokered by Acosta). Barr personally overseeing 4 federal inquiries into Epstein death, briefed multiple times daily. BOP staffing under Trump: correctional officers down from 16,623 (Dec 2016) to 15,012. MCC Manhattan: 111 officers, down from 137 (end 2016), 17 vacant positions. Barr hired Kathleen Hawk Sawyer (whom he first appointed in 1992) to run BOP. [v10.75]',date:'2019-08-23',type:'news-reporting'},
  {id:'acosta-immunity-coconspirators',dataset:'DS9-FBI',pages:10,severity:9,keywords:['alexander acosta','plea deal','immunity','coconspirators','virginia roberts giuffre','geoffrey berman'],summary:'CRITICAL — PRIMARY SOURCE: FBI Tactical Intelligence Report on Maxwell (Oct 2019) contains Vanity Fair passage: "As part of Epstein\\'s original plea deal, negotiated with Alexander Acosta, the others implicated were also given immunity from prosecution, which is partly why victims like Virginia Roberts Giuffre pursued her and others in civil courts." SDNY US Attorney Geoffrey Berman stated after Epstein death: "We remain committed to standing for you, and our investigation of the conduct charged in the Indictment — which included a conspiracy count — remains ongoing." Rumors of 5 imminent indictments circulated. Acosta resigned as Labor Secretary July 2019. [v10.75]',date:'2008-06-30',type:'fbi-intelligence'},
  {id:'maxwell-island-wired-blackmail',dataset:'DS9-FBI',pages:10,severity:8,keywords:['ghislaine maxwell','epstein island','video surveillance','blackmail','helicopter','rollerblades'],summary:'FBI Tactical Intelligence Report (Oct 2019) embeds Vanity Fair reporting: Maxwell said Epstein\\'s island "had been completely wired for video" — source thought "she and Epstein were videotaping everyone on the island as an insurance policy, as blackmail." Maxwell got helicopter license "so she could transport anyone she liked without pilots knowing who they were." Maxwell described recruiting girls at "spas and trailer parks in Florida," offering phone jobs: "you\\'ll make lots of money, meet everyone, and I\\'ll change your life." When asked about underage girls, Maxwell said: "They\\'re nothing, these girls. They are trash." [v10.75]',date:'2019-10-18',type:'fbi-intelligence'},
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
count = content.count('v10.74')
print(f"Replacing {count} occurrences of 'v10.74' with 'v10.75'")
content = content.replace('v10.74', 'v10.75')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.75 with birthday book, Johnson claim, Barr-Dalton findings.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.74')
new_ver = verify.count('v10.75')
print(f"Remaining v10.74: {remaining}")
print(f"Total v10.75: {new_ver}")

for check_id in ['birthday-book-trump-signature-revealed', 'birthday-book-full-contributors',
                  'johnson-trump-fbi-informant-claim', 'barr-dalton-kirkland-connections',
                  'acosta-immunity-coconspirators', 'maxwell-island-wired-blackmail']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
