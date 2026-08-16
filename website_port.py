from flask import Flask, render_template, request, redirect, url_for
import wordle_solver_main

app = Flask(__name__)

@app.route('/favicon.png')
def favicon():
    return app.send_static_file('favicon.png')

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        known_letters =  request.form.get('known_letters_input')
        bad_letters = request.form.get('bad_letters_input')
        clue_letters = request.form.get('clue_letters_input')
        return redirect(url_for('solution_page', known_letters=known_letters, bad_letters=bad_letters, clue_letters=clue_letters))
    return render_template('index.html')

@app.route("/solution")
def solution_page():
    known_letters = request.args.get('known_letters')
    bad_letters = request.args.get('bad_letters')
    clue_letters = request.args.get('clue_letters')
    results = wordle_solver_main.wordle_solver(known_letters=known_letters,
                                               bad_letters=bad_letters,
                                               clue_letters=clue_letters)

    return render_template('wordle_solved.html', high_potential_words=results[0], words_based_on_cl=results[1])

