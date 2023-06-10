import os
with open("E:\welcome.txt",'r',encoding='utf-8') as name_file:
    with open("E:\welcome1.txt",encoding='utf-8') as body_file:
        body=body_file.read()
        for name in name_file:
            mail="hello"+name+body

            with open(name.strip()+".txt",'w',encoding='utf-8') as mail_file:
               print(mail_file.write('E:'+mail))

