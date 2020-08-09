from flask import Flask, redirect, url_for ,request,abort,jsonify
import pymysql

host='xxxxxx.us-east-2.rds.amazonaws.com'
dbName='xxxx'
uname='xxxx'
upwd='xxxxx'

#********************** AWS RDS Connection Establisation ****************************************
try:
    #charset='utf8'
    conn = pymysql.connect(host=host,database=dbName, user=uname, password=upwd,charset='utf8',use_unicode=True)
    print('\n********************** AWS RDS Connection Establisation ****************************************\n')
except Exception as e:
    print(e)

application = Flask(__name__)



#----------------------index-------------------------------------


@application.route('/')
def admin():
   return 'API Application'




#-------------------DB search function-------------------------------
@application.route('/guest/<search>')
def db_search(search):
  s_cur = conn.cursor()
  s_cur.execute(search)
  rows = s_cur.fetchall()
  #print(rows)
  search_count=len(rows)
  print(search_count)
  payload = []
  content = {}
  for result in rows:
      content = {'alpha_two_code': result[0], 'country': result[1], 'domain': result[2],'name': result[3],'webpage': result[4],'id': result[5]}
      payload.append(content)
      content = {}
  return jsonify(payload)



#-------------------------Insert API-------------------------------


@application.route('/insert',methods = ['POST', 'GET'])
def API_create():
   if request.method == 'POST':
      req_type=request.is_json
      print(req_type)
      if str(req_type) == 'True':
          content = request.get_json()
          name=content.get("name")
          if str(name) != "":
              alpha_two_code=content.get("alpha_two_code")
              country=content.get("country")
              domain=content.get("domain")
              name=content.get("name")
              web_page=content.get("web page")
              #print(alpha_two_code+country+domain+name+web_page)
              print(name)
              search_name=str(name).lower()
              search_trim=search_name.replace(" ", "")
              search="select * from API_table where id='{}'".format(search_trim)
              #print(search)
              s_cur = conn.cursor()
              s_cur.execute(search)
              rows = s_cur.fetchall()
              #print(rows)
              search_count=len(rows)
              print(search_count)
              if search_count>0:
                  abort(409 ,'duplicate name' )
              else:
                  try:
                      insert_query="INSERT INTO API_table(alpha_code,country,domain,name,webpage,id)\
                                                values('{0}','{1}','{2}','{3}','{4}','{5}')".format(str(alpha_two_code),str(country),str(domain),str(name),str(web_page),\
                                                                                                                       str(search_trim))



                      print('insert_query',insert_query)
                      cust_cur = conn.cursor()
                      cust_cur.execute(insert_query)
                      conn.commit()
                      cust_cur.close()
                      return jsonify({'success':'true','record':'added','id':search_trim}),201
                  except Exception as e:
                      print('*************insert_query**********',e)
                      abort(502 ,'db error' )

          else:
              abort(401 ,'name empty' )
              
      else:
          abort(400 ,'Check Body Type' )
        
   else:
      abort(400 ,'Check Method Type' )



#--------------------------------------Update API------------------------------------


@application.route('/update',methods = ['POST','PUT'])
def API_update():
   if request.method == 'PUT':
      req_type=request.is_json
      print(req_type)
      if str(req_type) == 'True':
          content = request.get_json()
          name=content.get("name")
          if str(name) != "":
              alpha_two_code=content.get("alpha_two_code")
              country=content.get("country")
              domain=content.get("domain")
              name=content.get("name")
              web_page=content.get("web page")
              #print(alpha_two_code+country+domain+name+web_page)
              print(name)
              search_name=str(name).lower()
              search_trim=search_name.replace(" ", "")
              search="select * from API_table where id='{}'".format(search_trim)
              #print(search)
              s_cur = conn.cursor()
              s_cur.execute(search)
              rows = s_cur.fetchall()
              #print(rows)
              search_count=len(rows)
              print(search_count)
              if search_count==0:
                  abort(404 ,'No Record Found based on Name' )
              else:
                  try:
                      update_query="UPDATE API_table SET alpha_code='{0}',country='{1}',domain='{2}',name='{3}',webpage='{4}' where id='{5}'".format(str(alpha_two_code),str(country),str(domain),str(name),str(web_page),str(search_trim))
                      print('update_query',update_query)
                      cust_cur = conn.cursor()
                      cust_cur.execute(update_query)
                      conn.commit()
                      cust_cur.close()
                      return jsonify({'success':'true','record':'updated','id':search_trim}),200
                  except Exception as e:
                      print('*************update_query**********',e)
                      abort(502 ,'db error' )

          else:
              abort(401 ,'name empty' )
              
      else:
          abort(400 ,'Check Body Type' )
        
   else:
      abort(400 ,'Check Method Type' )



