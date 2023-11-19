import json
from model.bulletpoint import BulletPoint


class Headline:
    def __init__(self, id: int, title: str, bulletpoints: [BulletPoint]):
        self.id = id
        self.title = title
        self.bulletpoints = bulletpoints

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "bulletpoints": [bulletpoint.serialize() for bulletpoint in self.bulletpoints]
        }


class HeadlineResponse:
    def __init__(self, headlines: [Headline]):
        self.headlines = headlines

    def serialize(self):
        return {
            "headlines": [headline.serialize() for headline in self.headlines]
        }
