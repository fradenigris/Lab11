from database.DB_connect import DBConnect
from model.rifugio import Rifugio
from model.connessione import Connessione

class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    # TODO

    @staticmethod
    def get_all_rifugi():

        cnx = DBConnect.get_connection()
        result = []

        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT * FROM rifugio """

        try:
            cursor.execute(query)
            for row in cursor:
                rifugio = Rifugio(
                    id=row['id'],
                    nome=row['nome'],
                    localita=row['localita'],
                    altitudine=row['altitudine'],
                    capienza=row['capienza'],
                    aperto=row['aperto'],
                )
                result.append(rifugio)

        except Exception as e:
            print(f"Errore durante la query get_all_rifugi: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result


    @staticmethod
    def get_all_connessioni():

        cnx = DBConnect.get_connection()
        result = []

        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT * FROM connessione """

        try:
            cursor.execute(query)
            for row in cursor:
                connessione = Connessione(
                    id = row['id'],
                    id_rifugio1 = row['id_rifugio1'],
                    id_rifugio2 = row['id_rifugio2'],
                    distanza = row['distanza'],
                    difficolta = row['difficolta'],
                    durata = row['durata'],
                    anno = row['anno']
                )
                result.append(connessione)

        except Exception as e:
            print(f"Errore durante la query get_all_connessioni: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result


    @staticmethod
    def get_connessioni_filtrate(anno):

        cnx = DBConnect.get_connection()
        result = []

        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT * FROM connessione c
                    WHERE c.anno <= %s"""

        try:
            cursor.execute(query, (anno,))
            for row in cursor:
                connessione = Connessione(
                    id = row['id'],
                    id_rifugio1 = row['id_rifugio1'],
                    id_rifugio2 = row['id_rifugio2'],
                    distanza = row['distanza'],
                    difficolta = row['difficolta'],
                    durata = row['durata'],
                    anno = row['anno']
                )
                result.append(connessione)

        except Exception as e:
            print(f"Errore durante la query get_connessioni_filtrate: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result

