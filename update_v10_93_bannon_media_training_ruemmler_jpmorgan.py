#!/usr/bin/env python3
"""Update dashboard with Bannon media training shoot at Epstein's home April 2019, Bannon advisory Sept 2018, Ruemmler JPMorgan account — v10.93"""
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
timeline_entries = """  {date:'2019-04-01',event:'Epstein iMessages Terje Roed-Larsen from Paris: "Steve Bannon is here with me. If you come early. Tomorrow or late tonight. He has to leave at around 11 am." Terje responds: "Give Steve my best. Would very much like to catch up with him. Will see Bill Burns in London in the evening." Bannon and Epstein together in Paris.',source:'EFTA00509548'},
  {date:'2019-04-02',event:'Contact iMessages Epstein about upcoming media training: "Friday afternoon media training @ your place -- 2 camera shoot; my crew so totally confidential" and "3 pm to 6 pm???" and "On trial that matters / Ok, trial by fire." Planning Bannon-led interview preparation at Epstein\\'s NYC home.',source:'EFTA00509548'},
  {date:'2019-04-03',event:'Epstein iMessages Woody Allen contact: "on friday at 3 pm bannon is bring camera crew to the house to try to teach me how to respond in interviews. would woody like to join and help?" Inviting Woody Allen to participate in Bannon\\'s media coaching session.',source:'EFTA00509566'},
  {date:'2019-04-04',event:'Contact iMessages Epstein: "Talked to Wolfe few minutes ago -- get everything to him" and "Did u get the talking points???" and "We need a punch list of ALL the lies and misrepresentations in the MH piece --- this is massive opening." Michael Wolff receiving talking points for counter-narrative. Also: "today with Spiro and tomrw with kathry" -- legal meetings with Marc Spiro and Kathy Ruemmler.',source:'EFTA00509566'},
  {date:'2019-04-05',event:'THE SHOOT DAY: Contact texts Epstein: "We need to work around your 38--first we need to push back on the lies; then crush the pedo/trafficking narrative; then rebuild your image as philanthropist." Epstein texts Woody Allen: "bannon michael kathy will also be here around 3, what food would you like." Allen declines: over budget on new film. "Dan" texts: "Steve wants to start the shoot at 3:00 - can we get in at about 2:00 to set up?" Then: "Myself and one of my guys are en route. Steve will follow later." Bannon\\'s camera crew sets up at Epstein\\'s NYC home for media training session.',source:'EFTA00509584'},
  {date:'2018-09-03',event:'Epstein iMessages Terje: "Btw. Bannon is in venice." Next day Woody Allen texts Epstein: "I\\'m sure you saw that Bannon was disinvited from the New Yorker festival." Writes long text defending Bannon. Epstein gives Bannon strategic advice through intermediary: "1. a concise vision for what comes after the burning down. 2. be seen to pose more complicated questions... 3. I would think about your brand."',source:'EFTA00509602'},
  {date:'2019-02-07',event:'Lesley Groff emails Mary Erdoes (JPMorgan): "Jeffrey wanted me to reach out to you re his very good friend and former White House counsel to Pres. Barack Obama, Kathy Ruemmler. She would like to open an account with JPM. Jeffrey requests she deal with you personally." Epstein facilitating JPMorgan accounts five months before arrest.',source:'EFTA00490434'},
"""

