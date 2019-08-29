import os
directory = ".././"

for filename in os.listdir(directory):
    if filename.endswith(".txt"): 
        dir = (os.path.join(directory, filename))
        print dir
        lines = loadStrings(dir)
        if (lines[1] == "1900.1.1={"):
            lines[1] = "800.1.1={"
            saveStrings(dir, lines)
        try:
            if (lines[6] == "1911.1.1 = {"):
                lines[6] = "860.1.1={"
                saveStrings(dir, lines)
        except:
            pass
