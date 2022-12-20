from Mailer import Mailer
from Server import Server
from dotenv import load_dotenv
from collector import Collector

if __name__ == "__main__":
    load_dotenv()

    server = Server()
    server.connect()

    mailer = Mailer(server.EMAIL, server.PASSWORD)
    collector = Collector(server.EMAIL, server.PASSWORD, )

    while True:
        try:
            data = server.client_socket.recv(1024).decode("utf-8")
            data = str(data).split(":")
            mailer.send(data[0], data[1])
            mailer.echo(data[1])
            collector.log("success_request.log", f"[Token #{mailer.ID}] {mailer.MSG}")
            exit(0)
        except TypeError:
            print("TypeError!")
            mailer.echo(data[1], False)
            collector.log("error_request.log", str(TypeError))
        except ValueError:
            print("ValueError!")
            mailer.echo(data[1], False)
            collector.log("error_request.log", str(ValueError))
        except Exception as e:
            print("Invalid Error!")
            mailer.echo(data[1], False)
            collector.log("error_request.log", str(e))
