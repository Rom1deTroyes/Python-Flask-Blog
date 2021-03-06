import mysql.connector as mysqlpyth

bdd = None
cursor = None

def connexion():
  global bdd
  global cursor
  bdd = mysqlpyth.connect(user='flaskblog', password='blog', host='172.23.208.1', port="3306", database='flask_blog')
  cursor = bdd.cursor()

def deconnexion():
  global bdd
  global cursor

  cursor.close()
  bdd.close()

def lire_posts():
  global cursor

  connexion()
  query = "SELECT * FROM posts"
  cursor.execute(query)
  posts = []
  
  for enregistrement in cursor :
    post = {}
    post['id'] = enregistrement[0]
    post['created'] = enregistrement[1]
    post['title'] = enregistrement[2]
    post['content'] = enregistrement[3]
    posts.append(post)

  deconnexion()
  return posts


def get_post(id):
  global cursor

  connexion()
  query = "SELECT * FROM posts WHERE id=" + str(id)
  cursor.execute(query)
  post = {}
  
  for enregistrement in cursor :
    post['id'] = enregistrement[0]
    post['created'] = enregistrement[1]
    post['title'] = enregistrement[2]
    post['content'] = enregistrement[3]

  deconnexion()
  return post

def set_post(title, content):
  global cursor
  global bdd
  connexion()

  query = 'INSERT INTO posts(title, content) VALUES ("'+title+'","'+content+'");'
  cursor.execute(query)
  bdd.commit()

  deconnexion()
