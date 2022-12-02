def calculate_order(file_path):
    '''
    try:
        with open(file_path, "r") as file:
            total = 0
            lines = file.readlines()
            for line in lines:
                parts = line.split(",")
                prices = parts[-1].strip()
                total += float(prices)
            print("total: \n", round(total, 2))

    except FileNotFoundError:
        print("File not found")
    except IndexError:
        print("something worong with the file")
    except ValueError:
        print("price is invalid")
    '''

    try:
        with open(file_path, "r") as file:
            total = 0
            for line in file:
                try:
                    parts = line.split(",")
                    prices = parts[-1].strip()
                    total += float(prices)
                    print("total: \n", round(total, 2))
                except IndexError:
                    print("something worong with the file")
                except ValueError:
                    print("price is invalid")
    except FileNotFoundError:
        print("File not found")


def main():
    file_path = "lecture07/exercise/order.txt"
    calculate_order(file_path)


if __name__ == "__main__":
    main()
