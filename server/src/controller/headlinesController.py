from model.headline import Headline, HeadlineResponse
from model.bulletpoint import BulletPoint
import json

class HeadlinesController:
    def __init__(self):
        headline = self.parseJsonOutput()
        self.headlines = [headline]

    def parseJsonOutput(self):
        with open('controller/output.json', 'r') as file:
            parsed_data = json.load(file)
        
        bulletpoints = []
        for i in range(len(parsed_data)):
            text = parsed_data[i]["text"]
            publishers = parsed_data[i]["publishers"]
            bulletpoint = BulletPoint(i, text, publishers)
            bulletpoints.append(bulletpoint)
        
        return Headline(1, "Sam Altman & OpenAI News", bulletpoints)

    
    def getHeadlines(self) -> HeadlineResponse:
        headlineResponse = HeadlineResponse(self.headlines)
        return headlineResponse
    
    def getHeadlineById(self, id) -> Headline:
        for headline in self.headlines:
            if int(headline.id) == int(id):
                return headline
            
        
