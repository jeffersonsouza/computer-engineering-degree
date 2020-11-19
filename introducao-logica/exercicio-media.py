#!/usr/bin/python
# -*- coding: utf8 -*-

def calcular_media(nota01, nota02, nota03):
    return (nota01 + nota02 + nota03) / 3

nota01 = float(input("Informe o valor da primeira nota: "))
nota02 = float(input("Informe o valor da segunda nota: "))
nota03 = float(input("Informe o valor da terceira nota: "))


print(f"A Média do Aluno é {calcular_media(nota01, nota02, nota03)}")
