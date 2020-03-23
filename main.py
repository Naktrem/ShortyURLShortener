import rumps
import clipboard
import validators
import pyshorteners as pst

shortenerMenuItems = []
chosenShortener = ""
parameterlessShorteners = ["tinyurl", "chilpit", "clickru", "dagd", "isgd", "osdb", "owly", "qpsru"]

class URLShortenerApp(rumps.App):

    def choose(self, sender):
        for item in app.menu.values()[0].values():
            item.state = False
        sender.state = True

        for i in pst.Shortener().available_shorteners:
            if i.__eq__(sender.key):
                global chosenShortener
                chosenShortener = i

    @rumps.clicked("Shorten!")
    def shorten(self, _):
        s = pst.Shortener()
        retrieved_url = clipboard.paste()
        is_valid = validators.url(retrieved_url)
        if is_valid:
            if chosenShortener.__eq__(""):
                rumps.notification("Unspecified Shortener Service", "Please choose shortener service to use.", "")

            if chosenShortener.__eq__("chilpit"):
                clipboard.copy(s.chilpit.short(retrieved_url))
            elif chosenShortener.__eq__("clckru"):
                clipboard.copy(s.clckru.short(retrieved_url))
            elif chosenShortener.__eq__("dagd"):
                clipboard.copy(s.dagd.short(retrieved_url))
            elif chosenShortener.__eq__("isgd"):
                clipboard.copy(s.isgd.short(retrieved_url))
            elif chosenShortener.__eq__("osdb"):
                clipboard.copy(s.osdb.short(retrieved_url))
            elif chosenShortener.__eq__("owly"):
                clipboard.copy(s.owly.short(retrieved_url))
            elif chosenShortener.__eq__("qpsru"):
                clipboard.copy(s.qpsru.short(retrieved_url))
            elif chosenShortener.__eq__("tinyurl"):
                clipboard.copy(s.tinyurl.short(retrieved_url))
        else:
            rumps.notification("Invalid URL", "Make sure to copy URL in correct form.", "")
            clipboard.copy("Invalid URL")

    #Replace parameterlessShorteners with pst.Shortener().available_shorteners in order to include every service inside pyshorteners
    for i in parameterlessShorteners:
        shortenerMenuItems.append(rumps.MenuItem(i.capitalize(), callback=choose, key=i))

if __name__ == "__main__":
    app = URLShortenerApp("-><-", icon="./ShortIcon.png")
    app.menu = [
        {'Shortener Service':
            shortenerMenuItems
        },
        None
    ]

    app.run()
