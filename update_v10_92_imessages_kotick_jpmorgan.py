#!/usr/bin/env python3
"""Update dashboard with Epstein Feb-April 2019 iMessages, Bobby Kotick relationship, JP Morgan 2017 meeting — v10.92"""
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
timeline_entries = """  {date:'2019-02-13',event:'Epstein iMessage to contact "Eva": "Trump- pb this weekend" -- tracking President Trump\\'s Palm Beach movements and informing associates. Same day, Epstein tells another contact "Im back tomorrow. schedule" and texts Karin "On plane." Five months before arrest.',source:'EFTA00509225'},
  {date:'2019-02-12',event:'OSCE-connected European contact iMessages Epstein: "Had Pompeo in Bratislava today. Good visit, positive atmosphere." Epstein already knew: "Pompeo was with miro in slovakia." Same day Epstein writes: "I had a briefing that was one holy shit after another. Wild times. Everyone angry distrustful. Looking for daddy."',source:'EFTA00509225'},
  {date:'2019-04-07',event:'Someone iMessages Epstein: "FBI up to their neck on this." Separate thread: Epstein planning Chomsky filming, discusses Palais Epstein in Vienna, mentions "Druckenmiller. Gattes. buffet." Three months before arrest.',source:'EFTA00509638'},
  {date:'2019-04-21',event:'Contact warns Epstein via iMessage: "ABC News has 5 man investigative team on you -- digging deep. Perversion of Justice is 3 hour+ Netflix series that has all the girls plus in -- full onslaught." Epstein responds: "Thoughts? Letter putting them on notice? And or cooperation?" Contact advises: "They would kill u if cooperate."',source:'EFTA00509744'},
  {date:'2019-04-22',event:'Epstein iMessages about counter-documentary strategy: "Do you think, the end of the patriarchy, should be the working title. Do you interview powerful women. this will give us cover if it comes out that a filming is taking place." Planning a feminist-themed film as cover for counter-narrative.',source:'EFTA00509750'},
  {date:'2019-04-20',event:'Larry Summers iMessages Epstein for relationship advice about a "36 years old. Beautiful" woman. Epstein advises on strategy. Same day Epstein sends Summers: "Ehud said that Bibi won the election because the other guy didn\\'t really look like he wanted to win." Next day sends Summers a legal definition of obstruction of justice.',source:'EFTA00509735'},
  {date:'2012-11-17',event:'Bobby Kotick (Activision Blizzard CEO) confirmed dinner at Epstein\\'s NYC home. Schedule: "7:30-8:00 Bobby Kotick to arrive the house." Chef Francis Derby prepares meal. Epstein had invited Kotick: "come see me, possibly david blaine, and woody allen at the house, you will enjoy them."',source:'EFTA00401784/EFTA00401661'},
  {date:'2012-11-24',event:'Epstein considers going to his island specifically to see Bobby Kotick: "Possibly go to the island for the night? (Bobby Kotick on St Thomas)." Kotick was vacationing near Epstein\\'s St. James island over Thanksgiving.',source:'EFTA00401086'},
  {date:'2011-05-01',event:'Epstein\\'s schedule: "5:00 Appt w/Howard Lutnick (drinks)" followed by "6:30 Dinner w/Woody Allen, Soon-Yi, Prof. Steve Kosslyn, Katherine Keating." Next day May 2: "9:00 Dinner w/Bill Gates and Larry Summers." May 3: "Appt w/Mary Erdoes" (JPMorgan).',source:'EFTA00434346'},
  {date:'2017-02-06',event:'JP Morgan Private Bank Managing Director Justin D. Nelson schedules in-person meeting with Epstein at his NYC residence. Nelson emails from Greenwich CT office. JPMorgan has publicly stated they ended the Epstein relationship in 2013 -- this meeting is four years later.',source:'EFTA00444494'},
"""

