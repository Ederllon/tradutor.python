from translate import Translator

translator = Translator(to_lang="pt")  


texto = str(input('Insira uma frase para traduzir para pt/br: '))


traducao = translator.translate(texto)


print(f"Texto original: {texto}")
print(f"Tradução para o Português: {traducao}")
