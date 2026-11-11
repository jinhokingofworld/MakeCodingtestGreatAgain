class circleQueue:
    def __init__(self, data):
        self.queue = [None for x in range(data)]
        self.front = 0
        self.rear = 0
        self.size = data

    # rear와 front의 인덱스가 같아지면 비어있는 상태
    # (rear + 1) % size == front이면 다 찬 상태

    # rear를 늘려서 큐를 집어넣는다.
    def enqueue(self, data):
        # 큐가 다 찼는지 확인
        if (self.rear + 1) % self.size == self.front: 
            return False

        self.queue[self.rear] = data
        self.rear = (self.rear + 1) % self.size

        return True

    def dequeue(self):
        # 큐가 비어있는지 확인
        if self.rear == self.front:
            return None

        data = self.queue[self.front]
        self.front = (self.front + 1) % self.size

        return data

    def printQueue(self):
        return print(self.queue)