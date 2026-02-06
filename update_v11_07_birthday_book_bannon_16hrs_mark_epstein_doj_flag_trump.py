#!/usr/bin/env python3
"""Update dashboard with Trump birthday book, Bannon 16hrs tape, Mark Epstein FBI interview, DOJ flag Trump records, prison video modified, 12yo French girls — v11.07"""
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
timeline_entries = """  {date:'2025-09-08',event:'WSJ REVEALS TRUMP BIRTHDAY BOOK LETTER: Epstein\\'s estate turned over a professionally bound 50th birthday book to House Oversight Committee. It contained a letter bearing TRUMP\\'S SIGNATURE -- typewritten text "framed by the outline of a naked woman," ending with "Happy Birthday -- and may every day be another wonderful secret," with "Donald" signed in a style mimicking pubic hair. Separate letter from Joel Pashcow included a MOCK $22,500 CHECK suggesting Epstein "sold" a woman to Trump. Book listed Donald Trump and Bill Clinton under the "Friends" section.',source:'EFTA00163802'},
  {date:'2025-09-08',event:'BIRTHDAY BOOK CONTENTS: Other letters included Les Wexner\\'s brief note with a suggestive drawing, Alan Dershowitz\\'s mock "Vanity Unfair" magazine cover, Leon Black\\'s rhymed poem signed "Love and kisses, Leon." House Speaker Mike Johnson initially claimed Trump had been "an FBI informant to try and take this stuff down" regarding Epstein, before walking back the statement. Trump now calls the matter the "Democrat Epstein Hoax."',source:'EFTA00163802'},
  {date:'2025-07-08',event:'DOJ ABOUT-FACE ON EPSTEIN FILES: Trump\\'s Justice Department concluded there was no evidence to support conspiracy theories about Epstein\\'s death or clientele. Conservative influencers from Laura Loomer to Elon Musk criticized AG Bondi and Director Patel. Patel had previously told Benny Johnson that Congress was blocking the list "because of who\\'s on that list," asking "you don\\'t think Bill Gates is lobbying Congress night and day to prevent the disclosure of that list?" Tom Fitton told Steve Bannon: "I don\\'t even think the Biden administration would have written anything like this."',source:'EFTA00163550'},
  {date:'2025-07-01',event:'CONGRESSIONAL LETTER TO AG BONDI: DOJ/FBI released an UNSIGNED MEMORANDUM with two findings: (1) no incriminating "client list" and (2) Epstein committed suicide. OVERSIGHT DISCOVERY: DOJ personnel were instructed to "FLAG" any records in which President Trump was mentioned during their Epstein file review. Letter demands: "Why were personnel told to flag records in which President Trump was mentioned?" and "Please list all political appointees and senior DOJ officials involved." References WIRED report: "Metadata Shows the FBI\\'s Raw Jeffrey Epstein Prison Video Was Likely Modified."',source:'EFTA00173350'},
  {date:'2020-01-01',event:'MARK EPSTEIN FBI INTERVIEW: Jeffrey\\'s brother states "Steve Bannon has 16 HOURS OF VIDEO TAPE." Mark contacted Bannon after seeing tape his brother sent him after his death. Bannon told Mark the tape "should protect him" and invoked "attorney/client privilege, as witnessed preparation. But Bannon is not an attorney." MARK SUSPECTS TRUMP: "I think Trump is behind it. If someone was closer on the inside told me Trump [indiscernible], after his death." Also: "personally, I think Trump was jealous that people [indiscernible], and wanted to take that power." On why they stopped being friends: "He stopped hanging out with Trump when he realized Trump was a dick. That\\'s exactly what he said."',source:'EFTA00113482'},
  {date:'2011-03-17',event:'FBI FD-302 VICTIM INTERVIEW (12 pages): Victim began working at TRUMP\\'S MAR-A-LAGO CLUB circa 1998-1999. Was "approached by Ghislaine Maxwell at Mar-a-Lago" while reading anatomy/massage book; Maxwell offered $200/hr. Jean-Luc Brunel "would bring girls to Epstein -- many had poor English language skills and appeared to be very young...estimated some were as young as 16." MOST SHOCKING: "An unknown individual sent Epstein THREE 12-YEAR-OLD GIRLS FROM FRANCE as a birthday gift."',source:'EFTA00269967'},
  {date:'2011-03-17',event:'FBI FD-302 VICTIM INTERVIEW (continued): Victim provided erotic massage to LESLIE WEXNER in New York; described Wexner as "a creep." PRINCE ANDREW PUPPET INCIDENT: Maxwell purchased a puppet resembling Prince Andrew; "the puppet\\'s hand was placed on one of the girls\\' breasts and then Prince Andrew mimicked the puppet by placing his hand on another female\\'s breast." Manhattan residence had a SURVEILLANCE ROOM displaying APPROXIMATELY 50 CAMERAS. Victim met Bill Clinton and Al Gore at Epstein\\'s island (did not engage in sexual activity with either).',source:'EFTA00269967'},
  {date:'2019-08-15',event:'AG BARR after FBI/NYPD raided Epstein\\'s private island: "Any co-conspirators should not rest easy. The victims deserve justice and they will get it." Barr said the criminal investigation into any possible co-conspirators would continue. Despite this public statement, only Ghislaine Maxwell was ever charged. All other named and unnamed co-conspirators protected by the NPA or never prosecuted.',source:'EFTA00095847'},
"""

