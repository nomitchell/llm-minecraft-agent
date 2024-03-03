import mcwiki

page = mcwiki.load("Diamond")
print(page.extract(mcwiki.PARAGRAPH, index=1000))
