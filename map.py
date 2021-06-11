from items import *

room_warehouse = {
    "name": "Warehouse",

    "description":
    """
An old abandoned warehouse that used to be a car wash. It's around 2:30am
in the morning ,the only source of light in the room is the moonlight
through barred windows, a luminescent veil bouncing off the walls. You take
a deep breath bracing yourself for the mission to come. There is an old
wrench and a hacking device placed on the table.

    """,

    "alt_description":
    """The warehouse is the same as you left it, eerily quiet.""",

    "exits": {"forward": "Main Entrance to the Research Facility"},

    "items": [item_hacking_device,item_wrench,item_uniform,item_cap,item_map]
}

room_research = {
    "name": "Main Entrance",

    "description":
        """
As the doors swiftly part, you feel a sudden brush of warmth, the regal interior of
the facility masking its cruel purpose. No expense was wasted, fanciful furniture
dotting the lobby, whilst a large, marble statue of the founder graces the centre.
Ahead, you note a sign leading you to one of their no doubt exquisite bathrooms.
To your right you see a cooped up Security Booth, certainly leading to further rooms
in the facility. """,

    "alt_description":
    """You better hurry with your mission before you are spotted.""",

    "exits":  {"right": "Security Booth", "left" : "Bathroom"},

    "items": []
}

room_security = {
    "name": "Security Booth",

    "description":
    """
The booth is small and well lit, an array of CCTV screens displayed on the wall.
A keen eye would note several of the screens looping the same image repeatedly.
By the desk is a security guard, who is busy playing on their phone. Atop the
desk itself rests a cup of coffee, steam slowly wafting from its lid. There
is a key placed on the table.
""",

    "alt_description":
    """The cup of coffee is spilled across the desk, slowly dripping down
on the phone on the floor. The security guard is still unconscious.""",

    "exits":  {"back":"Main Entrance to the Research Facility"},

    "items": [item_key]
}

room_bathroom = {
    "name": "Bathroom",

    "description":
    """
Compared to the rest of the facility, the bathroom is rather bland and dull.
Simple stalls dot the room, matching sinks opposite them.Above, your eye catches
upon a mettalic vent, with a couple bolts already missing. You see that there is
a soap over there. """,

    "alt_description":
    """
The bathroom continues to look both bland and clean. With all the money in
the facility, they could at least improve their bathrooms?""",

    "exits": {"back":"Main Entrance to the Research Facility"},

    "items": [item_soap]
}

room_vent = {
    "name": "Vents",

    "description":
    """The vents are dark and narrow. They're a tight fit, but there's thankfully
just enough space to crawl. Occasionally, you catch a glimpse of other
rooms in the building on your way through. Most of them consist of
bland office rooms, however you do come across questionable operating
rooms...
You really hope it's not too late. """,

    "alt_description":
    """The vents are still dark and narrow.You're running out of time.""",

    "exits": {"down": "Main Corridor","back":"Bathroom"},

    "items": []
}

room_maincorridor = {
    "name": "Main Corridor",

    "description":
    """
The corridors have white walls and white floors like ones from a hospital, which is
ironic considering how this facility was built for a purpose opposite of that of a
hospital.""",

    "alt_description":
    """You fear that going backwards would endanger your mission.""",

    "exits": {"left": "Office","forward":"Laboratory F137","right":"Inner Corridor"},

    "items": []
}

room_office = {
    "name": "Office",

    "description":
    """
You enter an office, noticing the title "Director" on the door. A breeze blows
from an exit hatch in the ceiling. A pile of documents sits unsorted on the desk.
Glancing at the top document you see the name Moira. Thats the agent name.
She's here. There is a broken piece of a mirror and on the coffee table there is
a bottle of water to drink.""",

    "alt_description":
    """It's a decent room with a desk and a chair.""",

    "exits": {"back": "Main Corridor","up":"Roof"},

    "items": [item_mirror,item_water]
}

room_lab = {
    "name": "Labratory F137",

    "description":
    """This would look like a normal lab to someone oblivious to the facility's purpose.
For you, that is not the case. Only thing you notice is a canister of smoke.""",

    "alt_description":
    """The sooner you leave this horrifying building, the better.""",

    "exits": {"back": "Main Corridor"},

    "items": [item_smoke]
}

room_trappedRoom = {
    "name": "Inner Corridor",

    "description":
    """This is the room that kills.
You. Tread. Carefully.""",

    "alt_description":
    """All traps have been revealed and dodged.""",

    "exits": {"right": "Secret Laboratory","back":"Main Corridor","forward":"deathroom"},

    "items": []
}

room_deathroom = {
    "name": " Vault",

    "description":
    """You try and walk through the corridor, but as you step forward, you smell something
burning. The pain hits a moment later. You have died.""",

    "alt_description":
    """this may be unnecessary. edit as required.""",

    "exits": {"back":"Main Corridor"},

    "items":[]
}

room_vault_unlocked = {
    "name": "Vault ",

    "description":
    """
You step into the vault to find four people tied up with black bags covering their
heads. Unaware of who has entered, they start to tremble with fear. You take off
the bag off the person on the far left first, and find yourself looking into the
soft but scared eyes of the undercover agent. Your heart floods with relief. All
the hostages are also tied with a rope. You untie the rope and think that this
might be hopeful.""",

    "alt_description":
    """The vault is empty, all hostages safe for now.""",

    "exits": {"back": "Inner Corridor"},

    "items": [item_treasure,item_rope]

}

room_vault_locked = {
    "name": "Vault",

    "description":
    """You notice you're stood outside a vault, as big as a grage.
You run your hand over the door, realising it's metal.
       """,

    "alt_description":
    """You notice you're stood outside a vault, as big as a grage.
You run your hand over the door, realising it's metal.""",

    "exits": {"back": "Inner Corridor"},

    "items": []

}

room_secret_lab = {
    "name": "Secret Lab",

    "description":
    """You try to keep down the nausea from all the horrors brewing in this labratory.
    You notice a container full of acid.""",

    "alt_description":
    """The sooner you leave this horrifying building, the better.""",

    "exits": {"back": "Inner Corridor"},

    "items": [item_acid]
}

room_roof = {
    "name": "Roof",

    "description":
    """Evertyhing still seems quiet which means nobody has been alerted of your break in yet.""",

    "exits": {"back": "Vents"},

    "items": []
}

rooms = {
    "Warehouse":room_warehouse,
    "Roof":room_roof,
    "Main Entrance to the Research Facility":room_research,
    "Security Booth":room_security,
    "Bathroom":room_bathroom,
    "Vents":room_vent,
    "Main Corridor":room_maincorridor,
    "Office":room_office,
    "Laboratory F137":room_lab,
    "Inner Corridor":room_trappedRoom,
    "Vault locked":room_vault_locked,
    "Vault unlocked":room_vault_unlocked,
    "Secret Laboratory":room_secret_lab,
    "deathroom":room_deathroom
}
