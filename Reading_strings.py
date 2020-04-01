def read_line(skip=0, count=-1): # Читает строки с нужной до какой либо другой, где skip - это то, сколько нужно пропустить, а count - сколько прочитать
    with open(filename) as f:
        line = f.readline()
        start, cnt = 0, 0
        while line:
            if start >= skip:
                print(line.strip())
                cnt += 1
            if count != -1 and cnt >= count:
                break
            start += 1
            line = f.readline()

read_line()  # прочитать все
read_line(1, 2)  # пропустить 1 строку прочитать две последующие
read_line(5)  # пропустить 5 строк прочитать остальные