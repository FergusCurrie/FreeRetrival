
import sqlite3
import sys
import os
from SqliteConnector import SqliteConnector
import uuid 

class FreeRetrival():
    def __init__(self) -> None:
        self.sqlite_connector = SqliteConnector()

    def read_all_from_database(self):
        self.sqlite_connector.query("SELECT * FROM retrivals")

    def scheduler(self) -> int:
        pass

    def next_card(self):
        # 1. get next card
        card_id = self.scheduler()
        card_row = self.sqlite_connector.query(f"SELECT * FROM cards WHERE card_id = {card_id}")
        print(f'Card to study : {card_row["card_header"]}')
        return card_id

    def show_card(self):
        print('place holder for showing card ')

    def rate_card(self, card_id):
        rating = input('Rate card (1-3): ')
        self.sqlite_connector.query(
            f"SELECT LAST_INSERT_ROWID() + 1 AS next_id FROM retrivals; INSERT INTO retrivals (id, card_id, rating) VALUES (next_id, {card_id}, {rating})"
        )

    def check_continue():
        stopping = False
        do_stop = input('Continue? (y/n): ')
        if do_stop.strip().lower() == 'n':
            stopping = True
            print('Stopping...')
        return stopping

    def main(self):
        # 1. get next card 
        # 2. wait for user to input 
        # 3. show card 
        # 4. user input to rate card 
        # 5. repeat 

        stopping = False

        while not stopping:
            # 1. get next card
            card_id = self.do_next_card()

            # 2. wait for user to input
            input('press any key to continue...')

            # 3. show card 
            self.show_card()

            # 4.   user input to rate card
            self.rate_card(card_id=card_id)


            # 5. Repeat 
            stopping = self.check_continue()
        
        # clean up
        self.sqlite_connector.close()





if __name__ == "__main__":
    # check if we're studying or filling the db 
    response = input('enter "9" to fill db otherwise press any key to start study')
    if response == '9':
        print('filling db')
        sqlite_connector = SqliteConnector()
        for fn in os.listdir('data/to_add'):
            print(f'\nProcessing filename = {fn}')
            # use uuid library to generate a uuid
            uuid = str(uuid.uuid4())
            header = input('Enter the card header: ')
            
            sqlite_connector.query(
                f"SELECT LAST_INSERT_ROWID() + 1 AS next_id FROM cards; INSERT INTO cards (id, file_name, card_header) VALUES (next_id, {uuid}, {header})"
            )

            # now move files into the data/cards folder
            os.rename(f'to_add/{fn}', f'data/cards/{uuid}.pdf')

        sqlite_connector.close()
    else:
        print('starting study')
        fr = FreeRetrival()
        fr.main()


