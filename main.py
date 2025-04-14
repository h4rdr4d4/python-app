import requests

URL = "https://db.ygoprodeck.com/api/v7/cardinfo.php{}"

# def get_card_info_by_name(name: str, race: str, atk: int, deff: int, level: int, attribute: str, archetype: str) -> dict:
def get_card_info_by_name(name: str) -> dict:
    """
    Fetches card information from the YGOProDeck API by card name.
    """
    name = name.replace(" ", "%20") # URL encode spaces
    response = requests.get(URL.format(f"?fname={name}"))
    if response.status_code == 200:
        return response.json()
    else:
        return None

ygo_card_by_name = get_card_info_by_name("Reasoning")
# ygo_db = ygo_db.json()
# print(ygo_card_by_name)
if ygo_card_by_name:
    for card in ygo_card_by_name['data']:
        try:
            banlist_status = card['banlist_info']['ban_tcg']
            is_banned = True if banlist_status == 'Forbidden' else False
        except:
            is_banned = False
        if is_banned:
            pass
        else:
            print(card['name'])
            monster_effect = card['desc'] if card['type'] != 'Normal Monster' else "No effect."
            print(f"Effect: {monster_effect}")
            print("\n")
else:
    print("Card not found or API error.")



# Keys

# id
# name
# typeline ([Spellcaster, Effect])
# type (Effect Monster, Fusion Monster)
# desc (efeito)
# humanReadableCardType (Fusion Effect Monster)
# race (Spellcaster)
# atk
# def
# level
# attribute
# archetype
