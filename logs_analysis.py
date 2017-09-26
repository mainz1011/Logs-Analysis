import psycopg2

# Create a view for top_articles
top_articles = "CREATE VIEW top_articles_view AS SELECT title, author, count(*) AS views FROM articles, log WHERE log.path = concat('/article/', articles.slug) GROUP BY articles.title, articles.author ORDER BY views DESC;"

# Select the top 3 popular articles from top_articles_view
top3_articles = "SELECT title, views FROM top_articles_view LIMIT 3;"

# Select popular authors
popular_authors = "SELECT authors.name AS name, sum(top_articles_view.views) AS author_views FROM top_articles_view, authors WHERE authors.id = top_articles_view.author GROUP BY name ORDER BY author_views DESC;"

# Create an error view for log
errors = "CREATE VIEW error_log_view AS SELECT date(TIME), round(100.0 * sum(CASE log.status WHEN '200 OK' THEN 0 ELSE 1 END) / count(log.status), 2) AS \"Percent Error\" FROM log GROUP BY date(TIME) ORDER BY \"Percent Error\" DESC;"

# Select days on which precent_error is more than 1%  
errors_log = "SELECT * FROM error_log_view WHERE \"Percent Error\" > 1;"


# Define functions to execute views
def allviews():
    db = psycopg2.connect(database=DB_NAME)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM top_article_view")
    cursor.execute("SELECT * FROM error_log_view")
    db.close()

def create_views():
    db = psycopg2.connect(database="news")
    cursor = db.cursor()
    cursor.execute(top_articles)
    cursor.execute(errors)
    db.commit()
    db.close()


# Define a function to print results
def print_results(queryResult, ending):
    for res in queryResult:
        print('\t' + str(res[0]) + ' --- ' + str(res[1]) + ' ' + ending)

if __name__ == '__main__':
    db = psycopg2.connect(database="news")
    cursor = db.cursor()

    cursor.execute(top3_articles)
    print("\n1. The most popular three articles of all time are: ")
    print_results(cursor.fetchall(), 'views')

    cursor.execute(popular_authors)
    print("\n2. The most popular article authors of all time are: ")
    print_results(cursor.fetchall(), 'views')

    cursor.execute(errors_log)
    print("\n3. Days on which more than 1% of requests leading to errors: ")
    print_results(cursor.fetchall(), '%')
db.close()
