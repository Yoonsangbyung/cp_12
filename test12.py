class pasta:
    def __init__(self, pasta_type,sauce):
        self.pasta_type = pasta_type
        self.sauce = sauce

    def cook(self):
        return f"{self.pasta_type} 파스타가 {self.sauce} 소스와 함께 완성되었습니다."

spaghetti = pasta("스파게티","토마토")
linguine = pasta("알리오 올리오", "올리브 유")

print(spaghetti.cook())
print(linguine.cook())



