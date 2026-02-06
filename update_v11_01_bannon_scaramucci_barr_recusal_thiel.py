#!/usr/bin/env python3
"""Update dashboard with Bannon 83-file nexus, Scaramucci-Ruemmler-Bannon meeting, Barr recusal reversal, Thiel 2017 — v11.01"""
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
timeline_entries = """  {date:'2019-04-05',event:'Epstein schedule: "2:00pm Appt w/Mooch, Ruemmler, Bannon." Anthony Scaramucci (Trump\\'s former White House Communications Director), Kathy Ruemmler (Obama\\'s White House Counsel), and Steve Bannon (Trump\\'s Chief Strategist) all meeting at Epstein\\'s home on the same afternoon -- 92 DAYS before Epstein\\'s arrest on July 6, 2019. Same schedule includes lunch with Deepak Chopra.',source:'EFTA00492534'},
  {date:'2018-05-12',event:'Epstein assistant Lesley Groff emails Noam Chomsky\\'s wife: "Jeffrey says he would love to see you both on Friday! ...he would also like to extend an invitation to dinner on Saturday May 12th...Steve Bannon and Ehud Barak will be here." Trump\\'s former Chief Strategist and former Israeli PM at Epstein\\'s townhouse dinner, 14 months before arrest.',source:'EFTA00473701'},
  {date:'2018-03-01',event:'Groff emails UN General Assembly President Miroslav Lajcak\\'s office: "Jeffrey will be in NY and is asking if President Lajcak could please come join him, Steve Bannon and Ehud Barak at 7:30 for dinner and interesting conversation." Address: 9 East 71st Street. Epstein brokering dinner between Trump\\'s chief strategist, former Israeli PM, and sitting UN President.',source:'EFTA00471126'},
  {date:'2018-02-01',event:'Epstein directly emails Bannon: "have you gone dark?" Bannon: "No way...back in nyc next week." Epstein: "me too. will share some funny stories." Bannon: "Tuesday @ Regency say @ 1 pm???" Epstein: "Wouldn\\'t you like to come to house? I also have an espresso machine." Direct personal communication showing casual, familiar relationship -- Bannon left White House just 6 months earlier.',source:'EFTA00469070'},
  {date:'2019-01-09',event:'Epstein schedule: "TBD Bannon (give him Apple Watches!)" and "TBD Kathy Ruemmler." Also "5:00pm Tea w/Michael Wolff" (author of Fire and Fury). Separate email: "We have 2 watches at the house for you to give to Steve and Sean Bannon." Hermes watch back-ordered for Ruemmler. Epstein buying expensive gifts for Trump\\'s strategist and his son.',source:'EFTA00486484'},
  {date:'2016-11-28',event:'Epstein emails French contact: "can you delay your trip one week. trump related issues occupying my time. say 13 14 instead." Three weeks after Election Day, during the Trump transition period. Not casual news commentary -- a business delay caused by "trump related issues."',source:'EFTA00439050'},
  {date:'2017-08-18',event:'Peter Thiel emails Epstein: "OK, see you at your place." Confirming lunch at Epstein\\'s home. Epstein to Thiel: "im going to meet chomsky in tucson wednesday. you are welcome. sat larry summers at harvard again you are welcome. and then carib." Thiel visiting Epstein 7 months into Trump presidency; invited to meet Chomsky and Summers.',source:'EFTA00456651'},
  {date:'2019-07-09',event:'AG William Barr reverses his recusal from Epstein case within 24 hours. Initially told media: "I\\'m recused from that matter because one of the law firms that represented Epstein long ago was a firm I subsequently joined." After consulting "career ethics officials," Barr decided he did NOT need to recuse from the Manhattan prosecution -- only from reviewing the earlier Acosta deal. Barr maintained oversight of the prosecution of the man whose defense firm later employed him.',source:'EFTA00018398'},
  {date:'2017-09-01',event:'Contact writes Epstein about Qatar-Saudi crisis: "things look very bad in the gulf.. my feeling trump do not want to end it." Then: "tamem just called mbs.. he want to sit and talk.. breakthrough." Epstein: "I think trump cut the legs off your guy. He would like to take all the credit." Real-time Gulf political intelligence linking Epstein to MBS/Qatar crisis and Trump\\'s geopolitical maneuvering.',source:'EFTA00457710'},
  {date:'2018-10-01',event:'Epstein instructs staff about combined Bannon-Barak lunch: "ask him. for bannnon get jew food" and "will Bannon come at 12:30pm with Ehud?" -- "he wil come at 12 and stay." Epstein personally orchestrating Bannon-Barak meetings at his home. The pairing of Trump\\'s strategist with the former Israeli PM was a recurring pattern.',source:'EFTA00483381'},
  {date:'2011-03-28',event:'Epstein emails assistant his call list including: "dersh acosta" -- Dershowitz and Acosta listed together. Groff produces formal list: "Acosta ??" (needs his number), Alan Dershowitz (with number), Roy Black (defense attorney). Epstein actively directing contact with the US Attorney who gave him the lenient plea deal, in 2011, well after his release from prison.',source:'EFTA00436354'},
  {date:'2018-09-01',event:'Epstein\\'s shorthand to staff: "Earlier Bannon Rummrlrr miro at 1." Bannon, Ruemmler ("Rummrlrr"), and Miro (Miroslav Lajcak) scheduled together at Epstein\\'s home. The Bannon-Ruemmler pairing shows Epstein as nexus between Trump and Obama White House power brokers.',source:'EFTA00481433'},
"""

