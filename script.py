#Lista de dominios para teste
top_level_domains = [
    ".org",
    ".net",
    ".edu",
    ".ac",
    ".gov",
    ".com",
    ".io"
]

#Variavel para validar o nome de usuario, onde deve conter mais de 2 caracteres
#Precisa conter o tipo de dado string
def validate_name(name_data):
    if type(name_data) == str and len(name_data) > 2:
        return True, 'True' 
    else:
        return False, 'False' 

#Verifica se o email é valido, se possui @ e se está na lista de dominios.    
def validate_email(email_data):
    if '@' in email_data:
        verify_email = email_data.split('.')
        if '.'+ verify_email[-1] in top_level_domains:
            return True, 'True' 
        else:
            return False, 'False' 
    else:
        return False, 'False' 