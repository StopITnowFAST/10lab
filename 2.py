#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    s1 = input("Введите первую строку: ")
    s2 = input("Введите вторую строку: ")

    s1 = s1.replace(' ', '')
    a = {i for i in s1.lower()}

    s2 = s2.replace(' ', '')
    b = {i for i in s2.lower()}

    c = a.intersection(b)
    print(f"Пересечение: {c}")