#!/usr/bin/python
# -*- coding: utf8 -*-

def calcular_media(nota01, nota02, nota03):
    media = (nota01 + nota02 + nota03) / 3
    return media

av01 = float(input("Informe o valor da primeira nota: "))
av02 = float(input("Informe o valor da segunda nota: "))
av03 = float(input("Informe o valor da terceira nota: "))


print(f"A Média do Aluno é {calcular_media(av01, av02, av03)}")
