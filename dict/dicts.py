# import matplotlib.pyplot as plt
# import numpy as np

# # Время после чашки кофе (в часах)
# hours = np.linspace(0, 6, 100)

# # Модель бодрости: эффект кофеина + накопление аденозина
# # Эффект кофеина (пик через ~1 час, потом спадает)
# caffeine_effect = np.exp(-((hours-1)**2)/0.5)

# # Эффект накопления аденозина (постепенная сонливость)
# adenosine_effect = 0.3 * (hours/6)**2

# # Итоговая бодрость (больше - бодрее)
# alertness = caffeine_effect - adenosine_effect

# plt.figure(figsize=(8,5))
# plt.plot(hours, alertness, label='Бодрость после кофе', color='brown')
# plt.axvline(1, color='orange', linestyle='--', label='Пик кофеина ~1 час')
# plt.axhline(0, color='gray', linestyle=':')
# plt.xlabel('Время после чашки кофе (часы)')
# plt.ylabel('Уровень бодрости (условная шкала)')
# plt.title('Как меняется бодрость после кофе')
# plt.legend()
# plt.grid(True)
# plt.show()