# New FINDINGS entries
findings_entries = """  {id:'bannon-media-training-epstein-home-april2019',dataset:'DS9-Digital',pages:54,severity:10,keywords:['steve bannon','media training','camera crew','woody allen','michael wolff','kathy ruemmler','dan','paris','pedo trafficking narrative','philanthropist','talking points','miami herald','punch list','spiro','april 2019','three months before arrest'],summary:'CRITICAL -- PRIMARY SOURCE: Forensic iMessage extraction from Epstein\\'s Mac (NYC024328.aff4, EFTA00509548-509584, 54 pages combined, April 1-5, 2019 -- three months before arrest). THE MOST EXPLOSIVE BANNON-EPSTEIN FINDING: COMPLETE TIMELINE OF MEDIA TRAINING OPERATION: (1) APRIL 1 -- PARIS: Epstein texts Terje Roed-Larsen: "Steve Bannon is here with me. If you come early. Tomorrow or late tonight. He has to leave at around 11 am." Terje responds: "Give Steve my best. Would very much like to catch up with him. Will see Bill Burns in London in the evening." Bannon physically with Epstein in Paris; (2) APRIL 2 -- PLANNING: Contact texts: "Friday afternoon media training @ your place -- 2 camera shoot; my crew so totally confidential" and "On trial that matters / Ok, trial by fire"; (3) APRIL 3 -- WOODY ALLEN INVITED: Epstein texts Allen contact: "on friday at 3 pm bannon is bring camera crew to the house to try to teach me how to respond in interviews. would woody like to join and help?"; (4) APRIL 4 -- WOLFF TALKING POINTS: "Talked to Wolfe few minutes ago -- get everything to him" and "Did u get the talking points???" and "We need a punch list of ALL the lies and misrepresentations in the MH piece --- this is massive opening." Also: "today with Spiro and tomrw with kathry" -- meetings with lawyers; (5) APRIL 5 -- THE SHOOT: Contact outlines strategy: "We need to work around your 38--first we need to push back on the lies; then crush the pedo/trafficking narrative; then rebuild your image as philanthropist." Epstein texts Woody Allen: "bannon michael kathy will also be here around 3, what food would you like." Allen declines (film budget meeting). "Dan" texts: "Jeff - dan here - saw you in Paris last week - Steve wants to start the shoot at 3:00 - can we get in at about 2:00 to set up?" Then: "Myself and one of my guys are en route. Steve will follow later." SIMULTANEOUSLY Epstein texts young woman in Moscow requesting photos, tells her "your cheeks are as big as your tits," and texts contact: "each girl knew why she was coming to the house massage with extra, hardly coercion." This finding shows Steve Bannon actively coaching a convicted sex offender on media strategy with a professional camera crew at Epstein\\'s NYC home, while Epstein was simultaneously soliciting young women and minimizing his crimes -- all three months before his July 6, 2019 arrest. [v10.93]',date:'2019-04-05',type:'digital-forensics'},
  {id:'epstein-bannon-advisory-sept2018-new-yorker-venice',dataset:'DS9-Digital',pages:18,severity:9,keywords:['steve bannon','woody allen','new yorker festival','venice','american dharma','brand','liberal censorship','strategic advice','september 2018','terje'],summary:'HIGH VALUE -- PRIMARY SOURCE: Forensic iMessage extraction (EFTA00509602-509619, 18 pages, September 2-4, 2018). Reveals Epstein-Bannon strategic advisory relationship predating the April 2019 media training. September 3: Epstein texts Terje: "Btw. Bannon is in venice" (Venice Film Festival, where Bannon premiered "American Dharma"). September 4: Woody Allen texts Epstein: "I\\'m sure you saw that Bannon was disinvited from the New Yorker festival" and writes long defense: "As much as I hate Bannon and all that he stands for...I think this was very cowardly of the New Yorker." Epstein relays strategic advice to Bannon through intermediary [17]: (1) "a concise vision for what comes after the burning down"; (2) "be seen to pose more complicated questions than often trying to give answers"; (3) "I would think about your brand.. represent that American dharma is the first in a series"; (4) "stifling open debate comes not from hate but from fear"; (5) "expound on Gutless"; (6) "and keep in the fore of your mind that there are no longer secrets." The intermediary asks: "How do I use wisely." This proves Epstein was actively providing strategic communications advice to Bannon and serving as an informal advisor on brand and messaging -- a relationship that deepened into the April 2019 media training operation. Same document: contact offers Epstein "a nice smart girl" (Russian exchange student in San Diego), Epstein sends $5,000. [v10.93]',date:'2018-09-04',type:'digital-forensics'},
  {id:'ruemmler-jpmorgan-account-epstein-referral-feb2019',dataset:'DS9-Email',pages:1,severity:9,keywords:['kathy ruemmler','mary erdoes','jpmorgan','jp morgan','account','white house counsel','obama','referral','february 2019','five months before arrest','lesley groff'],summary:'HIGH VALUE -- PRIMARY SOURCE: Email from Lesley Groff to Mary Erdoes at JPMorgan (EFTA00490434, 1 page, February 7, 2019 -- five months before arrest). TEXT: "Jeffrey wanted me to reach out to you re his very good friend and former White House counsel to Pres. Barack Obama, Kathy Ruemmler. She would like to open an account with JPM. Jeffrey requests she deal with you personally." SIGNIFICANCE: (1) Epstein is personally facilitating JPMorgan account openings for Obama\\'s White House counsel in February 2019 -- contradicting JPMorgan\\'s claim they ended the relationship in 2013; (2) Epstein addresses Mary Erdoes (CEO of JPMorgan Asset & Wealth Management, one of the most powerful women on Wall Street) as someone who takes his personal requests -- showing continued institutional access; (3) Ruemmler\\'s relationship with Epstein was so close she used him as her JPMorgan banking referral rather than going through normal channels; (4) This connects to the v10.92 finding of JPMorgan Managing Director Justin Nelson meeting Epstein at his home in February 2017 -- the bank\\'s relationship with Epstein clearly continued well past 2013; (5) Ruemmler was already documented attending Epstein-Gates-Leon Black meetings (Sept 2014, v10.90) and appearing on Epstein\\'s January 2019 schedule (v10.90). This email proves the relationship was transactional and ongoing. [v10.93]',date:'2019-02-07',type:'email-evidence'},
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
count = content.count('v10.92')
print(f"Replacing {count} occurrences of 'v10.92' with 'v10.93'")
content = content.replace('v10.92', 'v10.93')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.93.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.92')
new_ver = verify.count('v10.93')
print(f"Remaining v10.92: {remaining}")
print(f"Total v10.93: {new_ver}")

for check_id in ['bannon-media-training-epstein-home-april2019',
                  'epstein-bannon-advisory-sept2018-new-yorker-venice',
                  'ruemmler-jpmorgan-account-epstein-referral-feb2019']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
print(f"Arrays at different positions: {f_close2 != t_close2}")
