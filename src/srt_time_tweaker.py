from datetime import datetime, timedelta

read_file = "input.srt"
write_file = "output.srt"

lines = []
for i in range(0,1500):
    lines.append([])
with open(read_file, "r") as file:
    num = 0
    for line in file:
        line = line.strip()
        try:
            if int(line)-1==num:
                num+=1
        except:
            pass
        lines[num].append(line)

with open(write_file, "w") as file:
    for i in lines:
        if len(i)<3:
            continue
        file.write(f"{i[0]}\n")
        time = i[1]
        a = time[0:12]
        b = time[17:29]
        time_format = "%H:%M:%S,%f"
        a = datetime.strptime(a, time_format)
        b = datetime.strptime(b, time_format)
        delta = timedelta(seconds=6, milliseconds=500)
        a = a - delta
        b = b - delta
        a = a.strftime(time_format)[:-3]
        b = b.strftime(time_format)[:-3]
        file.write(f"{a} --> {b}\n")
        for j in i[2:]:
            file.write(f"{j}\n")


# INITIAL CODE written as: srt-delay-editor.py