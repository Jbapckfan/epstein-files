#!/usr/bin/env python3
"""Update dashboard with OIG Report, MCC death-night logs, BOP incident reports, psych reconstruction, falsified records, camera failure — v11.09"""
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
timeline_entries = """  {date:'2023-06-01',event:'OIG MEMORANDUM 23-085 -- OFFICIAL INVESTIGATION OF EPSTEIN\\'S DEATH: Inspector General finds BOP staff "did not conduct any 30-minute rounds after about 10:40 p.m. on August 9." Count slips and round sheets were "FALSIFIED to show that they had been performed." Video evidence: "only available from one prison security camera due to a malfunction" — DVR recording failure began JULY 29, eleven days before death, meaning half the cameras were not recording. Epstein "was not assigned a new cellmate" after transfer on August 9. An "unrecorded, unmonitored telephone call" was allowed that evening. Two MCC employees Noel and Thomas charged criminally with falsifying BOP records.',source:'OIG-23-085'},
  {date:'2019-08-10',event:'BOP INCIDENT REPORTS -- DEATH TIMELINE: 6:33 AM body alarm activated in SHU, "Staff found inmate Epstein unresponsive in cell Z06-220 CPR in progress." 6:35 AM 911 notified. 6:43 AM EMS arrives. 7:10 AM EMS departs to Beekman Hospital. 7:36 AM "Inmate Epstein was pronounced deceased." BOP memo notes "circumficial bruising around the neck." MCC warden instructed: "I instructed the escorting staff not to speak to anyone and or the media."',source:'EFTA00049963'},
  {date:'2019-08-09',event:'SUICIDE TIMELINE -- MINUTE-BY-MINUTE FINAL DAY: 8:00 AM cellmate Efrain Reyes departs for court. 8:30 AM Epstein arrives in Attorney Conference room. 6:45 PM Epstein returns to SHU. 7:00 PM "inmate Epstein provided a social call by IDO" — this is the unrecorded, unmonitored call flagged by OIG. No replacement cellmate assigned. After 10:40 PM, no rounds conducted. Epstein reportedly "was in good spirits, nothing unusual" in final observation.',source:'EFTA00045963'},
  {date:'2019-10-04',event:'PSYCHOLOGICAL RECONSTRUCTION REPORT: Documents anomaly — Epstein told staff he was "calling his mother" despite her being DECEASED. Cellmate Nicholas Tartaglione "had attempted to kill him." Funds were deposited to "cellmate\\'s (inmate Reyes) commissary account for unknown reasons." Staff "did not complete proper 30-minute rounds at 3:00 a.m. or 5:00 a.m." Leslie Wexner identified as "Mr. Epstein\\'s sole client" who "granted him power of attorney over his affairs."',source:'EFTA00041963'},
  {date:'2019-07-24',event:'EPSTEIN PSYCHOLOGY ASSESSMENT: Psych note records Epstein "explicitly denied recent and current suicidal ideation, planning, and intent." Direct quote: "I have no interest in killing myself." Risk factors listed: "High Profile Crime, Lack of family connections, Sex offender status." Physical findings: "Mr. EPSTEIN has a significant scar around his neck, which is now scabbing over." He was "fearful for his safety" if returned to previous cellmate.',source:'EFTA00048963'},
  {date:'2019-07-23',event:'FIRST INCIDENT -- ROPE AROUND NECK: BOP TRUINTEL log entry records staff observing Epstein with a "handmade orange rope wound [around] neck" at 05:14 AM. Separate medical assessment: "inmate Epstein was found in his cell with a rope around his neck." Suicide watch initiated. FBI medical notes (EFTA00132684, 498 pages) document resuscitation steps on Aug 10 including CPR, epinephrine, intubation. Staff memo acknowledges: "we did not complete the 3am nor 5am rounds."',source:'EFTA00120887'},
  {date:'2019-07-29',event:'DVR RECORDING FAILURE BEGINS: OIG investigation determines that the DVR system recording SHU camera footage malfunctioned starting July 29, 2019 — ELEVEN DAYS before Epstein\\'s death. This meant half the cameras in the SHU were not recording. By August 9-10, "recorded video evidence... only available from one prison security camera." The cell door was NOT in its field of view. This is the basis for the WIRED report that "Metadata Shows the FBI\\'s Raw Jeffrey Epstein Prison Video Was Likely Modified."',source:'OIG-23-085'},
  {date:'2019-08-09',event:'CELLMATE REMOVED -- NO REPLACEMENT: USMS notified MCC of cellmate transfer on August 8. On August 9, Efrain Reyes departed for court and was not returned. Despite BOP policy requiring cellmates for at-risk inmates, "Epstein was not assigned a new cellmate." The previous cellmate, Nicholas Tartaglione (a former police officer charged with quadruple murder), had allegedly "attempted to kill" Epstein during the July 23 incident. Epstein was left alone in his cell for the final night.',source:'OIG-23-085'},
  {date:'2015-02-11',event:'CVRA LITIGATION -- TRUMP DEPOSITION NOTICE: Bradley Edwards filed notice to take the "deposition of Donald Trump" based on phone messages, press quotes, and Mar-a-Lago connections. Filing references the "Holy Grail" journal list and explicitly names Donald Trump among listed individuals. The filing alleges "Trump allegedly banned Epstein" from Mar-a-Lago due to an underage assault allegation. Alfredo Rodriguez attempted to sell the journal for $50,000; witness tampering pressure documented in 2007 plea negotiations.',source:'EFTA00188608'},
"""

