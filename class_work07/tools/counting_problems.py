def  count_errors(data):
    counter_failer=0
    #print(data)
    for line in data:
    # line=line[:-1]
        line = line.strip() #очищуєм вхід наших даних ʼ
        line_split = line.split() #використовуємо пробіли, як розділювачі
        if len(line_split) != 5:
            continue
        date = line_split[0]+" "+line_split[1]
        status, user, ip =line_split[2:5]
        print(f"{date=}, {status=}, {user=}, {ip=}")
    # date = line[0:19]
        #  status=line_split[2]
        #  user=line_split[3]
        #  ip=line_split[4]
        #print(f"{date=}, {status=}, {user=}, {ip=}")
        if status == 'FAILED':
            counter_failer +=1
        #break
    return counter_failer