class WorkerImmuneSystem:
    def __init__(self):
        self.workers = []

    def register(self, worker):
        self.workers.append(worker)

    def scale_if_needed(self):
        active_load = sum(w.load for w in self.workers)

        if active_load > 10:
            return "SCALE_UP_TRIGGERED"
        if active_load == 0:
            return "IDLE_STATE"

        return "STABLE"

    def heal_workers(self):
        for w in self.workers:
            if not w.alive:
                w.self_heal()
