#!/usr/bin/env python3
"""Update dashboard with Barrack/Manafort/Patten, Deutsche Bank WH panic, Elon Musk denial, Elysee Palace — v10.97"""
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
timeline_entries = """  {date:'2018-08-31',event:'Epstein iMessages contact: "They all connect to Tom Barrack, oy." Then: "Is patten flipping meaningful?" (Sam Patten pleaded guilty that exact day for acting as unregistered foreign agent with Manafort associate Kilimnik). Contact responds about someone: "deeper into manafort than he ever told anybody -- hates trump." Epstein tracking Mueller cooperators in real time.',source:'EFTA00509430'},
  {date:'2018-08-30',event:'Epstein iMessages contact: "Contrary to cnbc report I am not advising Elon musk. And I told them so. but.... He did my on the interview with the times." Denying CNBC report while acknowledging connection to Musk\\'s NYT interview during the "funding secured" Tesla controversy.',source:'EFTA00509242'},
  {date:'2019-04-24',event:'Epstein shares CNN article about Deutsche Bank turning over Trump financial records, writes: "Say bye bye." Contact: "WTF." Epstein: "No court can stop it." Contact: "They are freaked out@ the WH." Epstein: "they should be, but no one really knows the depth." Contact had insider knowledge of White House reaction.',source:'EFTA00509770'},
  {date:'2019-03-29',event:'Epstein iMessages: "Im in the elysee. On line again in 45 min." Then: "Need to be at elysee tomorrow." Then: "Now at the pyramid. With the entire govt." Contact: "Macron govt??" Epstein: "Yup." Another contact: "just us two entire place. French power Powermove." Epstein inside French presidential palace with Macron\\'s government, three months before arrest.',source:'EFTA00509519'},
  {date:'2019-02-22',event:'Epstein shares Business Insider article explicitly linking "friends of Trump" -- Epstein, Robert Kraft -- in simultaneous scandals. Separately, "Jack" (attorney at Quinn Emanuel) tells Epstein he is handling Kraft\\'s legal defense: "kraft too many people advising him but after call...wants me and my Quinn Emanuel guy to handle it." Epstein warns Jack: "you need to know about a past issue with Kraft that may come to light."',source:'EFTA00509312'},
  {date:'2019-02-25',event:'Ehud Barak visits Epstein\\'s NYC home multiple times: "ehud will join at 930" then next day "ehud here" then "ehud coming at 1230, want to join at 115?" Former Israeli PM visiting Epstein repeatedly during active scandal period. Same day Epstein: "MICHAEL and reid at my house Monday 830 morning trying to strategize pr re my craziness."',source:'EFTA00509330'},
  {date:'2019-02-24',event:'Epstein texts contact about dinner with Woody Allen: "dinner with woody? or too many pedos in one place." Self-aware admission calling both himself and Allen pedophiles in casual text. Same period: "goal to humanize the monster" with Woody Allen\\'s help editing video.',source:'EFTA00509330'},
  {date:'2019-02-20',event:'Contact asks Epstein: "Macron scandal-- is that Erik Prince company???" Discussing whether Blackwater founder Erik Prince (brother of Trump Education Secretary Betsy DeVos) was involved in Macron scandal. Same day Epstein: "Michalel Cohen prison delayed so he can testify in front of congress." Also: "Cnn reports mueller next week.. surprise surprise."',source:'EFTA00509312'},
  {date:'2019-01-30',event:'Epstein coaches World Bank-connected woman on how to handle reporter. She describes dinner with Bill Gates, Mark Suzman, and Geoff Lamb alongside Jim Yong Kim. Epstein: "The reporter clearly believes a relationship occurred- we must be careful." Instructs: "No phone!!!" Contact: "i wouldn\\'t use your name but I might." Epstein managing Gates/World Bank media narrative.',source:'EFTA00509137'},
  {date:'2019-04-24',event:'Larry Summers asks Epstein: "is it true that Delaware is a great place to hide money." Epstein: "There is tax. And there is tax." Sends Summers Guardian article about Panama Papers and Delaware as tax haven. Same period Summers tells Epstein: "Won\\'t answer without consulting. Am greedy but not mean." Epstein coaching Summers on romantic manipulation: "The hook is in."',source:'EFTA00509770'},
  {date:'2019-03-04',event:'Epstein and contact discuss placing a "Jim Kim story" with reporters -- Epstein potentially holding leverage over former World Bank President. Contact: "Not sure a Jim kim story would be newsworthy at this point." Same day Epstein distributes NYT opinion letter to his entire contact list. Contact on Acosta: "I\\'m sorry that this has become more about the politics of Acosta than anything else."',source:'EFTA00509384'},
"""

