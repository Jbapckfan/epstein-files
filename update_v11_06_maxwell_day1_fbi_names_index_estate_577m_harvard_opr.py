#!/usr/bin/env python3
"""Update dashboard with Maxwell proffer Day 1, FBI internal names index, estate $577M, Harvard donation brokering, OPR 60-count indictment, work release fraud — v11.06"""
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
timeline_entries = """  {date:'2025-07-24',event:'MAXWELL PROFFER DAY 1 (Todd Blanche, DAG): On Trump: "President Trump was always very cordial and very kind to me." "I never witnessed the President in any inappropriate setting in any way." "Did you ever observe President Trump receive a massage?" -- "Never." "Did you ever hear Epstein say Trump had done anything inappropriate?" -- "Absolutely never, in any context." Met Trump ~1990 through her father Robert Maxwell who "liked him very much." Last saw Trump in person "mid 2000s" in "social setting."',source:'PROFFER_transcript_day1_cft'},
  {date:'2025-07-24',event:'MAXWELL PROFFER DAY 1: On Epstein\\'s death: "I do not believe he died by suicide, no." Does NOT believe he was killed by an outsider: "If it is indeed murder, I believe it was an internal situation." On intelligence: "Bullshit" that Epstein was connected to CIA/DIA. On Mossad: "Not deliberately" when asked if she had contact. Her father Robert Maxwell "was a British intelligence officer" in WWII and "once you\\'ve been an intelligence officer, you\\'re kind of always." On blackmail: "I never heard that. I never saw it and I never imagined it." Claims NO hidden cameras in any property.',source:'PROFFER_transcript_day1_cft'},
  {date:'2025-07-24',event:'MAXWELL PROFFER DAY 1: On Wexner: Client #1. "Epstein restructured The Limited, restructured his entire personal finances, handled all investment strategy" down to "contracts for household maids." On Leon Black: "Same as what he did for Wexner." On Jes Staley: "heavily involved with Highbridge Capital and the financing or selling of Highbridge to JP Morgan." On Eva Dubin: Epstein\\'s actual girlfriend of ~10 years before Maxwell. "She was his best friend and his everything." On Glenn Dubin: Client, became one after marrying Eva.',source:'PROFFER_transcript_day1_cft'},
  {date:'2025-07-24',event:'MAXWELL PROFFER DAY 1: On Lynn Forester de Rothschild: Epstein "helped her financially. She\\'ll deny it and she has, but she -- she can\\'t." Believes Forester introduced Epstein to BOTH Prince Andrew and Dershowitz at Martha\\'s Vineyard. On "finding masseuses": Admitted Epstein asked her starting 1992-93. She would visit spas, find masseuses, ask if they did home visits. "I never, ever checked their age and I never checked their credentials." On Prince Andrew photo: "Literally a fake photo." On Epstein\\'s "stolen money" business: he showed her "a photograph that he had with some African warlords."',source:'PROFFER_transcript_day1_cft'},
  {date:'2025-07-22',event:'FBI INTERNAL NAMES INDEX: FBI email listing all "positive case hits" in the Epstein file, with highlighted names containing "salacious information." Key entry: DONALD TRUMP -- "one identified victim claimed abuse by Trump but ultimately refused to cooperate." Also listed: Prince Andrew, Jes Staley, Leon Black, Glenn Dubin, Harvey Weinstein, Bill Clinton, Alan Dershowitz, David Copperfield, Les Wexner, Jean-Luc Brunel, Naomi Campbell, Chris Tucker, Larry Summers, Kevin Spacey, Bill Gates. NO hits for: Adnan Khashoggi, Reid Hoffman, Piers Morgan.',source:'EFTA00161528'},
  {date:'2019-08-08',event:'EPSTEIN\\'S ESTATE: Total value $577,672,654. Breakdown: $56.5M cash, $127M fixed income/equity, $195M hedge funds/PE, $18.5M planes/boats/cars. Properties: NYC brownstone $56M, NM ranch $72M, Palm Beach $12M, Paris $8M, Great St. James + Little St. James $86M combined. TWO DAYS before death, Epstein changed his will and created "The 1953 Trust." Executors: Darren Indyke and Richard Kahn ($250K each). BORIS NIKOLIC (Bill Gates\\' science advisor) listed as alternate executor.',source:'EFTA00104216'},
  {date:'2011-09-01',event:'Epstein personally brokered a $2,000,000 donation from Leon Black to Harvard\\'s Program for Evolutionary Dynamics (PED), run by Professor Martin Nowak. Draft letter prepared by Nowak, directed to Harvard\\'s Recording Secretary, forwarded through Epstein\\'s assistant Lesley Groff to Black. Direct primary source evidence of Epstein using his relationship with Black to funnel money into his scientific network.',source:'EFTA00428494'},
  {date:'2002-09-01',event:'FBI FD-302 of Secret Service-contracted doctor on Clinton Africa trip via Epstein\\'s plane: Passengers included Clinton, staffers, Secret Service, Kevin Spacey, Chris Tucker, Ronald Burkle, Casey Wasserman, Rodney Slater, Ghislaine Maxwell, and "about four young women aged 20 to 22." Doctor witnessed "Epstein grab and rub [a woman\\'s] buttocks" and saw a woman "shut the door to the bedroom abruptly" not wanting him to see what was inside.',source:'EFTA00086866'},
  {date:'2015-01-01',event:'Reid Hoffman brought Epstein to Palo Alto for dinner with Mark Zuckerberg, Elon Musk, and Peter Thiel -- SEVEN YEARS after Epstein\\'s sex offender conviction. Separately, Epstein in 2014 claimed to have arranged donations to MIT from Bill Gates ($2M) and Leon Black. MIT Goodwin Procter report: Epstein donated $850K total to MIT ($100K to Marvin Minsky\\'s lab, $525K to Media Lab, $225K to Seth Lloyd). Seth Lloyd received $60K personally from Epstein deposited into his personal account.',source:'EFTA00105378'},
  {date:'2018-12-06',event:'FBI DISCOVERY -- WEXNER/LIMITED LINK: FBI discovered Epstein\\'s sex offender registration phone number was linked to "THE LIMITED EXE" at 11 Saint Marks Place, New York -- a Wexner/Limited company address. Thousands of records at this address showed "individuals with foreign passports entering the country and putting that address as their destination address. Ages for those individuals is a wide range from teenagers to adults." FBI opened investigation same month after Miami Herald series.',source:'EFTA00152144'},
  {date:'2008-12-01',event:'WORK RELEASE FRAUD: US Attorney letter to Palm Beach Sheriff exposed multiple frauds in Epstein\\'s work release application. The "Florida Science Foundation" was created on the EVE of incarceration; its phone number was actually his law firm\\'s; IRS returns showed Epstein worked ONE HOUR PER WEEK for no compensation; yet he claimed $250,000 salary. His W-2 was actually from Financial Trust Company, Inc. in the US Virgin Islands at $180,785.62. Despite this, Epstein was granted 12 hours/day work release 6 days/week.',source:'EFTA00224439'},
  {date:'2006-06-01',event:'DOJ OPR REPORT: Federal prosecutors drafted a 60-COUNT INDICTMENT against Epstein but it was NEVER FILED. Instead, the investigation was resolved through the NPA. OPR found Acosta\\'s "view of the federal interest in prosecuting Epstein was too narrow." The drafted indictment would have charged Epstein with multiple counts of sex trafficking -- significantly more serious than the single state charge he ultimately pleaded to.',source:'MEMO_2020.11_DOJ_OPR_Report'},
  {date:'2019-07-25',event:'FBI and SDNY met with attorneys for Les Wexner and Abigail Wexner (Debevoise). Attorney proffer: "the Wexners were not close with Epstein and had no knowledge of his sexual misconduct. They further advised that they severed ties with Epstein in 2007 after discovering that Epstein had stolen hundreds of thousands of dollars from them while managing their finances." Wexner served Grand Jury subpoena alongside Maxwell, Kellen, Groff, Brunel, and pilots.',source:'EFTA00174356'},
"""

