def get_entity_data(entities, fields):
    results = []
    query = "SELECT * from " + entities
    first = True
    params = {}
    for field in fields:
        params[field] = flask.request.args.get(field)
        if params[field] != None:
            if first:
                query += " WHERE " + field + " = %(" + field + ")s"
                first = False
            else:
                query += " AND " + field + " = %(" + field + ")s"
    try:
        cursor.execute(query, params)
    except Exception as e:
        print(e)
        exit()
    for row in cursor:
        results.append(row)
    return json.dumps(results)
    
  
      fields = ['id', 'first_name', 'last_name', 'party', 'state', 'seat']

            if first:
                query += " WHERE " + field
                first = False
            else:
                query += " AND " + field
            if ('name' not in field):
                query += " = %(" + field + ")s"
            else:
                query += " LIKE \%%(" + field + ")s\%"
                
                
            if first:
                query += " WHERE " + field + " = %(" + field + ")s"
                first = False
            else:
                query += " AND " + field + " = %(" + field + ")s"
                
                
@app.route('/transactions')
def get_transactions():
    fields = ['date', 'amount', 'contributor_id', 'contributor_type', 'recipient_id', 'recipient_type']
    