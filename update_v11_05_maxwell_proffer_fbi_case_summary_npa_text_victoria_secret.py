#!/usr/bin/env python3
"""Update dashboard with Maxwell proffer transcript, FBI case initiation summary, NPA co-conspirator immunity text, Victoria's Secret modeling book, Deutsche Bank consent order — v11.05"""
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
timeline_entries = """  {date:'2025-07-25',event:'MAXWELL PROFFER DAY 2 (Todd Blanche, DAG): On Clinton and the island: "He never. Absolutely never went. And I can be sure of that because there\\'s no way he would\\'ve gone to the island, had I not been there." But: "Without me, I don\\'t think there would\\'ve been those flights, because I was the one who asked Epstein to provide the plane." On $30M in payments (1999-2007): "That is categorically false" that it was for recruiting. On Wexner: "Wexner was, in my opinion, his closest friend." On Mar-a-Lago recruiting: "in the realms of possibility, it could have, but I have no memory of it." On Epstein: "He\\'s a disgusting guy who did terrible things to young kids."',source:'PROFFER_transcript_day2'},
  {date:'2025-07-25',event:'MAXWELL PROFFER DAY 2: On RFK Jr.: "Bobby knew Mr. Epstein." Went on "dinosaur bone hunting in the Dakotas" trip with Epstein and Bobby Kennedy (~1993-1994). On Elon Musk: met at Sergey Brin\\'s birthday on Jean Pigozzi\\'s island; "in discovery, they were communicating on email." On Prince Andrew photo: "The fake, just to be..." On Clinton Global Initiative: Maxwell was "part of the beginning process." Said she suggested Clinton "should have his own Davos." On the famous photo of Andrew with victim: "The idea of him doing anything of that nature in my house...is so mind-blowingly not conceivable to me."',source:'PROFFER_transcript_day2'},
  {date:'2019-07-29',event:'FBI CASE SUMMARY: Epstein\\'s own attorneys "in very general terms, discussed the possibility of a resolution of the case, and the possibility of the defendant\\'s cooperation." SDNY told them to come back with a specific proposal. EPSTEIN DIED 12 DAYS LATER on August 10, 2019. Had Epstein cooperated, he would have had information on numerous powerful individuals documented throughout the EFTA files.',source:'EFTA00174356'},
  {date:'2019-10-01',event:'FBI CASE SUMMARY: An adult victim described being directed by Epstein to massage Leon Black, who "initiated sexual contact" (victim fled). Same victim described Jes Staley, who "forced her to touch his genitals and raped her." Manhattan DA began looking into Leon Black based on this victim\\'s account. Separate finding: "No other victim described being directed by either Epstein or Maxwell to engage in sexual activity with any other men" except one asked to massage Harvey Weinstein.',source:'EFTA00174356'},
  {date:'2019-11-26',event:'FBI CASE SUMMARY: Sarah Kellen (Epstein\\'s personal assistant/"lieutenant") conducted proffer sessions with SDNY on 11/26/2019 and 12/4/2019. Kellen\\'s lawyers "provided details about evidence destruction at Epstein\\'s direction" and characterized her relationship with Epstein as "sexually abusive" -- positioning her as victim rather than co-conspirator. Post-death investigation focused on "Ghislaine Maxwell, Sarah Kellen, [redacted], and Lesley Groff."',source:'EFTA00174356'},
  {date:'2007-09-24',event:'THE ACTUAL NPA TEXT: "the United States also agrees that it will not institute any criminal charges against any potential co-conspirators of Epstein, including but not limited to Sarah Kellen, Adriana Ross, Lesley Groff, or Nadia Martinkova." Also: "the parties anticipate that this agreement will not be made part of any public record." Signed by R. Alexander Acosta. This single clause immunized an unknown number of co-conspirators and was kept secret from victims.',source:'EFTA00040089'},
  {date:'1996-08-29',event:'FBI NOTICE OF CLAIM: A victim reported Epstein and Maxwell to the FBI on August 29, 1996, telling the FBI "she believed that they were operating a pedophile ring and producing child pornography." Maxwell "put together what she called a \\'modeling book\\' containing photographs of young girls and boys in various stages of undress. Maxwell kept the \\'modeling book\\' in Epstein\\'s safe." Maxwell said "the \\'modeling book\\' was used to recruit models for Victoria Secret which was one of the businesses of Les Wexner." THE FBI TOOK NO ACTION FOR NEARLY 25 YEARS.',source:'EFTA00143419'},
  {date:'2013-08-19',event:'DEUTSCHE BANK CONSENT ORDER (NY DFS): Deutsche Bank opened brokerage accounts for Southern Trust Company Inc. and Southern Financial LLC. Over the relationship, Epstein opened MORE THAN 40 ACCOUNTS. Bank classified Epstein as "Honorary PEP" (Politically Exposed Person). ATTORNEY-1 withdrew over $800,000 IN CASH from Epstein\\'s accounts over four years, asking "how often they could come in to withdraw cash without creating some sort of alert." Before branch closed, ATTORNEY-1 withdrew $100,000 in a single cash transaction.',source:'EFTA00151495'},
  {date:'2017-03-01',event:'DEUTSCHE BANK CONSENT ORDER: Internal email about "payments to a Russian model and Russian publicity agent" -- transaction monitoring team stated: "Once this type of activity is normal for this client it is not deemed suspicious." Separate inquiry about "payments to the accounts of women with Eastern European surnames at a Russian bank" -- explanation: "SENT TO A FRIEND FOR TUITION FOR SCHOOL." Press reports noted Epstein\\'s modeling agency "brought \\'young girls...often from Eastern Europe\\' to the U.S. on Mr. Epstein\\'s private jets."',source:'EFTA00151495'},
  {date:'2009-12-01',event:'ALFREDO RODRIGUEZ FBI INTERVIEW: Epstein\\'s butler describes the black book, explaining he came into possession of it during his employment (2004-2005). Rodriguez describes "photographs of naked underage girls arranged in collages" displayed in Epstein\\'s home. Also: "JEAN LUC BRUNEL would also bring girls to the house and would sometimes arrange for girls to be flown in via commercial and private planes." Rodriguez was later convicted of obstruction for attempting to sell the black book.',source:'EFTA00108668'},
  {date:'2019-09-01',event:'SDNY INTERNAL FINANCIAL ANALYSIS: "he was getting a huge chunk of money from Wexner (and possibly others like Black, Dubin, etc.) in the 90s and early 00s and then basically living off the income from his own investments after his first arrest." Payments identified to: Ehud Barak, Bruce Moskowitz (Mar-a-Lago member running the VA), Noam Chomsky, Woody Allen, and "more than 25 women who appear to be Eastern European models." SDNY concluded: "None of the payments...appear to have any connection to criminal activity."',source:'EFTA00105304'},
  {date:'2019-01-01',event:'DOJ OPR EXECUTIVE SUMMARY on Acosta/NPA: "the government also immunized from prosecution Epstein\\'s co-conspirators and concealed from Epstein\\'s victims the terms of the NPA." Finding: "OPR concludes that Acosta\\'s decision to resolve the federal investigation through the NPA constitutes poor judgment" but NOT "professional misconduct." Acosta\\'s "view of the federal interest in prosecuting Epstein was too narrow."',source:'EFTA00011475'},
"""

