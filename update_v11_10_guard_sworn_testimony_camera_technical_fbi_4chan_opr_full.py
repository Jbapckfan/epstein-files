#!/usr/bin/env python3
"""Update dashboard with MCC guard sworn testimony (Noel prepopulated rounds, never did 30-min checks), camera technical failures (20yr analog, screens active but not recording, triple DVR failure), FBI 4chan subpoena, OPR full report details — v11.10"""
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
timeline_entries = """  {date:'2021-06-22',event:'SWORN STATEMENT -- CO TOVA NOEL (481 pages): Guard admits she PRE-FILLED round sheets at start of shift: "prepopulated that entire thing at the very beginning of your shift? ... Yes." Admits NO rounds on Aug 10: "Did you conduct any rounds on August 10th? ... No I did not." Admits she NEVER did 30-minute rounds: "I\\'ve never worked in the SHU and actually done rounds every 30 minutes." Did not know cellmate was removed. Left SHU at 10:00 PM Aug 9. Denies browsing Epstein articles at 5:42-5:52 AM. "The last person to see him alive? I would guess me." Does not recall suicide prevention training.',source:'EFTA00118226'},
  {date:'2021-07-14',event:'SWORN STATEMENT -- SHU OIC LIEUTENANT (290 pages): Posted explicit instruction: "Mandatory rounds must be conducted every 30 minutes on Epstein, as per God." And: "Make sure rounds are conducted and he has a bunkie at all times." Documented 1:50 PM Aug 9 notice that Reyes would not return: "inmate Reyes was going WAB... Epstein will be needing a cellmate upon arrival." Explains early release from suicide watch: "Because he was Epstein." Confirms policy: "if somebody comes off of suicide watch, they have to go with a cellmate until Psychology clears them."',source:'EFTA00060373'},
  {date:'2021-10-13',event:'SWORN STATEMENT -- RETIRED REGIONAL DIRECTOR (109 pages): Confirms unmonitored call: "7:00 p.m., Epstein was provided a social call by the institution duty officer." And: "This call was done on an unmonitored line." OIG assessment: "It is extremely concerning why this call would have been placed, and why it would be done on an unmonitored line." Staff knew cameras were down: "SIS Lieutenant Doctor, and the AW became aware cameras were not recording" as of August 8.',source:'EFTA00061927'},
  {date:'2021-08-04',event:'SWORN STATEMENT -- CORRECTIONAL COUNSELOR (258 pages): Reports post-incident camera admission: "yo, the cameras didn\\'t work. The cameras didn\\'t pick anything up." Describes chronic staff exhaustion: "staff would be zombies" from repeated shifts. Recounts cellmate comment during earlier incident: "His cellmate said, yo, you want to take care of this?" Says if Epstein "really wanted to commit suicide, nothing would have prevented it."',source:'EFTA00061061'},
  {date:'2021-06-16',event:'SWORN STATEMENT -- FORMER LIEUTENANT (62 pages): Reveals structural gap: "There is no nighttime SHU lieutenant scheduled at MCC." States Epstein should have been on suicide watch: "They should have put him on suicide watch until they confirmed which would be his next cellmate." Confirms 1:50 PM notice: "the institution was called at 1:50 advising that he was not coming back."',source:'EFTA00060971'},
  {date:'2019-12-23',event:'FBI FD-302s AND CAMERA TECHNICAL ANALYSIS (482 pages): Camera system described as "over 20 years old," analog, "not maintained properly." TRIPLE DVR FAILURE: "system failure of DVR 2 on July 29, 2019... motherboard failed on DVR 2 on August 8, 2019... hard drive failure occurred on August 10, 2019." Only one hard drive working. Critical detail: "screen would be active indicating that the camera was working, however, the video would not be recording." Both officers admitted "willfully and knowingly completed materially false count and round slips on August 9, 2019 and August 10, 2019." Autopsy conclusion: "cause of death was hanging and the manner of death was suicide."',source:'EFTA00131726'},
  {date:'2019-08-28',event:'FBI FD-302 -- PSYCHOLOGY REQUIREMENT VIOLATED: BOP psychologist explicitly required: "EPSTEIN must be housed with a cell mate when he returned to the SHU." This requirement was violated on Aug 9-10. Epstein stated: "I don\\'t want to be here" and "I\\'m not going to hurt myself." July 23 incident: "found in his cell with a loose noose around his neck and had been placed on Suicide Watch." Inmate Fernandez: Epstein "would be in legal from approximately 9am to 9pm."',source:'EFTA00132208'},
  {date:'2019-12-06',event:'FBI GRAND JURY SUBPOENA TO 4CHAN: FBI subpoenaed 4chan for anonymous post claiming: "after 0415 count they took him medical in a wheelchair." Also: "the trip van did NOT sign in and we did not record the plate number" and "a guy in a green dress military outfit was in the back of the van." Poster asserted: "i think they switched him out." FBI also issued grand jury subpoenas to AT&T for telecom records. The fact that FBI pursued grand jury process for an anonymous internet post suggests investigators took alternative theories seriously enough to investigate.',source:'EFTA00133349'},
  {date:'2020-11-01',event:'FULL DOJ OPR REPORT (347 pages): AUSA drafted a 60-COUNT FEDERAL INDICTMENT in May 2007, but leadership opted for state resolution instead. Palm Beach Post article circulated to USAO leadership described Epstein as having "socialized with Donald Trump, Bill Clinton and Kevin Spacey." Defense claimed prosecution was "politically motivated" due to Epstein\\'s "close personal association with former President Bill Clinton." OPR found no evidence of political influence but concluded Acosta\\'s NPA decision "constitutes poor judgment." In 2017, Trump nominated Acosta as Secretary of Labor.',source:'OPR-Report'},
  {date:'2015-08-03',event:'CVRA CASE -- NPA IMMUNITY CLAUSE TEXT: Filing contains the actual NPA immunity language: "will not institute any criminal charges against any potential co-conspirators of Epstein, including but not limited to Sarah Kellen, Adriana Ross, Lesley Groff, or Nadia Marcinkova." Victim notification letter: "You also are entitled to notification when Mr. Epstein is released." NPA sentencing: "Epstein shall be sentenced to consecutive terms of twelve (12) months and six (6) months in county jail." Acosta confirmed in USAO-SDFL leadership communications loop.',source:'EFTA00190318'},
"""

