with open('names_grndb.txt') as read:
    for line in read:
        final_name = 'http://www.grndb.com/download/txt?condition='+ line
        open('GRNdb.txt','a').write(final_name)