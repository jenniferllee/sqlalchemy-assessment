"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

A base query object.


# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

An association table manages many-to-many table relationships. It usually
contains foreign keys which reference primary keys for two (or many) other
tables. This allows the association table to bridge the many-to-many
relationship between two tables. For example, a book could have many genres,
and a genre could have many books. A BookGenre "middle table" would be an
association table which provides the "glue" between books and genres (although
it may not necessarily contain any meaningful fields, outside the associative
keys).


# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the ``id`` of "ram."
q1 = db.session.query(Brand).filter(Brand.brand_id == "ram").all()

# Get all models with the name "Corvette" and the brand_id "che."
q2 = db.session.query(Model).filter((Model.name == "Corvette") & (Model.brand_id == "che")).all()

# Get all models that are older than 1960.
q3 = db.session.query(Model).filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
q4 = db.session.query(Brand).filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor."
q5 = db.session.query(Model).filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = db.session.query(Brand).filter((Brand.founded == 1903) & (Brand.discontinued == None)).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = db.session.query(Brand).filter((Brand.discontinued.isnot(None)) | (Brand.founded < 1950)).all()

# Get any model whose brand_id is not "for."
q8 = db.session.query(Model).filter(Model.brand_id != 'for').all()



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    cars = db.session.query(Model.name, Brand.name, Brand.headquarters).filter((Model.year == year) & (Model.brand_id == Brand.brand_id)).all()

    for model_name, brand_name, brand_headquarters in cars:
        print "Model:%s, Brand:%s, Headquarters%s" % (model_name, brand_name, brand_headquarters)


def get_brands_summary():
    """Prints out each brand name and each model name with year for that brand
    using only ONE database query."""

    cars = db.session.query(Brand.name, Model.name, Model.year).filter(Brand.brand_id == Model.brand_id).all()

    for brand_name, model_name, model_year in cars:
        print "Brand: %s, Model: %s, Year: %s" % (brand_name, model_name, model_year)


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    mystr = "%" + mystr + "%"
    return db.session.query(Brand).filter(Brand.name.like(mystr)).all()


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    return db.session.query(Model).filter((Model.year >= start_year) & (Model.year < end_year)).all()
