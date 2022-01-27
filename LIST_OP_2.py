with open("/Users/fafakhan/PycharmProjects/Machine_Learning_Projects/data_dir/input_for_prgs.txt","r") as f:
    temp = f.readlines()

for lst in temp:
    if lst.count(lst[4]) == 3 and len(lst) == 8:
        print("True")
    else:
        print("False")
