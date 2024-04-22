def draw_cards(*args, **kwargs):
    cards = {}
    for name, card_type in args:
        cards[card_type] = cards.get(card_type, []) + [name]

    for name, card_type in kwargs.items():
        cards[card_type] = cards.get(card_type, []) + [name]

    monster_cards, spell_cards = [], []
    for key, value in cards.items():
        if key == "monster":
            monster_cards.append(value)
        else:
            spell_cards.append(value)

    monster_cards = sorted(*monster_cards, key=lambda x: x, reverse=True) if monster_cards else []
    spell_cards = sorted(*spell_cards) if spell_cards else []

    output = []
    if monster_cards:
        output.append("Monster cards:")
        for x in monster_cards:
            output.append(f"  ***{x}")

    if spell_cards:
        output.append("Spell cards:")
        for x in spell_cards:
            output.append(f"  $$${x}")

    return "\n".join(output)


print(draw_cards(
    ("cyber dragon", "monster"),
    freeze="spell", ))

print(draw_cards(
    ("celtic guardian", "monster"),
    ("earthquake", "spell"),
    ("fireball", "spell"),
    raigeki="spell",
    destroy="spell", ))

print(draw_cards(
    ("brave attack", "spell"),
    ("freeze", "spell"),
    lightning_bolt="spell",
    fireball="spell", ))
