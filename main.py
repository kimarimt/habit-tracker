import requests
import os
import datetime
from dotenv import load_dotenv

load_dotenv()
GRAPH_NAME = 'Meditation'
GRAPH_ID = 'med-tracker'
TOKEN = os.getenv('PIXELA_TOKEN')


def create_graph():
    graph_endpoint = f'https://pixe.la/v1/users/agdeveloper93/graphs'
    headers = {
        'X-USER-TOKEN': TOKEN,
    }
    config = {
        'id': GRAPH_ID,
        'name': GRAPH_NAME,
        'unit': 'minutes',
        'type': 'int',
        'color': 'sora',
    }

    response = requests.post(
        url=graph_endpoint,
        headers=headers,
        json=config
    )

    print(response.json())


def update_point():
    today = datetime.datetime.today().strftime('%Y%m%d')
    update_graph = f'https://pixe.la/v1/users/agdeveloper93/graphs/{GRAPH_ID}'
    headers = {
        'X-USER-TOKEN': TOKEN
    }
    config = {
        'date': today,
        'quantity': '30'
    }

    response = requests.post(
        url=update_graph,
        headers=headers,
        json=config
    )

    print(response.json())


def main():
    create_graph()
    update_point()


if __name__ == '__main__':
    main()
