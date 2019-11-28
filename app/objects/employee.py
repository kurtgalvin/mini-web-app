from typing import List
from .abstract import Model


class Employee(Model):
    
    @staticmethod
    def form_fields() -> List[dict]:
        ''' Static method returning a list of dict's.
        Each dict represents a single value of employee, with the layout:
        {
            'label': str,
            'id': str,
            'required': bool
        }
        example:
        {
            'label': First Name,
            'id': first_name,
            'required': True
        }

        '''
        return [
            {
                'label': 'First Name',
                'id': 'first_name',
                'required': True
            },
            {
                'label': 'Last Name',
                'id': 'last_name',
                'required': True
            },
            {
                'label': 'E-mail',
                'id': 'email',
                'required': True
            },
            {
                'label': 'Position',
                'id': 'position',
                'required': True
            },
            {
                'label': 'Phone Number',
                'id': 'phone_number',
                'required': True
            },
            {
                'label': 'Salary',
                'id': 'salary',
                'required': True
            },
            {
                'label': 'Date Hired',
                'id': 'date_hired',
                'required': True
            },
        ]