#!/usr/bin/env python3
"""Update dashboard with Acting AG Whitaker leak, Kushner 'squashed', SDNY vs Mueller, Summers PR advising — v10.96"""
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
timeline_entries = """  {date:'2019-02-02',event:'Epstein iMessages contact: "Im pushing, jared needs squashed." Contact responds: "He is killing trump." Discussion of Jared Kushner\\'s political damage to Trump. Same conversation: "I think Whittaker gave him a heads up on troubles" -- alleging Acting Attorney General Matthew Whitaker leaked DOJ information. Also discusses "textualist argument" against presidential indictment and whether it applies to SDNY.',source:'EFTA00509155'},
  {date:'2019-02-02',event:'Epstein iMessages contact: "the trump comment about you, no surprise, only a matter of time." Contact: "You mean in the haberman piece???" Epstein: "You are his only hope." Recipient is someone Trump publicly commented about, covered by Maggie Haberman (NYT). Same conversation discusses MBS UN investigation tribunal: "There is a push at the un to form an investigation tribunal for mbs."',source:'EFTA00509155'},
  {date:'2019-02-02',event:'Epstein texts a governor about Opportunity Zones (Trump\\'s 2017 Tax Cuts and Jobs Act program): "gm gov Would like to talk opportunity zones." Also discusses Iran/Russia/Europe forming cryptocurrency to circumvent SWIFT and US dollar dominance, shared CNBC article on EU\\'s INSTEX mechanism to bypass Trump\\'s Iran sanctions.',source:'EFTA00509155'},
  {date:'2019-02-05',event:'Epstein iMessages Terje: "David malpass - world hank" -- aware of Trump\\'s World Bank nominee before public announcement. Contact later confirms: "Trump just nominated Malpass For WB President so Hopefully attention will shift soon." Same period: Epstein shares Fox News article about DOJ probe into Acosta\\'s plea deal with himself.',source:'EFTA00509208'},
  {date:'2019-02-07',event:'Epstein outraged that Senator Ben Sasse called him a "child rapist": "sasse calling me a child rapist, is nuts!!!" Considers having "Ken" (likely Ken Starr) speak directly to Sasse. Also discusses Ann Coulter on Hannity and media counter-strategy. Separately shares Zerohedge article about Senate investigating Mueller/FBI\\'s handling of original Epstein prosecution.',source:'EFTA00509208'},
  {date:'2019-03-14',event:'Top Mueller prosecutor Andrew Weissmann steps down. Epstein\\'s contact shares NPR article, writes: "Band is breaking up." Epstein: "And he\\'s the lead singer." Contact: "And guitarist." Celebratory tone about Mueller investigation ending.',source:'EFTA00509466'},
  {date:'2019-03-28',event:'Epstein iMessages contact: "SDNY. Is the punch. , the mueller report the head fake." Contact responds: "I think folks may actually see that as witch hunt now since this so clean." Days after AG Barr released Mueller report summary. Same contact had just appeared on CNN Anderson Cooper for 30 minutes from Vatican City, and shares Steve Bannon Daily Mail article.',source:'EFTA00509502'},
  {date:'2019-03-28',event:'Epstein advises contact on pivoting from Russia to China as political target: "They need an enemy, china fits the bill" and "Russia not useful, trump dead for a while. Health care over. China perfect pinata." Proposes "red white and blue hats" hacker group: "Unrestricted warfare. American style." Contact: "Genius." Also: "Arab league meeting in Tunis on weekend. Then group coming to download to me on tues."',source:'EFTA00509502'},
  {date:'2019-03-17',event:'Epstein tells contact: "Reminder. I fully understand my toxicity for the moment. and I want you to win. !! so no awkwardness." Acknowledging his reputation could damage someone\\'s political campaign. Same period: discusses Bolsonaro, shares Khashoggi/MBS articles, asks about Le Pen and Salvini fundraising.',source:'EFTA00509466'},
  {date:'2019-04-15',event:'Epstein drafts PR statement sent to Terje: "Mr Epstein has accepted full responsibility for his actions, served time, provided restitution. He is attempting to give back, quietly, through continuing his philanthropic work." Larry Summers advises on media strategy, suggests citing former Harvard President Derek Bok as "moral force" to defend accepting Epstein\\'s funds.',source:'EFTA00509689'},
  {date:'2019-04-14',event:'Larry Summers confides affair details to Epstein using racist code name "Yellow Peril" for woman connected to IMF/China economics. Summers: "I\\'d be happy to have a rational affair w yellow peril." Discusses her "child," moving in together, and IMF briefings. Epstein: "Need I remind you that you are married."',source:'EFTA00509689'},
  {date:'2019-03-05',event:'Epstein\\'s crisis communications consultant advises: "stick to legal legal legal. A deal is a deal etc. and then a few months from now. Decide how to deal with the pervert hermit image and fill the box with another narrative." Contact recommends: "You should bring Spiro and burck on your team-- rock stars." Same contact raising money "for LePen and Salvini so they can actually run full slates."',source:'EFTA00509401'},
"""

