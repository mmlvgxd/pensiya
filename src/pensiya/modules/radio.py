from pyradios import RadioBrowser


browser = RadioBrowser()


def search(name: str) -> None:
    return browser.search(name=name, limit=10, hidebroken=True)
