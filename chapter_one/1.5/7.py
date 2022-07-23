class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *memory):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = memory

    def get_config(self):
        return [
             f'Материнская плата: {self.name}',
             f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
             f'Слотов памяти: {self.total_mem_slots}',
             f'Память: {"; ".join([f"{i.name} - {i.volume}" for i in self.mem_slots])}'
        ]


cpu = CPU('cpu1', 123)
mem1 = Memory('mem1', 4096)
mem2 = Memory('mem2', 4096)
mb = MotherBoard('mb1', cpu, mem1, mem2)
