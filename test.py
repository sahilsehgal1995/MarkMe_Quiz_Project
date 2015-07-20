from dbConnect import connection

c, conn= connection()

def test(id):
  c.execute("select * from questions where qno ='%s'" %(id))
  return c.fetchone()
  