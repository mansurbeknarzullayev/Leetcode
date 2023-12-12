class BrowserHistory:

    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.ind = 0

    def visit(self, url: str) -> None:
        self.urls = self.urls[:self.ind + 1]
        self.urls.append(url)
        self.ind += 1

    def back(self, steps: int) -> str:
        self.ind = max(0, self.ind - steps)
        return self.urls[self.ind]

    def forward(self, steps: int) -> str:
        self.ind = min(self.ind + steps, len(self.urls) - 1)
        return self.urls[self.ind]
