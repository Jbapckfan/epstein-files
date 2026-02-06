#!/usr/bin/env python3
"""Update dashboard with FBI NTOC Trump complaints, Lutnick-Epstein deep ties, Kimbal Musk, Bannon-Barak coordination — v10.83"""
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
timeline_entries = """  {date:'2012-10-07',event:'Jeffrey Epstein has private lunch with Kimbal Musk (Elon Musk\\'s brother) at his residence. Staff responds: "Oh my... And Kimbal is a foodie." Driver Janusz may take Kimbal to LGA for 3pm flight.',source:'EFTA02316582'},
  {date:'2012-12-19',event:'Lesley Groff emails Howard Lutnick (Cantor Fitzgerald CEO): "Jeffrey Epstein understands you will be down in St. Thomas some over the holidays." Provides Epstein\\'s island caretakers\\' contacts. Lutnick\\'s office responds with Howard\\'s cell number.',source:'EFTA00399296'},
  {date:'2012-12-21',event:'Allison Lutnick confirms visit to Epstein\\'s island with "entire clan" -- 2 families, 8 children ages 7-16, traveling on yacht Excellence for 1:30pm lunch. Epstein confirms "130."',source:'EFTA00398729'},
  {date:'2018-03-19',event:'Epstein emails Ehud Barak: "thurs night with bannon?" Barak replies: "Yes. Of course. Nili will coordinate." This initiates the March 22 dinner at 71st Street with UN GA President Lajcak.',source:'EFTA00470791'},
  {date:'2020-10-19',event:'FBI NTOC receives whistleblower report: "CEO of Cantor Fitzgerald, Howard Lutnick, was Jeffrey Epstein\\'s neighbor" and alleges "suspicious financial activities could be related to Epstein\\'s case." Case ID 50D-NY-3027571.',source:'EFTA00020515'},
"""

