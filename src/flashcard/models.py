from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.flashcard.database import Base


class UserBoard(Base):
    __tablename__ = "user_board"

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    board_id: Mapped[int] = mapped_column(
        ForeignKey("board.id"), primary_key=True
    )
    can_delete: Mapped[bool] = mapped_column(default=False)
    can_add: Mapped[bool] = mapped_column(default=False)
    board: Mapped["Board"] = relationship(back_populates="users")
    user: Mapped["User"] = relationship(back_populates="boards")


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(30), unique=True)
    password: Mapped[str] = mapped_column(String(30))
    boards: Mapped[List["UserBoard"]] = relationship(
        back_populates="user"
    )


class Board(Base):
    __tablename__ = "board"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)
    users: Mapped[List["UserBoard"]] = relationship(
        back_populates="board"
    )
    flashcards: Mapped[List["Flashcard"]] = relationship(back_populates="board")


class Flashcard(Base):
    __tablename__ = "flashcard"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    question: Mapped[str] = mapped_column(String(255))
    answer: Mapped[str] = mapped_column(String(255))
    board_id: Mapped[int] = mapped_column(ForeignKey("board.id"))
    board: Mapped["Board"] = relationship(back_populates="flashcards")