#--------------------------Delete API----------------------------------



@application.route('/delete',methods = ['DELETE','POST'])
def API_delete():
   if request.method == 'DELETE':
      req_type=request.is_json
      print(req_type)
      if str(req_type) == 'True':
          content = request.get_json()
          name=content.get("name")
          if str(name) != "":
              alpha_two_code=content.get("alpha_two_code")
              country=content.get("country")
              domain=content.get("domain")
              name=content.get("name")
              web_page=content.get("web page")
              #print(alpha_two_code+country+domain+name+web_page)
              print(name)
              search_name=str(name).lower()
              search_trim=search_name.replace(" ", "")
              search="select * from API_table where id='{}'".format(search_trim)
              #print(search)
              s_cur = conn.cursor()
              s_cur.execute(search)
              rows = s_cur.fetchall()
              #print(rows)
              search_count=len(rows)
              print(search_count)
              if search_count==0:
                  abort(404 ,'No Record Found based on Name' )
              else:
                  try:
                      delete_query="DELETE FROM API_table  where id='{0}'".format(str(search_trim))
                      print('delete_query',delete_query)
                      cust_cur = conn.cursor()
                      cust_cur.execute(delete_query)
                      conn.commit()
                      cust_cur.close()
                      return jsonify({'success':'true','record':'deleted','id':search_trim}),200
                  except Exception as e:
                      print('*************delete_query**********',e)
                      abort(502 ,'db error' )

          else:
              abort(401 ,'name empty' )
              
      else:
          abort(400 ,'Check Body Type' )
        
   else:
      abort(400 ,'Check Method Type' )



#------------------------Search API--------------------------------------


@application.route('/search',methods = ['GET','POST'])
def API_search():
   if request.method == 'GET':
      req_dict=request.args.to_dict()
      print(req_dict)
      res = not bool(req_dict)
      if str(res) != 'True':
          search_term = request.args.get("search_term")
          print(search_term)
          if str(search_term) !='None':
              if str(search_term) != '':
                 country_code=request.args.get("country_code")
                 end_of_domain = request.args.get("end_of_domain")
                 print(country_code)
                 print(end_of_domain)
                 if str(country_code) =='None' and  str(end_of_domain) =='None':
                    search="select * from API_table where name LIKE '%"+str(search_term)+"%'"
                    print(search)
                    return redirect(url_for('db_search',search = search))
      
                 elif str(country_code) != 'None' and str(end_of_domain) =='None':
                    search="select * from API_table where name LIKE '%"+str(search_term)+"%' and alpha_code LIKE'%"+str(country_code)+"%'"
                    print(search)
                    return redirect(url_for('db_search',search = search))

                 elif str(country_code) == 'None' and str(end_of_domain) !='None':
                    search="select * from API_table where name LIKE '%"+str(search_term)+"%' and domain LIKE'%"+str(end_of_domain)+"'"
                    print(search)
                    return redirect(url_for('db_search',search = search))

                 else:
                    abort(400 ,'Parameters exceeded' )

              else:
                  abort(401 ,'search_term empty' )
          else:
              abort(400 ,'Parameters missing' )
              
      else:
          abort(400 ,'Parameters missing' )
        
   else:
      abort(400 ,'Check Method Type' )



#----------------------Read API--------------------------------------------------------

@application.route('/read',methods = ['GET','POST'])
def API_read():
   if request.method == 'GET':
      search="select * from API_table"
      print(search)
      return redirect(url_for('db_search',search = search))                
   else:
      abort(400 ,'Check Method Type' )


if __name__ == '__main__':
   application.debug = True
   application.run()
