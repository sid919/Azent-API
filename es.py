import logging
from flask import Flask, redirect, url_for ,request,abort,jsonify
from elasticsearch import Elasticsearch

application = Flask(__name__)

def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es.ping():
        print('Yay Connect')
    else:
        print('Awww it could not connect!')
    return _es

@application.route('/')
def admin():
   return 'API Application'

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
                 	  es = connect_elasticsearch()
                 	  search_object = {'query': {'match': {'name': search_term}}}
                 	  response = es.search(index="universites", body=search_object)
                 	  print ('response:', response)
                 	  return jsonify(response['hits'])
                  elif str(country_code) != 'None' and str(end_of_domain) =='None':
                 	  es = connect_elasticsearch()
                 	  search_object = {'query':{ "bool": { "must": [{'match': {'name': search_term}}],"filter": [{ "term":  { "alpha_two_code": country_code }}]}}}
                 	  print(search_object)
                 	  response = es.search(index="universites", body=search_object)
                 	  print ('response:', response)
                 	  return jsonify(response['hits'])
                  elif str(country_code) == 'None' and str(end_of_domain) !='None':
                 	  es = connect_elasticsearch()
                 	  search_object = {"query":{"bool":{"must":[{"query_string":{"default_field" : "domain","query" : "*"+end_of_domain+"*"}},{"match":{"name":search_term}}]}}}
                 	  response = es.search(index="universites", body=search_object)
                 	  print ('response:', response)
                 	  return jsonify(response['hits'])
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



if __name__ == '__main__':
   application.debug = True
   application.run()
