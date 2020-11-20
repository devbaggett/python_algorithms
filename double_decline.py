# Calculates double-declining balance depreciation
#
# This solution works in all cases

original_cost = float(5000)
salvage_value = float(200)
useful_life = int(5)
dep_year = int(3)


# depreciable amount = original_cost - salvage_value = 5000 - 200 = 4800

# year 1: annual depreciation = bookvalue x rate = 5000 x .5 = 2500

# last year = previous bookvalue - salvage_value

def ddb(original_cost, salvage_value, useful_life, dep_year):
    depreciation = 0

    acc_depn = 0
    counter = 1

    rate = 1 / useful_life * 2
    book_value = original_cost

    while book_value > salvage_value and counter < useful_life:
        depn = (original_cost - acc_depn) * rate
        acc_depn = acc_depn + depn
        book_value = original_cost - acc_depn

        if counter == dep_year:
            depreciation = depn

        print("Year ", counter, "   Annual Dep: ", depn, "  Acc Depn: ", acc_depn, "    Book Value: ", book_value)
        counter += 1

    depn = book_value - salvage_value
    acc_depn += depn
    book_value -= depn
    print("Year ", counter, "   Annual Dep: ", depn, "  Acc Depn: ", acc_depn, "    Book Value: ", book_value)
    print("Depreciation for year {}: ${}".format(dep_year, depreciation))

    if dep_year:
        return depreciation
    else:
        return False


ddb(original_cost, salvage_value, useful_life, dep_year)
