import sys

filepath = '/tmp/epstein-files-update/dashboard_v10_latest.html'

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

# Find closing positions
findings_close = find_array_closing(content, 'FINDINGS_DATA')
timeline_close = find_array_closing(content, 'TIMELINE_DATA')

print(f"FINDINGS_DATA closing ']' at position: {findings_close}")
print(f"TIMELINE_DATA closing ']' at position: {timeline_close}")

if findings_close == -1 or timeline_close == -1:
    print("ERROR: Could not find one or both array closings!")
    sys.exit(1)

# Verify timeline_close > findings_close (timeline is later in file)
assert timeline_close > findings_close, "Expected TIMELINE_DATA closing to be after FINDINGS_DATA closing"

# New TIMELINE_DATA entries
timeline_entries = """  {date:'2020-04-03',event:'US DOJ sends formal MLAT request to UK Central Authority requesting interview of Prince Andrew regarding Epstein and Peter Nygard investigations. Requests voluntary or compelled interview under oath. 20+ detailed questions prepared.',source:'EFTA00087994'},
  {date:'2002-09-01',event:'Epstein Africa trip: President Clinton, Kevin Spacey, Chris Tucker, Ronald Burkle, Rodney Slater, Ghislaine Maxwell, ~4 young women on Boeing 727. Doctor witnesses Epstein grab buttocks, bedroom door incident. 10 days, 7 countries.',source:'EFTA00086866'},
  {date:'2020-07-02',event:'Maxwell bodyguard Martin Jackson interviewed the day of arrest. Kevin Maxwell arranged ex-British Army security. Maxwell hiding in Bradford NH since Christmas 2019. Scott Borgerson visited regularly.',source:'EFTA00089381'},
  {date:'1991-07-01',event:'David Rogers begins as Epstein pilot (salary $165K). Provided 2004-2005 passenger manifests via Grand Jury Subpoena. Boeing 727 and Gulfstream. "Too many to count" females aged 21-23.',source:'EFTA00087610'},
"""

