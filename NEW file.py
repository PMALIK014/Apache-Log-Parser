print('''████████╗██╗  ██╗███████╗    ██████╗  █████╗ ██╗     
╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗██╔══██╗██║     
   ██║   ███████║█████╗      ██████╔╝███████║██║     
   ██║   ██╔══██║██╔══╝      ██╔═══╝ ██╔══██║██║     
   ██║   ██║  ██║███████╗    ██║     ██║  ██║███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝  ╚═╝╚══════╝
                                                      ''')
with open("website.log", "r")as f:
    lines=f.readlines()
    with open("output.txt",'w+')as nf:
        for line in lines:
           l=line.split(" ")
           nf.write("IP Address: {}\t" .format(l[0]))
           nf.write("Date and Time: {}\t" .format( l[3] , l[4]))
           nf.write("Request_Type: {}\t" .format(l[5]))
           nf.write("File_Path: {}\t" .format(l[6]))
           nf.write("Protocol: {}\t" .format(l[7]))
           nf.write("Status_Code: {}\t" .format(l[8]))
           nf.write("Packet_size: {}t".format(l[9]))
           nf.write("User_Agent: ".format( str(l[11:]).replace('"',' ').replace('[',' ').replace(']',' ')))
        
           
