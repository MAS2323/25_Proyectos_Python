from translate import Translator

translaitor = Translator(from_lang='spanish', to_lang='english')

txt = input("Que quieres traducir? ")

res = translaitor.translate(txt)

print(res)
