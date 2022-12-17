#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    ao = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}

    stroka = input('Введите строку: ')
    count = 0

    for i in stroka:
        if i.lower() in ao:
            count += 1

    print(f"Количество согласных: {count}")