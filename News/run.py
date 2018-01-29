from app import app

if __name__ == '__main__':
    app.run(debug = True)

def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The Best News Page Online'
    return render_template('index.html',title = title)
