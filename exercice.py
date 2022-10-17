#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyexpat import model
from matplotlib.colors import cnames


def list_to_dict(some_list: list) -> dict:
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs
    # dic = {}
    # for i in range(len(some_list)):
    #     dic[some_list[i]] = i
    # return dic

    return {key: some_list.index(key) for key in some_list}


def color_name_to_hex(colors: list) -> list:
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex
    # result = []
    # for color in colors:
    #     result.append((color, cnames[color]))
    # return result
    return [(color, cnames[color]) for color in colors]


def create_list() -> list:
    # TODO: Créer une liste des 1 000 premiers entiers positif, sauf pour les entiers de 15 à 350
    # times, number, result = 0, 0, []
    # while times < 1000:
    #     if number < 15 or number > 350:
    #         result.append(number)
    #         times += 1
    #     number += 1
    # return result

    return [nb for nb in range(1336) if not 15<=nb<=350]


def compute_mse(model_dict: dict) -> dict:
    # TODO: Calculer l'erreur quadratique moyen pour chaque modèle. Retourner un dictionnaire contenant les MSE.
    result = {}

    for key, value in model_dict.items():
        total = 0
        for tuple in value:
            total += (tuple[1]-tuple[0])**2
        result[key] = total/(len(value))

    return result


def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    print(f"La liste des 1000 entiers est: {create_list()}")

    model_dict = {"LR": [(90, 92), (96, 100), (20, 25), (21, -2), (3, -20)],
                  "DNN": [(100, 101), (50, 50), (1,2), (-10, -12), (-1, 7)],
                  "RF": [(10, 19), (56, 70), (1, 9), (-100, -12), (-11, 7)]}
    print(f"Le mse des différents modèles est: {compute_mse(model_dict)}")


if __name__ == '__main__':
    main()
