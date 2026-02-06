#!/usr/bin/env python3
"""Update dashboard with Mark Epstein sworn statement, Bannon tapes, Dropbox share — v10.79"""
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
timeline_entries = """  {date:'2021-09-22',event:'Mark Epstein (Jeffrey\\'s brother) gives sworn digitally recorded statement to DOJ Office of Inspector General at NYC Field Office. States: "Steve Bannon has 16 hours of video tape" of interviews with Jeffrey Epstein. Says "I think Trump is behind it" regarding his brother\\'s death. Says Jeffrey "stopped hanging out with Trump when he realized Trump was a dick."',source:'EFTA00113482'},
  {date:'2019-04-13',event:'Steve Bannon shares Dropbox folder directly with Jeffrey Epstein (jeevacation@gmail.com). Epstein forwards to Karyna Shuliak. Communication occurs just 84 days before Epstein\\'s arrest on July 6, 2019.',source:'EFTA02315270'},
  {date:'2012-03-17',event:'Epstein emails Lesley Groff planning elite "Money" and "Power" seminars. Attendee lists include: Thiel, Bezos, Gates, Clinton, Sergey/Larry (Brin/Page), Schmidt, Andreessen, Milken, Simons, Kahneman. Epstein as convener of billionaires and political power.',source:'EFTA00417385'},
"""

