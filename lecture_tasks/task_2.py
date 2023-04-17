import matplotlib.pyplot as plt
import pandas as pd

FILE = 'company_sales_data.csv'
X_AXIS_MONTH = 'Month number'
Y_AXIS_MONEY = 'Amount of $'
Y_AXIS_SALES = 'Sales units in number'
COMPANY_PROFIT_TITLE = 'Company profit per month'
SALES_TITLE = 'Sales data'
TOOTH_SALES = 'Tooth paste Sales Data'


def read_data():
    data = pd.read_csv(FILE)
    profit = data['total_profit'].tolist()
    month = data['month_number'].tolist()
    return profit, month


def task_1():
    profit, month = read_data()

    plt.figure(figsize=(5, 2.7))
    plt.plot(month, profit)
    plt.xticks(month)
    plt.yticks([100000, 200000, 300000, 400000, 500000])
    plt.xlabel(X_AXIS_MONTH)
    plt.ylabel(Y_AXIS_MONEY)
    plt.title(COMPANY_PROFIT_TITLE)

    plt.show()


def task_2():
    profit, month = read_data()

    plt.figure(figsize=(5, 2.7), layout='constrained')
    plt.plot(month, profit, marker='o', markerfacecolor='k'
             , color='red', linewidth=3, linestyle='--', label='profit data of last year')
    plt.xticks(month)
    plt.yticks([100000, 200000, 300000, 400000, 500000])
    plt.xlabel(X_AXIS_MONTH)
    plt.ylabel(Y_AXIS_MONEY)
    plt.title(COMPANY_PROFIT_TITLE)
    plt.legend()

    plt.show()


def task_3():
    data = pd.read_csv(FILE)
    facecream_profit = data['facecream'].tolist()
    facewash_profit = data['facewash'].tolist()
    toothpaste_profit = data['toothpaste'].tolist()
    bathingsoap_profit = data['bathingsoap'].tolist()
    shampoo_profit = data['shampoo'].tolist()
    moisturizer_profit = data['moisturizer'].tolist()
    month = data['month_number'].tolist()

    plt.xlabel(X_AXIS_MONTH)
    plt.ylabel(Y_AXIS_SALES)
    plt.title(SALES_TITLE)

    plt.plot(month, facewash_profit, marker='o', label='facecream sales')
    plt.plot(month, facecream_profit, marker='o', label='facewash sales')
    plt.plot(month, toothpaste_profit, marker='o', label='toothpaste sales')
    plt.plot(month, bathingsoap_profit, marker='o', label='bathingsoap sales')
    plt.plot(month, shampoo_profit, marker='o', label='shampoo sales')
    plt.plot(month, moisturizer_profit, marker='o', label='moisturizer sales')

    plt.legend()
    plt.show()


def task_4():
    data = pd.read_csv(FILE)
    tooth_paste_sales = data['toothpaste'].tolist()
    month = data['month_number'].tolist()

    plt.scatter(month, tooth_paste_sales, label=TOOTH_SALES)
    plt.title(TOOTH_SALES)
    plt.ylabel('Number of units sold')
    plt.xlabel(X_AXIS_MONTH)
    plt.xticks(month)

    plt.legend()
    plt.grid(True, linestyle='--')
    plt.show()


def task_5():
    data = pd.read_csv(FILE)
    facecream_profit = data['facecream'].tolist()
    facewash_profit = data['facewash'].tolist()
    month = data['month_number'].tolist()

    plt.xlabel(X_AXIS_MONTH)
    plt.ylabel(Y_AXIS_SALES)
    plt.xticks(month)
    plt.bar(month, facewash_profit, width=0.25, align='edge', label='Face Wash sales data')
    plt.bar(month, facecream_profit, width=-0.25, align='edge', label='Face Cream sales data')

    plt.legend()
    plt.grid(True, linestyle='--')
    plt.show()


def task_6():
    data = pd.read_csv(FILE)
    bathingsoap_profit = data['bathingsoap'].tolist()
    month = data['month_number'].tolist()

    plt.xlabel(X_AXIS_MONTH)
    plt.ylabel(Y_AXIS_SALES)
    plt.xticks(month)
    plt.bar(month, bathingsoap_profit)

    plt.grid(True, linestyle='--')
    plt.savefig('bathingsoap_sales_plot.png')
    plt.show()


if __name__ == '__main__':
    task_6()
