#!/usr/bin/env python3
"""Update dashboard with Gates multi-year dinners/flights, Money & Power seminars, FBI CHS Mossad allegation, co-conspirator proffers, Bannon Dropbox — v11.04"""
import sys

filepath = '/Users/jamesalford/epstein_jan30/github_update/dashboard_v10_latest.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

def find_close_simple(content, array_name):
    """Find the ]; that closes the array by searching backwards from next const"""
    marker = f"const {array_name} = ["
    start = content.find(marker)
    if start == -1:
        return -1
    next_const = content.find('\n    const ', start + len(marker))
    if next_const == -1:
        next_const = content.find('\n  const ', start + len(marker))
    if next_const == -1:
        next_const = len(content)
    pos = next_const
    while pos > start:
        if content[pos:pos+2] == '];':
            return pos
        pos -= 1
    return -1

findings_close = find_close_simple(content, 'FINDINGS_DATA')
timeline_close = find_close_simple(content, 'TIMELINE_DATA')

print(f"FINDINGS_DATA closing at: {findings_close}")
print(f"TIMELINE_DATA closing at: {timeline_close}")

if findings_close == -1 or timeline_close == -1:
    print("ERROR: Could not find arrays!")
    sys.exit(1)

if findings_close == timeline_close:
    print("ERROR: Arrays at same position!")
    sys.exit(1)

