class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = []
        for word in title.lower().split(" "):
            if len(word) >= 3:
                words.append(word.title())
            else:
                words.append(word)
        return " ".join(words)

        