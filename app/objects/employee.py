from typing import List

import configparser
import psycopg2


class Employee:
    def __init__(self, **kwargs):
        self.id = None
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.phone_number = ''.join(i for i in self.phone_number if i.isdigit())

    def create(self) -> dict:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute("""
                        INSERT INTO employee(first_name, last_name, email, "position", phone_number, salary, date_hired)
                        VALUES (%s, %s, %s, %s, %s, %s, %s);
                    """, (self.first_name, self.last_name, self.email, self.position, int(self.phone_number), int(self.salary), self.date_hired))
                except psycopg2.IntegrityError:
                    return {'complete': False, 'error': 'IntegrityError'}
                except:
                    return {'complete': False, 'error': 'database error'}
        return {'complete': True}

    @staticmethod
    def get_all() -> list:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM employee')
                return [{
                    'id': i[0],
                    'first_name': i[1],
                    'last_name': i[2],
                    'email': i[3],
                    'position': i[4],
                    'phone_number': i[5],
                    'salary': i[6],
                    'date_hired': i[7],
                } for i in cur.fetchall()]
    
    @staticmethod
    def form_fields() -> List[dict]:
        ''' Static method returning a list of dict's.
        Each dict represents a single value of employee, with the layout:
        {
            'label': str,
            'id': str,
            'type': str,
            'required': bool
        }
        example:
        {
            'label': 'First Name',
            'id': 'first_name',
            'type': 'text',
            'required': True
        }

        '''
        return [
            {
                'label': 'First Name',
                'id': 'first_name',
                'type': 'text',
                'required': True
            },
            {
                'label': 'Last Name',
                'id': 'last_name',
                'type': 'text',
                'required': True
            },
            {
                'label': 'E-mail',
                'id': 'email',
                'type': 'email',
                'required': True
            },
            {
                'label': 'Position',
                'id': 'position',
                'type': 'text',
                'required': True
            },
            {
                'label': 'Phone Number',
                'id': 'phone_number',
                'type': 'tel',
                'required': True
            },
            {
                'label': 'Salary',
                'id': 'salary',
                'type': 'number',
                'required': True
            },
            {
                'label': 'Date Hired',
                'id': 'date_hired',
                'type': 'date',
                'required': True
            },
        ]


def get_db_connection():
    config = configparser.ConfigParser()
    config.read('app/env/config.ini')
    return psycopg2.connect(
        host=config['aws']['host'],
        database=config['aws']['database'],
        user=config['aws']['user'],
        password=config['aws']['password']
    )