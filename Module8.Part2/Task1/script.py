# Реалізувати серіалізацію об'єктів класу User без полів is_online та connected_device. При десеріалізації встановити
# значення за змовчуванням. Використовувати модуль pickle.
import pickle
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class User:
    username: str
    password_hash: str
    is_admin: bool
    is_online: bool
    connected_device: Optional[str]

    def __getstate__(self):
        return {
            key: value for key, value in self.__dict__.items()
            if key not in ("is_online", "connected_device")
        }

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.is_online = False
        self.connected_device = None


def update_user_list(user_list):
    pass


if __name__ == "__main__":
    dump_path = Path("users.pickle")

    if dump_path.exists():
        with open(dump_path, mode="rb") as dump_file:
            users = pickle.load(dump_file)
    else:
        users = []

    update_user_list(users)

    print(users)

    with open(dump_path, "wb") as dump_file:
        pickle.dump(users, dump_file)
