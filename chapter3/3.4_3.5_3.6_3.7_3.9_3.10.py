# список гостей
spisok_gostey = ["alpha", "beta", "gamma", "delta"]
message = (f"\nПривет, {spisok_gostey[0].title()}, приходи в гости!\nПривет, {spisok_gostey[1].title()}, приходи в "
           f"гости!\nПривет, {spisok_gostey[2].title()}, приходи в гости!\nПривет, {spisok_gostey[3].title()}, приходи"
           f" в гости!")
print(message)

# гость, который не сможет прийти
print(f"\nК сожалению, {spisok_gostey[1].title()} прийти не сможет.")

spisok_gostey.remove("beta")
spisok_gostey.append("omega")
# новый список гостей
message = (f"\nПривет, {spisok_gostey[0].title()}, приходи в гости!\nПривет, {spisok_gostey[1].title()}, приходи в "
           f"гости!\nПривет, {spisok_gostey[2].title()}, приходи в гости!\nПривет, {spisok_gostey[3].title()}, приходи "
           f"в гости!")
print(message)

# уведомление о расширении списка гостей
print(f"\nМы расширяем список гостей!")

spisok_gostey.insert(0, 'solo')
spisok_gostey.insert(2, 'booster')
spisok_gostey.append('mira')
message_2 = (f"\nПривет, {spisok_gostey[0].title()}, приходи в гости!\nПривет, {spisok_gostey[2].title()}, приходи в "
             f"гости!\nПривет, {spisok_gostey[-1].title()}, приходи в гости!")
print(message, message_2)
# 3.9 начинался
print(f"Количество гостей: {len(spisok_gostey)}")
# 3.9 закончился
print(f"\nК сожалению, места для гостей стало меньше и мы урезаем персонал.")

print(f"\n{spisok_gostey[0].title()}, мне очень жаль, но я вынужден отменить приглашение.")
spisok_gostey.pop(0)

print(f"\n{spisok_gostey[1].title()}, мне очень жаль, но я вынужден отменить приглашение.")
spisok_gostey.pop(1)

print(f"\n{spisok_gostey[2].title()}, мне очень жаль, но я вынужден отменить приглашение.")
spisok_gostey.pop(2)

print(f"\n{spisok_gostey[3].title()}, мне очень жаль, но я вынужден отменить приглашение.")
spisok_gostey.pop(3)

print(f"\n{spisok_gostey[0].title()}, приглашение остаётся в силе.")
print(f"\n{spisok_gostey[1].title()}, приглашение остаётся в силе.")
print(f"\n{spisok_gostey[2].title()}, приглашение остаётся в силе.")

del spisok_gostey[0 | 1 | 2]

print(spisok_gostey)
