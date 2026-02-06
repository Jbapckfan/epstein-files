#!/usr/bin/env python3
"""Update dashboard with SDNY Trump 8+ flights, Epstein-Elon Musk emails, witness tampering, Richardson/Reid — v10.85"""
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
timeline_entries = """  {date:'1993-01-01',event:'SDNY prosecutors discover Trump listed as passenger on Epstein\\'s private jet "at least eight flights between 1993 and 1996." On one 1993 flight, only Trump and Epstein are listed as passengers. On another, only Epstein, Trump, and a then-20-year-old woman.',source:'EFTA00016732'},
  {date:'2012-01-23',event:'Epstein to-do item: "Will Gov. Richardson be in NY Jan. 30? lunch/dinner w/Reid & je?" -- coordinating dinner with former Governor Bill Richardson and Senate Majority Leader Harry Reid, post-conviction.',source:'EFTA00421998'},
  {date:'2013-04-10',event:'Epstein emails Elon Musk: "are you coming to east coast?" Musk: "No firm plans." Epstein: "april 23, you are welcome to come to dinner with woody allen and crowd at my house, it will be fun." Musk: "I might be in town for the Time 100." Epstein confirms he\\'ll "see Elon at the Milken conference."',source:'EFTA00392585'},
  {date:'2018-11-30',event:'Two days after Miami Herald publishes Epstein expose, Epstein wires $100,000 to one NPA co-conspirator and $250,000 three days later to another -- apparent witness tampering identified by SDNY prosecutors in bail opposition filing.',source:'EFTA00028785'},
"""

