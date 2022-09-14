import re
class seco:
    with open("Output.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            try:
                z = re.search(r"\b(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9])\.){3}(?:(?:2([0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9]))\b", line)
                ip = z.group().strip()
                x = re.search(r"\s[0-9]+\s", line)
                port = x.group().strip()
                mrx = ip + ":" + port + "\n"
                i = open("MASSCAN HITLERI.txt","a")
                i.write(mrx)
                i.close()
            except AttributeError:
                pass
