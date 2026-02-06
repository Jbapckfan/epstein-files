#!/usr/bin/env python3
"""Update dashboard with Musk 'musk boys' meeting, January 2019 Bannon schedule, Ruemmler-Gates connections — v10.90"""
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
timeline_entries = """  {date:'2012-09-23',event:'Elon Musk visits Epstein\\'s 71st Street residence with Talulah Riley, Nick Pritzker, and filmmaker Jonah Nolan. Epstein had emailed Pritzker: "the musk boys told me you are in town, come see me." Pritzker confirmed: "Elon and talulah WILL come at 1. Working on Kimbal." After the visit was arranged, Epstein told his assistant: "we need to talk about content of emails .. remind me toomrw."',source:'EFTA00404447'},
  {date:'2019-01-09',event:'Epstein January 2019 schedule -- 6 months before arrest. Entries include: "TBD Bannon (give him Apple Watches!)", "TBD Kathy Ruemmler" (Obama\\'s White House counsel), "5:00pm Tea w/Michael Wolff" (author of Fire and Fury), "TBD Robert Kuhn", "TBD Jide Zeldin", "TBD Barnaby Marsh."',source:'EFTA00486484'},
  {date:'2019-01-10',event:'Epstein January 2019 schedule continues: "12:30pm LUNCH w/Ehud" (Barak, former Israeli PM). Demonstrates Epstein\\'s social calendar remained active with high-profile political and intelligence figures just months before his July 2019 arrest.',source:'EFTA00486484'},
  {date:'2014-09-08',event:'Epstein schedule: "10:00am Meet Bill Gates at the Four Seasons Hotel" then "11:30-3:00pm Walk over to Leon Black\\'s office w/Bill Gates, Kathy Ruemmler. Maybe Tom Pritzker." Obama\\'s former White House counsel attending meetings alongside Gates through Epstein.',source:'EFTA00363514'},
"""

