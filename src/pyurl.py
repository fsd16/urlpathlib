class URL:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")

    def __truediv__(self, other):
        other = str(other).lstrip("/")
        return URL(f"{self.base_url}/{other}")

    def __str__(self):
        return self.base_url
