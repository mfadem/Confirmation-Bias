from bottle import *
import webbrowser


@route('/cnn')
def CNN():
    return ("<strong>Welcome to CNN top stories<strong>")

@route('/')
def main():
    yield("<h1>Welcome to Conformation Bias</h1>")
    yield("<h2>The news how you see it</h2>")
    return ()

#webbrowser.open_new_tab('http://localhost:8080/')
#run(host='localhost', port=8080, debug=True) # Set home to 0.0.0.0 and use your_ip:8080 to resolve page

if __name__ == '__main__':
    main()
