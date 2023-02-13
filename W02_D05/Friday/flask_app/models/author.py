# 
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Author:
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.nationality = data_dict['nationality']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.books_list = []
    
    #  READ ALL (SELECT All Authors)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_authors = []
        if results:
            for row in results:
                all_authors.append(cls(row))
            return all_authors
        return []

    # CREATE ONE AUTHOR
    @classmethod
    def create_author(cls, data_dict):
        query = """
        INSERT INTO authors (name, nationality) VALUES
        (%(name)s, %(nationality)s);
        """
        # ! This Method RETURN THE ID of the nex created Author
        result  = connectToMySQL(DATABASE).query_db(query,data_dict)
        print(f"this is the result after INSERT One Author {result} ***************")
        return result
    
    #  READ ONE AUTHOR
    @classmethod
    def get_one(cls,data_dict):
        query = """
        SELECT * FROM authors WHERE id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data_dict)
        if results:
            return cls(results[0])
        return None

    # UPDATE ONE AUTHOR
    @classmethod
    def update_author(cls,data_dict):
        query = """
        UPDATE authors SET name = %(name)s, nationality = %(nationality)s WHERE id  = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data_dict)

    # DELETE ONE AUTHOR
    @classmethod 
    def delete_author(cls, data_dict):
        query = """
        DELETE FROM authors WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data_dict)