# New FINDINGS entries
findings_entries = """  {id:'maxwell-proffer-july2025-clinton-island-wexner-rfk-musk-andrew',dataset:'DS10-Official',pages:85,severity:10,keywords:['ghislaine maxwell','proffer','todd blanche','deputy attorney general','david markus','spencer horn','fbi','clinton','island','never','absolutely never','plane','flights','without me','$30 million','$18.3 million','categorically false','wexner','closest friend','rfk','bobby kennedy','dinosaur bone','dakotas','elon musk','sergey brin','pigozzi','discovery','email','prince andrew','fake','mar-a-lago','recruiting','realms of possibility','disgusting guy','terrible things','young kids','sarah ferguson','chris tucker','kevin spacey','naomi campbell','larry summers','george soros','richard branson','clinton global initiative','davos','july 2025'],summary:'CRITICAL -- PRIMARY SOURCE: Ghislaine Maxwell proffer transcript Day 2 (PROFFER_transcript_day2, July 25, 2025, certified by Cathy M. Ayotte). MAXWELL UNDER OATH WITH DAG TODD BLANCHE: (1) CLINTON AND ISLAND: \\\\\\\"He never. Absolutely never went\\\\\\\" to the island. But: \\\\\\\"Without me, I don\\\\\\\\'t think there would\\\\\\\\'ve been those flights, because I was the one who asked Epstein to provide the plane\\\\\\\"; (2) $30 MILLION PAYMENTS ($18.3M in 1999, $5M in 2002, $7.4M in 2007): \\\\\\\"That is categorically false\\\\\\\" that payments were for recruiting; (3) WEXNER: \\\\\\\"Wexner was, in my opinion, his closest friend\\\\\\\" -- Wexner \\\\\\\"didn\\\\\\\\'t want to be seen too much with me because of my family problems\\\\\\\"; (4) RFK JR: \\\\\\\"Bobby knew Mr. Epstein.\\\\\\\" Went on \\\\\\\"dinosaur bone hunting in the Dakotas\\\\\\\" trip with Epstein (~1993-94); (5) ELON MUSK: Met at Sergey Brin\\\\\\\\'s birthday; \\\\\\\"in discovery, they were communicating on email\\\\\\\"; (6) PRINCE ANDREW PHOTO: Called it \\\\\\\"The fake\\\\\\\"; (7) MAR-A-LAGO RECRUITING: \\\\\\\"in the realms of possibility, it could have, but I have no memory of it\\\\\\\"; (8) EPSTEIN: \\\\\\\"He\\\\\\\\'s a disgusting guy who did terrible things to young kids\\\\\\\"; (9) CLINTON GLOBAL INITIATIVE: Maxwell was \\\\\\\"part of the beginning process,\\\\\\\" suggested Clinton \\\\\\\"should have his own Davos\\\\\\\"; (10) NO BLACKMAIL KNOWLEDGE: Denied knowing about leverage, photos, or control over associates; (11) PROFFER AGREEMENT (PROFFER_proffer_agreement.txt): Maxwell met with DAG Todd Blanche at Northern District of Florida, July 24-25, 2025. Explicitly \\\\\\\"NOT A COOPERATION AGREEMENT.\\\\\\\" [v11.05]',date:'2025-07-25',type:'proffer-transcript'},
  {id:'fbi-case-initiation-summary-kellen-cooperation-epstein-explored-cooperation',dataset:'DS10-Official',pages:35,severity:10,keywords:['fbi','case initiation','sdny','december 2018','miami herald','sarah kellen','proffer','evidence destruction','sexually abusive','lesley groff','reverse proffer','leon black','sexual contact','jes staley','raped','manhattan da','harvey weinstein','cooperation','resolution','12 days','august 10','no cameras','csam','small number','80 victims','hundreds unidentified','january 2019','west palm beach'],summary:'CRITICAL -- PRIMARY SOURCE: FBI Case Initiation Summary (EFTA00174356, ~35 pages). THE DEFINITIVE OVERVIEW OF THE SDNY INVESTIGATION: (1) Investigation started December 2018 after Miami Herald series; SDNY traveled to West Palm Beach January 2019 to meet original FBI agents; (2) EPSTEIN EXPLORED COOPERATION: On 7/29/2019, Epstein\\\\\\\\'s attorneys \\\\\\\"discussed the possibility of a resolution of the case, and the possibility of the defendant\\\\\\\\'s cooperation.\\\\\\\" SDNY told them to come back with a specific proposal. EPSTEIN DIED 12 DAYS LATER; (3) KELLEN COOPERATING: Sarah Kellen conducted proffer sessions 11/26/2019 and 12/4/2019, provided \\\\\\\"details about evidence destruction at Epstein\\\\\\\\'s direction,\\\\\\\" lawyers called her relationship with Epstein \\\\\\\"sexually abusive\\\\\\\"; (4) LEON BLACK ASSAULT: Adult victim described being directed to massage Black, who \\\\\\\"initiated sexual contact\\\\\\\" (victim fled). STALEY RAPE: Same victim described Staley who \\\\\\\"forced her to touch his genitals and raped her\\\\\\\"; Manhattan DA investigated Black; (5) NO CAMERAS IN BEDROOMS: \\\\\\\"contrary to some news reports, these searches did not reveal any cameras in any of the bedrooms or massage rooms\\\\\\\"; (6) CSAM: \\\\\\\"a small number of CSAM images found on one of Epstein\\\\\\\\'s devices\\\\\\\"; (7) \\\\\\\"No other victim described being directed by either Epstein or Maxwell to engage in sexual activity with any other men\\\\\\\" except one asked to massage Weinstein; (8) Post-death investigation focused on Maxwell, Kellen, Groff, and others -- only Maxwell was charged. [v11.05]',date:'2019-07-29',type:'fbi-investigation'},
  {id:'npa-text-co-conspirator-immunity-opr-poor-judgment-acosta',dataset:'DS10-Official',pages:120,severity:10,keywords:['non-prosecution agreement','npa','alexander acosta','sarah kellen','adriana ross','lesley groff','nadia martinkova','co-conspirator','immunity','public record','secret','concealed','victims','opr','office of professional responsibility','poor judgment','professional misconduct','federal interest','too narrow','federalism','september 2007','southern district florida'],summary:'CRITICAL -- PRIMARY SOURCES: The actual signed NPA (EFTA00040089) and DOJ OPR Executive Summary (EFTA00011475, combined ~120 pages). THE AGREEMENT THAT PROTECTED EVERYONE: (1) NPA TEXT: \\\\\\\"the United States also agrees that it will not institute any criminal charges against any potential co-conspirators of Epstein, including but not limited to Sarah Kellen, Adriana Ross, Lesley Groff, or Nadia Martinkova\\\\\\\" -- this clause immunized an UNKNOWN NUMBER of unnamed co-conspirators; (2) SECRECY: \\\\\\\"the parties anticipate that this agreement will not be made part of any public record\\\\\\\"; (3) Signed by R. Alexander Acosta, who became Trump\\\\\\\\'s Secretary of Labor in 2017; (4) OPR FINDING: \\\\\\\"the government also immunized from prosecution Epstein\\\\\\\\'s co-conspirators and concealed from Epstein\\\\\\\\'s victims the terms of the NPA\\\\\\\"; (5) OPR concluded Acosta\\\\\\\\'s decision \\\\\\\"constitutes poor judgment\\\\\\\" but NOT \\\\\\\"professional misconduct\\\\\\\"; (6) Acosta\\\\\\\\'s \\\\\\\"view of the federal interest in prosecuting Epstein was too narrow\\\\\\\"; (7) Maxwell later argued the NPA\\\\\\\\'s immunity bound ALL federal prosecutors nationwide, not just SDFL (EFTA00065989); (8) SDNY took the position they were not bound by the Florida agreement and prosecuted Maxwell. [v11.05]',date:'2007-09-24',type:'legal-agreement'},
  {id:'victoria-secret-modeling-book-fbi-1996-deutsche-bank-consent-order',dataset:'DS10-Official',pages:180,severity:10,keywords:['victoria secret','les wexner','modeling book','photographs','young girls','boys','undress','recruit','models','fbi','1996','pedophile ring','child pornography','no action','25 years','deutsche bank','consent order','ny dfs','southern trust','40 accounts','honorary pep','politically exposed','$800000 cash','cash alert','russian model','eastern european','tuition','modeling agency','private jets','alfredo rodriguez','butler','black book','naked underage girls','collages','jean-luc brunel','obstruction'],summary:'CRITICAL -- PRIMARY SOURCES: FBI Notice of Claim (EFTA00143419), Deutsche Bank NY DFS Consent Order (EFTA00151495), Alfredo Rodriguez FBI Interview (EFTA00108668, combined ~180 pages). THE INSTITUTIONAL FAILURES: (1) FBI 1996 REPORT IGNORED: Victim reported to FBI on August 29, 1996 that Epstein and Maxwell were \\\\\\\"operating a pedophile ring and producing child pornography.\\\\\\\" Maxwell maintained a \\\\\\\"modeling book\\\\\\\" used \\\\\\\"to recruit models for Victoria Secret which was one of the businesses of Les Wexner.\\\\\\\" FBI TOOK NO ACTION FOR NEARLY 25 YEARS; (2) DEUTSCHE BANK CONSENT ORDER: Epstein opened 40+ accounts; classified as \\\\\\\"Honorary PEP\\\\\\\" due to political connections; Attorney-1 withdrew $800,000+ in cash, asking \\\\\\\"how often they could come in to withdraw cash without creating some sort of alert\\\\\\\"; payments to Russian models deemed \\\\\\\"not suspicious\\\\\\\" because \\\\\\\"normal for this client\\\\\\\"; payments to Eastern European women at Russian bank explained as \\\\\\\"SENT TO A FRIEND FOR TUITION\\\\\\\"; (3) RODRIGUEZ INTERVIEW: Epstein\\\\\\\\'s butler describes \\\\\\\"photographs of naked underage girls arranged in collages\\\\\\\" in Epstein\\\\\\\\'s home; Brunel \\\\\\\"would bring girls to the house and arrange for girls to be flown in\\\\\\\"; Rodriguez convicted of obstruction for attempting to sell the black book; (4) SDNY INTERNAL ANALYSIS (EFTA00105304): Payments to Barak, Chomsky, Woody Allen, and \\\\\\\"more than 25 women who appear to be Eastern European models\\\\\\\" -- SDNY concluded none \\\\\\\"appear to have any connection to criminal activity.\\\\\\\" [v11.05]',date:'1996-08-29',type:'multi-source-evidence'},
  {id:'1953-trust-disloyalty-clause-gvi-complaint-391m-financial-empire',dataset:'DS11-Financial',pages:60,severity:9,keywords:['1953 trust','disloyalty clause','doj','sdny','enjoin','bequest','maxwell','employees','beneficiaries','cooperating','nefarious','exorbitant','trustees','virgin islands','gvi','financial informatics','$391 million','southern trust','$212 million','financial trust','shell companies','2011','2012','sex offender','plan d','nautilus','great st jim','lsj','freedom air','two days before death','amended','will','testament','butterfly trust','caterpillar trust','couq foundation','gratitude america','leon black','$10 million grant','charities never received'],summary:'HIGH VALUE -- PRIMARY SOURCES: DOJ internal emails on 1953 Trust (EFTA00094916/091624/087336), GVI Complaint (EFTA00104291), SDNY Financial Analysis (EFTA00105304, combined ~60 pages). EPSTEIN\\\\\\\\'S FINANCIAL EMPIRE AND POST-DEATH CONTROL: (1) THE 1953 TRUST: Two days before death, Epstein amended the trust and his will. DOJ planned to \\\\\\\"attach the various iterations of the trust agreement that show the addition of employees/beneficiaries over time, particularly since Epstein\\\\\\\\'s arrest\\\\\\\"; (2) DISLOYALTY CLAUSE: Trust contained provision that could strip bequests from employees who cooperated with the government. DOJ: \\\\\\\"the disloyalty provision may be used for nefarious purposes\\\\\\\" and trustees making \\\\\\\"exorbitant and highly unusual sums\\\\\\\"; DOJ sought to enjoin any bequest to Maxwell; (3) GVI COMPLAINT: Financial Informatics Inc. (Southern Trust) had assets of $391 MILLION (2015); Financial Trust Company had $212 MILLION (2012); Epstein created numerous shell companies in 2011-2012 \\\\\\\"soon after registering as a sex offender\\\\\\\"; (4) GRATITUDE AMERICA: Got \\\\\\\"most of its funding from a $10 million grant from a foundation controlled by Leon Black\\\\\\\" (2015); some donations \\\\\\\"were never received by the named charities\\\\\\\"; Epstein attempted to use the charity to pay fines; (5) BUTTERFLY/CATERPILLAR TRUSTS: Deutsche Bank compliance flagged a woman \\\\\\\"named as one of the beneficiaries of a trust that he is the Grantor of (Butterfly Trust).\\\\\\\" [v11.05]',date:'2019-08-08',type:'financial-legal-evidence'},
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
count = content.count('v11.04')
print(f"Replacing {count} occurrences of 'v11.04' with 'v11.05'")
content = content.replace('v11.04', 'v11.05')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v11.05.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v11.04')
new_ver = verify.count('v11.05')
print(f"Remaining v11.04: {remaining}")
print(f"Total v11.05: {new_ver}")

for check_id in ['maxwell-proffer-july2025-clinton-island-wexner-rfk-musk-andrew',
                  'fbi-case-initiation-summary-kellen-cooperation-epstein-explored-cooperation',
                  'npa-text-co-conspirator-immunity-opr-poor-judgment-acosta',
                  'victoria-secret-modeling-book-fbi-1996-deutsche-bank-consent-order',
                  '1953-trust-disloyalty-clause-gvi-complaint-391m-financial-empire']:
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
