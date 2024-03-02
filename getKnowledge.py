import mcwiki

class mcwiki:
    def retrieveKnowledge(pageName):
        try:
            return mcwiki.load(pageName)
        except:
            print("Page not found")
            return "page not found"