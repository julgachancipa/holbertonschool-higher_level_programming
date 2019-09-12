#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as h
    names = dir(h)
    for i in range(len(names)):
        if names[i][0:2] != "__":
            print(names[i])