# New FINDINGS entries — using \\' for JS apostrophe escaping (Python \\' = file \' = valid JS escaped quote)
findings_entries = """  {id:'musk-epstein-sept2012-muskboys-pritzker-nolan',dataset:'DS9-Email',pages:8,severity:10,keywords:['elon musk','talulah riley','nick pritzker','jonah nolan','kimbal musk','71st street','musk boys','september 2012','emails'],summary:'CRITICAL -- PRIMARY SOURCE: Email chain between Epstein, Nick Pritzker, and Lesley Groff (EFTA00404447-404461, 8 pages combined, September 21-23, 2012). Epstein initiates contact: "the musk boys told me you are in town, come see me, sat sun? anytime" -- referring to Elon and Kimbal Musk, indicating they were in regular enough contact with Epstein to relay who was visiting NYC. Pritzker responds asking about "Brockman" (John Brockman, literary agent who connected tech figures to Epstein) and confirms: "Elon and talulah WILL come at 1. Working on Kimbal." Final guest list: Elon Musk, Talulah Riley (Musk\\'s wife), Nick Pritzker (billionaire, Hyatt Hotels family), and Jonah Nolan (filmmaker, brother of Christopher Nolan) -- but not Kimbal Musk. Meeting at Epstein\\'s 9 East 71st Street residence, September 23, 2012. After the visit was arranged, Epstein tells his assistant: "we need to talk about content of emails .. remind me toomrw" -- showing security consciousness about his email communications. This is FOUR YEARS after Epstein\\'s 2008 conviction. The phrase "the musk boys" is devastating because it implies Elon and Kimbal Musk were regular social contacts who communicated with Epstein about their NYC movements. Combined with Maxwell\\'s proffer confirmation that Epstein knew Musk, the Sergey Brin birthday party meeting (~2010), the direct email dinner invitation (EFTA00509312), and the "Mr. Musk\\'s brother as well" dinner reference, this establishes a sustained Musk-Epstein relationship spanning at least 2010-2012+. [v10.90]',date:'2012-09-23',type:'email-evidence'},
  {id:'epstein-jan2019-schedule-bannon-barak-wolff-ruemmler',dataset:'DS9-Email',pages:2,severity:10,keywords:['bannon','steve bannon','apple watches','ehud barak','michael wolff','kathy ruemmler','january 2019','schedule','six months before arrest','robert kuhn','barnaby marsh'],summary:'CRITICAL -- PRIMARY SOURCE: Epstein schedule email from Lesley Groff (EFTA00486484, 2 pages, January 6, 2019 -- six months before Epstein\\'s July 2019 arrest). KEY ENTRIES: (1) "TBD Bannon (give him Apple Watches!)" -- Steve Bannon, Trump\\'s former chief strategist, scheduled for a gift-bearing meeting. The gift-giving suggests an active social relationship, not just casual contact; (2) "12:30pm LUNCH w/Ehud" (January 10) -- Ehud Barak, former Israeli PM with documented deep ties to Epstein. Barak has been photographed entering Epstein\\'s NYC residence and invested in Carbyne911 with Epstein funding; (3) "5:00pm Tea w/Michael Wolff" -- author of Fire and Fury (2018), the explosive Trump White House book. Wolff also met Epstein same day as Dershowitz and Leon Black (EFTA00368776); (4) "TBD Kathy Ruemmler" -- Obama\\'s White House counsel (2011-2014), later Goldman Sachs General Counsel. 156 documents connect Ruemmler to Epstein, including walking to Leon Black\\'s office with Bill Gates, wanting to join Ehud Barak and Nobel Committee chair Jagland meetings; (5) "TBD Robert Kuhn" and "TBD Barnaby Marsh" -- recurring Epstein associates. This schedule proves Epstein\\'s political and intelligence network remained fully operational in early 2019 despite his registered sex offender status. The Bannon entry is especially significant given Bannon\\'s 9+ other documented Epstein connections including flights, island visits, and the 16-hour surveillance tape. [v10.90]',date:'2019-01-09',type:'email-evidence'},
  {id:'ruemmler-gates-burns-thiel-sept2014-schedule',dataset:'DS9-Email',pages:6,severity:9,keywords:['kathy ruemmler','bill gates','leon black','peter thiel','bill burns','ehud barak','jagland','ariane de rothschild','tom pritzker','boris nikolic','nathan myhrvold','september 2014','four seasons','schedule'],summary:'HIGH VALUE -- PRIMARY SOURCE: Epstein\\'s September 2014 schedule (EFTA00363514, 6 pages). Reveals Kathy Ruemmler (Obama\\'s former White House counsel) deeply embedded in Epstein\\'s inner circle. KEY ENTRIES: (1) September 8: "10:00am Meet Bill Gates at the Four Seasons Hotel" then "11:30-3:00pm Walk over to Leon Black\\'s office w/Bill Gates, Kathy Ruemmler. Maybe Tom Pritzker" -- Epstein facilitating meetings between Obama\\'s top lawyer and the Gates/Black/Pritzker billionaire network; (2) September 13-14: "TBD LUNCH w/Peter Thiel, Bob Kerry, Bill Burns is invited" -- this is the Burns-Thiel joint meeting previously documented (EFTA00362678), now shown in broader context; (3) September 24: "TBD Jagland (Kathy Ruemmler is in NY and would love to join)" -- Thorbjorn Jagland was chair of the Norwegian Nobel Committee; (4) September 25: "TBD Ehud Barak (Kathy Ruemmler is in NY and would love to join)" -- Ruemmler specifically requesting to attend meeting with former Israeli PM; (5) September 11: "11:00am Appt w/Boris Nikolic" -- Gates\\' science advisor, later named in Epstein\\'s will as backup executor; (6) September 10: "5:00pm Appt w/Ariane de Rothschild"; (7) September 5: email confirms Mort Zuckerman meeting with Gates at Epstein\\'s house. The guest list names 30+ people including Larry Summers. This document shows Epstein functioning as a power broker connecting Obama administration officials, Israeli intelligence figures, Nobel Committee leadership, and tech billionaires -- all six years after his 2008 conviction. [v10.90]',date:'2014-09-08',type:'email-evidence'},
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
count = content.count('v10.89')
print(f"Replacing {count} occurrences of 'v10.89' with 'v10.90'")
content = content.replace('v10.89', 'v10.90')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.90.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.89')
new_ver = verify.count('v10.90')
print(f"Remaining v10.89: {remaining}")
print(f"Total v10.90: {new_ver}")

for check_id in ['musk-epstein-sept2012-muskboys-pritzker-nolan',
                  'epstein-jan2019-schedule-bannon-barak-wolff-ruemmler',
                  'ruemmler-gates-burns-thiel-sept2014-schedule']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
print(f"Arrays at different positions: {f_close2 != t_close2}")
