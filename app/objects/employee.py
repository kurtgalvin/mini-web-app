from typing import List

import configparser
import os
import psycopg2


class Employee:
    def __init__(self, id=None, **kwargs):
        if id:
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM employee WHERE id = %s', (id,))
                    r = cur.fetchone()
                    for k, v in self._normalize_to_dict(r).items():
                        setattr(self, k, v)

        for k, v in kwargs.items():
            setattr(self, k, v)
            
        if isinstance(self.phone_number, str):
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

    def update(self) -> dict:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute("""
                        UPDATE employee
                        SET first_name=%s, last_name=%s, email=%s, "position"=%s, phone_number=%s, salary=%s, date_hired=%s
                        WHERE id=%s
                    """, (self.first_name, self.last_name, self.email, self.position, int(self.phone_number), int(self.salary), self.date_hired, self.id))
                except psycopg2.IntegrityError:
                    return {'complete': False, 'error': 'IntegrityError'}
                except:
                    return {'complete': False, 'error': 'database error'}
        return {'complete': True}

    def delete(self) -> dict:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute("""
                        DELETE FROM employee
                        WHERE id=%s
                    """, (self.id,))
                except:
                    return {'complete': False}
        return {'complete': True}
                    

    @staticmethod
    def _normalize_to_dict(result: tuple) -> dict:
        return {
            'id': result[0],
            'first_name': result[1],
            'last_name': result[2],
            'email': result[3],
            'position': result[4],
            'phone_number': result[5],
            'salary': result[6],
            'date_hired': result[7],
        }

    @staticmethod
    def get_all() -> list:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM employee')
                return [Employee._normalize_to_dict(i) for i in cur.fetchall()]
    
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
    # config = configparser.ConfigParser()
    # config.read('app/env/config.ini')
    # return psycopg2.connect(
    #     host=config['aws']['host'],
    #     database=config['aws']['database'],
    #     user=config['aws']['user'],
    #     password=config['aws']['password']
    # )
    return psycopg2.connect(
        host=os.environ.get('host'),
        database=os.environ.get('database'),
        user=os.environ.get('user'),
        password=os.environ.get('password')
    )