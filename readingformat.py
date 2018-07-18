import re

with open('moby-linebyline.txt', 'a') as intrm_file:
    #lets get each sentence on one line, and no more than one sentence on one line.
    for line in open('moby-clean.txt'):
        #some special exceptions such as formatted visual text like indent blocks
        # maybe skip doublespacing since it is useful to find paragraphs
        ##if line
        #print " ".join(line.strip() 
        intrm_file.write(re.sub(r'\. *$','.\n',line.rstrip() + " ") )
    
intrm_file.close()
