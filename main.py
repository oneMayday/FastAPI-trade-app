from datetime import datetime
from enum import Enum
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
	title="Trading app"
)

fake_users = [
	{'id': 1, 'role': 'admin', 'name': 'Админ Василий', "degree": [
		{"id": 0, "degree_type": "newbie", "created_at": "2023-05-18T08:35:32.321Z"}
	]},
	{'id': 2, 'role': 'investor', 'name': 'Инвестор Петрович', "degree": [
		{"id": 0, "degree_type": "newbie", "created_at": "2023-05-18T08:35:32.321Z"}
	]},
	{'id': 3, 'role': 'trader', 'name': 'Трейдер Михалыч',  "degree": [
		{"id": 0, "degree_type": "newbie", "created_at": "2023-05-18T08:35:32.321Z"}
	]
	}
]

fake_trades = [
	{'id': 1, 'user_id': 1, 'currency': 'BTC', 'side': 'buy', 'price': 212.2, 'amount': 2.2},
	{'id': 2, 'user_id': 1, 'currency': 'ETH', 'side': 'sell', 'price': 217.5, 'amount': 2.15}
]


class DegreeType(Enum):
	newbie = 'newbie'
	expert = 'expert'


class Degree(BaseModel):
	id: int
	degree_type: DegreeType
	created_at: datetime


class Side(Enum):
	buy = 'buy'
	sell = 'sell'


class User(BaseModel):
	id: int
	role: str
	name: str
	degree: List[Degree]


class Trade(BaseModel):
	id: int
	user_id: int
	currency: str
	side: str = Side
	price: float = Field(ge=0)
	amount: float = Field(ge=0)


@app.get('/users/{user_id}', response_model=List[User])
def get_user(user_id: int):
	return [user for user in fake_users if user['id'] == user_id]


@app.post('/users/create')
def create_user(user_params: List[User]):
	fake_users.extend(user_params)
	current_user = fake_users[-1]
	return {'status': 200, 'data': current_user}


@app.post('/users/{user_id}')
def change_name(user_id: int, new_name: str):
	current_user = list(filter(lambda user: user.get('id') == user_id, fake_users))[0]
	current_user['name'] = new_name
	return {'status': 200, 'data': current_user}


@app.post('/trades')
def add_trades(trades: List[Trade]):
	fake_trades.extend(trades)
	return {'status': 200, 'data': fake_trades}