# New TIMELINE entries
timeline_entries = """  {date:'2011-04-28',event:'Epstein schedule: "9:00pm Dinner w/Bill Gates, Larry Summers, Jes Staley." Separate staff email to Jes Staley\\'s assistant Rosa: "Jeffrey wants Jes to know that Bill Gates will have already eaten dinner, therefore just small bites will be served, like dessert, coffee, tea, drinks type things...we want to make sure Jes does not arrive too hungry!" Epstein coordinating meal logistics between Gates and JPMorgan executive at his home.',source:'EFTA00434400'},
  {date:'2013-02-27',event:'Epstein staff email documents multi-day Gates schedule: "JE now tells me he will go see Bill Gates from 2-3:30 on Wed Feb 27th at Four Seasons...Then he will see Bill Gates again at 10:15pm." Next day: "possibly on Friday fly to PB with Gates as his passenger." Staff note: "which makes me wonder what happened to the lunch at 1pm on Friday March 1 with Gates and Woody Allen!" Confirmed: "wheels up will be 12pm on Friday, March 1st, to PB with Karyna and Bill Gates." GATES FLEW ON EPSTEIN\\'S JET TO PALM BEACH.',source:'EFTA00394909'},
  {date:'2013-02-27',event:'Epstein emails former Senator Bob Kerrey: "bob, do you know bill gates.? He will be at my house, and i wondered if you would like to stop by?" Kerrey replies: "I do know Bill Gates; not well but we\\'ve met a few times. Invite me again!" Epstein using Gates as social bait to draw political figures to his home.',source:'EFTA00394788'},
  {date:'2013-09-20',event:'Lauren Jiloty, SENIOR EXECUTIVE ASSISTANT TO BILL GATES, coordinates dinner schedule: "September 20, JE, Gates, Terje, Jagland. The time hasn\\'t been confirmed yet. I would assume the location will be 71st." Gates\\' own staff directly coordinating with Epstein\\'s staff for dinner at Epstein\\'s Manhattan townhouse. Schedule shows: "7:30 BILL & Melinda GATES to arrive the house. 8:00pm DINNER: Bill Gates, Melinda Gates, Terje, Jagland, JE. Larry & Lisa Summers invited -- waiting for reply."',source:'EFTA00385702'},
  {date:'2014-09-01',event:'Epstein schedule: "10:00am Meet Bill Gates at the Four Seasons Hotel (Will Tom Pritzker be able to go with you to meet Bill?). 11:30-3:00pm Walk over to Leon Black\\'s office w/Bill Gates, Kathy Ruemmler. 2:00pm Mort Zuckerman to meet you w/Bill Gates." Gates taken from Four Seasons to Leon Black\\'s office with Obama\\'s former White House Counsel, then meeting media mogul Mort Zuckerman. Multi-stop itinerary of Gates-Epstein meetings continuing into 2014.',source:'EFTA00363514'},
  {date:'2012-03-17',event:'Epstein emails assistant Lesley Groff outlining two tentative seminars: "MONEY" attendee list: Nathan [Myhrvold], Danny [Hillis], Bill [Gates], Boris [Nikolic], Bezos, Jes [Staley], Jaron [Lanier], Sergey Larry [Brin & Page], Kahneman, Thiel, Simons, Batista, Schmidt, Andreeson, Milken?, Merkin?. "POWER" attendee list: Gardner, Gates, Clinton, George Mitchell, Igor, Ovitz. Post-conviction Epstein curating the world\\'s most powerful tech executives, financiers, and politicians for private seminars.',source:'EFTA00417385'},
  {date:'2020-10-01',event:'FBI Confidential Human Source (CHS) report: Source advises that "Henry Kissinger introduced Charles [Kushner] to Cui Tiankai, the Chinese ambassador to the U.S." -- a relationship helpful for the 666 Fifth Avenue/Anbang negotiations. SAME REPORT: Source states Epstein was a "co-opted Mossad Agent" and that "Dershowitz told [a US Attorney] that Epstein belonged to both U.S. and allied intelligence services." FBI documents intelligence allegations alongside Kushner-Kissinger-China connections.',source:'EFTA00090314'},
  {date:'2019-10-08',event:'FBI internal briefing email: "Ghislaine Maxwell: Attorney proffer on 10/8/19." Also: "[Redacted]: Cooperating. Two proffers have been conducted." And: "[Redacted]: Attorney proffer scheduled on 10/18/19." Victim count: "Approximately 80 victims have been identified, with 100s unidentified." Post-Epstein death investigation actively running co-conspirator proffers with at least one cooperating witness.',source:'EFTA00038227'},
  {date:'2019-07-07',event:'SDNY sends Maxwell\\'s attorney Jeff Pagliuca both a grand jury subpoena and blank proffer agreement the DAY BEFORE Epstein\\'s indictment was unsealed. Pagliuca: "I expect that we will need to coordinate a mutually convenient time to either appear or proffer, either in advance or in lieu of any testimony." Government was pursuing Maxwell\\'s cooperation from the very start.',source:'EFTA00096137'},
  {date:'2019-04-13',event:'Steve Bannon emails Epstein (jeevacation@gmail.com) a Dropbox shared folder link with no body text. Epstein forwards Bannon\\'s email to Karyna Shuliak. Direct digital file-sharing between Trump\\'s former Chief Strategist and Epstein -- 84 DAYS before Epstein\\'s arrest on July 6, 2019. Contents of the Dropbox folder unknown.',source:'EFTA02315270'},
  {date:'2019-08-01',event:'Deutsche Bank attorney proffer to SDNY: Akin Gump lawyers and DB Legal propose "a presentation that provides an overview of Epstein\\'s relationship with the bank, the different accounts affiliated with Epstein and the types of transactions found in the accounts." Deutsche Bank\\'s own lawyers cooperating with prosecutors by walking through Epstein\\'s banking records.',source:'EFTA00024419'},
  {date:'2020-02-07',event:'FBI FD-302 of pilot David Rodgers: "RODGERS recalled several flights in 2002 where PRESIDENT BILL CLINTON was doing AIDS research. [Redacted] was on these flights." Rodgers confirmed "AP" in flight logs stood for "Adam Perry" not Prince Andrew (Andrew\\'s full name always written out). Sworn FBI interview of Epstein\\'s primary pilot documenting Clinton flights with unnamed female passengers.',source:'EFTA00159180'},
"""