# New FINDINGS entries
findings_entries = """  {id:'fbi-ntoc-trump-complaints-15plus-compilation',dataset:'DS11-FBI',pages:6,severity:10,keywords:['fbi','ntoc','trump','complaints','victims','mar-a-lago','calendar girls','parties','epstein','maxwell','task force'],summary:'CRITICAL -- PRIMARY SOURCE: FBI NTOC (National Threat Operations Center) compilation spreadsheet (EFTA01660679, 6 pages, compiled August 6-7, 2025 by FBI Child Exploitation and Human Trafficking Task Force, NY Field Office). Internal FBI email chain compiles 15+ separate victim/complainant reports naming Donald Trump in connection with Jeffrey Epstein. Key entries: (1) Victim alleges forced oral sex on Trump at age 13-14 in NJ; (2) Epstein personal assistant (1986-1992) names Clinton and Trump at Epstein parties; (3) 16-year-old model at 8 Epstein NY parties names Clinton and Trump at "big orgy parties" with Victoria\\'s Secret models; (4) Trump Golf Course (Rancho Palos Verdes, CA) sex trafficking 1995-1996 with Maxwell as "madam and broker" -- FBI disposition: "deemed not credible"; (5) Mar-a-Lago party invitation described by associate as "for prostitutes"; (6) Limo driver (1995) says Trump repeatedly said "Jeffrey" on phone; (7) "Calendar girls" parties at Mar-a-Lago. IMPORTANT CAVEATS: These are UNVERIFIED tips received by FBI. FBI dispositions include "deemed not credible," "no contact made," "voicemail left, no response." Many are second-hand reports. The document\\'s value is as an official FBI record showing the volume and nature of complaints received, and that FBI was still actively reviewing these as of August 2025. One agent notes: "Yellow highlighting is for the salacious piece." [v10.83]',date:'2025-08-07',type:'fbi-compilation'},
  {id:'lutnick-epstein-island-invitation-st-thomas-dec2012',dataset:'DS9-Email',pages:2,severity:10,keywords:['howard lutnick','epstein','island','st thomas','little st james','groff','cantor fitzgerald','december 2012'],summary:'CRITICAL -- PRIMARY SOURCE: Email from Lesley Groff to Howard Lutnick (EFTA00399296, 2 pages, November-December 2012). Groff writes on behalf of Jeffrey Epstein: "Jeffrey Epstein understands you will be down in St. Thomas some over the holidays. Jeffrey requested I please pass along some phone numbers to you so the two of you can possibly get together." Email provides Epstein\\'s island caretakers\\' contact numbers and FTC St. Thomas office info. Response from Matthew Gilbert, Office of Howard W. Lutnick, Chairman, Cantor Fitzgerald, provides Howard\\'s personal cell and Allison Lutnick\\'s number. This establishes direct coordination between Epstein and Lutnick (now Trump\\'s Commerce Secretary) for a meeting near Epstein\\'s island in the USVI. [v10.83]',date:'2012-12-19',type:'email-evidence'},
  {id:'lutnick-family-clan-island-visit-dec2012',dataset:'DS9-Email',pages:2,severity:9,keywords:['howard lutnick','allison lutnick','epstein','island','family','children','yacht','excellence','december 2012'],summary:'HIGH VALUE -- PRIMARY SOURCE: Email chain (EFTA00398729, 2 pages, December 21, 2012). Allison Lutnick emails Groff: "This is Allison Lutnick. We are looking forward to visiting you. We will be coming from Caneel Bay in the morning. We are a crowd...2 families each with 4 kids ranging in age from 7-16! 6 boys and 2 girls." Confirms 1:30pm Sunday lunch at Epstein\\'s island. Traveling on yacht called "Excellence." Forwarded to Epstein at jeevacation@gmail.com who confirms "130." This documents the Lutnick family visiting Epstein\\'s private island. Howard Lutnick is now Trump\\'s Secretary of Commerce. [v10.83]',date:'2012-12-21',type:'email-evidence'},
  {id:'fbi-ntoc-lutnick-cantor-financial-crimes-oct2020',dataset:'DS11-FBI',pages:2,severity:10,keywords:['howard lutnick','cantor fitzgerald','bgc','epstein','fbi','ntoc','financial','neighbor','whistleblower'],summary:'CRITICAL -- PRIMARY SOURCE: FBI NTOC Intake Report (EFTA00020515, 2 pages, October 19, 2020, Case ID 50D-NY-3027571, "EPSTEIN, JEFFREY; CHILD SEX TRAFFICKING"). Official FBI record documenting a whistleblower who worked in New York 2015-2017 alleging: "The CEO of Cantor Fitzgerald, Howard Lutnick, was Jeffrey Epstein\\'s neighbor and he believes some of the suspicious financial activities could be related to Epstein\\'s case." Also alleges Cantor Fitzgerald\\'s 9/11 charity day is "fraudulent." Caller has documentation willing to provide to FBI. Additionally, FBI case log (EFTA02730741) contains separate entry: "NTOC2020 288hmb01 Alleged Money Laundering by Howard Lutnick via BGC Financial and Cantor Fitzgerald." Two independent FBI records reference Lutnick financial activity in connection with Epstein. Lutnick is now Trump\\'s Secretary of Commerce. [v10.83]',date:'2020-10-19',type:'fbi-intake'},
  {id:'epstein-barak-bannon-dinner-direct-coordination',dataset:'DS11-Email',pages:2,severity:9,keywords:['epstein','ehud barak','steve bannon','dinner','coordination','march 2018','jeevacation'],summary:'HIGH VALUE -- PRIMARY SOURCE: Email chain (EFTA00470791, 2 pages, March 19-20, 2018). Jeffrey Epstein emails Ehud Barak from jeevacation@gmail.com with a single line: "thurs night with bannon?" Barak replies: "Yes. Of course. Nili will coordinate." Epstein forwards to Lesley Groff for logistics. The casual one-line message suggests arranging Bannon meetings was routine. This is the initiating email for the March 22, 2018 dinner at 71st Street where UN GA President Lajcak was also invited (EFTA00471126). Supplements Bannon-Epstein evidence from v10.82. [v10.83]',date:'2018-03-19',type:'email-evidence'},
  {id:'kimbal-musk-lunch-epstein-oct2012',dataset:'DS9-Email',pages:1,severity:8,keywords:['kimbal musk','elon musk','epstein','lunch','october 2012','boris','driver','janusz'],summary:'NOTABLE -- PRIMARY SOURCE: Email chain (EFTA02316582, 1 page, October 3, 2012). Epstein staff emails driver Janusz Banasiak: "Jeffrey will be having a lunch with Kimbal Musk this Sunday, Oct. 7th at noon...Boris may be coming as well." Lunch to be ordered in. Staff may need to drive Kimbal to LGA for 3pm flight. Response: "Oh my... And Kimbal is a foodie :(" Kimbal Musk is the brother of Elon Musk, who now heads DOGE in the Trump administration. While there is no evidence in these files of Elon Musk himself meeting Epstein, this documents a Musk family member dining privately at Epstein\\'s residence. [v10.83]',date:'2012-10-07',type:'email-evidence'},
  {id:'lutnick-epstein-complete-relationship-v1083',dataset:'DS9-Combined',pages:0,severity:10,keywords:['howard lutnick','epstein','cantor fitzgerald','bgc','island','donation','close friend','fbi','money laundering','commerce secretary'],summary:'STRUCTURAL FINDING -- LUTNICK-EPSTEIN COMPLETE RELATIONSHIP compiled from 7+ primary source documents: (1) Nov-Dec 2012: Groff emails Lutnick arranging holiday meeting near Epstein\\'s island, provides caretaker contacts (EFTA00399296); (2) Dec 2012: Allison Lutnick confirms visit to Epstein\\'s island with "entire clan" -- 2 families, 8 children ages 7-16, on yacht Excellence (EFTA00398729); (3) Nov 2017: Epstein donates $50,000 to UJA dinner honoring Lutnick, organizers describe Epstein as "a close friend of the Lutnicks" (EFTA00462693); (4) 2018: Active Lutnick-Epstein collaboration on NYC real estate/zoning matter (EFTA00474455); (5) Calendar entries: "5:00pm Appt w/Howard Lutnick (drinks)" (EFTA00434348); (6) Oct 2020: FBI NTOC intake -- whistleblower alleges Lutnick/Cantor financial irregularities connected to Epstein, "Lutnick was Epstein\\'s neighbor" (EFTA00020515); (7) FBI Case Log entry: "NTOC2020 288hmb01 Alleged Money Laundering by Howard Lutnick via BGC Financial and Cantor Fitzgerald" (EFTA02730741). Howard Lutnick is now Donald Trump\\'s Secretary of Commerce. This relationship spans at least 2012-2020 with family island visits, social events, financial donations, professional collaboration, and two separate FBI records alleging financial crimes. [v10.83]',date:'2020-10-19',type:'compiled-timeline'},
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
count = content.count('v10.82')
print(f"Replacing {count} occurrences of 'v10.82' with 'v10.83'")
content = content.replace('v10.82', 'v10.83')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.83.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.82')
new_ver = verify.count('v10.83')
print(f"Remaining v10.82: {remaining}")
print(f"Total v10.83: {new_ver}")

for check_id in ['fbi-ntoc-trump-complaints-15plus-compilation',
                  'lutnick-epstein-island-invitation-st-thomas-dec2012',
                  'lutnick-family-clan-island-visit-dec2012',
                  'fbi-ntoc-lutnick-cantor-financial-crimes-oct2020',
                  'epstein-barak-bannon-dinner-direct-coordination',
                  'kimbal-musk-lunch-epstein-oct2012',
                  'lutnick-epstein-complete-relationship-v1083']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
