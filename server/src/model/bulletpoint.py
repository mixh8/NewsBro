class BulletPoint:
    def __init__(self, id: int, value: str, sources: [str]):
        self.id = id
        self.value = value
        self.sources = sources
    
    def serialize(self):
        return {
            "id": self.id,
            "value": self.value,
            "sources": self.sources
        }
