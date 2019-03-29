import pymysql

class Pets(object):
    def select(self, id=None, name=None, sex=None, color=None, status=None, originator=None):
        params = {'id': id, 'name': name, 'sex': sex, 'color': color, 'status': status, 'originator': originator}
        query = "SELECT * FROM pets"
        
        set_where = False
        for key, value in params.items():
            if value is not None:
                if set_where is False:
                    query += " WHERE "
                query += "{0} = %({0})s,".format(key)
        
        if query[-1] == ',':
            query = query[:-1]
        
        cnx = pymysql.connect(host='127.0.0.1',user='root',db='finder', cursorclass=pymysql.cursors.DictCursor)
        with cnx.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
        
        return result
    
    def insert(self, args):
        params = {'name': args.name, 'sex': args.sex, 'color': args.color, 'status': args.status, 'originator': args.originator}

        query = "INSERT INTO pets ("

        keys = []
        for key, value in params.items():
            if value is not None:
                keys.append(key)
                query += " {0},".format(key)

        if query[-1] == ',':
            query = query[:-1]

        query += ") values ("
        for key in keys:
            query += "%({0})s,".format(key)
        if query[-1] == ',':
            query = query[:-1]

        query += ")"

        cnx = pymysql.connect(host='127.0.0.1',user='root',db='finder', cursorclass=pymysql.cursors.DictCursor)
        with cnx.cursor() as cursor:
            cnx.begin()
            try:
                print(cursor.mogrify(query, params))
                cursor.execute(query, params)
                new_id = cursor.lastrowid
                cnx.commit()
            except Exception as ex:
                cnx.rollback()
                raise
        
        return new_id