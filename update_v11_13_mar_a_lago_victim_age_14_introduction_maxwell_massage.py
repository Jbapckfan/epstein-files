#!/usr/bin/env python3
"""Update dashboard with Mar-a-Lago victim statements, Trump introduction at age 14, Maxwell Mar-a-Lago massage — v11.13"""
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
timeline_entries = """  {date:'2019-08-27',event:'SDNY HEARING -- VICTIM STATEMENT: MAR-A-LAGO AT AGE 16 (121 pages): After Epstein\\'s death, victim tells federal court: \"Mar-a-Lago, just before I was 17, I thought I was given a big.\" This places a minor victim at Trump\\'s private club in direct connection with the Epstein trafficking operation. Court proceeding before Judge Richard M. Berman discusses case dismissal following Epstein\\'s death.',source:'EFTA00019994'},
  {date:'2016-06-20',event:'COURT EXHIBIT -- EPSTEIN INTRODUCED VICTIM TO TRUMP AT AGE 14: Media article filed as court exhibit states: \"The court papers also claim Epstein introduced her to President Trump when she was 14 years old, allegedly elbowing Trump and saying, This is a good one, right?\" This allegation -- that Epstein presented a 14-year-old to Trump with approval-seeking language -- appears in civil court filings.',source:'EFTA00084366'},
  {date:'2002-07-01',event:'CHAUFFEUR TESTIMONY -- MAXWELL DRIVEN TO MAR-A-LAGO FOR MASSAGE (190 pages): Witness describes \"summer of 2002 when he drove Maxwell to Mar-a-Lago and waited for her to receive a massage.\" This places Ghislaine Maxwell at Trump\\'s private club receiving services, establishing a direct operational connection between Maxwell\\'s activities and the Mar-a-Lago property. Filed alongside sealed indictment charging Epstein with sex trafficking of minors.',source:'EFTA02731082'},
"""

# New FINDINGS entry
findings_entries = """  {id:'mar-a-lago-victim-age-14-introduction-maxwell-massage-trump-property-connection',dataset:'DS10-Official',pages:500,severity:10,keywords:['mar-a-lago','victim','age 14','before I was 17','introduced','trump','this is a good one right','elbowing','maxwell','massage','chauffeur','drove','summer of 2002','sex trafficking of minors','sealed indictment','judge berman','sdny hearing','court exhibit'],summary:'CRITICAL -- PRIMARY SOURCES: SDNY hearing transcript (EFTA00019994, 121 pages), court exhibit media article (EFTA00084366, 115 pages), sealed indictment filing with chauffeur testimony (EFTA02731082, 190 pages). MAR-A-LAGO AS TRAFFICKING NEXUS: (1) VICTIM AT MAR-A-LAGO AGE 16: Victim tells federal court after Epstein\\\\\\\\\\\\\\\\'s death: \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"Mar-a-Lago, just before I was 17, I thought I was given a big\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\" -- minor victim at Trump\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'s private club; (2) INTRODUCED TO TRUMP AT 14: Court exhibit states Epstein \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"introduced her to President Trump when she was 14 years old, allegedly elbowing Trump and saying, This is a good one, right?\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\" -- Epstein presenting underage victim to Trump with approval language; (3) MAXWELL AT MAR-A-LAGO: Chauffeur drove Maxwell to Mar-a-Lago \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"summer of 2002\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\" for a massage -- Maxwell operational presence at Trump property. These three sources establish Mar-a-Lago as a location where underage victims were present, where Epstein introduced minors to Trump, and where Maxwell conducted activities. [v11.13]',date:'2019-08-27',type:'victim-statement'},
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
count = content.count('v11.12')
print(f"Replacing {count} occurrences of 'v11.12' with 'v11.13'")
content = content.replace('v11.12', 'v11.13')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v11.13.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v11.12')
new_ver = verify.count('v11.13')
print(f"Remaining v11.12: {remaining}")
print(f"Total v11.13: {new_ver}")

for check_id in ['mar-a-lago-victim-age-14-introduction-maxwell-massage-trump-property-connection']:
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
