def não_possui_a_letra_u(palavra):
    if 'u' in palavra:
        return False
    else:
        if 'ú' in palavra:
            return False
        else:
            if 'ù' in palavra:
                return False
            else:
                if 'û' in palavra:
                    return False
                else:
                    if 'ü' in palavra:
                        return False
                    else:
                        if 'ũ' in palavra:
                            return False
                        else:
                            if 'U' in palavra:
                                return False
                            else:
                                if 'Ú' in palavra:
                                    return False
                                else:
                                    if 'Ù' in palavra:
                                        return False
                                    else:
                                        if 'Ü' in palavra:
                                            return False
                                        else:
                                            if 'Ũ' in palavra:
                                                return False
                                            else:
                                                if 'Û' in palavra:
                                                    return False
                                                return True
                                            return True
                                        return True
                                    return True
                                return True
                            return True
                        return True
                    return True
                return True
            return True
        return True
    return True

print(não_possui_a_letra_u("Universidade"))
print(não_possui_a_letra_u("szkûnet"))
print(não_possui_a_letra_u("Baú"))
print(não_possui_a_letra_u("carro"))
print(não_possui_a_letra_u('Latex'))