# New FINDINGS entries
findings_entries = """  {id:'sdny-trump-8plus-epstein-flights-1993-1996',dataset:'DS9-Legal',pages:1,severity:10,keywords:['trump','epstein','flights','private jet','sdny','maxwell','8 flights','1993','1996','marla maples','tiffany','eric','20-year-old','situational awareness'],summary:'CRITICAL -- PRIMARY SOURCE: Internal SDNY prosecution email (EFTA00016732, 1 page, January 7-8, 2020). Subject: "Epstein flight records." An AUSA writes to colleagues: "For your situational awareness, wanted to let you know that the flight records we received yesterday reflect that Donald Trump traveled on Epstein\\'s private jet many more times than previously has been reported (or that we were aware), including during the period we would expect to charge in a Maxwell case. In particular, he is listed as a passenger on at least eight flights between 1993 and 1996, including at least four flights on which Maxwell was also present. He is listed as having traveled with, among others and at various times, Marla Maples, his daughter Tiffany, and his son Eric. On one flight in 1993, he and Epstein are the only two listed passengers; on another, the only three passengers are Epstein, Trump, and then-20-year-old [name redacted]. On two other flights, two of the passengers were women who would be possible witnesses in a Maxwell case." Prosecutors had reviewed "more than 100 pages of very small script" of flight records and "didn\\'t want any of this to be a surprise down the road." This establishes: (1) SDNY prosecutors themselves documented 8+ Trump flights on Epstein\\'s jet; (2) Four flights with Maxwell present; (3) One flight with only Trump and Epstein; (4) One flight with Trump, Epstein, and a 20-year-old woman; (5) Two flights with potential Maxwell trial witnesses. [v10.85]',date:'2020-01-07',type:'prosecution-evidence'},
  {id:'epstein-elon-musk-direct-emails-dinner-invitation-2013',dataset:'DS9-Email',pages:2,severity:9,keywords:['elon musk','epstein','email','dinner','woody allen','71st street','time 100','milken conference','2013','post-conviction'],summary:'HIGH VALUE -- PRIMARY SOURCE: Direct email chain between Jeffrey Epstein and Elon Musk (EFTA00392585, 2 pages, April 10-11, 2013). Full exchange: Epstein: "are you coming to east coast?" Musk: "No firm plans." Epstein: "april 23, you are welcome to come to dinner with woody allen and crowd at my house, it will be fun." Musk: "Thanks. I might be in town for the Time 100. Not sure yet." Epstein then tells staff he\\'ll "see him at milken conference" (EFTA00392060). Staff emails Musk\\'s assistant Mary Beth Brown confirming (EFTA00392063). Dinner address given as 9 East 71st Street (EFTA00392295). This proves: direct personal email communication between Epstein and Elon Musk in April 2013, FIVE YEARS after Epstein\\'s 2008 conviction. Epstein invited Musk to dinner at the mansion. Musk declined this specific dinner but indicated he would see Epstein at Milken Conference. Elon Musk now heads DOGE in the Trump administration. [v10.85]',date:'2013-04-10',type:'email-evidence'},
  {id:'sdny-bail-opposition-witness-tampering-500m-net-worth',dataset:'DS9-Legal',pages:14,severity:10,keywords:['sdny','bail','witness tampering','100000','250000','co-conspirator','500 million','net worth','miami herald','photographs','mitchell'],summary:'CRITICAL -- PRIMARY SOURCE: SDNY Government Response to Epstein\\'s Bail Motion (EFTA00028785, 14 pages, July 12, 2019, Case 1:19-cr-00490-RMB Doc 11, signed Geoffrey S. Berman). Key findings: (1) Epstein\\'s net worth exceeded $500 million per financial records; (2) Two days after Miami Herald expose (Nov 28, 2018), Epstein wired $100,000 to one NPA co-conspirator on Nov 30, 2018, then $250,000 to another on Dec 3, 2018 -- "Neither of these payments appears to be recurring" -- apparent witness tampering; (3) "Hundreds or thousands of nude and seminude photographs of young females" found in mansion at arrest; (4) CDs labeled "Young [Name] + [Name]," "Misc nudes I," and "Girl pics nude"; (5) Victims told: "Those who help him will be compensated and those who hurt him will be dealt with"; (6) George Mitchell proposed as bail co-signer, described as Epstein\\'s "close personal friend of decades"; (7) 20+ international flights since 2018 alone; (8) PI drove victim\\'s parent off the road. [v10.85]',date:'2019-07-12',type:'prosecution-filing'},
  {id:'epstein-richardson-harry-reid-dinner-post-conviction',dataset:'DS9-Email',pages:1,severity:8,keywords:['bill richardson','harry reid','epstein','dinner','lunch','senate majority leader','governor','2012','post-conviction'],summary:'NOTABLE -- PRIMARY SOURCE: Epstein to-do item from personal email/calendar (EFTA00421998, 1 page, January 2012). Entry reads: "Will Gov. Richardson be in NY Jan. 30? lunch/dinner w/Reid & je?" Alarm set for January 23, 2012. This documents Epstein coordinating a dinner or lunch with Governor Bill Richardson AND Senator Harry Reid (then-Senate Majority Leader) in January 2012 -- FOUR YEARS after Epstein\\'s 2008 conviction and sex offender registration. The casual shorthand "je" suggests routine coordination. Reid was the most powerful Democrat in the Senate. Richardson was named by Virginia Giuffre as someone Epstein directed her to have sex with. [v10.85]',date:'2012-01-23',type:'email-evidence'},
  {id:'trump-epstein-flights-complete-evidence-v1085',dataset:'DS9-Combined',pages:0,severity:10,keywords:['trump','epstein','flights','mar-a-lago','jane doe','fbi','maxwell','private jet','complete','evidence'],summary:'STRUCTURAL FINDING -- TRUMP-EPSTEIN COMPLETE EVIDENCE COMPILATION from 10+ primary sources across v10.78-v10.85: (1) SDNY prosecutors document 8+ Trump flights on Epstein\\'s jet 1993-1996, including 4 with Maxwell and 1 with a 20-year-old (EFTA00016732); (2) Jane Doe federal complaint: Trump introduced to 14-year-old at Mar-a-Lago, "This is a good one, right?" (EFTA00019101); (3) FBI Assessment: Katie Johnson alleges rape by Trump and Epstein at age 13 (EFTA00129126); (4) FBI NTOC compilation: 15+ victim/complainant reports naming Trump (EFTA01660679); (5) FBI CHS report: "Trump has been compromised by Israel," Epstein "belonged to intelligence" (EFTA00090314); (6) SDNY subpoena to Mar-a-Lago for Epstein victim employment records (EFTA00078510); (7) Epstein iMessages monitoring Cohen/Mueller hearings, "trumping" (EFTA00509312); (8) SDNY bail filing: $100K/$250K witness tampering payments, $500M net worth (EFTA00028785); (9) Trump\\'s birthday letter to Epstein framed by outline of naked woman (EFTA00163802). Current Trump administration connections documented on this dashboard: Bannon (9+ docs, flights, island, 16hrs tape), Lutnick (7+ docs, island visits, FBI financial crimes), Barr (Kirkland & Ellis conflict), Bondi/Patel (about-face on client list), Dershowitz (Giuffre sworn: 6 encounters), Acosta ("belonged to intelligence"), Elon Musk (direct email, dinner invitation). [v10.85]',date:'2020-01-07',type:'compiled-timeline'},
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
count = content.count('v10.84')
print(f"Replacing {count} occurrences of 'v10.84' with 'v10.85'")
content = content.replace('v10.84', 'v10.85')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.85.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.84')
new_ver = verify.count('v10.85')
print(f"Remaining v10.84: {remaining}")
print(f"Total v10.85: {new_ver}")

for check_id in ['sdny-trump-8plus-epstein-flights-1993-1996',
                  'epstein-elon-musk-direct-emails-dinner-invitation-2013',
                  'sdny-bail-opposition-witness-tampering-500m-net-worth',
                  'epstein-richardson-harry-reid-dinner-post-conviction',
                  'trump-epstein-flights-complete-evidence-v1085']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
