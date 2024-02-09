from tabulate import tabulate
class CommonUtils:

    def __init__():
        pass
    
    @staticmethod
    def show_df(data, n=5):
        print(tabulate(data.head(n), headers="keys", tablefmt="psql"))