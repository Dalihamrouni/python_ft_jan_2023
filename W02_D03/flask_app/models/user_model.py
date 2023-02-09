from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import book_model
class User:
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.username = data_dict['username']
        self.email = data_dict['email']
        self.age = data_dict['age']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.my_books = []

    # ! All queries are classmethod

    # ================ READ ALL USERS ===============
    @classmethod
    def get_all(cls):
        query =  """
        SELECT * FROM users ;
        """
        results = connectToMySQL(DATABASE).query_db(query)
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
        return connectToMySQL(DATABASE).query_db(query,data_dict)

    # ================ READ ONE USER ===============
    @classmethod
    def get_one(cls,data_dict):
        query = """
        SELECT * FROM users WHERE id  = %(id)s;
        """
        query_2 = """
        SELECT * from users join books on users.id  = books.user_id where users.id = %(id)s;
        """
        # results = connectToMySQL(DATABASE).query_db(query,data_dict)
        results = connectToMySQL(DATABASE).query_db(query_2,data_dict)
        print(results)
        books = []
        if results:
            this_user =  cls(results[0])
            for row in results:
                book_data = {
                    'id':row['books.id'],
                    'title':row['title'],
                    'pages': row['pages'],
                    'user_id': row['user_id'],
                    'created_at' :row['books.created_at'],
                    'updated_at' :row['books.updated_at']
                }
                book = book_model.Book(book_data)
                books.append(book)
            this_user.my_books = books
            return this_user
        return []

    