# New FINDINGS entries
findings_entries = """  {id:'barrack-manafort-patten-flipping-mueller-aug2018',dataset:'DS9-Digital',pages:17,severity:10,keywords:['tom barrack','paul manafort','sam patten','mueller','flipping','cooperating witness','guilty plea','kilimnik','elon musk','cnbc','tesla','funding secured','nyt interview','administrative state','woody allen','bard college','bechet','orrin hatch','google','ftc','august 2018'],summary:'CRITICAL -- PRIMARY SOURCE: Forensic iMessage extraction from Epstein\\'s Mac (NYC024328.aff4, EFTA00509430-509448, 17 pages, August 31 - September 2, 2018). REAL-TIME MUELLER INVESTIGATION TRACKING: (1) TOM BARRACK CONNECTION: Epstein writes: \"They all connect to Tom Barrack, oy\" -- linking multiple Trump-orbit figures back to Trump\\'s closest friend and inaugural committee chair (later indicted July 2021 for illegal UAE lobbying); (2) SAM PATTEN FLIPPING: On the EXACT DAY of Patten\\'s guilty plea (August 31, 2018), Epstein asks: \"Is patten flipping meaningful?\" Patten cooperated with Mueller\\'s investigation after working with Manafort associate Konstantin Kilimnik; (3) MANAFORT INSIDER KNOWLEDGE: Contact describes someone as \"deeper into manafort than he ever told anybody -- hates trump\" -- revealing inside knowledge of the Manafort prosecution circle; (4) ELON MUSK DENIAL: Same period, Epstein texts: \"Contrary to cnbc report I am not advising Elon musk. And I told them so. but.... He did my on the interview with the times\" -- denying the CNBC report while cryptically referencing Musk\\'s NYT interview during the August 2018 \"funding secured\" Tesla controversy; (5) \"ADMINISTRATIVE STATE\": Contact shares \"dislike of the administrative state\" -- Trump-era deregulation language; (6) WOODY ALLEN / BARD: Allen to Epstein: \"Bechet just left for her sophomore year at Bard. Thank you for making this possible\" -- Epstein played role in Allen\\'s daughter\\'s education. [v10.97]',date:'2018-08-31',type:'digital-forensics'},
  {id:'deutsche-bank-wh-freaked-out-summers-delaware-apr2019',dataset:'DS9-Digital',pages:17,severity:10,keywords:['deutsche bank','trump','financial records','subpoena','white house','freaked out','privilege waiver','larry summers','delaware','tax haven','panama papers','hide money','passover','hook is in','zelensky','ukraine','poroshenko','mike crow','asu','terje','vienna','april 2019','three months before arrest'],summary:'CRITICAL -- PRIMARY SOURCE: Forensic iMessage extraction from Epstein\\'s Mac (NYC024328.aff4, EFTA00509770-509786, 17 pages, April 23-25, 2019 -- three months before arrest). WHITE HOUSE INSIDER KNOWLEDGE AND SUMMERS FINANCIAL ADVICE: (1) DEUTSCHE BANK / WHITE HOUSE PANIC: Epstein shares CNN article about Deutsche Bank turning over Trump financial records. Writes: \"Say bye bye.\" Contact: \"WTF.\" Epstein: \"No court can stop it.\" Contact: \"They are freaked out@ the WH.\" Epstein: \"they should be, but no one really knows the depth.\" Epstein then provides legal analysis: \"The legal arguments are bogus. McCann already waived privilege.\" This shows Epstein had contacts with INSIDER KNOWLEDGE of White House reactions to legal proceedings; (2) SUMMERS ASKS ABOUT HIDING MONEY: Larry Summers texts Epstein: \"is it true that Delaware is a great place to hide money.\" Epstein: \"There is tax. And there is tax.\" Sends Guardian article about Panama Papers and Delaware as tax haven; (3) SUMMERS ROMANTIC MANIPULATION: Epstein coaches Summers on emotional manipulation of a woman: \"The hook is in\" / \"We are in a long game\" / \"HAD. Strong feelings. Past tense. She will respond.\" Summers: \"Won\\'t answer without consulting. Am greedy but not mean\" then \"Guess tough and mean is sexier\"; (4) UKRAINE ELECTION: Discusses Zelensky\\'s victory: \"The Russians hate Poroshenko, so this could be good.\" Contact: \"I\\'m trying to intercede.\" [v10.97]',date:'2019-04-24',type:'digital-forensics'},
  {id:'elysee-palace-macron-kraft-defense-gates-dinner-2019',dataset:'DS9-Digital',pages:52,severity:9,keywords:['elysee palace','macron','french government','emmanuel macron','robert kraft','quinn emanuel','jack','legal defense','bill gates','mark suzman','geoff lamb','jim yong kim','world bank','onno ruehl','reporter','no phone','erik prince','betsy devos','blackwater','michael cohen','congress','ehud barak','pedos','humanize the monster','february 2019','march 2019'],summary:'HIGH VALUE -- PRIMARY SOURCE: Forensic iMessage extraction from Epstein\\'s Mac (NYC024328.aff4, EFTA00509312-509400 and EFTA00509519-509537, 52 pages combined, February-March 2019). EXTRAORDINARY ACCESS AND LEGAL FIXING: (1) ELYSEE PALACE: March 29, 2019 -- Epstein texts: \"Im in the elysee\" then \"Now at the pyramid. With the entire govt.\" Contact: \"Macron govt??\" Epstein: \"Yup.\" Inside the French presidential palace with the Macron government, three months before arrest; (2) ROBERT KRAFT DEFENSE: \"Jack\" (attorney at Quinn Emanuel) tells Epstein he is handling Kraft\\'s legal defense in the Florida prostitution case: \"kraft...wants me and my Quinn Emanuel guy to handle it.\" Epstein warns: \"you need to know about a past issue with Kraft that may come to light\" and \"Two not one extortion\"; (3) BILL GATES DINNER: World Bank-connected contact describes dinner with Bill Gates, Mark Suzman, Geoff Lamb, and Jim Yong Kim. Epstein coaches her: \"The reporter clearly believes a relationship occurred- we must be careful\" and \"No phone!!!\"; (4) ERIK PRINCE: Contact asks: \"Macron scandal-- is that Erik Prince company???\" -- linking Blackwater founder (Betsy DeVos\\'s brother) to French intelligence operations; (5) EHUD BARAK: Former Israeli PM visits Epstein\\'s NYC home repeatedly Feb 25-26: \"ehud will join at 930\" / \"ehud here\" / \"ehud coming at 1230\"; (6) \"TOO MANY PEDOS\": Epstein texts about Woody Allen dinner: \"dinner with woody? or too many pedos in one place\" -- calling both himself and Allen pedophiles; (7) JIM KIM LEVERAGE: Discussion of placing \"Jim Kim story\" with reporters, suggesting Epstein held leverage over former World Bank President. [v10.97]',date:'2019-03-29',type:'digital-forensics'},
  {id:'gates-world-bank-coaching-money-laundering-jan2019',dataset:'DS9-Digital',pages:18,severity:9,keywords:['bill gates','mark suzman','geoff lamb','jim yong kim','world bank','shalimar','onno ruehl','reporter coaching','no phone','hamza','money laundering','dark arts','saudi','egypt','uae','project raven','terje','false flag','cyber warfare','osce','january 2019','five months before arrest'],summary:'HIGH VALUE -- PRIMARY SOURCE: Forensic iMessage extraction from Epstein\\'s Mac (NYC024328.aff4, EFTA00509137-509154 and EFTA00509384-509400, 36 pages combined, January 30 - March 5, 2019). GATES CONNECTION AND CRISIS MANAGEMENT: (1) GATES DINNER: Contact describes dinner with Bill Gates, Mark Suzman (Gates Foundation CEO), and Geoff Lamb alongside Jim Yong Kim; (2) REPORTER CRISIS: Epstein actively coaching World Bank-connected associate on handling reporter inquiry about relationship with Jim Kim: \"The reporter clearly believes a relationship occurred- we must be careful\" / \"He believes you lied\" / \"No phone!!!\" Contact reveals: \"i wouldn\\'t use your name but I might\"; (3) REAL AFFAIR: Advisor \"Steve\" reveals to contact: \"He doesn\\'t know about the real affair that Jim is having with shalimar\" -- inside knowledge of World Bank president\\'s affair with his secretary; (4) MONEY LAUNDERING WARNING: Epstein warns Terje about \"Hamza\" (half Egyptian/Saudi): \"very involved in the dark arts\" / \"money movement. bank laundering. many things that i can\\'t and you shouldn\\'t go near\"; (5) FALSE FLAG / CYBER: Epstein discusses cyber warfare: \"False flag operations...With computers I can bounce of 100 false flags in a nanosecond\" / proposes \"the miro doctrine\" for understanding new security threats; (6) BIOLOGICAL WARFARE: Epstein discusses targeted genetic attacks: \"attacking only blue eyed people becomes possible. Or those with Jewish genes.\" [v10.97]',date:'2019-01-30',type:'digital-forensics'},
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
count = content.count('v10.96')
print(f"Replacing {count} occurrences of 'v10.96' with 'v10.97'")
content = content.replace('v10.96', 'v10.97')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.97.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.96')
new_ver = verify.count('v10.97')
print(f"Remaining v10.96: {remaining}")
print(f"Total v10.97: {new_ver}")

for check_id in ['barrack-manafort-patten-flipping-mueller-aug2018',
                  'deutsche-bank-wh-freaked-out-summers-delaware-apr2019',
                  'elysee-palace-macron-kraft-defense-gates-dinner-2019',
                  'gates-world-bank-coaching-money-laundering-jan2019']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
print(f"Arrays at different positions: {f_close2 != t_close2}")
