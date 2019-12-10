from app import app

app.secret_key = 'forsafe'
if __name__ == '__main__':
    app.run(processes=True)