# New FINDINGS entries
findings_entries = """  {id:'mark-epstein-oig-trump-behind-it-bannon-tapes',dataset:'DS9-DOJ',pages:70,severity:10,keywords:['mark epstein','oig','sworn statement','trump behind it','bannon','16 hours','video tape','death','murder','jealous','crook'],summary:'CRITICAL — PRIMARY SOURCE: Digitally recorded sworn statement of Mark Epstein to DOJ Office of Inspector General (Sept 22, 2021, OIG Case #2019-010614, ~70 pages). Jeffrey Epstein\\'s brother testifies under oath: (1) \"Steve Bannon has 16 hours of video tape\" — interviews Bannon conducted with Jeffrey Epstein; (2) \"I think Trump is behind it\" — referring to his brother\\'s death in MCC; (3) \"He stopped hanging out with Trump when he realized Trump was a dick. That\\'s exactly what he said\"; (4) \"Trump is a crook. Everybody knows trump is a crook. That\\'s why no legitimate real estate people would deal with him\"; (5) \"Trump was jealous that people [Indiscernible], and wanted to take that power\"; (6) Bannon told Mark Epstein the tapes \"should protect him\" by \"attorney/client privilege, as witnessed preparation. But Bannon is not an attorney\"; (7) \"Bannon was helping him. Because Bannon was going to come out with another story\"; (8) Mark Epstein received death threats, hired armed guards, worked with FBI and NYPD for two years; (9) Questions why body was moved from cell, why dressed in hospital gown, where is handheld video from hospital. NOTE: This is one person\\'s opinion expressed under oath. Mark Epstein also minimized victims (\"good time Charlies\") and characterized accusers dismissively. [v10.79]',date:'2021-09-22',type:'sworn-statement'},
  {id:'bannon-epstein-dropbox-share-april2019',dataset:'DS11-Email',pages:1,severity:9,keywords:['steve bannon','epstein','dropbox','file sharing','april 2019','jeevacation','karyna shuliak','84 days'],summary:'CRITICAL — PRIMARY SOURCE: Email from Jeffrey Epstein (jeevacation@gmail.com) to Karyna Shuliak (April 13, 2019). Forwards a message FROM Steve Bannon containing a Dropbox shared folder link (dropbox.com/sqn8ah6w6r2b440ek/...). Under JEE (Jeffrey E. Epstein enterprises) confidentiality notice claiming attorney-client privilege. This communication occurred just 84 days before Epstein\\'s arrest on July 6, 2019. Combined with: (a) Feb 2018 scheduling email showing Bannon meeting; (b) Jan 2019 Paris \"People to See\" list including Bannon; (c) Mark Epstein\\'s testimony that Bannon had 16 hours of video tape — this establishes an active, ongoing Bannon-Epstein relationship through at least April 2019. Bannon was Trump\\'s White House Chief Strategist until Aug 2017 and remained a close Trump ally. [v10.79]',date:'2019-04-13',type:'email-evidence'},
  {id:'mark-epstein-bannon-16hrs-videotape-details',dataset:'DS9-DOJ',pages:70,severity:9,keywords:['mark epstein','bannon','16 hours','video tape','witnessed preparation','not attorney','armed guards','death threats','rehabilitate'],summary:'HIGH VALUE — PRIMARY SOURCE: Same Mark Epstein OIG sworn statement. Detailed Bannon section: \"When I met with Steve Bannon, after I saw the tape that my brother sent me after his death, I contacted Steve Bannon.\" Bannon told Mark Epstein \"about the 16 hours of tape, and he told me that the tape should protect him, and that by attorney/client privilege, as witnessed preparation. But Bannon is not an attorney.\" Context: Jeffrey Epstein was \"trying to rehabilitate his reputation\" and \"That\\'s why Bannon was helping him. Because Bannon was going to come out with another story.\" The OIG agents ask \"And which tapes are we talking about?\" Mark Epstein: \"The 16 hours of video tape interviews that [Indiscernible] with my brother.\" Mark also received death threats and hired armed guards. Questions remain: (1) What is on the 16 hours of Bannon-Epstein tape? (2) Does Bannon still possess them? (3) Were they ever turned over to investigators? [v10.79]',date:'2021-09-22',type:'sworn-statement'},
  {id:'epstein-money-power-seminars-thiel-gates-bezos',dataset:'DS11-Email',pages:1,severity:8,keywords:['epstein','seminar','money','power','thiel','bezos','gates','clinton','sergey','larry','schmidt','andreessen','milken','simons','kahneman'],summary:'HIGH VALUE — PRIMARY SOURCE: Epstein email to Lesley Groff (March 17, 2012). Epstein personally plans two elite seminars — \"MONEY\" and \"Power\" — and names attendees: MONEY: \"nathan, danny, bill boris, bezos, jes, tom, jaron, sergey larry, kahneman -- thiel. simons, batista, shmidt, andreeson, milken?, merkin?\" POWER: \"gardner, gates, clinton, george mitchell, igor, ovitz.\" Likely identities: Jeff Bezos, Peter Thiel, Jim Simons, Eric Schmidt, Marc Andreessen, Michael Milken, Ezra Merkin, Sergey Brin & Larry Page, Daniel Kahneman, Jes Staley, Bill Gates, Bill Clinton, George Mitchell, Michael Ovitz, Jaron Lanier. Peter Thiel is a major Trump donor/ally who met Epstein 134+ times per other documents. This shows Epstein as convener of the world\\'s most powerful figures across technology, finance, and politics. [v10.79]',date:'2012-03-17',type:'email-evidence'},
  {id:'bannon-epstein-relationship-timeline-complete',dataset:'DS9-Combined',pages:0,severity:9,keywords:['steve bannon','epstein','timeline','2018','2019','16 hours','dropbox','paris','scheduling','mark epstein','white house'],summary:'STRUCTURAL FINDING — COMPLETE BANNON-EPSTEIN TIMELINE compiled from primary sources: (1) Feb 8, 2018: Epstein emails \"we will have to delay eric. i have bannon on tucs at 1\" — scheduling direct meeting (EFTA02237514); (2) Jan 22, 2019: Epstein assistant Lesley Groff lists \"Bannon\" on \"People to See in Paris\" for Jan 23-31 trip (EFTA02276212); (3) April 13, 2019: Bannon shares Dropbox folder directly with Epstein\\'s personal email (EFTA02315270); (4) Pre-death: Bannon conducts 16 hours of recorded video interviews with Jeffrey Epstein (per Mark Epstein OIG testimony, EFTA00113482); (5) Post-death: Mark Epstein contacts Bannon about \"a tape that my brother sent me after his death\"; (6) Bannon claims tapes are protected by attorney-client privilege as \"witnessed preparation\" — but \"Bannon is not an attorney.\" Bannon left Trump White House as Chief Strategist Aug 2017 and maintained active Epstein relationship through at least April 2019. These tapes have never been publicly disclosed. [v10.79]',date:'2019-04-13',type:'compiled-timeline'},
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
count = content.count('v10.78')
print(f"Replacing {count} occurrences of 'v10.78' with 'v10.79'")
content = content.replace('v10.78', 'v10.79')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.79 with Mark Epstein sworn statement + Bannon tapes.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.78')
new_ver = verify.count('v10.79')
print(f"Remaining v10.78: {remaining}")
print(f"Total v10.79: {new_ver}")

for check_id in ['mark-epstein-oig-trump-behind-it-bannon-tapes', 'bannon-epstein-dropbox-share-april2019',
                  'mark-epstein-bannon-16hrs-videotape-details', 'epstein-money-power-seminars-thiel-gates-bezos',
                  'bannon-epstein-relationship-timeline-complete']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
