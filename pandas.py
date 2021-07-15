import pandas as pd
from matplotlib import pyplot as plt

data = {
    'Sells': {
        0: 0,
        1: 2,
        2: 8,
        3: 1,
        4: 10,
        5: 5,
        6: 12,
        7: 16,
        8: 8,
        9: 20,
        10: 19,
        11: 3,
        12: 8,
        13: 0,
        14: 10,
        15: 20,
        16: 18,
        17: 10,
        18: 8,
        19: 12,
        20: 6
    },
    'Clients': {
        0: 0,
        1: 9,
        2: 3,
        3: 10,
        4: 4,
        5: 7,
        6: 10,
        7: 12,
        8: 15,
        9: 18,
        10: 16,
        11: 20,
        12: 11,
        13: 9,
        14: 19,
        15: 14,
        16: 8,
        17: 6,
        18: 9,
        19: 12,
        20: 19
    },
    'Prices': {
        0: 0,
        1: 7,
        2: 5,
        3: 10,
        4: 12,
        5: 13,
        6: 10,
        7: 15,
        8: 8,
        9: 9,
        10: 13,
        11: 17,
        12: 19,
        13: 15,
        14: 13,
        15: 16,
        16: 20,
        17: 18,
        18: 16,
        19: 14,
        20: 10
    }
}

datas = pd.DataFrame(data)

plt.rc('grid', linestyle='--', color='#bbb')

plt.plot(datas['Prices'], label='Prices', color='green', linewidth=1, marker='o', markersize='4', linestyle='-')
plt.plot(datas['Sells'], label='Sells', color='red', linewidth=1, marker='o', markersize='4', linestyle='-.')
plt.plot(datas['Clients'], label='Clients', color='blue', linewidth=1, marker='o', markersize='4', linestyle='--')
plt.title("Clients Diagram 2021", fontdict={'fontname': 'Courier New', 'fontsize': 20})
plt.xlabel("Days", fontdict={'fontname': 'Courier New', 'fontsize': 20})
plt.ylabel("Statistics", fontdict={'fontname': 'Courier New', 'fontsize': 20})
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

plt.grid()
plt.legend()
plt.show()
