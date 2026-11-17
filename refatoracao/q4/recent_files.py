class RecentFiles:

    def __init__(self, limit: int):
        self._items: list[str] = []
        self._limit = limit

    def add_file(self, path: str) -> None:
        if path in self._items:
            self._items.remove(path)
        self._items.insert(0, path)
        while len(self._items) > self._limit:
            self._items.pop()

    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, index: int) -> str:
        return self._items[index]

    def __iter__(self):
        return iter(self._items)