# New FINDINGS entries
findings_entries = """  {id:'bannon-83-files-scaramucci-ruemmler-epstein-2018-2019',dataset:'DS9-Email',pages:83,severity:10,keywords:['steve bannon','chief strategist','trump','anthony scaramucci','mooch','white house communications director','kathy ruemmler','obama','white house counsel','ehud barak','noam chomsky','miroslav lajcak','un general assembly','apple watch','gifts','sean bannon','michael wolff','fire and fury','deepak chopra','9 east 71st street','dinner','lunch','2018','2019','92 days before arrest'],summary:'CRITICAL -- PRIMARY SOURCE: 83 email/schedule files documenting Steve Bannon\\\\'s extensive relationship with Epstein (EFTA004xxxxx range, 2018-2019). BANNON AS RECURRING EPSTEIN VISITOR: (1) SCARAMUCCI-RUEMMLER-BANNON MEETING (April 5, 2019 -- EFTA00492534): Schedule shows \\\"2:00pm Appt w/Mooch, Ruemmler, Bannon\\\" -- Trump\\\\'s former Comms Director, Obama\\\\'s former White House Counsel, and Trump\\\\'s former Chief Strategist all at Epstein\\\\'s home, 92 DAYS before arrest; (2) BANNON-BARAK-CHOMSKY DINNER (May 2018 -- EFTA00473701): \\\"Steve Bannon and Ehud Barak will be here\\\" -- invitation to dinner at Epstein\\\\'s with Noam Chomsky; (3) BANNON-BARAK-UN PRESIDENT (March 2018 -- EFTA00471126): \\\"come join him, Steve Bannon and Ehud Barak at 7:30 for dinner\\\" -- with UN General Assembly President Lajcak at 9 East 71st St; (4) DIRECT PERSONAL EMAILS (Feb 2018 -- EFTA00469070): Epstein to Bannon: \\\"have you gone dark?\\\" / \\\"Wouldn\\\\'t you like to come to house? I also have an espresso machine\\\"; (5) EXPENSIVE GIFTS (Jan 2019 -- EFTA00486484/488226): \\\"2 watches at the house for you to give to Steve and Sean Bannon\\\" (Apple Watches) plus Hermes watch for Ruemmler; (6) BANNON-BARAK RECURRING PATTERN (Oct 2018 -- EFTA00483381): \\\"for bannnon get jew food\\\" / \\\"will Bannon come at 12:30pm with Ehud?\\\"; (7) BANNON-RUEMMLER-MIRO (Sept 2018 -- EFTA00481433): \\\"Bannon Rummrlrr miro at 1\\\"; (8) TEA WITH MICHAEL WOLFF same day as Bannon/Ruemmler (Jan 2019). Bannon appears in 83 EFTA files -- one of the most frequent Epstein associates documented in the entire collection. [v11.01]',date:'2019-04-05',type:'email-schedule-evidence'},
  {id:'barr-recusal-reversal-kirkland-ellis-epstein-jul2019',dataset:'DS10-Official',pages:3,severity:10,keywords:['william barr','attorney general','recusal','kirkland ellis','sdny','southern district new york','epstein prosecution','ethics officials','career ethics','law firm','defense firm','manhattan','july 2019','conflict of interest'],summary:'CRITICAL -- PRIMARY SOURCE: Internal SDNY Public Affairs email forwarding CNN/CNBC reporting (EFTA00018398, July 9, 2019). AG BARR REVERSES RECUSAL IN 24 HOURS: (1) Barr initially stated to media: \\\"I\\\\'m recused from that matter because one of the law firms that represented Epstein long ago was a firm I subsequently joined for a period of time\\\" -- referring to KIRKLAND & ELLIS, which represented Epstein in the 2008 NPA and which Barr joined in 2009; (2) After consulting \\\"career ethics officials,\\\" Barr REVERSED course and decided he did NOT need to recuse from the current Manhattan prosecution; (3) He ONLY recused from \\\"any retrospective review of the resolution of the earlier matter\\\" (the Acosta plea deal in SDFL); (4) This meant BARR MAINTAINED OVERSIGHT of the prosecution of the man whose defense firm later employed him; (5) Email marked \\\"Importance: High\\\" and circulated urgently within SDNY; (6) Barr was subsequently briefed \\\"multiple times a day\\\" on the death investigation and personally intervened in BOP personnel decisions. The recusal reversal is significant because Kirkland & Ellis partners Jay Lefkowitz and others were directly involved in Epstein\\\\'s lenient treatment. [v11.01]',date:'2019-07-09',type:'official-correspondence'},
  {id:'trump-related-issues-transition-thiel-2017-mbs-gulf',dataset:'DS9-Email',pages:12,severity:9,keywords:['trump','transition','trump related issues','peter thiel','palantir','paypal','larry summers','noam chomsky','harvard','tucson','mbs','mohammed bin salman','qatar','gulf crisis','tamem','cut the legs off','geopolitical','foreign policy','november 2016','august 2017','september 2017'],summary:'HIGH VALUE -- PRIMARY SOURCE: Epstein emails documenting Trump-era political engagement (EFTA00439050, EFTA00456651, EFTA00457710, 12 pages combined, 2016-2017). EPSTEIN\\\\'S TRUMP-ERA POLITICAL OPERATIONS: (1) \\\"TRUMP RELATED ISSUES\\\" (Nov 28, 2016 -- EFTA00439050): Three weeks after Election Day, Epstein emails French contact: \\\"can you delay your trip one week. trump related issues occupying my time.\\\" Not casual commentary -- a business delay caused by Trump transition matters; (2) THIEL AT EPSTEIN\\\\'S HOME (Aug 2017 -- EFTA00456651): Peter Thiel emails Epstein: \\\"OK, see you at your place.\\\" Epstein invites Thiel to meet Chomsky in Tucson and \\\"sat larry summers at harvard again you are welcome. and then carib.\\\" Thiel visiting 7 months into Trump presidency; (3) GULF/MBS INTELLIGENCE (Sept 2017 -- EFTA00457710): Contact writes about Qatar-Saudi crisis: \\\"things look very bad in the gulf.. my feeling trump do not want to end it.\\\" Then: \\\"tamem just called mbs.. he want to sit and talk.. breakthrough.\\\" Epstein: \\\"I think trump cut the legs off your guy. He would like to take all the credit.\\\" Real-time Gulf political intelligence with insider access to MBS communications. [v11.01]',date:'2016-11-28',type:'email-evidence'},
  {id:'acosta-on-epstein-call-list-post-prison-mar2011',dataset:'DS9-Email',pages:3,severity:9,keywords:['alexander acosta','alan dershowitz','dersh acosta','call list','post-prison','lesley groff','roy black','defense attorney','mike tein','steve susman','bill scherer','pete briger','fortress','shaikh abdulla','march 2011'],summary:'HIGH VALUE -- PRIMARY SOURCE: Epstein email to assistant with call list (EFTA00436354/436359/436395, 3 pages, March 28, 2011). EPSTEIN CONTACTING ACOSTA POST-PRISON: (1) Epstein emails Groff: \\\"jes cutler meeting, gruss, briger, glenn, scherer. steve ssmn, tein, roy dexter. dersh acosta.\\\" -- \\\"DERSH ACOSTA\\\" listed together as single action item; (2) Groff produces formal call list including \\\"Acosta ??\\\" (needs his phone number), Alan Dershowitz (with number), Roy Black (defense attorney); (3) This is March 2011 -- Epstein actively directing contact with the US Attorney who gave him the lenient plea deal, well AFTER his release from prison; (4) The casual pairing of \\\"dersh acosta\\\" suggests routine contact with both the defense attorney and the prosecutor who enabled the sweetheart deal; (5) Acosta later became Trump\\\\'s Secretary of Labor in 2017, resigned July 2019 under pressure over this same plea deal. [v11.01]',date:'2011-03-28',type:'email-evidence'},
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
count = content.count('v11.00')
print(f"Replacing {count} occurrences of 'v11.00' with 'v11.01'")
content = content.replace('v11.00', 'v11.01')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v11.01.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v11.00')
new_ver = verify.count('v11.01')
print(f"Remaining v11.00: {remaining}")
print(f"Total v11.01: {new_ver}")

for check_id in ['bannon-83-files-scaramucci-ruemmler-epstein-2018-2019',
                  'barr-recusal-reversal-kirkland-ellis-epstein-jul2019',
                  'trump-related-issues-transition-thiel-2017-mbs-gulf',
                  'acosta-on-epstein-call-list-post-prison-mar2011']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
print(f"Arrays at different positions: {f_close2 != t_close2}")
