def from_string(enum, names, default=None):
    if type(names) is list or type(names) is tuple:
        return [from_string(enum, n) for n in names]
    else:
        return enum.__dict__.get(names, default)

class CARD_TYPE:
    MINION = 0
    SPELL = 1
    WEAPON = 2
    HERO = 3
    HERO_POWER = 4
    ENCHANTMENT = 5

class CARD_RARITY:
    FREE = 0
    COMMON = 1
    RARE = 2
    EPIC = 3
    LEGENDARY = 4

class CARD_CLASS:
    NEUTRAL = 0
    DRUID = 1
    HUNTER = 2
    MAGE = 3
    PALADIN = 4
    PRIEST = 5
    ROGUE = 6
    SHAMAN = 7
    WARLOCK = 8
    WARRIOR = 9
