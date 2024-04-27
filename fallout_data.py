####################### text strings ########################

ROBCO_HEADERS = (
    'ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM',
    'COPYRIGHT 2075-2077 ROBCO INDUSTRIES',
    '-SERVER 6-',
    ''
)

TURRET_HEADERS = (
    '-RobCo Trespasser Management System-',
    '====================================',
    ''
)

TURRET_HEADERS2 = (
    'RobcOS v.85',
    '(C)2076 RobCo',
    '========================',
    '| User Log:',
    '| >> Administrator (RobCoID 2398-H)',
    '| >> New_Admin: FIRE PUP',
    '| Welcome new user, FIRE PUP',
    '| >> New_Targeting_Param:',
    '| >>> FIRE PUP_userGroup',
    ''
)

SOFT_HEADERS = (
    '\tSoftLock Solutions, Inc',
    '"Your Security is Our Security"',
    '>\\ Welcome, USER',
    ''
)

MAIN_MENU = (
    'Lock Control',
    'Turret Control',
    'Read Log',
    'Log out'
)

LOCK_MENU = {
    'LOCKED': ["Disengage Lock", "Engage Lock"],
    'RETURN': ["Return"]
}


TURRET_MENU = {
    'TARGETING': ["Re-configure Targeting Parameters", "<!>WARNING: No Targeting Data<!>"],
    'ENABLED': ["Deactivate Turret System", "Activate Turret System"],
    'RETURN': ["Return"]
}

MAIN_MSGS = (
    '',
    '',
    '',
    'Shutting Down.'
)

TURRET_MSGS = {
    'TARGETING': ['Target Data Cleared. Exercise Caution.', '<!>Please Exercise Caution<!>'],
    'ENABLED': ['Powering Down...', 'Booting...'],
    'RETURN': ['']
}

LOCK_MSGS = {
    'LOCKED': ['Clearance granted, Unlocking...', 'Clearance granted, Locking...'],
    'RETURN': ['']
}

TURRET_CONDS = {
    'TARGETING': 0,
    'ENABLED': 0,
    'RETURN': 0
}

LOCK_CONDS = {
    'LOCKED': 0,
    'RETURN': 0
}

