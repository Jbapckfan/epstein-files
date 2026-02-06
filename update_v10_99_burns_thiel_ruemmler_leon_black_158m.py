#!/usr/bin/env python3
"""Update dashboard with Burns-Thiel-Ruemmler nexus Sept 2014, Leon Black $158M Dechert memo — v10.99"""
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
timeline_entries = """  {date:'2014-09-13',event:'EPSTEIN SCHEDULE: 2-4pm Peter Thiel meeting. 3-4pm "Bill Burns will join Jeffrey and Peter Thiel meeting." 4-5pm "Meeting with Bill Burns alone." "JOJO YOU ARE TO TAKE BILL BURNS TO THE AIRPORT." 7:30pm "DINNER w/Woody Allen (JE to invite Kathy Ruemmler and Peter Thiel to dinner)." CIA Director, Trump mega-donor, Obama White House Counsel, all at Epstein\\'s home in one day.',source:'EFTA00363098'},
  {date:'2014-09-02',event:'Epstein\\'s assistant emails Bob Kerrey (former Senator): "Jeffrey is having Peter Thiel and possibly Bill Burns for lunch at his home in NY on Sat. Sept 13th and Sun. Sept 14th...Jeffrey is asking if you might be available to join." Kerrey responds: "I think both work."',source:'EFTA00363688'},
  {date:'2014-09-22',event:'Epstein\\'s "People To See" master list for the week: "Jagland, Terje, Thiel, Simon, Kathy, Cass, Woody, Ehud, Leon, Stone, Summers, Boris, Bill Burns." Schedule: 3pm Larry Summers, 11am Leon Black (Sept 21), 2pm Boris Nikolic (Sept 21), 5pm Bill Burns (Sept 24). "TBD Boris, Kathy, Peter, Bill Burns, Leon (?)" -- grouping the entire nexus.',source:'EFTA00362192'},
  {date:'2014-09-23',event:'Epstein schedule: "12:00pm Lunch w/Ehud [Barak]. 1:00pm Kathy Ruemmler to join you and Ehud." Sept 24: "Jagland (Kathy Ruemmler is in NY and would love to join)." Sept 25: "Ehud Barak (Kathy Ruemmler is in NY and would love to join)." Ruemmler attending multiple Epstein meetings with former Israeli PM and Nobel Committee chair.',source:'EFTA00362192'},
  {date:'2017-11-28',event:'Epstein schedule: "9:30am BREAKFAST Appt w/Leon Black. 12:30pm LUNCH w/Ehud Barak. 1:30-2:30pm Appt w/Kathy Ruemmler." Email subject: "Re: Kathy Ruemmler." Epstein: "tell ehud 12 leon confirmed?" Three years after the 2014 meetings, the same cast -- Black, Barak, Ruemmler -- still converging at Epstein\\'s home.',source:'EFTA00464624'},
  {date:'2014-09-11',event:'Epstein schedule: "4:00pm TENTATIVE Appt w/Boris Nikolic. 5:30pm Appt w/Leon Black." Two days before the Burns-Thiel summit. Boris Nikolic was Bill Gates\\'s science advisor and was named in Epstein\\'s will as a backup executor.',source:'EFTA00363098'},
  {date:'2021-01-22',event:'Dechert LLP memorandum to Apollo Conflicts Committee documenting $158 million in payments from Leon Black to Jeffrey Epstein (2012-2017). Investigation reviewed 60,000+ documents and 20+ witness interviews. Epstein\\'s advice allegedly worth "$1 billion to $2 billion or more" to Black. Payments: $50M in 2013, $70M in 2014, $30M in 2015, $0 in 2016, $8M in 2017.',source:'EFTA02730996'},
  {date:'2013-02-15',event:'First documented payment from Leon Black to Epstein: $15 million via signed service agreement with Southern Trust Company. By October 2013, total reaches $50 million. Epstein told Black payments would be tax deductible ("sixty cent dollars") -- which was false. Epstein represented he "generally charged clients $40 million per year."',source:'EFTA02730996'},
  {date:'2011-03-01',event:'Financial Trust Company (Epstein entity) purchases 263,257 shares of Apollo Global Management stock during its IPO. Shares later transferred to Southern Financial LLC. Apollo publicly stated they "never did any business with" Epstein -- Dechert notes this claim is "perhaps more nuanced than might appear at first glance."',source:'EFTA02730996'},
"""

