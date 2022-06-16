from website import create_app

app = create_app()


#This means the file needs to be run directly - can't be imported
#debug=True displays changes - in production False
if __name__ == '__main__':
    app.run(debug=True)