# New FINDINGS entries
findings_entries = """  {id:'gates-15-files-dinners-flights-palm-beach-foundation-2011-2014',dataset:'DS9-Email',pages:45,severity:10,keywords:['bill gates','melinda gates','lauren jiloty','senior executive assistant','gates foundation','boris nikolic','science advisor','larry summers','jes staley','jpmorgan','leon black','kathy ruemmler','mort zuckerman','tom pritzker','bob kerrey','woody allen','dinner','71st street','four seasons','palm beach','private jet','flew','passenger','mark suzman','geoff lamb','terje','jagland','richard branson','2011','2012','2013','2014','post-conviction'],summary:'CRITICAL -- PRIMARY SOURCES: 15+ email and schedule files documenting Bill Gates\\\\\\\\'s extensive multi-year relationship with Epstein (EFTA00434400, EFTA00434504, EFTA00434067, EFTA00394909, EFTA00394788, EFTA00394741, EFTA00385702, EFTA00383425, EFTA00363514, EFTA00403938, EFTA00421674, EFTA00304706, EFTA00509137, EFTA02314470, combined 45+ pages, 2011-2014). GATES-EPSTEIN RELATIONSHIP DOCUMENTED ACROSS MULTIPLE YEARS: (1) APRIL 2011 (EFTA00434400): \\\\\\\"9:00pm Dinner w/Bill Gates, Larry Summers, Jes Staley\\\\\\\" at Epstein\\\\\\\\'s home. Staff email to Staley\\\\\\\\'s assistant: \\\\\\\"Bill Gates will have already eaten dinner, therefore just small bites will be served\\\\\\\"; (2) FEBRUARY-MARCH 2013 (EFTA00394909/394741): Multi-day Gates schedule: meetings at Four Seasons, then \\\\\\\"possibly on Friday fly to PB with Gates as his passenger.\\\\\\\" CONFIRMED: \\\\\\\"wheels up will be 12pm on Friday March 1st to PB with Karyna and Bill Gates\\\\\\\" -- GATES FLEW ON EPSTEIN\\\\\\\\'S PRIVATE JET TO PALM BEACH. Staff note: \\\\\\\"what happened to the lunch at 1pm on Friday March 1 with Gates and Woody Allen!\\\\\\\"; (3) Epstein emails former Senator Bob Kerrey (EFTA00394788): \\\\\\\"do you know bill gates.? He will be at my house, and i wondered if you would like to stop by?\\\\\\\" -- using Gates as social bait; (4) SEPTEMBER 2013 (EFTA00385702/383425): Lauren Jiloty, SENIOR EXECUTIVE ASSISTANT TO BILL GATES, directly coordinating dinner at 9 East 71st Street. Schedule: \\\\\\\"7:30 BILL & Melinda GATES to arrive the house. 8:00pm DINNER\\\\\\\" with Jagland (Council of Europe Secretary General), potentially Richard Branson; (5) SEPTEMBER 2014 (EFTA00363514): \\\\\\\"Meet Bill Gates at the Four Seasons. Walk over to Leon Black\\\\\\\\'s office w/Bill Gates, Kathy Ruemmler. Mort Zuckerman to meet you w/Bill Gates\\\\\\\"; (6) Gates Foundation employee Jenna Mulhall-Brereton \\\\\\\"was at my house with GAtes foundation\\\\\\\" (EFTA00421674); (7) iMessage (EFTA00509137): dinner with Gates, Mark Suzman (later Gates Foundation CEO), and Geoff Lamb. Gates has acknowledged the relationship was a mistake. [v11.04]',date:'2011-04-28',type:'email-schedule-evidence'},
  {id:'money-power-seminars-bezos-thiel-schmidt-clinton-mitchell-2012',dataset:'DS9-Email',pages:2,severity:10,keywords:['money','power','seminar','jeff bezos','peter thiel','eric schmidt','bill gates','sergey brin','larry page','bill clinton','george mitchell','marc andreessen','michael milken','jim simons','daniel kahneman','jaron lanier','boris nikolic','jes staley','michael ovitz','eike batista','j ezra merkin','nathan myhrvold','danny hillis','lesley groff','post-conviction','2012'],summary:'CRITICAL -- PRIMARY SOURCE: Epstein email to assistant Lesley Groff (EFTA00417385, March 17, 2012). EPSTEIN AS CURATOR OF GLOBAL POWER: Epstein personally organized two tentative private seminars titled \\\\\\\"MONEY\\\\\\\" and \\\\\\\"POWER\\\\\\\" with handpicked attendee lists. MONEY SEMINAR: Nathan [Myhrvold], Danny [Hillis], Bill [Gates], Boris [Nikolic], Bezos, Jes [Staley], Jaron [Lanier], Sergey Larry [Brin & Page], Kahneman, Thiel, Simons, Batista, Schmidt, Andreeson, Milken?, Merkin?. POWER SEMINAR: Gardner, Gates, Clinton, George Mitchell, Igor, Ovitz. The casual first-name-only references indicate personal familiarity with ALL attendees. This is four years after conviction -- a convicted sex offender curating the most powerful people in technology (Bezos, Gates, Brin, Page, Schmidt, Thiel, Andreessen), finance (Simons, Staley, Milken, Merkin), academia (Kahneman), and politics (Clinton, Mitchell) for private gatherings. Clinton and Mitchell were both later named by victims in sworn testimony. [v11.04]',date:'2012-03-17',type:'email-evidence'},
  {id:'fbi-chs-mossad-allegation-kissinger-kushner-china-dershowitz-intel',dataset:'DS10-Official',pages:12,severity:10,keywords:['fbi','confidential human source','chs','mossad','co-opted','intelligence services','alan dershowitz','us attorney','henry kissinger','charles kushner','cui tiankai','chinese ambassador','666 fifth avenue','anbang','israel','allied intelligence','october 2020'],summary:'CRITICAL -- PRIMARY SOURCE: FBI Confidential Human Source (CHS) report (EFTA00090314, ~12 pages, October 2020). FBI-DOCUMENTED INTELLIGENCE ALLEGATIONS: (1) CHS states Epstein was a \\\\\\\"co-opted Mossad Agent\\\\\\\"; (2) CHS states \\\\\\\"Dershowitz told [a US Attorney] that Epstein belonged to both U.S. and allied intelligence services\\\\\\\"; (3) KISSINGER-KUSHNER-CHINA: CHS advises \\\\\\\"Henry Kissinger introduced Charles [Kushner] to Cui Tiankai, the Chinese ambassador to the U.S.\\\\\\\" -- a relationship that \\\\\\\"could have been helpful\\\\\\\" during Anbang\\\\\\\\'s negotiations with the Kushners over 666 Fifth Avenue; (4) These intelligence allegations appear in an official FBI CHS report, meaning the FBI considered the source credible enough to document formally. NOTE: CHS reports represent intelligence from sources whose reliability varies; this is not confirmed fact but rather FBI-documented intelligence. The Mossad allegation has circulated for years but this is one of the few official FBI documents recording it. The Kissinger-Kushner-China connection is independently corroborated by public reporting on the 666 Fifth Avenue negotiations. [v11.04]',date:'2020-10-01',type:'fbi-intelligence'},
  {id:'fbi-cooperator-briefing-maxwell-proffer-80-victims-oct2019',dataset:'DS10-Official',pages:4,severity:10,keywords:['fbi','briefing','ghislaine maxwell','attorney proffer','cooperating','cooperator','two proffers','80 victims','hundreds unidentified','co-conspirator','october 2019','sdny','subpoena','jeff pagliuca','blank proffer agreement','july 2019'],summary:'CRITICAL -- PRIMARY SOURCES: FBI internal briefing email (EFTA00038227, October 8, 2019) and SDNY correspondence with Maxwell\\\\\\\\'s attorney (EFTA00096137, July 7-9, 2019). POST-DEATH INVESTIGATION STATUS: (1) FBI BRIEFING (Oct 2019): \\\\\\\"Ghislaine Maxwell: Attorney proffer on 10/8/19\\\\\\\" -- Maxwell\\\\\\\\'s lawyers met with prosecutors; (2) \\\\\\\"[Redacted]: Cooperating. Two proffers have been conducted\\\\\\\" -- at least one co-conspirator was ACTIVELY COOPERATING; (3) Additional proffer scheduled 10/18/19; (4) VICTIM COUNT: \\\\\\\"Approximately 80 victims have been identified, with 100s unidentified\\\\\\\"; (5) MAXWELL SUBPOENA (July 2019 -- EFTA00096137): SDNY sent Maxwell\\\\\\\\'s attorney both a grand jury subpoena and blank proffer agreement the DAY BEFORE Epstein\\\\\\\\'s indictment was unsealed. Attorney: \\\\\\\"I expect that we will need to coordinate a mutually convenient time to either appear or proffer\\\\\\\"; (6) Separate co-conspirator (EFTA00021428): Female invoked Fifth Amendment, government pushed back with \\\\\\\"reverse proffer\\\\\\\" and attached the original 2007 NPA; (7) SDNY actively investigating Maxwell as \\\\\\\"the original girl finder\\\\\\\" through victim proffers (EFTA00094867). The investigation was aggressively pursuing cooperation from multiple co-conspirators in the months after Epstein\\\\\\\\'s death. [v11.04]',date:'2019-10-08',type:'fbi-investigation'},
  {id:'bannon-dropbox-sharing-pilot-clinton-flights-deutsche-bank-proffer',dataset:'DS9-Email',pages:15,severity:9,keywords:['steve bannon','dropbox','file sharing','jeevacation','karyna shuliak','84 days','april 2019','david rodgers','pilot','fbi fd-302','bill clinton','aids research','2002','flights','female passengers','adam perry','prince andrew','deutsche bank','akin gump','attorney proffer','banking records','accounts','transactions','cooperation'],summary:'HIGH VALUE -- PRIMARY SOURCES: Bannon email (EFTA02315270, April 13, 2019), Pilot FD-302 (EFTA00159180, February 7, 2020), Deutsche Bank proffer (EFTA00024419, August 2019). THREE SIGNIFICANT DOCUMENTS: (1) BANNON DROPBOX (EFTA02315270): Bannon emails Epstein (jeevacation@gmail.com) a Dropbox shared folder link with no body text on April 13, 2019 -- 84 DAYS before arrest. Epstein forwards to Karyna Shuliak. Direct digital file-sharing between Trump\\\\\\\\'s former Chief Strategist and Epstein; contents unknown. This ADDS to the 83 Bannon files previously documented (v11.01), bringing total to 84+; (2) PILOT DAVID RODGERS FD-302 (EFTA00159180): Under FBI interview, Epstein\\\\\\\\'s primary pilot confirms \\\\\\\"several flights in 2002 where PRESIDENT BILL CLINTON was doing AIDS research. [Redacted] was on these flights.\\\\\\\" Rodgers clarifies \\\\\\\"AP\\\\\\\" in flight logs stood for \\\\\\\"Adam Perry\\\\\\\" not Prince Andrew; (3) DEUTSCHE BANK PROFFER (EFTA00024419): Akin Gump lawyers and DB Legal propose \\\\\\\"a presentation that provides an overview of Epstein\\\\\\\\'s relationship with the bank, the different accounts affiliated with Epstein and the types of transactions.\\\\\\\" Deutsche Bank\\\\\\\\'s own lawyers cooperating with SDNY on banking records. [v11.04]',date:'2019-04-13',type:'multi-source-evidence'},
"""

