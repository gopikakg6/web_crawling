
import psycopg2

def get_connection(db_name="lyrics"):
    return psycopg2.connect(f"dbname={db_name}")


def add_artists(artist_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("insert into artists (artist_name) values (%s)",(artist_name,))
    cursor.execute("select id from artists order by id desc")
    id = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return id



def add_songs(song_name,artist_id,lyrics):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("insert into songs (song_name,artist_id,lyrics) values (%s,%s,%s)",(song_name,artist_id,lyrics))
    conn.commit()
    conn.close()





