with open("/Users/fafakhan/PycharmProjects/Machine_Learning_Projects/data_dir/input_for_prgs.txt","r") as f:
    temp = f.readlines()

for lst in temp:
    if lst.count("19") == 2 and lst.count("5") >= 3:
        print("True")
    else:
        print("False")