# New FINDINGS entries
findings_entries = """  {id:'guard-sworn-testimony-noel-prepopulated-rounds-never-30min-oic-bunkie-mandate-regional-director-unmonitored-call',dataset:'DS10-Official',pages:1500,severity:10,keywords:['sworn statement','tova noel','prepopulated','round sheets','no rounds','august 10','never','30 minutes','shu','cellmate','removed','5:42','internet','last person alive','oic lieutenant','mandatory rounds','as per god','bunkie','at all times','1:50 pm','reyes','because he was epstein','suicide watch','regional director','unmonitored','social call','extremely concerning','cameras not recording','sis lieutenant doctor','august 8','correctional counselor','cameras didnt work','zombies','exhaustion','want to take care of this','former lieutenant','no nighttime shu lieutenant','should have been on suicide watch'],summary:'CRITICAL -- PRIMARY SOURCES: Eight OIG sworn statements from MCC staff (EFTA00118226, EFTA00060373, EFTA00060822, EFTA00060876, EFTA00060971, EFTA00061061, EFTA00061698, EFTA00061927; combined 1,500+ pages, June-October 2021). THE GUARDS\\\\\\\\\\\\\\' OWN WORDS: (1) CO TOVA NOEL: \\\\\\\\\\\\\\\"prepopulated that entire thing at the very beginning of your shift? ... Yes.\\\\\\\\\\\\\\\" \\\\\\\\\\\\\\\"Did you conduct any rounds on August 10th? ... No I did not.\\\\\\\\\\\\\\\" \\\\\\\\\\\\\\\"I\\\\\\\\\\\\\\\\'ve never worked in the SHU and actually done rounds every 30 minutes.\\\\\\\\\\\\\\\" \\\\\\\\\\\\\\\"The last person to see him alive? I would guess me.\\\\\\\\\\\\\\\"; (2) SHU OIC: \\\\\\\\\\\\\\\"Mandatory rounds must be conducted every 30 minutes on Epstein, as per God.\\\\\\\\\\\\\\\" Posted bunkie requirement. 1:50 PM Aug 9 notice cellmate not returning. Early suicide-watch release: \\\\\\\\\\\\\\\"Because he was Epstein\\\\\\\\\\\\\\\"; (3) RETIRED REGIONAL DIRECTOR: Unmonitored call confirmed: \\\\\\\\\\\\\\\"This call was done on an unmonitored line.\\\\\\\\\\\\\\\" OIG: \\\\\\\\\\\\\\\"It is extremely concerning.\\\\\\\\\\\\\\\" Staff knew cameras not recording as of Aug 8; (4) COUNSELOR: \\\\\\\\\\\\\\\"yo, the cameras didn\\\\\\\\\\\\\\\\'t work. The cameras didn\\\\\\\\\\\\\\\\'t pick anything up.\\\\\\\\\\\\\\\" Staff \\\\\\\\\\\\\\\"would be zombies\\\\\\\\\\\\\\\"; (5) FORMER LIEUTENANT: \\\\\\\\\\\\\\\"There is no nighttime SHU lieutenant scheduled at MCC.\\\\\\\\\\\\\\\" \\\\\\\\\\\\\\\"They should have put him on suicide watch until they confirmed which would be his next cellmate.\\\\\\\\\\\\\\\" [v11.10]',date:'2021-06-22',type:'sworn-testimony'},
  {id:'camera-technical-triple-dvr-failure-20yr-analog-screens-active-not-recording-fbi-4chan-subpoena-opr-60count',dataset:'DS10-Official',pages:1100,severity:10,keywords:['camera','dvr','20 years old','analog','not maintained','system failure','july 29','motherboard','august 8','hard drive','august 10','one hard drive','screen active','not recording','willfully','knowingly','materially false','count slips','round slips','4chan','subpoena','grand jury','wheelchair','trip van','switched him out','att','telecom','opr','60 count','indictment','may 2007','socialized','donald trump','bill clinton','kevin spacey','politically motivated','poor judgment','acosta','secretary of labor','npa','co-conspirators','sarah kellen','adriana ross','lesley groff','nadia marcinkova'],summary:'CRITICAL -- PRIMARY SOURCES: FBI FD-302s/camera analysis (EFTA00131726, 482 pages), FBI psychology notes (EFTA00132208, 476 pages), FBI grand jury subfile (EFTA00133349, 274 pages), DOJ OPR Report (347 pages), CVRA filing (EFTA00190318, 446 pages). CAMERA SYSTEM AND INVESTIGATION DETAILS: (1) TRIPLE DVR FAILURE: Camera system \\\\\\\\\\\\\\\"over 20 years old,\\\\\\\\\\\\\\\" analog, \\\\\\\\\\\\\\\"not maintained properly.\\\\\\\\\\\\\\\" DVR 2 failure July 29, motherboard failure Aug 8, hard drive failure Aug 10. \\\\\\\\\\\\\\\"Screen would be active indicating that the camera was working, however, the video would not be recording\\\\\\\\\\\\\\\"; (2) PSYCHOLOGY VIOLATED: BOP psychologist required \\\\\\\\\\\\\\\"EPSTEIN must be housed with a cell mate when he returned to the SHU\\\\\\\\\\\\\\\" -- violated Aug 9-10; (3) FBI SUBPOENAED 4CHAN: Anonymous post claimed wheelchair transfer and \\\\\\\\\\\\\\\"i think they switched him out\\\\\\\\\\\\\\\" -- FBI pursued with grand jury subpoenas to 4chan and AT&T; (4) OPR: 60-count federal indictment drafted May 2007 but never filed. Epstein \\\\\\\\\\\\\\\"socialized with Donald Trump, Bill Clinton and Kevin Spacey\\\\\\\\\\\\\\\" (Palm Beach Post). Defense claimed \\\\\\\\\\\\\\\"politically motivated\\\\\\\\\\\\\\\"; (5) NPA IMMUNITY: \\\\\\\\\\\\\\\"will not institute any criminal charges against any potential co-conspirators of Epstein, including but not limited to Sarah Kellen, Adriana Ross, Lesley Groff, or Nadia Marcinkova.\\\\\\\\\\\\\\\" [v11.10]',date:'2019-12-23',type:'fbi-investigation'},
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
count = content.count('v11.09')
print(f"Replacing {count} occurrences of 'v11.09' with 'v11.10'")
content = content.replace('v11.09', 'v11.10')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v11.10.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v11.09')
new_ver = verify.count('v11.10')
print(f"Remaining v11.09: {remaining}")
print(f"Total v11.10: {new_ver}")

for check_id in ['guard-sworn-testimony-noel-prepopulated-rounds-never-30min-oic-bunkie-mandate-regional-director-unmonitored-call',
                  'camera-technical-triple-dvr-failure-20yr-analog-screens-active-not-recording-fbi-4chan-subpoena-opr-60count']:
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
