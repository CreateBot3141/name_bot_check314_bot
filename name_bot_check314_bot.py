 

def start_prog (user_id,namebot,message_in,status,message_id,name_file_picture,telefon_nome):
    import time
    import iz_func
    import iz_telegram    
    import datetime
    label_send = 'send'





    if message_in.find ('Контакты_main') != -1:
        label = 'no send'  
        message_out,markup = iz_telegram.get_kontakt (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)





    if status == 'Ввод сайта':
        label_send = 'no send'
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Задание получено. Тестирование запущено','S',0)
        name = message_in
        db,cursor = iz_func.connect () 
        unixtime = int(time.time ())        
        sql = "INSERT INTO bot_command (`answer`,`command`,`name`,`namebot`,`p1`,`p2`,`p3`,`status`,`type`,`unixtime`,`user_id`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}',{},'{}')".format ('','/home/izofen/Studiya/nikto/program/nikto.pl','',namebot,'-h',name,'','new','bot_nikto',unixtime,user_id)
        cursor.execute(sql)
        db.commit()
        sql = "INSERT INTO bot_command (`answer`,`command`,`name`,`namebot`,`p1`,`p2`,`p3`,`status`,`type`,`unixtime`,`user_id`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}',{},'{}')".format ('','/usr/bin/nmap','',namebot,name,'','','new','bot_nmap',unixtime,user_id)
        cursor.execute(sql)
        db.commit()
        sql = "INSERT INTO bot_command (`answer`,`command`,`name`,`namebot`,`p1`,`p2`,`p3`,`status`,`type`,`unixtime`,`user_id`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}',{},'{}')".format ('','/usr/bin/whatweb','',namebot,name,'--colour=never','-v','new','bot_whatweb',unixtime,user_id)
        cursor.execute(sql)
        db.commit()      

    if message_in == 'Задание':
        label_send = 'no send'

    if message_in == 'Отмена':
        label_send = 'no send'

    if message_in == '/send':
        iz_telegram.save_variable (user_id,namebot,"status",'Ждем текст')

    if message_in == '/start':
        label_send = 'no send'
        iz_telegram.send_photo (user_id,namebot,'main_picture.jpg') 
 
    if label_send != 'no send':
        pass    
     