LOGS = {
    'Megaton             - Afterword': """USER: MOIRA BROWN
PASS: ***********

Date: 09.10.2297

Welcome, MOIRA. It is another lovely day for science!

DAILY LOG:

Experiment Reports:
Irradiated Agriculture—Good response from mutfruit, strangely aggressive response to baseline sample. Purified water very helpful.
Deathclaw Communication—No language that I can discern, unless "Mutilating assistants" counts. What would they have to say, anyway?
Jefferson Purifier - Guards still refuse to allow access to see how the Purifier works. They say it's to prevent sabotage, but I think they aren't entirely certain.

Personal Note:
Just shipped out another crate of survival guides, and the caravans just can't seem to get enough of them. Sheriff Simms says they've really put Megaton on the map—pretty ironic, since I've had to redraw that map about a million times since the first edition came out 20 years ago. At least all the attention means there's no shortage of assistants, but I'm never getting another assistant like the Lone Wanderer who stumbled into my shop so long ago.

Just about everyone in the Capital Wasteland has a story about the Lone Wanderer, even though precious few ever really knew him. But that doesn't stop them from telling crazy tall tales about how he saved their lives, or blew up a mountain, or ate a car or something. Heck, if you get Simms drunk, he'll tell you that his dad died because of the Wanderer, even though he saved the town. People can't even agree on whether the Wanderer was a man or a woman, much less a saint or a monster. But they all agree on one thing: the Lone Wanderer changed the Capital Wasteland.

Of course, that's why I'm working on the new book, compiling the best and most useful tales of the Lone Wanderer for the next generation. It's not easy sorting out all the conflicting stories, but that'll be half of the fun for the readers. More importantly, between all of those crazy stories of bravery, barbarity, and everything in-between, we can all find a reason to keep on fighting our war for survival.

I guess some things never change, huh?""",
    'ERR                 - Ikkm00:Mvkz6x1ml:Nqtm': "[ERROR HX40-399: invalid decry.key]",
    'Nuka Cola           - Quantum Progress Report 0041': """Isotope CE770 has proven to be a disastrous failure. All of the test subjects suffered severe internal organ failures and died within three days of ingestion. We recommend the immediate destruction of container A32 in the production rooms and suggest switching to isotope CE772. Please send standard "Nuka Condolences" Fruit and Cheese Packages to test group member's families.""",
    'Nuka Cola           - Quantum Progress Report 0055': "Isotope CE772 has proven too damaging to the initial test group which now needs to be disbanded due to their reluctance to continue in our program. This group has suffered 4 fatalities, 12 major internal organ failures and 32 internal radiation burns. This is an unacceptable number of issues in a given test group and recommend we switch to an alternate isotope (such as CE774 or UR993).",
    'Nuka Cola           - Quantum Progress Report 0067': "Test subjects in the Nuka-Cola Quantum program are responding well to the reconfigured taste and the new isotope. The only listed side effects from the group are: 3 cases of dizziness, 1 case of nausea and 1 case of impaired vision. We find from a sampling of 50 that this is an acceptable number of cases and approve this product for production.",
    'Nuka Cola           - Company Announcement': "The Nuka-Cola Corporation is pleased to announce to all it's employees that the first shipments of our Nuka-Cola Quantum® are on their way to retailers in the Washington D.C. area! This flagship test market program is the culmination of a three year research program to bring the refreshing taste of Quantum to market. Congratulations to all employees on a job well done!",
    'Nuka Cola           - New Flavor Coming!': """Attention all Nuka-Cola Corporation Employees

We are very proud to announce that R&D has been completed on Nuka-Cola Clear! With an only minimal loss of life, we've been able to modify the look of Nuka-Cola but give it the same great taste. We will be submitting the product to Marketing shortly for bottle design and advertising strategies. From all of us in the Research Department, thanks for the support!""",
    'Nuka Cola           - From: Marketing': """The following locations have been accepted into the flagship Nuka-Cola Quantum test program. Please ensure that 1 (one) crate of Quantum is included with their regular deliveries along with the advertising package provided by our Marketing Department.

1. Paradise Falls Shopping Mart
2. Super Duper Mart
3. Old Olney Grocery""",
    'Nuka Cola           - Packing Line Instructions': """Welcome to the Nuka-Cola Packing Line Operator's Station! You are now instrumental in getting Nuka-Cola from our factory and to the public, so please read the simple instructions below. If you need assistance, please call x347 and ask for your Line Supervisor.

1. Access the Packing Terminal and choose desired inventory to load into Sorting Units.
2. Select "Activate Packing Line."
3. Monitor the Packing Line by listening for things such as mechanical screeching, explosions and/or human cries for help.
4. If there is an emergency, DO NOT PANIC! Simply call x347 and ask for your Line Supervisor. The Packing Line will automatically shut down in the event of an issue.

Remember, only you can prevent inventory loss by being attentive and vigilant!""",
    'Nuka Cola           - Packing Line Notice': """Attention all Packing Line employees!

Due to an oversight by the design department, the new Nuka-Cola Quantum bottles are slightly heavier than the standard Nuka-Cola bottles. As a result, the Packing Line is prone to jams and may cause damage to the equipment. Please DO NOT load Nuka-Cola Quantum bottles into the Sorting Units until further notice. All test samples of Quantum will be packaged by hand until a solution is reached.""",
    'Nuka Cola           - Stage One': """Stage One of the Nuka-Cola Quantum marketing will include: 2 (two) 15 (fifteen)-second television commercials, 4 (four) 10 (ten)-second radio commercials and a highway billboard campaign.

The spots on TV and radio will tease the consumer with the blue glow of the new drink, never showing the bottle in an illuminated environment. The billboard will show the bottle's blue silhouette on a black background.

The tag line will be "Try something new... Go Blue!". The name will not be revealed until Stage Two.""",
    'Nuka Cola           - Stage Two': """Stage Two of the Nuka-Cola Quantum marketing will include: 2 (two) 30 (thirty)-second television commercials, 4 (four) 15 (fifteen)-second radio commercials and a highway billboard campaign.

In this stage, the name "Quantum" will be revealed and the bottle shown in full view. We will emphasize the drink's new energy content and flavor.

The tag line will be "Take the leap... enjoy a Quantum!" """,
    'Nuka Cola           - Stage Three': """Stage Three of the Nuka-Cola Quantum marketing will include: 4 (four) 30 (thirty)-second television commercials, 4 (four) 15 (fifteen)-second radio commercials and a highway billboard campaign.

In this final stage we will aggressively compare the drink to other competitors and show their inferiority using hired actors at "taste tests". The actors will read pre-written scripts approved by our department. The text should give an authentic "on the spot" impression but still clearly point out Quantum's strengths.

The tag line will remain: "Take the leap... enjoy a Quantum!" """,
    'Capitol Post        - Commies Crushed - Alaska Liberated!': """By Dorothy Proud

Capital Post Staff Writer

In the late evening hours of January 10th, brave American Army forces launched an all-out offensive against the entrenched Chinese Communist invaders in the beleaguered seaport of Anchorage, Alaska, destroying all opposition and finally liberating the city after more than ten years of Chinese occupation.

No red-blooded American can ever forget that terrible winter of 2066, when Chairman Cheng's commie cutthroats mercilessly invaded the icy extension of the United States, in an unprecedented act of foreign aggression that sent shockwaves all the way back to our nation's Capital.

But the nightmare is finally over, and America, always the home of the brave, is once again the land of the free.""",
    'Capitol Post        - Food Riots Rile Feds': """By Walter "Street Beat" Munroe

Capital Post Staff Writer

It would appear that Washington's tolerance for American social disorder has finally reached its breaking point.

In a recent public statement, White House spokesman Warren Eccleston said:

"Okay, Americans are hungry. We get it. Well I've got news for you - things are tough all over, people. The President himself has been forced to substitute cube steak for his nightly prime rib, and the only wine available is a detestable Chateau Montrose 2043. But does he whine? Does he take to the streets like a rabid Red? So please, good people, please. Wait in line. Get your food. And then go home. We're Americans! We do not solve our problems with violence." """,
    'Capitol Post        - U.S. to Annex Canada!': """By Dorothy Proud

Capital Post Staff Writer

In a move that is being widely viewed as both necessary and overdue, the United States military today declared that they will begin the immediate annexation of the country of Canada.

The decision comes after a long and contentious relationship with the Canadian government that began shortly after the Chinese invasion of Anchorage, Alaska in the winter of 2066. The Canadian leadership at that time expressed its opposition to American troops passing through their country or traversing their airspace, but ultimately capitulated.

Tensions with our neighbor to the north have only escalated since then as the United States has found itself relying heavily on Canada's natural resources - including wood cultivated from the country's great Timberland forests - to maintain the war effort against China.

But it was a recent near-sabotage of the Alaskan pipeline that finally tipped the American military's hand.

"That was the last straw," said Buzz Babcock, commander of U.S. forces in Canada. "You know what's been stopping the Reds from pouring into downtown Juneau? American soldiers, that's what. And now we've got to worry about someone - Chinese, Alaskan, or otherwise - taking out the pipeline? I don't think so. Effectively immediately, United States troops are beginning a complete takeover of all Canadian assets and resources. Little America is ours. But let's face it - it always has been." """,
    'Capitol Post        - Development of Super Weapon Confirmed': """By Walter "Street Beat" Munroe

Capital Post Staff Writer

In a startling turnaround from their previous policy of complete covert development, the United States Army has confirmed that they are indeed working on a new super weapon, one designed specifically to crush the Red Chinese invasion force and liberate occupied Anchorage, Alaska once and for all.

Speaking at an Army press conference at the Pentagon, General Constantine Chase stated: "No more secrets. The time has come to lay all our cards on the table, so the Chinese can see with their own eyes that we've got the winning hand. The United States Army is proud to announce that for the first time in history, General Atomics International and RobCo have joined forces to create for this great country a super weapon that will leave every single yellow-bellied Red shaking in their Commie booties."

Unfortunately for our readers, that's as specific as Chase is willing to get. While he and the Army are ready for China to know the U.S. is developing a new weapon, they're not quite ready to divulge just what it is, or when it will be ready for deployment.

"All in due time, all in due time. Rest assured, when this weapon is complete, liberty will come to Anchorage... and Hell will follow." """,
    'Capitol Post        - United Nations Disbanded!': """By Dorothy Proud

Capital Post Staff Writer

In a crushing blow to foreign relations and world peace, the United Nations yesterday was completely disbanded, leaving its member nations to fend for themselves in these trying times.

Many had considered the United Nations the best hope for brokering a ceasefire between the European Commonwealth and the nations of the Middle East, but such an intervention is now impossible.

In a somber press conference at the United Nations building in New York City, United Nations president Sakugama Okiri had this to say: "It is a sad day for the United States. Sadder still for the world. An era of relative peace and prosperity has come to a tragic end. The Resources Wars are upon us, and in my humble opinion the United Nations is needed now more than ever. Sadly, the world disagrees."

Those nations that have not already moved out of the immense headquarters will have completely vacated the premises by the end of the week. Several organizations have already begun bidding on the prime real estate, but children's toy retailer Bumbalo's seems determined to transform the building into their new East Coast superstore.""",
    'Capitol Post        - Pint-Sized Slasher: More than Myth?': """By Walter "Street Beat" Munroe

Capital Post Staff Writer

What American child alive hasn't heard the story of the Pint-Sized Slasher, that diminutive demon in a clown mask who stalks and slashes the innocent residents of supposedly safe suburbia? It's just one of the many folk stories parents use to scare their youngsters into behaving themselves. Or is it?

According to Germantown police chief Joseph Field, the Pint-Sized Slasher may be more real than many people would like to admit. "After reviewing the autopsy results of the Linden Street slayings, we have confirmed that the force and direction of every knife wound are consistent with an attack from a much smaller assailant. A child, to be precise."

Add to the sinister forensic findings this statement from Christopher Atkinson, the one surviving victim of the adolescent assassin, and it becomes clear that the Pint-Sized Slasher does indeed walk among us: "The clown! The clown! He's going to kill us all, do you understand me? He stabbed my brother Shaun right in the face! He killed my brother! The little clown!"

But assuming the Pint-Sized Slasher is indeed a real, tangible threat to the peace loving residents of D.C. suburbia, one question remains: why? What could possible motivate a child to don a clown mask and murder innocent people in cold blood? We may never know. At least not until the miniature maniac is brought to justice. Until then, all we can do is lock our doors, kiss our children goodnight… and pray they live to see morning.""",
    'Robot Repair Center - Note From Frank': """I can't take it anymore, Bob. I don't trust those turrets in Sector A. I swear I saw one track me the other day when I left work a little late. If that thing opens up on me, I'm screwed, since the bastard Feds suspended workman's comp as part of the "war effort." Hell.

Snake helped me smuggle in some pulse grenades that I locked away in the box under my desk. I tried one out on our Handy at the house and the missus nearly killed me! Knocks 'em out like a light. If you ever need one just grab the key from behind my terminal and use it to unlock the box. You can't say I never did anything for you! See you around buddy.

Oh, and stop throwing those staples over at me, they get on the floor and you know how I like to take my shoes off during the day.""",
    'Robot Repair Center - Note from Management regarding Sector B': """<MEMO>
attn: Warehouse/Repair employees

Please make sure the main platform in the Repair Sector is properly raised before releasing the repaired bots from their pods. All units receive fimware programming to make their way to the main entrance and await pickup. Let's get them there safely and not repeat last week's accident involving a Protectron falling to the lower level. That error cost us time, money, and was an embarrassment to the company and our DCTA account client.

-- Management""",
   'L.O.B. Enterprises - Email: Weapon Practice Tonight?': """From: McCoy, Derrick
To: Entire Company

Subject: Weapon Practice Tonight?

If anyone would like to practice with their "low-grade, military-class" company issue, Sam and I will be shooting rounds off in the yard at 7:00PM.

BYOB.""",
    'L.O.B. Enterprises - Re: Weapon Practice': """From: McAndrews, Jeanne
To: McCoy, Derrick
Subject: Re: Weapon Practice Tonight?
Sure, I'll definitely be there. I wouldn't miss a chance to have my weapon accidentally discharge and hit that "grenade" in Sam's pocket.""",
    'L.O.B. Enterprises - Sent Item: MAN THE DOORS!!': """From: Warring, Joanna
To: Entire Company

Subject: Oh, !@#

THEY'RE HERE! MAN THE DOORS! THE FEDS ARE HERE!""",
    'L.O.B. Enterprises - All Personnel: Caps in Emails': """From: Director of Human Resources
To: Entire Company

Subject: Caps in Emails

I would like to remind everyone that, despite the impending Federal invasion, standard company policy is still in effect.

Specifically, do not write emails in all caps. This style is offensive to your coworkers.

Thank you for your cooperation.""",
    'L.O.B. Enterprises - Memo: Responding to Federal Raids': """Internal Memorandum

Due to the increased awareness of our upcoming project milestone, you and your fellow employees may be required to initiate Emergency Defensive Procedures, as outlined in the Employee Handbook. If required, please review policies #H31, #L04, #L05, #P55, #T01.

Your continued adherence to company policy is appreciated.""",
    'L.O.B. Enterprises - Weapons Policy #H31': """Weapons Policy #H31

As standard policy, all employees are required to carry low-grade military-class weaponry at all times (see HR Policy#A12). In the event of a hostile takeover, your desk can be used as a makeshift barricade. Position the desk between yourself and your opponent, then crouch behind the desk while firing any weapon approved on Form B43-2.

NOTE: Cafeteria privileges will be suspended in the event of a hostile takeover.""",
    'L.O.B. Enterprises - Evacuation Policy #T01': """Evacuation Policy #T01

In the event of emergency evacuation scenario F1-a, all executive staff not under penalty are to be evacuated from the building via the archives and connected civic tunnels. All other personnel will remain behind to safeguard active projvects{sic} from imminent Federal inquiry.

All employees are tasked with barricading the main doors, and will be further tasked with keeping the building secured until 5:00 PM, or until the Chief of Security enacts protocol #T81. The usual lunch break will be suspended for that day.""",
    'L.O.B. Enterprises - Inclement Weather Policy #C31': """Inclement Weather Policy #C31

In the event of extreme winter (nuclear) conditions, all employees are required to proceed to human resources and complete forms D87-a, D87-b, H04-1, and A14-3, addendum 7. In accordance with company policy #L83, employees will be issued iodine tablets, personal geiger counter, meal rations, and sworn into the sovereign L.O.B. republic.""",
    'L.O.B. Enterprises - Lab Report: Prototype ZRIN-363': """Lab Report: Prototype ZRIN-363

Experimental prototype makes extensive use of hardware common to liquid ammunition flame projection weapons. While initial test results were impressive, extreme weight of unit (118.3kg) and fume inhalation rendered most test subjects incapable of firing the unit or remaining conscious under typical field conditions.""",
    'L.O.B. Enterprises - Lab Report: Prototype ZRIN-375': """Lab Report: Prototype ZRIN-375

Prototype introduces proprietary ammunition type. Conventional 10mm shells house a caplet containing amalgamating agents. When the caplet was broken in lab tests, localized fireburst and shrapnel projection met requirements for project. However, in field tests amalgam caplet ammunition proved too fragile, and several detonated from excessive vibration or walk speed.""",
    'L.O.B. Enterprises - Lab Report: Prototype ZRIN-401': """Lab Report: Prototype ZRIN-401

Prototype attempts to refine results of acumist coating within weapon barrel. Initial tests showed promise. As predicted, delivery friction super-heats projectile as it is delivered from the weapon, and conventional 10mm ammunition can be used. However; during live-fire testing, subjects firing the weapon in rapid succession suffered severe burns to the fingers and palm.""",
    'L.O.B. Enterprises - Lab Report: Prototype ZRIN-418': """Lab Report: Prototype ZRIN-418

Prototype refines acumist barrel experiments by addition of retardant jacketing, as well as internal heat diffusers. Rate of fire diminished from un-modified version of weapon. Conventional 10mm ammunition does not fully liquefy until impact, giving the 418 exceptional accuracy compared to earlier prototypes. Live-fire tests report no major casualties. Recommend ZRIN-418 as production candidate.""",

}

LOG_NAMES = list(LOGS.keys())
LOG_NAMES.extend(["Return"])
LOG_RET_ID = len(LOG_NAMES) - 1