# New FINDINGS entries
findings_entries = """  {id:'burns-thiel-ruemmler-nexus-epstein-home-sept2014',dataset:'DS9-Email',pages:8,severity:10,keywords:['bill burns','cia director','deputy secretary of state','peter thiel','kathy ruemmler','white house counsel','obama','woody allen','bob kerrey','senator','ehud barak','leon black','larry summers','boris nikolic','bill gates','jagland','nobel committee','terje','september 2014','post-conviction'],summary:'CRITICAL -- PRIMARY SOURCE: Official Epstein schedules and email invitations (EFTA00363098, EFTA00363688, EFTA00362192, 8 pages combined, September 2014 -- six years post-conviction). THE NEXUS: On a SINGLE DAY (September 13, 2014) at Epstein\\'s NYC home: (1) 2-4pm: PETER THIEL meeting (Trump\\'s biggest tech donor, later transition team member, PayPal/Palantir founder); (2) 3-4pm: \"Bill Burns will join Jeffrey and Peter Thiel meeting\" -- BILL BURNS was then Deputy Secretary of State (later CIA Director 2021-2025); (3) 4-5pm: \"Meeting with Bill Burns alone\"; (4) \"JOJO YOU ARE TO TAKE BILL BURNS TO THE AIRPORT AFTER HIS MEETING WITH JEFFREY\"; (5) 7:30pm: \"DINNER w/Woody Allen (JE to invite Kathy Ruemmler and Peter Thiel to dinner)\" -- KATHY RUEMMLER was Obama\\'s former White House Counsel. In one day: CIA Director + Trump mega-donor + Obama White House Counsel + Woody Allen, all at a convicted sex offender\\'s home. BROADER WEEK: Sept 21-26 schedule shows \"People To See: Thiel, Kathy, Woody, Ehud, Leon, Summers, Boris, Bill Burns\" -- the ENTIRE power nexus. Ruemmler joins Epstein\\'s lunch with Ehud Barak (Sept 23), wants to join Jagland and Barak meetings (Sept 24-25). Larry Summers has 3pm meeting (Sept 22). Leon Black has 11am meeting (Sept 21). Bill Burns has standalone 5pm meeting (Sept 24). Bob Kerrey (former Senator/Governor) invited to the Thiel/Burns lunch via email. [v10.99]',date:'2014-09-13',type:'schedule-evidence'},
  {id:'leon-black-158m-payments-dechert-memo-jan2021',dataset:'DS11-Financial',pages:22,severity:10,keywords:['leon black','apollo global management','dechert llp','$158 million','158 million','payments','estate planning','grat','tax','step-up basis','southern trust','financial trust company','ipo shares','263257 shares','gratitude america','$1 billion','$2 billion','forty million per year','sixty cent dollars','tax deductible','family office','elysium management','paul weiss','conflicts committee','january 2021'],summary:'CRITICAL -- PRIMARY SOURCE: Dechert LLP independent investigation memorandum to Apollo Global Management Conflicts Committee (EFTA02730996-02731017, 22 pages, January 22, 2021). $158 MILLION IN PAYMENTS: Leon Black paid Epstein $158 million from 2012 to 2017 for advisory services: $50M in 2013, $70M in 2014, $30M in 2015, $0 in 2016, $8M in 2017. KEY FINDINGS: (1) Epstein\\'s advice allegedly conferred \"more than $1 billion and as much as $2 billion or more\" in value to Black; (2) Epstein told Black payments were tax deductible (\"sixty cent dollars\") -- which was FALSE; (3) Epstein represented he \"generally charged clients $40 million per year\"; (4) Financial Trust Company (Epstein entity) purchased 263,257 APOLLO IPO SHARES in March 2011 -- contradicting Apollo\\'s public claim they \"never did any business with\" Epstein, which Dechert notes is \"perhaps more nuanced than might appear at first glance\"; (5) $10M donation to Gratitude America (Epstein charity) in October 2015; (6) $30.5M in loans from Black to Epstein, of which only $10M was repaid -- $20M still owed at Epstein\\'s death; (7) RELATIONSHIP ENDED October 2018 over fee dispute -- Epstein demanded $60M for a step-up basis transaction, Black refused; (8) No evidence Black was involved in criminal activity; (9) Black knew about 2008 conviction but believed it was \"a single incident involving a 17-year-old with false ID.\" [v10.99]',date:'2021-01-22',type:'financial-investigation'},
  {id:'ruemmler-barak-black-recurring-meetings-2014-2017',dataset:'DS9-Email',pages:4,severity:9,keywords:['kathy ruemmler','ehud barak','leon black','obama','white house counsel','former israeli pm','recurring meetings','november 2017','schedule','breakfast','lunch','appointment','post-conviction'],summary:'HIGH VALUE -- PRIMARY SOURCE: Epstein schedules and email (EFTA00362192, EFTA00464624, 4 pages, September 2014 and November 2017). RECURRING CAST OF CHARACTERS: (1) SEPTEMBER 2014: Ruemmler joins Epstein\\'s lunch with Ehud Barak (Sept 23), wants to join meetings with Jagland (Nobel Committee chair, Sept 24) and Barak again (Sept 25). The \"TBD\" line groups: \"Boris, Kathy, Peter, Bill Burns, Leon\" as people to schedule; (2) NOVEMBER 2017 (three years later): Same day at Epstein\\'s home: \"9:30am BREAKFAST w/Leon Black. 12:30pm LUNCH w/Ehud Barak. 1:30-2:30pm Appt w/Kathy Ruemmler.\" Email subject literally \"Re: Kathy Ruemmler.\" Epstein coordinates timing: \"tell ehud 12 leon confirmed?\"; (3) This proves the BLACK-BARAK-RUEMMLER nexus was not a one-time occurrence but a RECURRING pattern of meetings at Epstein\\'s home spanning at least 2014-2017, all post-conviction. Ruemmler later became Goldman Sachs General Counsel. Epstein facilitated her JPMorgan account through Mary Erdoes (v10.93). [v10.99]',date:'2017-11-28',type:'schedule-evidence'},
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
count = content.count('v10.98')
print(f"Replacing {count} occurrences of 'v10.98' with 'v10.99'")
content = content.replace('v10.98', 'v10.99')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.99.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.98')
new_ver = verify.count('v10.99')
print(f"Remaining v10.98: {remaining}")
print(f"Total v10.99: {new_ver}")

for check_id in ['burns-thiel-ruemmler-nexus-epstein-home-sept2014',
                  'leon-black-158m-payments-dechert-memo-jan2021',
                  'ruemmler-barak-black-recurring-meetings-2014-2017']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
print(f"Arrays at different positions: {f_close2 != t_close2}")