# New FINDINGS entries
findings_entries = """  {id:'epstein-imessages-feb2019-trump-pompeo-briefings',dataset:'DS9-Digital',pages:17,severity:10,keywords:['trump','pompeo','bratislava','osce','eva','palm beach','briefing','imessage','february 2019','jeeitunes','terje','chomsky','weingarten','five months before arrest'],summary:'CRITICAL -- PRIMARY SOURCE: Forensic iMessage extraction from Epstein\\'s Mac (NYC024328.aff4, EFTA00509225-509241, 17 pages, February 10-14, 2019 -- five months before arrest). KEY REVELATIONS: (1) TRUMP TRACKING: On February 13, 2019, Epstein texts contact "Eva": "Trump- pb this weekend" -- Epstein was monitoring and communicating President Trump\\'s Palm Beach schedule to associates; (2) POMPEO DIPLOMATIC BRIEFING: On February 12, an OSCE-connected European diplomat/politician iMessages Epstein: "Had Pompeo in Bratislava today. Good visit, positive atmosphere." Epstein ALREADY KNEW: "Pompeo was with miro in slovakia" (likely Miroslav Lajcak, Slovak OSCE Chairman-in-Office 2019). The contact discusses OSCE work, Georgia visit, parliamentary refusal to support Guaido, migration compact failures; (3) INTELLIGENCE BRIEFINGS: Same day Epstein writes: "I had a briefing that was one holy shit after another. Wild times. Everyone angry distrustful. Looking for daddy" and "America pulling out from authority role is like the teacher leaving the classroom with all boys high school"; (4) NOAM CHOMSKY: Epstein describes someone as having "created a field from scratch / linguistics" to a contact who spent 3 hours with him -- confirmed as Noam Chomsky (age ~90); (5) TERJE ROD-LARSEN: Epstein sends financial figures to "Tetje" (former UN envoy): "Almost no money!! 11/12/19-01/18/19- 1,250"; (6) REID WEINGARTEN: "Weingarten coming for breakfast sat" -- prominent DC attorney; (7) HARRY FISH: casual personal friendship texts. This document shows Epstein maintained real-time intelligence on high-level US diplomatic activities and tracked Trump\\'s movements just months before arrest. [v10.92]',date:'2019-02-13',type:'digital-forensics'},
  {id:'epstein-imessages-apr2019-fbi-netflix-counter-strategy-summers',dataset:'DS9-Digital',pages:34,severity:10,keywords:['fbi','netflix','abc news','perversion of justice','counter documentary','larry summers','woody allen','le pen','macron','national rally','yellow vest','obstruction','three months before arrest','april 2019'],summary:'CRITICAL -- PRIMARY SOURCE: Forensic iMessage extraction from Epstein\\'s Mac (NYC024328.aff4, EFTA00509638-509752, 34 pages combined, April 7-22, 2019 -- less than three months before arrest). KEY REVELATIONS: (1) FBI AWARENESS: April 7 -- "FBI up to their neck on this" iMessaged to Epstein; (2) MEDIA INVESTIGATION WARNING: April 21 -- Contact warns: "ABC News has 5 man investigative team on you -- digging deep. Perversion of Justice is 3 hour+ Netflix series that has all the girls plus in -- full onslaught." Epstein responds: "Thoughts? Letter putting them on notice? And or cooperation?"; (3) COUNTER-DOCUMENTARY: April 22 -- Epstein plans cover film: "Do you think, the end of the patriarchy, should be the working title. Do you interview powerful women. this will give us cover if it comes out that a filming is taking place"; (4) WITNESS MANIPULATION: Contact suggests getting victims\\' lawyer to redirect victims from Netflix to "independent film"; (5) LARRY SUMMERS INTIMATE TEXTS: April 20 -- Former Treasury Secretary texts Epstein for relationship advice about "36 years old. Beautiful. Never had a bf who lasted 2 years." Summers discusses his "shrink." Epstein advises: "You lean towards feeling abused and victimized." Sends Summers definition of obstruction of justice; (6) FRENCH POLITICAL MEDDLING: Epstein discusses Macron En Marche fundraising ($2.0M), Le Pen strategy. Contact says: "I need to flip these brothers to National Rally." Epstein attending "yellow vest luncheon" in Paris; (7) WOODY ALLEN: Texts Epstein "We saw Eva last night." Epstein knows from Soon-Yi. These messages show Epstein three months before arrest: aware of FBI and media investigations, planning counter-narratives, providing relationship advice to Larry Summers, and meddling in French far-right politics. [v10.92]',date:'2019-04-21',type:'digital-forensics'},
  {id:'bobby-kotick-epstein-dinner-island-nov2012',dataset:'DS9-Email',pages:12,severity:9,keywords:['bobby kotick','activision','blizzard','woody allen','david blaine','st thomas','island','dinner','chef','thanksgiving','november 2012','lutnick','milken','elon'],summary:'HIGH VALUE -- PRIMARY SOURCE: Email chain and schedules documenting Bobby Kotick (CEO Activision Blizzard) relationship with Epstein (EFTA00401048-401937, 12 pages combined, November 2012). COMPLETE TRAIL: (1) Nov 10-12: Direct email exchange between Kotick and Epstein. Epstein invites: "come see me, i will be in new york, on sat possibly david blaine, and woody allen at the house, you will enjoy them as they will enjoy you." Kotick responds: "I should be in around 7. I will come find you saturday. What is your address?"; (2) Nov 17: Schedule confirms "7:30-8:00 Bobby Kotick to arrive the house." Chef Francis Derby asks: "Any word if I will be preparing dinner on saturday for bobby kotick?" Staff confirms private dinner at 7pm; (3) Nov 20: Groff emails Lutnick about St. Thomas holiday meeting. Internal email reveals: "I have heard through the grapevine that Bobby Kotick may be out St. Thomas way this coming weekend" -- Kotick vacationing near Epstein\\'s island; (4) Nov 24: "Possibly go to the island for the night? (Bobby Kotick on St Thomas)" -- Epstein considering island trip specifically to see Kotick; (5) April 2013 Milken Conference: "People to see in LA: Slayton, Sophie, Josephson, Elon, Kotick, Tisch" -- Kotick on contact list alongside Elon Musk. All contacts occurred post-conviction. Kotick led Activision Blizzard (now owned by Microsoft) for 30 years and was reported as a potential Trump administration advisor. [v10.92]',date:'2012-11-17',type:'email-evidence'},
  {id:'jpmorgan-2017-meeting-post-relationship-end',dataset:'DS9-Email',pages:2,severity:8,keywords:['jp morgan','jpmorgan','justin nelson','managing director','private bank','greenwich','february 2017','post-conviction','relationship end','2013'],summary:'NOTABLE -- PRIMARY SOURCE: Email exchange between Lesley Groff and Justin D. Nelson, Managing Director of J.P. Morgan Private Bank (EFTA00444494-444495, 2 pages, February 6, 2017). Groff emails: "Jeffrey will be in NY on Monday Feb. 13th...might you be available to come see him at 3:30?" Nelson, based at JPMorgan\\'s 100 West Putnam Avenue, Greenwich CT office, responds scheduling for Feb 14. SIGNIFICANCE: JPMorgan has publicly stated and confirmed in $290M settlement proceedings that they ended their banking relationship with Epstein in 2013. Yet four years later, a Managing Director from their Private Bank division is scheduling an in-person meeting at Epstein\\'s NYC residence. This contradicts the bank\\'s public timeline and suggests continued institutional contact well beyond the stated termination date. [v10.92]',date:'2017-02-06',type:'email-evidence'},
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
count = content.count('v10.91')
print(f"Replacing {count} occurrences of 'v10.91' with 'v10.92'")
content = content.replace('v10.91', 'v10.92')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.92.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.91')
new_ver = verify.count('v10.92')
print(f"Remaining v10.91: {remaining}")
print(f"Total v10.92: {new_ver}")

for check_id in ['epstein-imessages-feb2019-trump-pompeo-briefings',
                  'epstein-imessages-apr2019-fbi-netflix-counter-strategy-summers',
                  'bobby-kotick-epstein-dinner-island-nov2012',
                  'jpmorgan-2017-meeting-post-relationship-end']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
print(f"Arrays at different positions: {f_close2 != t_close2}")