# New FINDINGS entries
findings_entries = """  {id:'maxwell-proffer-day1-trump-gentleman-death-not-suicide-intelligence-wexner',dataset:'DS10-Official',pages:95,severity:10,keywords:['ghislaine maxwell','proffer','day 1','todd blanche','deputy attorney general','trump','cordial','gentleman','never inappropriate','never massage','absolutely never','robert maxwell','intelligence officer','british intelligence','wwii','mossad','not deliberately','bullshit','cia','dia','death','not suicide','internal situation','no cameras','no blackmail','wexner','client number one','restructured the limited','leon black','jes staley','highbridge','eva dubin','glenn dubin','lynn forester','rothschild','martha vineyard','prince andrew','fake photo','finding masseuses','never checked age','african warlords','stolen money','massage game','habit','july 2025'],summary:'CRITICAL -- PRIMARY SOURCE: Ghislaine Maxwell proffer transcript Day 1 (PROFFER_transcript_day1_cft, July 24, 2025). MAXWELL\\\\\\\\'S COMPREHENSIVE STATEMENTS: (1) ON TRUMP: \\\\\\\"President Trump was always very cordial and very kind to me.\\\\\\\" \\\\\\\"Never\\\\\\\" observed Trump receive a massage. \\\\\\\"Absolutely never\\\\\\\" heard Epstein say Trump did anything inappropriate. Met Trump ~1990 through her father; (2) ON EPSTEIN\\\\\\\\'S DEATH: \\\\\\\"I do not believe he died by suicide.\\\\\\\" If murder, \\\\\\\"I believe it was an internal situation\\\\\\\"; (3) ON INTELLIGENCE: \\\\\\\"Bullshit\\\\\\\" re CIA/DIA connections. On Mossad contact: \\\\\\\"Not deliberately.\\\\\\\" Her father was \\\\\\\"a British intelligence officer\\\\\\\" and \\\\\\\"once you\\\\\\\\'ve been an intelligence officer, you\\\\\\\\'re kind of always\\\\\\\"; (4) ON BLACKMAIL: \\\\\\\"I never heard that. I never saw it.\\\\\\\" Claims NO hidden cameras; (5) WEXNER: Client #1, restructured The Limited and all personal finances; (6) LEON BLACK: \\\\\\\"Same as what he did for Wexner\\\\\\\"; (7) JES STALEY: Involved in Highbridge Capital sale to JP Morgan; (8) LYNN FORESTER: Epstein \\\\\\\"helped her financially. She\\\\\\\\'ll deny it but she can\\\\\\\\'t\\\\\\\"; Maxwell believes Forester introduced Epstein to BOTH Andrew and Dershowitz; (9) FINDING MASSEUSES: Admitted Epstein asked her starting 1992-93. \\\\\\\"I never, ever checked their age\\\\\\\"; (10) PRINCE ANDREW PHOTO: \\\\\\\"Literally a fake photo\\\\\\\"; (11) EPSTEIN\\\\\\\\'S MONEY: Early business was \\\\\\\"finding stolen money,\\\\\\\" showed her \\\\\\\"a photograph with some African warlords.\\\\\\\" [v11.06]',date:'2025-07-24',type:'proffer-transcript'},
  {id:'fbi-names-index-trump-victim-refused-cooperate-salacious-jul2025',dataset:'DS10-Official',pages:4,severity:10,keywords:['fbi','internal','names index','positive case hits','salacious information','donald trump','one identified victim','claimed abuse','refused to cooperate','prince andrew','jes staley','leon black','glenn dubin','harvey weinstein','bill clinton','alan dershowitz','david copperfield','les wexner','jean-luc brunel','naomi campbell','chris tucker','larry summers','kevin spacey','bill gates','no hits','reid hoffman','piers morgan','july 2025'],summary:'CRITICAL -- PRIMARY SOURCE: FBI internal email listing all \\\\\\\"positive case hits\\\\\\\" in the Epstein file (EFTA00161528, July 22, 2025). FBI NAMES INDEX WITH SALACIOUS FLAGS: The FBI compiled a list of all names with \\\\\\\"salacious information\\\\\\\" in the Epstein files. KEY ENTRY -- DONALD TRUMP: \\\\\\\"one identified victim claimed abuse by Trump but ultimately refused to cooperate.\\\\\\\" Also flagged: Prince Andrew, Jes Staley, Leon Black, Glenn Dubin, Harvey Weinstein, Bill Clinton, Alan Dershowitz, David Copperfield, Les Wexner, Jean-Luc Brunel, Naomi Campbell, Chris Tucker, Larry Summers, Kevin Spacey, Bill Gates. Names with NO hits in the file: Adnan Khashoggi, Reid Hoffman, Piers Morgan. This is the FBI\\\\\\\\'s own internal assessment of which names carry investigative significance in the Epstein case. The Trump entry documents that a specific victim made an allegation but declined to pursue it. [v11.06]',date:'2025-07-22',type:'fbi-internal'},
  {id:'estate-577m-1953-trust-nikolic-executor-opr-60-count-indictment',dataset:'DS11-Financial',pages:200,severity:10,keywords:['estate','$577 million','$56.5 million cash','$127 million','$195 million','hedge funds','nyc brownstone $56m','nm ranch $72m','palm beach $12m','paris $8m','little st james','great st james','$86 million','1953 trust','two days before death','darren indyke','richard kahn','boris nikolic','alternate executor','bill gates','science advisor','opr','office of professional responsibility','60 count indictment','never filed','acosta','too narrow','federal interest'],summary:'CRITICAL -- PRIMARY SOURCES: USVI Complaint (EFTA00104216, 48 pages), DOJ OPR Report (MEMO_2020.11, ~150 pages). EPSTEIN\\\\\\\\'S FINANCIAL EMPIRE AND PROSECUTORIAL FAILURE: (1) ESTATE VALUED AT $577,672,654: $56.5M cash, $127M fixed income/equity, $195M hedge funds/PE, $18.5M planes/boats/cars. Properties: NYC $56M, NM $72M, Palm Beach $12M, Paris $8M, islands $86M combined; (2) THE 1953 TRUST: Created TWO DAYS before death (August 8, 2019). Executors: Darren Indyke and Richard Kahn ($250K each). BORIS NIKOLIC -- Bill Gates\\\\\\' former science advisor -- listed as ALTERNATE EXECUTOR; (3) DOJ OPR REPORT: Federal prosecutors drafted a 60-COUNT INDICTMENT against Epstein that was NEVER FILED. Investigation resolved through NPA instead. OPR found Acosta\\\\\\\\'s \\\\\\\"view of the federal interest in prosecuting Epstein was too narrow\\\\\\\"; (4) WORK RELEASE FRAUD (EFTA00224439): \\\\\\\"Florida Science Foundation\\\\\\\" created on eve of incarceration; phone number was his law firm\\\\\\\\'s; IRS showed ONE HOUR per week; W-2 was from Financial Trust Company USVI at $180,785; yet granted 12 hours/day work release 6 days/week; (5) WEXNER PROFFER (EFTA00174356): Wexner\\\\\\\\'s lawyers claimed \\\\\\\"Epstein had stolen hundreds of thousands of dollars\\\\\\\" (SDNY internal memo says \\\\\\\"several hundred million\\\\\\\"). Wexner served Grand Jury subpoena. [v11.06]',date:'2019-08-08',type:'financial-legal-evidence'},
  {id:'harvard-mit-scientific-patronage-black-2m-hoffman-palo-alto-dinner',dataset:'DS9-Email',pages:30,severity:9,keywords:['harvard','program for evolutionary dynamics','martin nowak','leon black','$2 million','donation','lesley groff','mit','media lab','$850000','marvin minsky','seth lloyd','$60000','personal account','reid hoffman','palo alto','dinner','mark zuckerberg','elon musk','peter thiel','2015','seven years','post-conviction','steven pinker','intellectual impostor','murray gell-mann','stephen hawking','frank wilczek','oliver sacks','eugenics','seed human race','dna','new mexico ranch'],summary:'HIGH VALUE -- PRIMARY SOURCES: Epstein email brokering Black donation (EFTA00428494, Sept 2011), MIT Goodwin Procter report via news clips (EFTA00105378, Jan 2020), Harvard program reporting (EFTA00018466). EPSTEIN\\\\\\\\'S ACADEMIC INFILTRATION: (1) LEON BLACK $2M TO HARVARD: Epstein personally brokered a $2,000,000 donation from Leon Black to Harvard\\\\\\\\'s Program for Evolutionary Dynamics (PED), run by Martin Nowak. Draft letter prepared by Nowak, forwarded through Groff to Black; (2) MIT: Epstein donated $850K total ($100K to Minsky, $525K to Media Lab, $225K to Seth Lloyd). Lloyd received $60K PERSONALLY from Epstein deposited into his personal account. Epstein visited MIT campus 9 times after 2013; (3) REID HOFFMAN DINNER (2015): Hoffman brought Epstein to Palo Alto for dinner with Zuckerberg, Musk, and Thiel -- SEVEN YEARS after conviction; (4) HARVARD: Epstein\\\\\\\\'s $6.5M donation created PED. Cultivated Nobel laureates Gell-Mann, Hawking, Wilczek; scientists Gould, Sacks, Pinker (who called Epstein an \\\\\\\"intellectual impostor\\\\\\\"). Epstein planned to \\\\\\\"seed the human race with his DNA\\\\\\\" via women at his NM ranch; (5) Clinton Africa trip doctor FD-302 (EFTA00086866): \\\\\\\"about four young women aged 20 to 22\\\\\\\" on plane; doctor saw Epstein \\\\\\\"grab and rub buttocks\\\\\\\" and woman \\\\\\\"shut the door to the bedroom abruptly.\\\\\\\" [v11.06]',date:'2015-01-01',type:'multi-source-evidence'},
  {id:'wexner-limited-sex-offender-registration-foreign-passports-teenagers',dataset:'DS10-Official',pages:8,severity:9,keywords:['les wexner','the limited','sex offender','registration','phone number','11 saint marks place','foreign passports','destination address','teenagers','adults','entering the country','fbi','december 2018','miami herald','investigation','stolen','hundreds of thousands','several hundred million','grand jury subpoena','debevoise'],summary:'HIGH VALUE -- PRIMARY SOURCE: FBI investigative email chain (EFTA00152144, December 2018). FBI DISCOVERY OF WEXNER/LIMITED CONNECTION: (1) FBI discovered Epstein\\\\\\\\'s sex offender registration phone number was linked to \\\\\\\"THE LIMITED EXE\\\\\\\" at 11 Saint Marks Place -- a Wexner/Limited company address; (2) Thousands of records at this address showed \\\\\\\"individuals with foreign passports entering the country and putting that address as their destination address. Ages for those individuals is a wide range from TEENAGERS to adults\\\\\\\"; (3) This discovery was made in December 2018 when FBI opened the investigation after the Miami Herald series; (4) The Limited connection persisted despite Wexner\\\\\\\\'s later claims of severing ties in 2007; (5) Wexner\\\\\\\\'s attorney proffer (EFTA00174356): claimed Epstein \\\\\\\"stolen hundreds of thousands\\\\\\\" but SDNY internal memo (EFTA02731082) says Wexner learned Epstein \\\\\\\"had stolen or otherwise misappropriated several hundred MILLION dollars.\\\\\\\" Epstein returned $100M in January 2008; (6) Wexner served Grand Jury subpoena alongside Maxwell, Kellen, Groff, Brunel, and pilots. [v11.06]',date:'2018-12-06',type:'fbi-investigation'},
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
count = content.count('v11.05')
print(f"Replacing {count} occurrences of 'v11.05' with 'v11.06'")
content = content.replace('v11.05', 'v11.06')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v11.06.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v11.05')
new_ver = verify.count('v11.06')
print(f"Remaining v11.05: {remaining}")
print(f"Total v11.06: {new_ver}")

for check_id in ['maxwell-proffer-day1-trump-gentleman-death-not-suicide-intelligence-wexner',
                  'fbi-names-index-trump-victim-refused-cooperate-salacious-jul2025',
                  'estate-577m-1953-trust-nikolic-executor-opr-60-count-indictment',
                  'harvard-mit-scientific-patronage-black-2m-hoffman-palo-alto-dinner',
                  'wexner-limited-sex-offender-registration-foreign-passports-teenagers']:
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
