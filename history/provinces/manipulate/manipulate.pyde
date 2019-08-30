import os
directory = ".././"

for filename in os.listdir(directory):
    if filename.endswith(".txt"): 
        dir = (os.path.join(directory, filename))
        #print dir
        lines = loadStrings(dir)
        for i in range(len(lines)):
            if lines[i] == "culture = turkish":
                print "sasd"
                if random(0,1) > 0.2:
                    lines[i] = "culture = white_american"
                else:
                    lines[i] = "culture = italian_american"
        
                saveStrings(dir, lines)