# New FINDINGS entries
findings_entries = """  {id:'trump-birthday-book-naked-woman-mock-check-doj-flag-records-jul2025',dataset:'DS10-Official',pages:25,severity:10,keywords:['trump','birthday book','50th birthday','naked woman','signature','donald','happy birthday','wonderful secret','joel pashcow','mock check','$22500','sold','friends section','bill clinton','les wexner','alan dershowitz','vanity unfair','leon black','love and kisses','mike johnson','fbi informant','walked back','democrat epstein hoax','house oversight','doj','flag','records','political appointees','wired','metadata','prison video','modified','bondi','patel','client list','no evidence','suicide','laura loomer','elon musk','tom fitton','bannon','biden administration','september 2025','july 2025'],summary:'CRITICAL -- PRIMARY SOURCES: FBI Daily Brief (EFTA00163802, September 8, 2025), Congressional letter to AG Bondi (EFTA00173350, July 2025), DOJ scramble report (EFTA00163550, July 8, 2025). THE BIRTHDAY BOOK AND DOJ COVER-UP ALLEGATIONS: (1) TRUMP BIRTHDAY LETTER: Epstein\\\\\\\\'s estate turned over professionally bound 50th birthday book to House Oversight. Trump\\\\\\\\'s letter: typewritten text \\\\\\\"framed by the outline of a naked woman,\\\\\\\" ending \\\\\\\"Happy Birthday -- and may every day be another wonderful secret,\\\\\\\" with \\\\\\\"Donald\\\\\\\" signed mimicking pubic hair. MOCK CHECK from Joel Pashcow: $22,500 suggesting Epstein \\\\\\\"sold\\\\\\\" a woman to Trump. Clinton and Trump listed under \\\\\\\"Friends\\\\\\\"; (2) DOJ FLAGGING TRUMP RECORDS: Congressional oversight discovered DOJ personnel instructed to \\\\\\\"FLAG\\\\\\\" records mentioning Trump. Congress demands: \\\\\\\"Why were personnel told to flag records in which President Trump was mentioned?\\\\\\\"; (3) PRISON VIDEO MODIFIED: WIRED reported \\\\\\\"Metadata Shows the FBI\\\\\\\\'s Raw Jeffrey Epstein Prison Video Was Likely Modified\\\\\\\"; (4) DOJ ABOUT-FACE: Bondi/Patel concluded no client list exists and suicide confirmed, despite Patel previously claiming Gates was \\\\\\\"lobbying Congress night and day\\\\\\\" to prevent disclosure. Tom Fitton to Bannon: \\\\\\\"I don\\\\\\\\'t even think the Biden administration would have written anything like this\\\\\\\"; (5) Speaker Johnson initially claimed Trump was \\\\\\\"an FBI informant\\\\\\\" against Epstein, then walked it back. [v11.07]',date:'2025-09-08',type:'congressional-oversight'},
  {id:'mark-epstein-fbi-interview-bannon-16hrs-tape-trump-behind-it',dataset:'DS10-Official',pages:50,severity:10,keywords:['mark epstein','fbi interview','steve bannon','16 hours','video tape','after his death','attorney client privilege','not an attorney','trump behind it','jealous','wanted to take that power','trump was a dick','stopped hanging out','insider','contacted bannon'],summary:'CRITICAL -- PRIMARY SOURCE: Mark Epstein (Jeffrey\\\\\\\\'s brother) FBI interview transcript (EFTA00113482, ~50 pages). BANNON\\\\\\\\'S 16 HOURS OF TAPE AND MARK\\\\\\\\'S SUSPICIONS: (1) BANNON\\\\\\\\'S TAPES: Mark states \\\\\\\"Steve Bannon has 16 hours of video tape.\\\\\\\" After Jeffrey\\\\\\\\'s death, Jeffrey had sent Mark a tape, and Mark \\\\\\\"contacted Steve Bannon.\\\\\\\" Bannon told Mark the tape \\\\\\\"should protect him\\\\\\\" and invoked \\\\\\\"attorney/client privilege, as witnessed preparation\\\\\\\" -- but Mark notes \\\\\\\"Bannon is not an attorney\\\\\\\"; (2) MARK SUSPECTS TRUMP: \\\\\\\"I think Trump is behind it. If someone was closer on the inside told me Trump [indiscernible], after his death.\\\\\\\" Also: \\\\\\\"personally, I think Trump was jealous that people [indiscernible], and wanted to take that power\\\\\\\"; (3) ON WHY THEY STOPPED BEING FRIENDS: \\\\\\\"He stopped hanging out with Trump when he realized Trump was a dick. That\\\\\\\\'s exactly what he said\\\\\\\"; (4) Separately, in a videotaped interview WITH Steve Bannon, Epstein differentiated between \\\\\\\"different kinds of power -- such as Bill Clinton\\\\\\\\'s political power, wrestlers\\\\\\' and weight lifters\\\\\\' physical power\\\\\\\" (EFTA00075792). This establishes Bannon possessed extensive Epstein video material and that Jeffrey\\\\\\\\'s own brother suspected Trump in connection with the death. [v11.07]',date:'2020-01-01',type:'fbi-interview'},
  {id:'fbi-fd302-mar-a-lago-12yo-french-girls-50-cameras-wexner-creep-andrew-puppet',dataset:'DS10-Official',pages:12,severity:10,keywords:['fbi','fd-302','victim interview','mar-a-lago','trump','ghislaine maxwell','approached','anatomy book','$200 per hour','jean-luc brunel','poor english','young','16','three 12-year-old girls','france','birthday gift','les wexner','creep','erotic massage','prince andrew','puppet','breast','50 cameras','surveillance room','manhattan','bill clinton','al gore','island','2011','1998','1999'],summary:'CRITICAL -- PRIMARY SOURCE: FBI FD-302 victim interview (EFTA00269967, 12 pages, March 17, 2011). THE MOST DETAILED SINGLE VICTIM ACCOUNT: (1) MAR-A-LAGO RECRUITMENT: Victim working at \\\\\\\"Trump\\\\\\\\'s Mar-a-Lago Club\\\\\\\" circa 1998-1999, \\\\\\\"approached by Ghislaine Maxwell\\\\\\\" while reading an anatomy/massage book. Maxwell offered $200/hour; (2) BRUNEL\\\\\\\\'S GIRLS: Jean-Luc Brunel \\\\\\\"would bring girls to Epstein -- many had poor English language skills and appeared to be very young...estimated some were as young as 16\\\\\\\"; (3) THREE 12-YEAR-OLD FRENCH GIRLS: \\\\\\\"An unknown individual sent Epstein three 12-year-old girls from France as a birthday gift\\\\\\\" -- the most disturbing single detail in the entire document collection; (4) WEXNER AS \\\\\\\"CREEP\\\\\\\": Victim provided erotic massage to Leslie Wexner in New York, described Wexner as \\\\\\\"a creep\\\\\\\"; (5) PRINCE ANDREW PUPPET: Maxwell purchased puppet resembling Andrew; \\\\\\\"the puppet\\\\\\\\'s hand was placed on one of the girls\\\\\\' breasts and then Prince Andrew mimicked the puppet by placing his hand on another female\\\\\\\\'s breast\\\\\\\"; (6) 50-CAMERA SURVEILLANCE: Manhattan residence had \\\\\\\"a surveillance room displaying approximately 50 cameras\\\\\\\" -- contradicting Maxwell\\\\\\\\'s claim of no hidden cameras and the FBI case summary\\\\\\\\'s finding of no cameras in bedrooms; (7) Victim met Clinton and Al Gore at island but denies sexual activity with either. [v11.07]',date:'2011-03-17',type:'fbi-victim-interview'},
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
count = content.count('v11.06')
print(f"Replacing {count} occurrences of 'v11.06' with 'v11.07'")
content = content.replace('v11.06', 'v11.07')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v11.07.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v11.06')
new_ver = verify.count('v11.07')
print(f"Remaining v11.06: {remaining}")
print(f"Total v11.07: {new_ver}")

for check_id in ['trump-birthday-book-naked-woman-mock-check-doj-flag-records-jul2025',
                  'mark-epstein-fbi-interview-bannon-16hrs-tape-trump-behind-it',
                  'fbi-fd302-mar-a-lago-12yo-french-girls-50-cameras-wexner-creep-andrew-puppet']:
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
