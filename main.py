from script import validate_email, validate_name, top_level_domains

#Chamando as funções
nome = validate_name(str(input('Digite seu nome: ')))
email = validate_email(str(input('Digite seu email: ')))

print(nome)
print(email)