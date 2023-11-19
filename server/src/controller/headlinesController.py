from model.headline import Headline, HeadlineResponse
from model.bulletpoint import BulletPoint

class HeadlinesController:
    def __init__(self):
        bulletpoints1 = [
            BulletPoint(1, "mich the boss", ["michel", "nasa"]),
            BulletPoint(2, "mich the boss", ["michel", "nasa"]),
            BulletPoint(3, "mich the boss", ["michel", "nasa"])
        ]
        bulletpoints2 = [
            BulletPoint(4, "mich the boss", ["michel", "nasa"]),
            BulletPoint(5, "mich the boss", ["michel", "nasa"]),
            BulletPoint(6, "mich the boss", ["michel", "nasa"])
        ]

        headline1 = Headline(1, "Mich the boss", bulletpoints1)
        headline2 = Headline(2, "Mich the boss", bulletpoints2)
        self.headlines = [headline1, headline2]
    
    def getHeadlines(self) -> HeadlineResponse:
        headlineResponse = HeadlineResponse(self.headlines)
        return headlineResponse
    
    def getHeadlineById(self, id) -> Headline:
        for headline in self.headlines:
            if int(headline.id) == int(id):
                return headline
            
        
