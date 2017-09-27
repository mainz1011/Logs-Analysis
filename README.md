# Logs Analysis
=============

## Setting up
### 1. Install Vagrant (link: https://www.vagrantup.com/downloads.html), Virtualbox (link: https://www.virtualbox.org/wiki/Downloads), and Python3 (link: https://www.python.org/downloads/).
### 2. Download the VM Configuration folder "fsnd-virtual-machine" (link: https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip).
### 3. Download the SQL data "newsdata.sql" (link: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip it, and then put it inside the folder "vagrant".
### 4. Right click on the folder "vagrant", click on "Git Bash here", a git bash terminal is open.
### 5. On the git bash terminal, set up vagrant by first running command `vagrant up`, second `vagrant ssh`. A "Ubuntu 16.04.3 LTS" virtual machine is built up.
### 6. Run command `cd /vagrant`, and then `ls`.
### 7. Run command `psql -d news -f newsdata.sql` to load the SQL data "newsdata.sql".
### 8. After loading "newsdata.sql", run `psql news` to explore the data.

## Exploring the data
### 1. Run `\dt`, it displays 3 tables: articles, authors, log.
### 2. Run `\d articles`, `\d authors`, `\d log`, respectively. Each command responds with the columns and their types of each table.
### 3. Run `select * from articles;`, `select * from authors;`, `select count(*) from log;`, respectively, to furthur explore the data.
### 4. Enter `\q` to exit from data exploration.

## Create views for the database
### 1. To reduce the complexity of creating queries for the first two questions: `CREATE VIEW top_articles_view AS SELECT title, count(*) AS views FROM log JOIN articles ON log.path = concat('/article/', articles.slug) GROUP BY articles.title ORDER BY views DESC;`./This view is created for listing articles according to their popularity in descending order, based on this, the queries for finding the three most popular articles and the most popular authors are created.
### 2. To reduce the complexity of creating a query for the third question: `CREATE VIEW error_log_view SELECT date(TIME), round(100.0 * sum(CASE log.status WHEN '200 OK' THEN 0 ELSE 1 END) / count(log.status), 2) AS \"Percent Error\" FROM log GROUP BY date(TIME) ORDER BY \"Percent Error\" DESC;`./This view is created for finding the days with percent of errors in descending order, based on this, the query for finding the days on which percent of errors is more than 1% is created.

## Run Python file and get the results
### 1. Place logs_analysis.py inside the folder "vagrant".
### 2. Run `python logs_analysis.py`.
