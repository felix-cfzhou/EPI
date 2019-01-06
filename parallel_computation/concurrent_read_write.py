class Reader(threading.Thread):
    def run(self):
        with RW.LR:
            RW.read_count += 1

        print(RW.data)
        with RW.LR:
            RW.read_count -= 1
            RW.LR.notify()
        do_something_else()

class Writer(threading.Thread):
    def run(self):
        while True:
            with RW.LW:
                done = False
                while not done:
                    with RW.LR:
                        if RW.read_count == 0:
                            RW.data == 1
                            done = True
                        else:
                            while RW.read_count != 0:
                                RW.LR.wait()
            do_something_else()
