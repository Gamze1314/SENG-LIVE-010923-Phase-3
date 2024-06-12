# Pet Attributes: 
# name: TEXT 
# species: TEXT
# breed: TEXT 
# temperament: TEXT

# https://docs.python.org/3/library/sqlite3.html#tutorial
import sqlite3

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection
CONN = sqlite3.connect('lib/resources.db')

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor
CURSOR = CONN.cursor()

# we first need to create classes before persisting data to database.

class Pet:
    
    # ✅ 1. Add "__init__" with "name", "species", "breed", "temperament", and "id" (Default: None) Attributes
    def __init__(self, name, species, breed, temperament, id=None): #db will handle id generation.we just creating py object, we will persist it to db later.
        self.id = id
        self.name = name
        self.species = species
        self.breed = breed
        self.temperament = temperament

    # ✅ 2. Add "create_table" Class Method to Create "pets" Table If Doesn't Already Exist
    #we only create this method once for all pets.
    # Pet.create_table() => creates table.
    @classmethod
    def create_table(cls):
        #SQL SYNTAX FOR CREATIGNG TABLE, 1ST COLUMN = ID, 2ND COLUMN ..ATTRIBUTES
        sql = """
            CREATE TABLE IF NOT EXISTS pets (
                id INTEGER PRIMARY KEY,
                name TEXT,
                species TEXT,
                breed TEXT,
                temperament TEXT)
        """

        #USE CURSOR TO EXECUTE SQL
        CURSOR.execute(sql)

    # ✅ 3. Add "drop_table" Class Method to Drop "pets" Table If Exists
    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS pets"
        CURSOR.execute(sql)


    # ✅ 4. Add "save" Instance Method to Persist New "pet" Instances to DB

    def save(self):  # insert new record into database
        sql = """
            INSERT INTO pets (name, species, breed, temperament)
            VALUES (?,?,?,?)
        """

        #USE CURSOR to execute sql, and pass values in tuple to database
        CURSOR.execute(sql, (self.name, self.species, self.breed, self.temperament))

        #COMMIT TO DB
        CONN.commit()

    # ✅ 5. Add "create" Class Method to Initialize and Save New "pet" Instances to DB

    #repeated Action that we are abstracting out into "create"
    @classmethod
    def create(cls, name, species, breed, temperament):

#instantiate the pets here __init__ method firing off.
        pet = cls(name, species, breed, temperament)
        pet.save() # we are referring back to save method here.
        return pet



    # ✅ 6. Add "new_from_db" Class Method to Retrieve Newest "pet" Instance w/ Attributes From DB
    @classmethod
    def new_from_db(cls, row):
        #reinstantiating class; takes the row and pulls the id from db and pass that as value.

        #row is tuple, we are pulling the values from the database when we reinstantiate the class.
        pet = cls(
            name=row[1],
            species=row[2],
            breed=row[3],
            temperament=row[4],
            id=row[0]
        )

        return pet


    # ✅ 7. Add "get_all" Class Method to Retrieve All "pet" Instances From DB
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM pets
            """

        return [cls.new_from_db(row) for row in CURSOR.execute(sql).fetchall()] #what does return to us from fetchall(), => returns a list of tuples.

    # ✅ 8. Add "find_by_name" Class Method to Retrieve "pet" Instance by "name" Attribute From DB

        # If No "pet" Found, return "None"

    @classmethod
    def find_by_name(cls, name): #find the matching name in the database.
        sql = """ SELECT * from pets 
        WHERE name = ?
        LIMIT 1
        """

        row = CURSOR.execute(sql, (name, )).fetchone() #1 row will be returned(tuple)

        #return None if no row is found
        if not row:
            return None
        #otherwise instantiate Pet class with tuple values and return that instance.
        return Pet.new_from_db(row)


    # ✅ 9. Add "find_by_id" Class Method to Retrieve "pet" Instance by "id" Attribute From DB => more likely to be used as callback

        # If No "pet" Found, return "None"

    @classmethod
    def find_by_id(cls, id):
        sql = """ SELECT * FROM pets
        WHERE id = ?
        LIMIT 1
        """
        row = CURSOR.execute(sql, (id, )).fetchone()

        if not row:
            return None
        # otherwise instantiate Pet class with tuple values and return that instance. we are going back and forth w database.
        return Pet.new_from_db(row)

    # ✅ 10. Add "find_or_create_by" Class Method to:

        #  Find and Retrieve "pet" Instance w/ All Attributes

        # If No "pet" Found, Create New "pet" Instance w/ All Attributes

    @classmethod
    def find_or_create_by(cls, name=None, species=None, breed=None, temperament=None):
        #look through all pets
        sql = """
        SELECT * FROM pets 
        WHERE (name, species, breed, temperament) = (?,?,?,?)
        """

        row = CURSOR.execute(sql, (name, species, breed, temperament)).fetchone()

        #if we do not find matching record
        if not row:
            #sql query for inserting new record into pets table
            sql = """
            INSERT INTO pets (name, species, breed, temperament)
            VALUES (?,?,?,?)
            """
            #execution of SQL
            row = CURSOR.execute(sql, (name, species, breed, temperament))

        #if we find a matching record...
        return Pet.new_from_db(row)


    # ✅ 12. Add "update" Class Method to Find "pet" Instance by "id" and Update "name" Attribute

    @classmethod
    def update(cls, id, name):
        sql = """
            """

    # ✅ 11. Add "update" Class Method to Find "pet" Instance by "id" and Update All Attributes

    def update(self):
        sql = """
            UPDATE pets
            SET name =?, species =?, breed =?, temperament =?
            WHERE id =?
            """

        #execute sql
        CURSOR.execute(sql, (self.name, self.species, self.breed, self.temperament, self.id))

        #commit to db
        CONN.commit()

    # ✅ 13. Add "delete" Class Method to Find "pet" Instance by "id" and Delete "pet" Instance From DB

    # def delete(self):
    #     sql =
    #     """