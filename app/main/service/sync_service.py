import requests
import json
import copy
from ..config import sync_url, sync_enum_url
from ..util.enum import from_string, CARD_CLASS, CARD_TYPE, CARD_RARITY

from app.main import db
from app.main.model.card import Card, CardTranslation, CardSet

class SyncService:

    @staticmethod
    def run_sync(data):
        enums = SyncService._sync_enums()
        counts = SyncService._sync_cards(enums)

        db.session.commit()
        data = {
            'message': "Successfully ran sync",
            'counts': counts,
        }
        return data, 200

    @staticmethod
    def _sync_cards(enums):
        r = requests.get(url=sync_url)
        cards = r.json()

        counts = {
            'added': 0,
            'modified': 0,
            'total_cards': len(cards)
        }

        for json_card in cards:
            db_card = Card.query.filter_by(id=json_card['id']).first()
            result = SyncService._save_card(json_card, db_card, enums)

            if result:
                counts[result] += 1

        return counts

    @staticmethod
    def _sync_enums():
        r = requests.get(url=sync_enum_url)
        enums = r.json()

        for set in enums['CardSet']:
            # ignore duplicates that aren't used as card sets directly
            if set in ['FP1', 'FP2', 'PE1', 'PE2', 'REWARD', 'TEMP1']:
                continue

            db_set = CardSet.query.filter_by(id=int(enums['CardSet'][set])).first()
            if db_set:
                db_set.api_name = set
            else:
                new_set = CardSet(id=enums['CardSet'][set], api_name=set)
                db.session.add(new_set)

        return {
            'card_sets': enums['CardSet']
        }


    @staticmethod
    def _save_card(json_card, db_card, enums):
        if 'dbfId' not in json_card:
            return

        result = None
        card_details = CardOperations.parse_json_card(json_card, enums)

        if db_card:
            db_details = copy.deepcopy(db_card.__dict__)
            del db_details['_sa_instance_state']
            if db_details != card_details:
                result = "modified"
                CardOperations.update_card_details(db_card, card_details)

            json_translations = json_card['name']
            db_translations = {t.locale: t.name for t in db_card.translations}
            if db_translations != json_translations:
                result = "modified"
                print("translations {}: {}".format(result, json_card['name']['enUS']))
                CardOperations.update_card_translations(db_card, json_translations, db_translations)

        if not db_card:
            result = "added"
            CardOperations.add_card(card_details, json_card['name'])

        return result


class CardOperations:
    @staticmethod
    def parse_json_card(json_card, enums):
        set_id = enums['card_sets'].get(json_card['set'], None) if 'set' in json_card else None
        rarity = from_string(CARD_RARITY, json_card['rarity']) if 'rarity' in json_card else None
        classes = (from_string(CARD_CLASS, json_card['classes'])
                   if 'classes' in json_card else
                   from_string(CARD_CLASS, [json_card.get('cardClass', None)], CARD_CLASS.NEUTRAL))

        return dict(
            id=json_card['id'],
            artist=json_card.get('artist', None),
            attack=json_card.get('attack', None),
            classes=json.dumps(classes),
            collectible=json_card.get('collectible', False),
            cost=json_card.get('cost', None),
            dbfid=json_card['dbfId'],
            flavor=(json.dumps(json_card['flavor']) if 'flavor' in json_card else None),
            health=json_card.get('health', None) or json_card.get('durability', None),
            name=json_card['name']['enUS'],
            rarity=rarity,
            set_id=set_id,
            text=(json.dumps(json_card['text']) if 'text' in json_card else None),
            type=from_string(CARD_TYPE, json_card['type']),
            tribes=json_card.get('race', None)
        )

    @staticmethod
    def add_card(card_details, translations):
        new_card = Card(**card_details)
        new_card.translations = [
            CardTranslation(card_id=card_details['id'], locale=l, name=translations[l])
            for l in translations]
        db.session.add(new_card)

    @staticmethod
    def update_card_details(db_card, card_details):
        for d in card_details:
            setattr(db_card, d, card_details[d])

    @staticmethod
    def update_card_translations(db_card, json_translations, db_translations):
        new_translations = list(set(json_translations.keys()) - set(db_translations.keys()))
        removed_translations = list(set(db_translations.keys()) - set(json_translations.keys()))

        for new in new_translations:
            db_card.translations.append(CardTranslation(card_id=db_card.id, locale=new, name=json_translations[new]))
        for removed in removed_translations:
            i = None
            for i in range(0, len(db_translations)):
                if db_translations[i].locale == removed:
                    break

            del db_translations[i]

        for translation in db_card.translations:
            translation.name = json_translations[translation.locale]
