def ajustar_indice(indice):
    indice_ajustado = int(indice) - 1
    return indice_ajustado


def ver_contatos(lista):
    if len(lista) == 0:
        print("Lista de contatos vazia.")
        return

    print("\nLista de contatos:")
    for indice, contato in enumerate(lista, start=1):
        favorito = "✔️" if contato["favorito"] else " "
        print(f"{indice}. Nome: {contato["nome"]}, Telefone: {
              contato["numero_contato"]}, E-mail: {contato["email"]}, Favorito: [{favorito}]")


def criar_contato(lista):
    nome = input("\nDigite o nome do contato: ")
    numero = input("\nDigite o número do contato: ")
    email = input("\nDigite o e-mail do contato: ")

    contato = {"nome": nome, "numero_contato": numero,
               "email": email, "favorito": False}

    lista.append(contato)
    print("Contato criado com sucesso.")
    return


def editar_contato(lista):
    ver_contatos(lista)
    indice_contato = input("Escolha o contato que você deseja editar: ")
    indice_ajustado = ajustar_indice(indice_contato)

    if indice_ajustado >= 0 and indice_ajustado < len(lista):
        while True:
            print("1. Nome")
            print("2. Número do telefone")
            print("3. E-mail")
            print("4. Sair")
            opcao_escolhida = input("Escolha qual opção você deseja: ")

            if opcao_escolhida == "1":
                nome = input("Digite o novo nome: ")
                lista[indice_ajustado]["nome"] = nome
                print("Contato editado com sucesso.")
            elif opcao_escolhida == "2":
                numero = input("Digite o novo número: ")
                lista[indice_ajustado]["numero_contato"] = numero
                print("Contato editado com sucesso.")
            elif opcao_escolhida == "3":
                email = input("Digite o novo e-mail: ")
                lista[indice_ajustado]["email"] = email
                print("Contato editado com sucesso.")
            elif opcao_escolhida == "4":
                return
    else:
        print("Indice incorreto.")
        return


def contato_favorito(lista):
    ver_contatos(lista)
    indice_contato = input("Escolha o contato que você deseja favoritar: ")
    indice_ajustado = ajustar_indice(indice_contato)

    if indice_ajustado >= 0 and indice_ajustado < len(lista):
        lista[indice_ajustado]["favorito"] = True
        print("Contato favoritado com sucesso.")
        return
    else:
        print("Indice incorreto.")
        return


def mostrar_favoritos(lista):
    for indice, contato in enumerate(lista, start=1):
        if contato["favorito"]:
            favorito = "✔️" if contato["favorito"] else " "
            print(f"{indice}. Nome: {contato["nome"]}, Telefone: {
                contato["numero_contato"]}, E-mail: {contato["email"]}, Favorito: [{favorito}]")
    return


def deletar_contato(lista):
    ver_contatos(lista)
    indice_contato = input("Escolha o contato que deseja deletar: ")
    indice_ajustado = ajustar_indice(indice_contato)

    if indice_ajustado >= 0 and indice_ajustado < len(lista):
        del (lista[indice_ajustado])
        print("Contato deletado com sucesso.")
        return
    else:
        print("Indice incorreto.")
        return


lista_telefonica = []

while True:
    print("\nMenu da Lista Telefonica:")
    print("1 - Visualizar contatos")
    print("2 - Criar contato")
    print("3 - Editar contato")
    print("4 - Marcar contato como favorito")
    print("5 - Mostrar contatos favoritos")
    print("6 - Apagar contato")
    print("7 - Sair")

    escolha = input("Digite a sua escola: ")

    match escolha:
        case "1":
            ver_contatos(lista_telefonica)
        case "2":
            criar_contato(lista_telefonica)
        case "3":
            editar_contato(lista_telefonica)
        case "4":
            contato_favorito(lista_telefonica)
        case "5":
            mostrar_favoritos(lista_telefonica)
        case "6":
            deletar_contato(lista_telefonica)
        case "7":
            break
        case _:
            print("Opção invalida")

print("\nPrograma finalizado.")