# New FINDINGS_DATA entries
findings_entries = """  {id:'mlat-uk-prince-andrew-interview',dataset:'DS9-DOJ',pages:22,severity:10,keywords:['prince andrew','nygard','maxwell','doj','mlat','uk'],summary:'CRITICAL: US DOJ Criminal Division MLAT request to UK (April 3, 2020) formally requesting interview of Prince Andrew regarding TWO investigations: (1) Epstein — "evidence that Prince Andrew engaged in sexual conduct involving one of Epstein victims" and "documentary evidence suggesting Prince Andrew had knowledge that Maxwell recruited females." (2) Peter Nygard sex trafficking — Andrew visited Nygard Cay. Requests voluntary interview; if declined, COMPELLED interview under oath. 20+ detailed questions on visits to Palm Beach, Little St. James, 9 E 71st St, Zorro Ranch, females under 18 observed, sexual encounters, payments, evidence destruction. Proffer agreement template signed by Geoffrey Berman, US Attorney SDNY. [v10.43]',date:'2020-04-03',type:'legal-filing'},
  {id:'fd302-africa-trip-doctor-manifest',dataset:'DS9-FD302',pages:2,severity:10,keywords:['bill clinton','kevin spacey','chris tucker','burkle','maxwell','slater'],summary:'CRITICAL: Emergency physician FD-302 (hired by Secret Service for Clinton Africa trip, Sept 2002). FULL PASSENGER MANIFEST on Epstein Boeing 727: PRESIDENT BILL CLINTON, KEVIN SPACEY, CHRIS TUCKER, RONALD BURKLE, CASEY WASSERMAN, RODNEY SLATER (Sec of Transportation), GHISLAINE MAXWELL, ~4 young women aged 20-22. Witnessed someone shut bedroom door — "very obvious she did not want him to see what was going on." Witnessed EPSTEIN "grab and rub buttocks." Spacey gave "awkward" hugs. 10 days, 7 countries. [v10.43]',date:'2002-09-01',type:'fbi-interview'},
  {id:'fd302-laura-newman-ballet-prince-andrew',dataset:'DS9-FD302',pages:2,severity:8,keywords:['prince andrew','brunel','marcinko','kellen','newman'],summary:'HIGH: Laura Newman FD-302 — met Epstein at 17 after ballet class at "Steps on Broadway." Met PRINCE ANDREW and a brunette at Epstein house. Sessions escalated from workouts to sexual acts. Met JEAN-LUC BRUNEL, NADIA MARCINKO, SARAH KELLEN. Abuse began at age 17. [v10.43]',date:'2020-12-15',type:'fbi-interview'},
  {id:'attorney-proffer-beverly-hills-faith-kates',dataset:'DS9-DOJ',pages:11,severity:8,keywords:['maxwell','brunel','faith kates','next model','smith barney','eva dubin'],summary:'HIGH: Detailed attorney proffer (Jan 2020). Victim recruited April 2004. Confirms Epstein said "MAXWELL was the original girl finder." FAITH KATES (Next Model Management) — Epstein asked "when she was going to find a girl." BRUNEL owned Karin Modeling then MC2. Victim placed at NEXT Model Management and SMITH BARNEY through Epstein. Directed to hotel rooms for Epstein "friends" every 3 months. FBI came to Brunel apartments late 2006 re: scared underage Brazilian models. 16-point manipulation tactics breakdown. [v10.43]',date:'2020-01-03',type:'legal-filing'},
  {id:'fd302-maxwell-bodyguard-arrest-day',dataset:'DS9-FD302',pages:3,severity:7,keywords:['maxwell','kevin maxwell','borgerson','british army','bradford'],summary:'FD-302 of Maxwell bodyguard Martin Jackson — interviewed THE DAY of Maxwell arrest (Jul 2, 2020). KEVIN MAXWELL (brother) arranged ex-British Army security. Maxwell hiding in Bradford NH since Christmas 2019 to "hide from the press." SCOTT BORGERSON visited multiple times. Paid $350/day. Jackson fully aware of allegations when taking assignment. [v10.43]',date:'2020-07-02',type:'fbi-interview'},
  {id:'fd302-david-rogers-pilot-manifests',dataset:'DS9-FD302',pages:3,severity:7,keywords:['rogers','pilot','manifests','boeing 727','gulfstream'],summary:'David Rogers pilot FD-302 (Aug 2006 Palm Beach investigation). Epstein pilot since July 1991, salary $165K. Provided 2004-2005 passenger manifests via Grand Jury subpoena. Boeing 727 (N908JE) and Gulfstream (N909JE). Complete employee/associate phone list. "Too many to count" females aged 21-23. Historical document from original investigation. [v10.43]',date:'2006-08-15',type:'fbi-interview'},
"""

# STEP 1: Insert TIMELINE entries first (higher position in file)
# Insert before the closing ] of TIMELINE_DATA
content = content[:timeline_close] + "\n" + timeline_entries + content[timeline_close:]

# STEP 2: Insert FINDINGS entries (lower position, unaffected by step 1)
# findings_close position is still valid since we inserted AFTER it
content = content[:findings_close] + "\n" + findings_entries + content[findings_close:]

# STEP 3: Replace all v10.42 with v10.43
count = content.count('v10.42')
print(f"Replacing {count} occurrences of 'v10.42' with 'v10.43'")
content = content.replace('v10.42', 'v10.43')

# Write back
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: File updated.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining_v1042 = verify.count('v10.42')
new_v1043 = verify.count('v10.43')
print(f"Remaining v10.42 occurrences: {remaining_v1042}")
print(f"Total v10.43 occurrences: {new_v1043}")

# Verify new entries exist
for check_id in ['mlat-uk-prince-andrew-interview', 'fd302-africa-trip-doctor-manifest', 'fd302-laura-newman-ballet-prince-andrew', 'attorney-proffer-beverly-hills-faith-kates', 'fd302-maxwell-bodyguard-arrest-day', 'fd302-david-rogers-pilot-manifests']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

for check_src in ['EFTA00087994', 'EFTA00086866', 'EFTA00089381', 'EFTA00087610']:
    if check_src in verify:
        print(f"  FOUND timeline source: {check_src}")
    else:
        print(f"  MISSING timeline source: {check_src}")

# Verify arrays still parse (basic bracket check)
f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
