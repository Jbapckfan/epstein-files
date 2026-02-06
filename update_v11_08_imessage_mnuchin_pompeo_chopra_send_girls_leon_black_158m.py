#!/usr/bin/env python3
"""Update dashboard with Epstein iMessage archive (Mnuchin/Pompeo, humanize the monster, Cohen/RONA, Acosta encounter), Chopra send two girls, Leon Black $158M Dechert report — v11.08"""
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
timeline_entries = """  {date:'2019-01-11',event:'EPSTEIN iMESSAGE: "Too bad. We will have MNUCHIN AND POMPEO." Followed by: "You will have fun. Pompeo will run for president." Sent from Epstein\\'s jeeitunes@gmail.com account on January 11, 2019 — six months before arrest. Someone described as "He\\'s bannon boy." Ehud (likely Barak): "Ehud also going to davos." Messages show Epstein actively planning gatherings with sitting Treasury Secretary Steven Mnuchin and Secretary of State Mike Pompeo.',source:'EFTA00509013'},
  {date:'2019-02-25',event:'EPSTEIN iMESSAGE -- "HUMANIZE THE MONSTER" STRATEGY: "woody said he would help edit. not sure how to stage, what points to make. but better than trying to do an interview that i have no experience doing. goal to humanize the monster. anything written carries little weight. tomorrow the juxtaposition of michael cohen testifying while trump is with kim is wild." Reveals Woody Allen helping Epstein craft a PR/rehabilitation strategy. Epstein explicitly calls himself "the monster."',source:'EFTA00509330'},
  {date:'2019-02-26',event:'EPSTEIN iMESSAGE -- COHEN TESTIMONY AND RONA GRAFF: "Cohen brought up RONA - keeper of the secrets" — reference to Rhona Graff, Trump\\'s longtime executive assistant and gatekeeper. "what do you think so far of cohen. are you back in fighting form?" Response: "Bad. but republicans stood strong, Cohen pretty detailed." Also: "Who would write a pro Acosta story" — seeking favorable media coverage for Labor Secretary Acosta. "Hes opened the door to questions re who are the other henchmen at trump org."',source:'EFTA00509347'},
  {date:'2019-01-18',event:'EPSTEIN iMESSAGE -- TRUMP ORG INDICTMENT WARNING: "If they indict trump org. You will have some decisions to make quickly." Follow-up: "Two stools won\\'t work. Either all in or all out." Epstein advising an associate on positioning regarding potential Trump Organization prosecution — suggesting he had strategic intelligence on the legal landscape around Trump.',source:'EFTA00509050'},
  {date:'2019-04-05',event:'EPSTEIN iMESSAGE -- RAN INTO ACOSTA: "Acosta is Harvard law 94 I am 89 just ran into him. Very small funny world that your friend Woody Allen has humorously observed!!!" — Someone physically encountered Labor Secretary Alexander Acosta (who had given Epstein the lenient 2008 plea deal). Same day: "Guys were blown away---mesmerized because they have been sold you are a \\'monster\\'."',source:'EFTA00509620'},
  {date:'2019-01-15',event:'EPSTEIN iMESSAGE -- GATES FOUNDATION OUTREACH: Terje (Roed-Larsen) to Epstein: "Was the mail to Bill ok? The mail to Chris Elias on the Gates Foundation worked. He is going to call me tomorrow." Later: "Gates didn\\'t answer email. However I had a good conversation with Chris Elias, head of the foundation on the phone. He is setting up a meeting with the head of Gates Foundation in London when I\\'m back from Davos. Would still be good to see Gates in Davos." Shows active outreach to Gates Foundation continuing into January 2019.',source:'EFTA00509032'},
  {date:'2019-01-12',event:'EPSTEIN iMESSAGE -- TOM BARRACK (Trump\\'s close friend/fundraiser): "Barrack said wacko. Also If trump runs Cuomo definitely not." Separate conversation with Harry Fish: "They all connect to tom barrack, oy." And about Barrack associate: "Grundoon; very nice guy, wealthy family; deeper into manafort than he ever told anybody-- hates trump." Shows Epstein connected to Trump\\'s inner circle through Barrack.',source:'EFTA00509032'},
  {date:'2018-08-30',event:'EPSTEIN iMESSAGE -- ELON MUSK DENIAL: "BTW. Contrary to cnbc report I am not advising Elon musk. And I told them so. but.... He did my on the interview with the times." Epstein denying publicly advising Musk while implying involvement in Musk\\'s NYT interview.',source:'EFTA00509242'},
  {date:'2019-03-30',event:'EPSTEIN iMESSAGE -- GEOPOLITICAL BROKERING: "saudi very tricky, Russia a potential friend.. Mongolian here yesterday, caught between china and Russia great insight. Trillion dollars of resources in the ground." And: "You would like the president. batuga. He is willing to see you." Recipient responded: "Love the Mongolian guys-- the ambassador came to breitbart embassy." Shows Epstein positioning himself as a geopolitical intermediary months before arrest.',source:'EFTA00509536'},
  {date:'2019-02-16',event:'EPSTEIN iMESSAGE -- LARRY SUMMERS ONGOING: Summers asking "Is indefinite involvement of this kind what I want." And: "Do you think you are coming to Paris?" Shows Summers questioning his continued relationship with Epstein but not severing it. Separate iMessage: "Still wrestling with your answer re trumps misdeeds." Also: "Yesterday was historic-- Reid is in the middle of everything that counts right now in world history---I feel terrible I didn\\'t push trump to hire him."',source:'EFTA00509519'},
  {date:'2017-11-30',event:'DEEPAK CHOPRA -- "SEND TWO GIRLS" EXCHANGE: After Chopra cancelled a dinner at Epstein\\'s with Woody Allen and the Slovak Foreign Minister, Chopra invited Epstein to a Wall Street event: "Come as my guest with anyone if easy. Love." Epstein replied: "im in florida but i would like to send two girls." Chopra responded: "Need names ASAP. Will send directions." No questions asked about who the girls were or why Epstein was sending them.',source:'EFTA00465169'},
  {date:'2019-02-13',event:'DEEPAK CHOPRA -- "CAN YOU SEND IT IN FEMALE FORM": After receiving a link to a Dalai Lama/Chopra article, Epstein texted someone (evidence strongly suggests Chopra himself, who was on PBS tour and in India at the time): "Can you send it in female form." Response: "Ha ha ha." This is one of the last documented Epstein-Chopra exchanges before arrest.',source:'EFTA00509225'},
  {date:'2016-11-10',event:'DEEPAK CHOPRA -- CIVIL CASE AWARENESS: Epstein sent Chopra a Daily Mail article about a woman who allegedly "FABRICATED" a story of assault by Trump and Epstein at a sex party when she was 13. Chopra replied: "Did she also drop civil case against you?" Epstein: "yup." Chopra: "Good. See you this Sat 230 PM?" Epstein: "great." Shows Chopra was aware of Epstein\\'s sexual abuse allegations and unbothered.',source:'EFTA00438829'},
  {date:'2017-02-19',event:'DEEPAK CHOPRA -- "THE GIRLS MIGHT ENJOY IT": Chopra invites Epstein to his "Journey Into Healing" course: "Anna or others could get massages. My office could work with someone you delegate to make all the arrangements. Also in June I\\'m doing a 1 week retreat in Banff Canada at a resort. The girls might enjoy it." — Chopra casually offering massages and referencing "the girls" in Epstein\\'s entourage.',source:'EFTA00446309'},
  {date:'2021-01-22',event:'LEON BLACK -- DECHERT LLP INVESTIGATION REPORT: Apollo Global Management\\'s conflicts committee retained Dechert LLP, which found Black paid Epstein $158 MILLION between 2012 and 2017. $70 million paid in 2014, $30 million in 2015 — with NO written service agreements. Epstein\\'s Financial Trust Company purchased 263,257 shares of Apollo stock at its 2011 IPO, transferred to Southern Financial LLC, held through at least September 2019. Epstein was on the Black Family Foundation board from 1997, and due to "oversight" was still listed on IRS Form 990s through 2012.',source:'EFTA02730996'},
  {date:'2023-07-24',event:'LEON BLACK -- SENATE FINANCE COMMITTEE INVESTIGATION: Senator Ron Wyden\\'s 16-page letter reveals Epstein helped Black avoid approximately $1 BILLION in gift and estate taxes through 2006 GRATs funded with interests in 11 separate Apollo entities valued at ~$585 million, expected to grow to $2+ billion. Epstein demanded $60 million for a step-up-basis transaction saving Black ~$600 million; Black settled on $20 million. Black had NO written services agreement for over $100 million in payments. Epstein told Black payments would be "tax deductible (\\'sixty cent dollars\\')" — which was FALSE. The IRS has NEVER audited these transactions. Black refused to answer multiple Committee questions.',source:'EFTA02731023'},
  {date:'2013-04-26',event:'LEON BLACK FLIES TO ZORRO RANCH: Melanie Spinella (Assistant to Leon D. Black, Apollo Management) confirms: "Leon and Debra are flying to Jeffrey\\'s Ranch in Santa Fe on Sunday morning." Then: "Leon, Debra, Jeffrey and two others will fly from Santa Fe to LA." Leon\\'s plane tail number N 624N. Epstein ordered a helicopter to fly Black from Santa Fe airport to the ranch. Epstein was also interviewing candidates for Black\\'s family office and attending Elysium Trustees meetings at Apollo offices.',source:'EFTA00391544'},
  {date:'2014-03-19',event:'EPSTEIN ASSEMBLES ELITE DINNER PARTY: Email from Epstein to staff: "lets try to set a dinner at 8 for 27th tetje lean, leon should invite others, shwartzman, geitner balnkfein if we thinkgs fun, I will invite jes. reid weingarten." Attempting to gather Leon Black, Stephen SCHWARZMAN (Blackstone CEO), Tim GEITHNER (former Treasury Secretary), Lloyd BLANKFEIN (Goldman Sachs CEO), Jes STALEY (JPMorgan/Barclays), and REID WEINGARTEN (Epstein\\'s own criminal defense attorney) — all at one dinner.',source:'EFTA00372779'},
"""

