import ibm_db

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32733;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bsb19147;PWD=M8Q6aCGQuLHwiHkU",'','')


'''insert_sql = "INSERT INTO  user VALUES (?, ?, ?, ?, ?, ?, ?)"
prep_stmt = ibm_db.prepare(conn, insert_sql)
ibm_db.bind_param(prep_stmt, 1, "sandeep")
ibm_db.bind_param(prep_stmt, 2, "sandeep@thesmartbridge.com")
ibm_db.bind_param(prep_stmt, 3, "8686560036")
ibm_db.bind_param(prep_stmt, 4, "Hyderabad")
ibm_db.bind_param(prep_stmt, 5, "uninfected")
ibm_db.bind_param(prep_stmt, 6, "B Positive")
ibm_db.bind_param(prep_stmt, 7, "123456")
ibm_db.exec_immediate(conn,prep_stmt)
print("Inserted")'''


sql = "SELECT * FROM user"
stmt = ibm_db.exec_immediate(conn, sql)
dictionary = ibm_db.fetch_assoc(stmt)
while dictionary != False:
    print ("The ID is : ", dictionary["NAME"])
    print ("The name is : ", dictionary["PHONE"])
    dictionary = ibm_db.fetch_assoc(stmt)