# New FINDINGS entries
findings_entries = """  {id:'oig-memorandum-23-085-death-investigation-falsified-records-camera-failure-cellmate-removed',dataset:'DS10-Official',pages:128,severity:10,keywords:['oig','inspector general','memorandum 23-085','bop','mcc new york','special housing unit','shu','falsified','count slips','round sheets','30-minute rounds','10:40 pm','camera','dvr','malfunction','july 29','one camera','cellmate','not assigned','unrecorded','unmonitored','telephone call','noel','thomas','criminally charged','august 9','august 10','suicide watch','july 23','excess linens','warden','reassigned'],summary:'CRITICAL -- PRIMARY SOURCE: DOJ Office of Inspector General Memorandum 23-085 (June 2023, 128 pages). THE AUTHORITATIVE DEATH INVESTIGATION: (1) FALSIFIED RECORDS: \\\\\\\\\\\\\\\"Count slips and round sheets were falsified to show that they had been performed\\\\\\\\\\\\\\\" -- staff Noel and Thomas criminally charged; (2) NO ROUNDS: \\\\\\\\\\\\\\\"did not conduct any 30-minute rounds after about 10:40 p.m. on August 9\\\\\\\\\\\\\\\"; (3) CAMERA FAILURE: DVR malfunction began JULY 29 -- eleven days before death. \\\\\\\\\\\\\\\"Recorded video evidence for August 9 and 10... only available from one prison security camera due to a malfunction.\\\\\\\\\\\\\\\" Cell door NOT in camera\\\\\\\\\\\\\\\\'s field of view; (4) CELLMATE REMOVED: \\\\\\\\\\\\\\\"Epstein was not assigned a new cellmate\\\\\\\\\\\\\\\" after Aug 9 transfer despite BOP policy; (5) UNRECORDED CALL: \\\\\\\\\\\\\\\"an unrecorded, unmonitored telephone call\\\\\\\\\\\\\\\" allowed on August 9 evening; (6) Warden reassigned, two staff on administrative leave. This is the single most authoritative government document on the circumstances of Epstein\\\\\\\\\\\\\\\\'s death and the cascade of failures that made it possible. [v11.09]',date:'2023-06-01',type:'oig-investigation'},
  {id:'death-night-timeline-bop-incident-reports-mcc-logs-psych-reconstruction-bruising-deceased-mother',dataset:'DS10-Official',pages:500,severity:10,keywords:['death night','august 10','august 9','6:33 am','body alarm','unresponsive','cell z06-220','cpr','6:43','ems','7:10','7:36','pronounced deceased','circumficial bruising','neck','do not speak','media','suicide timeline','reyes','cellmate','attorney conference','social call','good spirits','calling his mother','deceased','tartaglione','attempted to kill','commissary account','unknown reasons','3am','5am','rounds','missed','orange rope','05:14','scabbing','no interest in killing myself','fearful for safety','high profile crime'],summary:'CRITICAL -- PRIMARY SOURCES: BOP Form 583 Incident Reports (EFTA00049963), Suicide Timeline (EFTA00045963), Psychological Reconstruction (EFTA00041963), Psychology Assessment (EFTA00048963), TRUINTEL SHU logs (EFTA00120887), FBI Medical Notes (EFTA00132684, 498 pages), Daily Lieutenant\\\\\\\\\\\\\\\\'s Logs (EFTA00052963). THE DEATH-NIGHT RECONSTRUCTION: (1) FINAL DAY: Cellmate Reyes departed 8:00 AM Aug 9; Epstein in attorney conference 8:30 AM; returned SHU 6:45 PM; social call 7:00 PM (unrecorded per OIG); no rounds after 10:40 PM; (2) DISCOVERY: 6:33 AM body alarm, \\\\\\\\\\\\\\\"found unresponsive in cell Z06-220 CPR in progress\\\\\\\\\\\\\\\"; 6:43 EMS; 7:10 transport; 7:36 \\\\\\\\\\\\\\\"pronounced deceased\\\\\\\\\\\\\\\"; (3) PHYSICAL: \\\\\\\\\\\\\\\"circumficial bruising around the neck\\\\\\\\\\\\\\\"; (4) COVERUP INDICATORS: Staff instructed \\\\\\\\\\\\\\\"not to speak to anyone and or the media\\\\\\\\\\\\\\\"; count slips falsified; (5) ANOMALIES: Epstein told staff he was \\\\\\\\\\\\\\\"calling his mother\\\\\\\\\\\\\\\" -- she was deceased; funds deposited to cellmate\\\\\\\\\\\\\\\\'s commissary \\\\\\\\\\\\\\\"for unknown reasons\\\\\\\\\\\\\\\"; Tartaglione \\\\\\\\\\\\\\\"had attempted to kill him\\\\\\\\\\\\\\\"; (6) DENIALS: \\\\\\\\\\\\\\\"I have no interest in killing myself\\\\\\\\\\\\\\\" -- explicit denial 16 days before death; \\\\\\\\\\\\\\\"fearful for his safety\\\\\\\\\\\\\\\"; (7) FIRST INCIDENT: July 23, \\\\\\\\\\\\\\\"handmade orange rope wound around neck\\\\\\\\\\\\\\\" at 5:14 AM; (8) DVR FAILURE: Camera system malfunctioned from July 29 -- only one camera recording by death night, cell door not visible. [v11.09]',date:'2019-08-10',type:'death-investigation'},
  {id:'cvra-litigation-trump-deposition-notice-holy-grail-journal-mar-a-lago-witness-tampering',dataset:'DS10-Official',pages:389,severity:9,keywords:['cvra','crime victims rights act','trump','deposition','donald trump','bradley edwards','mar-a-lago','holy grail','journal','alfredo rodriguez','$50000','witness tampering','2007','plea negotiations','alan dershowitz','bill clinton','mark epstein','roy black','acosta','maria villafafia','ban','underage'],summary:'SIGNIFICANT -- PRIMARY SOURCE: CVRA litigation filings and exhibits (EFTA00188608, 389 pages, February 11, 2015). TRUMP DEPOSITION AND MAR-A-LAGO: (1) DEPOSITION NOTICE: Attorney Bradley Edwards filed notice to take the \\\\\\\\\\\\\\\"deposition of Donald Trump\\\\\\\\\\\\\\\" based on phone messages, press quotes, and Mar-a-Lago connections; (2) HOLY GRAIL JOURNAL: Filing references the \\\\\\\\\\\\\\\"Holy Grail\\\\\\\\\\\\\\\" journal list that \\\\\\\\\\\\\\\"explicitly names Donald Trump among listed individuals\\\\\\\\\\\\\\\"; (3) MAR-A-LAGO BAN: \\\\\\\\\\\\\\\"Trump allegedly banned Epstein\\\\\\\\\\\\\\\" from Mar-a-Lago due to an underage assault allegation; (4) RODRIGUEZ ATTEMPTED SALE: Alfredo Rodriguez attempted to sell the journal for $50,000; (5) WITNESS TAMPERING: Pressure documented during 2007 plea negotiations. Also names Dershowitz, Clinton, Mark Epstein. [v11.09]',date:'2015-02-11',type:'court-filing'},
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
count = content.count('v11.08')
print(f"Replacing {count} occurrences of 'v11.08' with 'v11.09'")
content = content.replace('v11.08', 'v11.09')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v11.09.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v11.08')
new_ver = verify.count('v11.09')
print(f"Remaining v11.08: {remaining}")
print(f"Total v11.09: {new_ver}")

for check_id in ['oig-memorandum-23-085-death-investigation-falsified-records-camera-failure-cellmate-removed',
                  'death-night-timeline-bop-incident-reports-mcc-logs-psych-reconstruction-bruising-deceased-mother',
                  'cvra-litigation-trump-deposition-notice-holy-grail-journal-mar-a-lago-witness-tampering']:
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
