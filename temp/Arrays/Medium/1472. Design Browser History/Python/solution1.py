# O(n) space - where n is the number of webpages visited
class BrowserHistory:

    # O(1) time
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.idx = 0

    # O(1) time
    def visit(self, url: str) -> None:
        self.history = self.history[:self.idx+1]
        self.history.append(url)
        self.idx += 1

    # O(1) time
    def back(self, steps: int) -> str:
        self.idx = max(0, self.idx - steps)
        return self.history[self.idx]

    # O(1) time
    def forward(self, steps: int) -> str:
        self.idx = min(len(self.history) - 1, self.idx + steps)
        return self.history[self.idx]