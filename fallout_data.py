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
    'Logoff Terminal'
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
    'Megaton   - Afterword': """USER: MOIRA BROWN
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
    'ERR       - Ikkm00:Mvkz6x1ml:Nqtm': "[ERROR HX40-399: invalid decry.key]",
    'Nuka Cola - Quantum Progress Report 0041': """Isotope CE770 has proven to be a disastrous failure. All of the test subjects suffered severe internal organ failures and died within three days of ingestion. We recommend the immediate destruction of container A32 in the production rooms and suggest switching to isotope CE772. Please send standard "Nuka Condolences" Fruit and Cheese Packages to test group member's families.""",
    'Nuka Cola - Quantum Progress Report 0055': "Isotope CE772 has proven too damaging to the initial test group which now needs to be disbanded due to their reluctance to continue in our program. This group has suffered 4 fatalities, 12 major internal organ failures and 32 internal radiation burns. This is an unacceptable number of issues in a given test group and recommend we switch to an alternate isotope (such as CE774 or UR993).",
    'Nuka Cola - Quantum Progress Report 0067': "Test subjects in the Nuka-Cola Quantum program are responding well to the reconfigured taste and the new isotope. The only listed side effects from the group are: 3 cases of dizziness, 1 case of nausea and 1 case of impaired vision. We find from a sampling of 50 that this is an acceptable number of cases and approve this product for production.",
    'Nuka Cola - Company Announcement': "The Nuka-Cola Corporation is pleased to announce to all it's employees that the first shipments of our Nuka-Cola Quantum® are on their way to retailers in the Washington D.C. area! This flagship test market program is the culmination of a three year research program to bring the refreshing taste of Quantum to market. Congratulations to all employees on a job well done!",
    'Nuka Cola - New Flavor Coming!': """Attention all Nuka-Cola Corporation Employees

We are very proud to announce that R&D has been completed on Nuka-Cola Clear! With an only minimal loss of life, we've been able to modify the look of Nuka-Cola but give it the same great taste. We will be submitting the product to Marketing shortly for bottle design and advertising strategies. From all of us in the Research Department, thanks for the support!""",
    'Nuka Cola - From: Marketing': """The following locations have been accepted into the flagship Nuka-Cola Quantum test program. Please ensure that 1 (one) crate of Quantum is included with their regular deliveries along with the advertising package provided by our Marketing Department.

1. Paradise Falls Shopping Mart
2. Super Duper Mart
3. Old Olney Grocery""",
    'Nuka Cola - Packing Line Instructions': """Welcome to the Nuka-Cola Packing Line Operator's Station! You are now instrumental in getting Nuka-Cola from our factory and to the public, so please read the simple instructions below. If you need assistance, please call x347 and ask for your Line Supervisor.

1. Access the Packing Terminal and choose desired inventory to load into Sorting Units.
2. Select "Activate Packing Line."
3. Monitor the Packing Line by listening for things such as mechanical screeching, explosions and/or human cries for help.
4. If there is an emergency, DO NOT PANIC! Simply call x347 and ask for your Line Supervisor. The Packing Line will automatically shut down in the event of an issue.

Remember, only you can prevent inventory loss by being attentive and vigilant!""",
    'Nuka Cola - Packing Line Notice': """Attention all Packing Line employees!

Due to an oversight by the design department, the new Nuka-Cola Quantum bottles are slightly heavier than the standard Nuka-Cola bottles. As a result, the Packing Line is prone to jams and may cause damage to the equipment. Please DO NOT load Nuka-Cola Quantum bottles into the Sorting Units until further notice. All test samples of Quantum will be packaged by hand until a solution is reached.""",
    'Nuka Cola - Stage One': """Stage One of the Nuka-Cola Quantum marketing will include: 2 (two) 15 (fifteen)-second television commercials, 4 (four) 10 (ten)-second radio commercials and a highway billboard campaign.

The spots on TV and radio will tease the consumer with the blue glow of the new drink, never showing the bottle in an illuminated environment. The billboard will show the bottle's blue silhouette on a black background.

The tag line will be "Try something new... Go Blue!". The name will not be revealed until Stage Two.""",
    'Nuka Cola - Stage Two': """Stage Two of the Nuka-Cola Quantum marketing will include: 2 (two) 30 (thirty)-second television commercials, 4 (four) 15 (fifteen)-second radio commercials and a highway billboard campaign.

In this stage, the name "Quantum" will be revealed and the bottle shown in full view. We will emphasize the drink's new energy content and flavor.

The tag line will be "Take the leap... enjoy a Quantum!" """,
    'Nuka Cola - Stage Three': """Stage Three of the Nuka-Cola Quantum marketing will include: 4 (four) 30 (thirty)-second television commercials, 4 (four) 15 (fifteen)-second radio commercials and a highway billboard campaign.

In this final stage we will aggressively compare the drink to other competitors and show their inferiority using hired actors at "taste tests". The actors will read pre-written scripts approved by our department. The text should give an authentic "on the spot" impression but still clearly point out Quantum's strengths.

The tag line will remain: "Take the leap... enjoy a Quantum!" """,




}

LOG_NAMES = list(LOGS.keys())
LOG_NAMES.extend(["Return"])
LOG_RET_ID = len(LOG_NAMES) - 1
