from Functions.api_client import ApiClient
from Functions.repository import Repository
from Functions.console_app import ConsoleApp

def main():
    base_url = "https://jsonplaceholder.typicode.com"
    api_client = ApiClient(base_url)
    repository = Repository(api_client)
    app = ConsoleApp(repository)
    app.run()

if __name__ == "__main__":
    main()
