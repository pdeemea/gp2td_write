import jaydebeapi,sys
import threading,logging,uuid

dump_file_folder=<path_to_the_dump _file_folder>
teradata_host=<teradata host name>
lib_path=<path_to_teradata_jdbc_libs>
teradata_user=<teradata username>
teradata_pass=<teradata password>
def start_import():
    filename = str(uuid.uuid4())
    fileout=open(dump_file_folder+filename+'.log','w+')
    conn = jaydebeapi.connect('com.teradata.jdbc.TeraDriver',['jdbc:teradata://'+teradata_host+'/TMODE=ANSI', teradata_user, teradata_pass],lib_path+'terajdbc4.jar:'+lib_path+'tdgssconfig.jar')
    curs = conn.cursor()
    u=[]
    for line in sys.stdin:
        t=int(line.split(',')[0]),str(line.split(',')[1][:-1]).strip()
        if len(u)<15000:
            u.append(t)
        else:
            try:
                #print "Writing Batch in LOOP at line: "+line
                curs.executemany("insert into gptest (id, note)values (?, ?)",u)
                u=[]
                #print "Sucessful write"
                u.append(t)
            except:
                #print "ERROR at line: "+line
                #print "Dumping inserts to file"
                for ln_lst in u:
		            fileout.write(str(ln_lst[0])+'\n')
                    u=[]
                    #curs.close()
    if len(u)<>0:
        #curs=conn.cursor()
        print "writing after LOOP"
        curs.executemany("insert into gptest (id, note)values (?, ?)",u)
        #curs.close()

#thread1=threading.Thread(target=start_import)
#thread1.start()
start_import()
