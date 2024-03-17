import ray
import prover
import random
import time
# establish connection to local ray head node
ray.init()

@ray.remote
class ProverActor:
    def __init__(self, q):
        self.queue = q
        self.rs_prover = prover.Prover(random.randint(0, 100))

    def prove_txn(self):
        # or use a long while loop to process a large amount of txns and do self call backs with next batch
        next_item = self.queue.get(block=True, timeout=1)
        ret = self.rs_prover.prove_txn(next_item)
        print(ret)
        return ret


from ray.util.queue import Queue
q = Queue()
items = list(range(10))
for item in items:
    q.put(item)
# optional to use detached actor and implement threading within the actor to have inifinite loop, or self callbacks
# constructing a list of prover Actors with name, and allow them to connect to the queue
proverRef = [ProverActor.options(name="ProverActor " + str(id)).remote(q) for id in range(2)]

# iterate over the lsit of proverActors and ask them to consume the queue
resultRef = [i.prove_txn.remote() for i in proverRef]


# blocking to get values
ray.get(resultRef)