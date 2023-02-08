from mysqlconnection import connectToMySQL

class User:
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.username = data_dict['username']
        self.email = data_dict['email']
        self.age = data_dict['age']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    # ! All queries are classmethod

    # ================ READ ALL USERS ================
    @classmethod
    def get_all(cls):
        query =  """
        SELECT * FROM users ;
        """
        results = connectToMySQL("W02_D03").query_db(query)
        print(f"Result from Database = {results}")
        all_users = []
        for row in results:
            all_users.append(cls(row))
        return all_users

    # ================ CREATE USER ================
    @classmethod
    def create_user(cls,data_dict):
        query = """
        INSERT INTO users (username,email,age) VALUES (%(username)s, %(email)s, %(age)s);
        """
        return connectToMySQL("W02_D03").query_db(query,data_dict)

    # ================ READ ONE USER ================
    @classmethod
    def get_one(cls,data_dict):
        query = """
        SELECT * FROM users WHERE id  = %(id)s;
        """
        results = connectToMySQL("W02_D03").query_db(query,data_dict)
        print(results)
        if results:
            return cls(results[0])
        return []