# New FINDINGS entries
findings_entries = """  {id:'whitaker-ag-heads-up-kushner-squashed-feb2019',dataset:'DS9-Digital',pages:17,severity:10,keywords:['matthew whitaker','acting attorney general','jared kushner','kushner','squashed','killing trump','haberman','maggie haberman','mbs','un tribunal','opportunity zones','iran','swift','cryptocurrency','instex','sanctions','presidential indictment','sdny','february 2019','five months before arrest'],summary:'CRITICAL -- PRIMARY SOURCE: Forensic iMessage extraction from Epstein\\'s Mac (NYC024328.aff4, EFTA00509155-509171, 17 pages, January 31 - February 2, 2019 -- five months before arrest). MOST EXPLOSIVE POLITICAL FINDINGS: (1) ACTING AG WHITAKER LEAK: Epstein states: \"I think Whittaker gave him a heads up on troubles\" -- alleging that Matthew Whitaker, the SITTING Acting Attorney General of the United States (Nov 2018 - Feb 2019), provided advance warning about pending legal matters to someone; (2) JARED KUSHNER TARGETED: Epstein writes: \"Im pushing, jared needs squashed.\" Contact responds: \"He is killing trump\" -- Epstein actively working to undermine Jared Kushner, Trump\\'s son-in-law and senior advisor, with someone who had inside knowledge of White House dynamics; (3) TRUMP COMMENT / HABERMAN: \"the trump comment about you, no surprise, only a matter of time\" then contact asks \"You mean in the haberman piece???\" Epstein: \"You are his only hope\" -- someone Trump publicly commented about in a Maggie Haberman NYT piece; (4) PRESIDENTIAL INDICTMENT: Epstein discusses \"textualist argument\" that kills \"any defense of indictment\" since \"it is not in the constitution.\" Contact asks: \"Including southern district?\" -- debating whether a president can be indicted by SDNY; (5) MBS UN TRIBUNAL: \"There is a push at the un to form an investigation tribunal for mbs\" -- Epstein had intelligence on Saudi Crown Prince proceedings; (6) OPPORTUNITY ZONES: Texts governor about Trump\\'s tax program: \"gm gov Would like to talk opportunity zones\"; (7) IRAN SANCTIONS BYPASS: Discusses Iran/Russia/Europe cryptocurrency to circumvent SWIFT, shares CNBC article on EU\\'s INSTEX mechanism challenging Trump\\'s sanctions. This document shows Epstein had alleged inside knowledge from the Acting Attorney General, was actively trying to influence Trump\\'s inner circle, and was engaged in real-time analysis of presidential legal exposure. [v10.96]',date:'2019-02-02',type:'digital-forensics'},
  {id:'sdny-punch-mueller-head-fake-china-warfare-mar2019',dataset:'DS9-Digital',pages:34,severity:10,keywords:['sdny','southern district','mueller','mueller report','witch hunt','anderson cooper','vatican city','steve bannon','china','unrestricted warfare','red white blue hats','hackers','arab league','le pen','salvini','toxicity','campaign','european populism','crisis communications','ann coulter','robert kraft','march 2019','three months before arrest'],summary:'CRITICAL -- PRIMARY SOURCE: Forensic iMessage extraction from Epstein\\'s Mac (NYC024328.aff4, EFTA00509401-509518, 34 pages combined, March 5-28, 2019 -- three months before arrest). FEDERAL INVESTIGATION ANALYSIS AND GEOPOLITICAL STRATEGY: (1) \"SDNY IS THE PUNCH\": Epstein writes: \"SDNY. Is the punch. , the mueller report the head fake.\" Contact responds: \"I think folks may actually see that as witch hunt now since this so clean\" -- using Trump\\'s exact language days after AG Barr released Mueller summary. Epstein CORRECTLY predicted SDNY (not Mueller) would bring the charges that led to his July 2019 arrest; (2) ANDERSON COOPER / VATICAN: Same contact reports: \"I did CNN. Live last night from Vatican City -- 30 minutes on Anderson Cooper.\" Contact shares Steve Bannon Daily Mail article, discusses \"Rome speeches\" about China -- profile strongly consistent with Bannon or close Bannon associate; (3) CHINA \"UNRESTRICTED WARFARE\": Epstein advises: \"They need an enemy, china fits the bill\" and \"Russia not useful, trump dead for a while. China perfect pinata.\" Proposes creating \"red white and blue hats\" hacker group: \"Unrestricted warfare. American style.\" Contact: \"Genius\"; (4) \"I WANT YOU TO WIN\": Epstein tells contact: \"Reminder. I fully understand my toxicity for the moment. and I want you to win\" -- acknowledging he could damage someone\\'s political campaign; (5) CRISIS COMMS: \"Hes here with me now. He thinks stick to legal legal legal. A deal is a deal. And then a few months from now. Decide how to deal with the pervert hermit image and fill the box with another narrative\"; (6) LE PEN / SALVINI FUNDRAISING: Contact \"just focused on raising money for LePen and Salvini so they can actually run full slates\" -- European far-right financing; (7) MUELLER \"BAND BREAKING UP\": When top prosecutor Weissmann steps down: \"Band is breaking up\" / \"And he\\'s the lead singer\"; (8) ANN COULTER reframes Epstein as \"Democrat Pedophile\" turned into \"Trump scandal\" -- Epstein: \"Im on her team.\" [v10.96]',date:'2019-03-28',type:'digital-forensics'},
  {id:'summers-pr-advising-affair-yellow-peril-apr2019',dataset:'DS9-Digital',pages:34,severity:9,keywords:['larry summers','yellow peril','derek bok','harvard','imf','china','affair','married','pr strategy','philanthropy statement','beast article','daily beast','connie bruck','new yorker','woody allen','terje','opportunity zones','virgin islands','trump tax returns','secret service','nunes','mcclatchy','miami herald','april 2019','three months before arrest'],summary:'HIGH VALUE -- PRIMARY SOURCE: Forensic iMessage extraction from Epstein\\'s Mac (NYC024328.aff4, EFTA00509655-509705, 34 pages combined, April 7-16, 2019 -- three months before arrest). LARRY SUMMERS AS PR ADVISOR AND INTIMATE CONFIDANT: (1) MEDIA STRATEGY: Epstein asks Summers: \"Do you think a statement to the reporter asking about the charity...something like, he paid his debt and is trying to do good?\" Summers suggests citing former Harvard President Derek Bok as a \"moral force\" to defend accepting Epstein\\'s funds; (2) PR STATEMENT: Epstein drafts: \"Mr Epstein has accepted full responsibility for his actions, served time, provided restitution. He is attempting to give back, quietly, through continuing his philanthropic work\"; (3) \"YELLOW PERIL\" AFFAIR: Summers confides extramarital affair details using racist code name for woman connected to IMF/China: \"I\\'d be happy to have a rational affair w yellow peril.\" Discusses moving in together, her child, IMF briefings. Epstein: \"Need I remind you that you are married\"; (4) TRUMP TAX RETURNS: Epstein shares NYT article about NY State efforts to obtain Trump\\'s tax returns; (5) SECRET SERVICE: Contact writes: \"All guys Secret service gone too. No waiting until jan 2021\" -- discussing Trump\\'s removal before end of term; (6) NUNES / MIAMI HERALD: Contact links Nunes $150M lawsuit to \"McClatchy owns MH\" -- connecting Epstein\\'s media antagonist to Trump-era political battles; (7) OPPORTUNITY ZONES: Epstein deeply engaged in exploiting Trump\\'s tax program in Virgin Islands: \"Final regs are in 3 weeks. Billions of dollars\"; (8) CONNIE BRUCK: Epstein plans off-the-record meeting with New Yorker journalist at his home, with counsel present. This finding shows former Treasury Secretary Larry Summers actively advising a convicted sex offender on media strategy while simultaneously confiding intimate personal secrets -- establishing a relationship of deep mutual trust and leverage. [v10.96]',date:'2019-04-15',type:'digital-forensics'},
  {id:'malpass-world-bank-sasse-child-rapist-feb2019',dataset:'DS9-Digital',pages:17,severity:9,keywords:['david malpass','world bank','ben sasse','child rapist','ken starr','ann coulter','hannity','fox news','doj probe','acosta','plea deal','zerohedge','mueller','fbi','woody allen','john quinn','quinn emanuel','chomsky','tucson','february 2019','five months before arrest'],summary:'HIGH VALUE -- PRIMARY SOURCE: Forensic iMessage extraction from Epstein\\'s Mac (NYC024328.aff4, EFTA00509208-509224, 17 pages, February 5-10, 2019 -- five months before arrest). TRUMP NOMINEES AND POLITICAL FALLOUT: (1) MALPASS WORLD BANK: Epstein texts Terje \"David malpass - world hank\" BEFORE public announcement. Contact later: \"Trump just nominated Malpass For WB President so Hopefully attention will shift soon\" -- hoping Trump\\'s nomination would divert media from Epstein; (2) SASSE \"CHILD RAPIST\": Senator Ben Sasse publicly labels Epstein -- Epstein furious: \"sasse calling me a child rapist, is nuts!!!\" Considers having \"Ken\" (likely Ken Starr, his attorney) intervene directly with the Senator; (3) FOX NEWS DOJ PROBE: Epstein shares Fox article: \"doj-opens-probe-into-plea-bargain-awarded-by-trump-official-to-alleged-pedophile-predator-jeffrey-epstein\" -- monitoring DOJ investigation of Acosta\\'s plea deal; (4) ANN COULTER / HANNITY: \"Continue to ignore? Ann Coulter on hannity/. Attack? Op ed?\" -- evaluating Trump-aligned media response; (5) ZEROHEDGE / MUELLER-FBI: Contact shares article about Senate investigating Mueller/FBI handling of original Epstein prosecution. Epstein: \"Yes! wild\"; (6) CHOMSKY IN TUCSON: Contact asks Epstein to arrange meeting with Noam Chomsky in Tucson -- Epstein as broker of access to intellectual figures; (7) WOODY ALLEN / QUINN EMANUEL: Epstein congratulates Allen on Amazon lawsuit, references John Quinn: \"Head of the law firm. He knows Kathy my lawyer friend well\" -- connecting Ruemmler to major law firm. [v10.96]',date:'2019-02-07',type:'digital-forensics'},
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
count = content.count('v10.95')
print(f"Replacing {count} occurrences of 'v10.95' with 'v10.96'")
content = content.replace('v10.95', 'v10.96')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Dashboard updated to v10.96.")

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

remaining = verify.count('v10.95')
new_ver = verify.count('v10.96')
print(f"Remaining v10.95: {remaining}")
print(f"Total v10.96: {new_ver}")

for check_id in ['whitaker-ag-heads-up-kushner-squashed-feb2019',
                  'sdny-punch-mueller-head-fake-china-warfare-mar2019',
                  'summers-pr-advising-affair-yellow-peril-apr2019',
                  'malpass-world-bank-sasse-child-rapist-feb2019']:
    if check_id in verify:
        print(f"  FOUND: {check_id}")
    else:
        print(f"  MISSING: {check_id}")

f_close2 = find_array_closing(verify, 'FINDINGS_DATA')
t_close2 = find_array_closing(verify, 'TIMELINE_DATA')
print(f"Post-update FINDINGS_DATA closing at: {f_close2} (valid: {f_close2 != -1})")
print(f"Post-update TIMELINE_DATA closing at: {t_close2} (valid: {t_close2 != -1})")
print(f"Arrays at different positions: {f_close2 != t_close2}")
