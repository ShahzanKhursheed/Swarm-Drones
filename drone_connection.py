from dronekit import connect
import time


def connect_drone(conn):

    for i in range(5):

        try:

            print("Connecting", conn)

            v = connect(
                conn,
                wait_ready=False,
                timeout=60,
                heartbeat_timeout=60
            )

            print("Connected")

            return v

        except:

            time.sleep(2)

    raise Exception("Connection failed")
