import logging
import time
import multiprocessing
import codecs

logging.basicConfig(level=logging.INFO, format="[%(asctime)s][%(levelname)s] %(message)s")

def run_a(inq, outq):
    while True:
        msg = inq.get()
        logging.info(f"(a) got message: {msg}")
        if msg == "DONE":
            break
        msg = msg.lower()
        logging.info(f"(a) send message: {msg}")
        outq.put(msg.lower())
        time.sleep(5)


def run_b(inq, outq):
    def rot13(s):
        return codecs.encode(s, "rot_13")

    while True:
        msg = inq.get()
        logging.info(f"(b) got message: {msg}")
        if msg == "DONE":
            break
        msg = rot13(msg)
        logging.info(f"(b) encoded message: {msg}")
        logging.info(f"(b) send message: {msg}")
        outq.put(msg)


def main():
    q1 = multiprocessing.Queue()
    q2 = multiprocessing.Queue()
    q3 = multiprocessing.Queue()

    process_a = multiprocessing.Process(target=run_a, args=(q1, q2))
    process_b = multiprocessing.Process(target=run_b, args=(q2, q3))

    process_a.start()
    process_b.start()

    try:
        while True:
            msg = input("message >>> ")
            if msg.lower() == "exit":
                break
            q1.put(msg)
    except KeyboardInterrupt:
        pass

    process_a.terminate()
    process_b.terminate()

    logging.info("the end")


if __name__ == "__main__":
    main()
