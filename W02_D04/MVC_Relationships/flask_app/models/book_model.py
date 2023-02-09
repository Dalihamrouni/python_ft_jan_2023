from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
class Book:
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.title = data_dict['title']
        self.pages = data_dict['pages']
        self.user_id = data_dict['user_id']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    # ! All queries are classmethod

    # ================ READ ALL USERS ===============
    @classmethod
    def get_all(cls):
        query =  """
        SELECT * FROM books ;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        print(f"Result from Database = {results}")
        all_books = []
        for row in results:
            all_books.append(cls(row))
        return all_books

    # ================ CREATE USER ================
    @classmethod
    def create_book(cls,data_dict):
        query = """
        INSERT INTO books (title, pages,user_id) VALUES (%(title)s,%(pages)s ,%(user_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data_dict)

    # ================ READ ONE USER ===============
    @classmethod
    def get_one(cls,data_dict):
        query = """
        SELECT * FROM books WHERE id  = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query,data_dict)
        print(results)
        if results:
            return cls(results[0])
        return []