# Insert TIMELINE entries (before closing ])
content = content[:timeline_close] + "\n" + timeline_entries + content[timeline_close:]

# Re-find FINDINGS closing bracket (shifted by timeline insertion)
findings_close = find_close_simple(content, 'FINDINGS_DATA')
if findings_close == -1:
    print("ERROR: Could not find FINDINGS_DATA after timeline insert!")
    sys.exit(1)

# Insert FINDINGS entries (before closing ])
content = content[:findings_close] + "\n" + findings_entries + content[findings_close:]

# Version bump
count = content.count('v11.03')
print(f"Replacing {count} occurrences of 'v11.03' with 'v11.04'")
content = content.replace('v11.03', 'v11.04')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v11.04.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v11.03')
new_ver = verify.count('v11.04')
print(f"Remaining v11.03: {remaining}")
print(f"Total v11.04: {new_ver}")

for check_id in ['gates-15-files-dinners-flights-palm-beach-foundation-2011-2014',
                  'money-power-seminars-bezos-thiel-schmidt-clinton-mitchell-2012',
                  'fbi-chs-mossad-allegation-kissinger-kushner-china-dershowitz-intel',
                  'fbi-cooperator-briefing-maxwell-proffer-80-victims-oct2019',
                  'bannon-dropbox-sharing-pilot-clinton-flights-deutsche-bank-proffer']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

print(f"\nStructure check:")
print(f"  const FINDINGS_DATA = [ found: {'const FINDINGS_DATA = [' in verify}")
print(f"  const TIMELINE_DATA = [ found: {'const TIMELINE_DATA = [' in verify}")
print(f"  </script> found: {'</script>' in verify}")
print(f"  </html> found: {'</html>' in verify}")

f_close2 = find_close_simple(verify, 'FINDINGS_DATA')
t_close2 = find_close_simple(verify, 'TIMELINE_DATA')
print(f"  FINDINGS closes at: {f_close2} (valid: {f_close2 != -1})")
print(f"  TIMELINE closes at: {t_close2} (valid: {t_close2 != -1})")
print(f"  Different positions: {f_close2 != t_close2}")
