from typing import List

from pydantic import BaseModel


class UserAdd(BaseModel):
    username: str
    login: str
    email: str
    password: str


class Flashcard(BaseModel):
    """Base flashcard class"""
    question: str
    answer: str
    board_id: int


class FlashcardGet(Flashcard):
    """Getting a flashcard"""
    id: int


class BoardCreate(BaseModel):
    """Creating board for flashcards"""
    name: str
    owner_id: int


class Board(BaseModel):
    """Base board class"""
    id: int
    name: str
    owner_id: int


class BoardGet(Board):
    """Getting a board info"""
    flashcards: List[Flashcard]


class BoardList(BaseModel):
    """Getting a boards info"""
    boards: List[Board]


class UserBoard(BaseModel):
    """Getting a boards of user"""
    user_id: int
    username: str
    boards: List[Board]