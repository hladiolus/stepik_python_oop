import sys
from typing import List, Dict, Optional


class Record:
    INCREMENTOR = 0

    def __init__(self, fio: str, descr: str, old: int):
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = Record.INCREMENTOR
        Record.INCREMENTOR += 1

    def __hash__(self) -> int:
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other: 'Record') -> bool:
        return self.__hash__() == other.__hash__()


class DataBase:
    def __init__(self, path: str):
        self.path = path
        self.dict_db: Dict[Record, List[Record]] = {}

    def write(self, record: Record) -> None:
        if isinstance(record, Record):
            self.dict_db[record] = self.dict_db.get(record, []) + [record]
        else:
            raise ValueError

    def read(self, pk: int) -> Optional[Record]:
        if isinstance(pk, int):
            for v in self.dict_db.values():
                for obj in v:
                    if obj.pk == pk:
                        return obj
            return None
        else:
            raise ValueError


lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in не менять!

db = DataBase('')
for line in lst_in:
    name, descr, old = line.split('; ')
    db.write(Record(name, descr, int(old)))