# New FINDINGS entries
findings_entries = """  {id:'epstein-imessage-archive-mnuchin-pompeo-humanize-monster-cohen-rona-acosta-bannon-musk-summers',dataset:'DS10-Official',pages:200,severity:10,keywords:['imessage','mnuchin','pompeo','treasury secretary','secretary of state','humanize the monster','woody allen','cohen','michael cohen','rhona graff','rona','keeper of the secrets','acosta','ran into','harvard law','trump org','indict','two stools','all in or all out','gates foundation','chris elias','davos','tom barrack','manafort','elon musk','cnbc','larry summers','indefinite involvement','erik prince','robert kraft','bannon boy','ehud','mongolia','breitbart embassy','geopolitics','saudi','russia','china','january 2019','february 2019','march 2019','april 2019','jeeitunes'],summary:'CRITICAL -- PRIMARY SOURCE: 29 iMessage files extracted from Epstein device NYC024328.aff4 (EFTA00509013 through EFTA00509787, December 2018 - May 2019). EPSTEIN\\\\\\\\\\\\\\\\'S FINAL MONTHS IN HIS OWN WORDS: (1) MNUCHIN/POMPEO: \\\\\\\\\\\\\\\"Too bad. We will have Mnuchin and Pompeo\\\\\\\\\\\\\\\" (Jan 11, 2019) -- Epstein planning gathering with sitting Treasury Secretary and Secretary of State. \\\\\\\\\\\\\\\"Pompeo will run for president\\\\\\\\\\\\\\\"; (2) HUMANIZE THE MONSTER: \\\\\\\\\\\\\\\"woody said he would help edit...goal to humanize the monster\\\\\\\\\\\\\\\" (Feb 25, 2019) -- Woody Allen helping craft Epstein\\\\\\\\\\\\\\\\'s rehabilitation PR; (3) COHEN/RONA: \\\\\\\\\\\\\\\"Cohen brought up RONA - keeper of the secrets\\\\\\\\\\\\\\\" -- reference to Rhona Graff, Trump\\\\\\\\\\\\\\\\'s gatekeeper. \\\\\\\\\\\\\\\"Who would write a pro Acosta story\\\\\\\\\\\\\\\"; (4) TRUMP ORG WARNING: \\\\\\\\\\\\\\\"If they indict trump org. You will have some decisions to make quickly. Two stools won\\\\\\\\\\\\\\\\'t work. Either all in or all out\\\\\\\\\\\\\\\"; (5) RAN INTO ACOSTA: \\\\\\\\\\\\\\\"Acosta is Harvard law 94 I am 89 just ran into him. Very small funny world\\\\\\\\\\\\\\\"; (6) GATES FOUNDATION: Active outreach to Chris Elias continuing Jan 2019, seeking Gates at Davos; (7) TOM BARRACK: Direct references to Trump\\\\\\\\\\\\\\\\'s close friend/fundraiser, Manafort connections; (8) MUSK: \\\\\\\\\\\\\\\"Contrary to cnbc report I am not advising Elon musk. And I told them so. but....\\\\\\\\\\\\\\\"; (9) SUMMERS: \\\\\\\\\\\\\\\"Is indefinite involvement of this kind what I want\\\\\\\\\\\\\\\"; (10) GEOPOLITICS: Saudi/Russia/Mongolia brokering, \\\\\\\\\\\\\\\"breitbart embassy.\\\\\\\\\\\\\\\" These 29 files are the closest thing to Epstein\\\\\\\\\\\\\\\\'s inner monologue in the final 6 months before arrest. [v11.08]',date:'2019-01-11',type:'imessage-forensic'},
  {id:'deepak-chopra-send-two-girls-female-form-12-meetings-civil-case-woody-allen',dataset:'DS10-Official',pages:48,severity:9,keywords:['deepak chopra','send two girls','need names asap','can you send it in female form','ha ha ha','civil case','did she also drop','good','journey into healing','the girls might enjoy it','massages','anna','woody allen','soon yi','miroslav lajcak','skeptic magazine','peter thiel','misha gromov','dalai lama','pbs tour','india','wall street event','2017','2018','2019','lunch','dinner','hunter college','rubin museum'],summary:'CRITICAL -- PRIMARY SOURCES: 48 files across schedules, emails, and iMessages (EFTA00317497, EFTA00438829, EFTA00446309, EFTA00465169, EFTA00509225, and others). DEEPAK CHOPRA\\\\\\\\\\\\\\\\'S 3+ YEAR RELATIONSHIP WITH EPSTEIN: (1) \\\\\\\\\\\\\\\"SEND TWO GIRLS\\\\\\\\\\\\\\\": Chopra invited Epstein to Wall Street event. Epstein: \\\\\\\\\\\\\\\"im in florida but i would like to send two girls.\\\\\\\\\\\\\\\" Chopra: \\\\\\\\\\\\\\\"Need names ASAP. Will send directions\\\\\\\\\\\\\\\" -- no questions asked (Nov 30, 2017); (2) \\\\\\\\\\\\\\\"CAN YOU SEND IT IN FEMALE FORM\\\\\\\\\\\\\\\": After Dalai Lama/Chopra article link, Epstein to likely-Chopra: \\\\\\\\\\\\\\\"Can you send it in female form.\\\\\\\\\\\\\\\" Response: \\\\\\\\\\\\\\\"Ha ha ha\\\\\\\\\\\\\\\" (Feb 13, 2019); (3) CIVIL CASE AWARENESS: Chopra asked \\\\\\\\\\\\\\\"Did she also drop civil case against you?\\\\\\\\\\\\\\\" re: the Trump-Epstein-13yo allegation. Epstein: \\\\\\\\\\\\\\\"yup.\\\\\\\\\\\\\\\" Chopra: \\\\\\\\\\\\\\\"Good. See you this Sat 230 PM?\\\\\\\\\\\\\\\" (Nov 10, 2016); (4) \\\\\\\\\\\\\\\"THE GIRLS MIGHT ENJOY IT\\\\\\\\\\\\\\\": Chopra inviting Epstein to Journey Into Healing, offering massages for \\\\\\\\\\\\\\\"Anna or others,\\\\\\\\\\\\\\\" suggesting \\\\\\\\\\\\\\\"the girls might enjoy\\\\\\\\\\\\\\\" Banff retreat (Feb 2017); (5) 12+ documented meetings/events from 2015-2019 including dinners with Woody Allen/Soon Yi, Peter Thiel invitations, Skeptic Magazine event. Last documented meeting: LUNCH April 3, 2019 -- 3 months before arrest. [v11.08]',date:'2017-11-30',type:'email-imessage'},
  {id:'leon-black-158m-dechert-report-senate-investigation-zorro-ranch-schwarzman-geithner-blankfein-dinner',dataset:'DS10-Official',pages:80,severity:10,keywords:['leon black','$158 million','dechert','apollo','conflicts committee','$70 million','$30 million','no written agreement','263257 shares','ipo','financial trust company','southern financial','black family foundation','irs form 990','senate finance committee','ron wyden','$1 billion','estate taxes','grats','11 apollo entities','$585 million','$2 billion','step-up-basis','$60 million','$20 million','sixty cent dollars','irs never audited','zorro ranch','santa fe','helicopter','n 624n','schwarzman','geithner','blankfein','jes staley','reid weingarten','dinner','elysium','family office','brad wechsler','susan estrich','victim compensation'],summary:'CRITICAL -- PRIMARY SOURCES: Dechert LLP Memorandum (EFTA02730996, January 22, 2021), Senate Finance Committee Letter (EFTA02731023, July 24, 2023), and 25+ primary schedule/email documents. LEON BLACK\\\\\\\\\\\\\\\\'S $158 MILLION AND THE APOLLO CONNECTION: (1) DECHERT REPORT: Black paid Epstein $158 million (2012-2017) -- $70M in 2014, $30M in 2015, with NO written service agreements after 2013. Epstein\\\\\\\\\\\\\\\\'s entity purchased 263,257 shares of Apollo stock at IPO; (2) SENATE INVESTIGATION: Epstein helped Black avoid ~$1 BILLION in estate taxes through 2006 GRATs funded with 11 Apollo entities valued at $585M. Epstein demanded $60M for step-up transaction saving Black ~$600M; settled for $20M. Told Black payments were \\\\\\\\\\\\\\\"tax deductible\\\\\\\\\\\\\\\" -- which was false. IRS has NEVER audited; (3) ZORRO RANCH: Black and wife Debra flew on private plane N 624N to Epstein\\\\\\\\\\\\\\\\'s New Mexico ranch; Epstein arranged helicopter transport. Epstein was interviewing Black\\\\\\\\\\\\\\\\'s family office candidates; (4) ELITE DINNER ASSEMBLY: Epstein email: \\\\\\\\\\\\\\\"lets try to set a dinner...leon should invite others, shwartzman, geitner balnkfein...I will invite jes. reid weingarten\\\\\\\\\\\\\\\" -- Schwarzman (Blackstone CEO), Geithner (former Treasury Sec), Blankfein (Goldman CEO), Staley, and Epstein\\\\\\\\\\\\\\\\'s own defense attorney at one table; (5) Black\\\\\\\\\\\\\\\\'s counsel Susan Estrich fought victim compensation claims in 2024. [v11.08]',date:'2021-01-22',type:'corporate-investigation'},
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
count = content.count('v11.07')
print(f"Replacing {count} occurrences of 'v11.07' with 'v11.08'")
content = content.replace('v11.07', 'v11.08')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v11.08.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v11.07')
new_ver = verify.count('v11.08')
print(f"Remaining v11.07: {remaining}")
print(f"Total v11.08: {new_ver}")

for check_id in ['epstein-imessage-archive-mnuchin-pompeo-humanize-monster-cohen-rona-acosta-bannon-musk-summers',
                  'deepak-chopra-send-two-girls-female-form-12-meetings-civil-case-woody-allen',
                  'leon-black-158m-dechert-report-senate-investigation-zorro-ranch-schwarzman-geithner-blankfein-dinner']:
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
