
from flask import Flask, jsonify, redirect, render_template, request, url_for, session
from datetime import datetime
from kgqa.exportPairs import exportToJSON
from kgqa.gep import GetEntity
from kgqa.qna import QuestionAnswer

app = Flask(__name__)

#set secret key
app.secret_key = 'SECRET_KEY'


class CheckAndSave:
    """docstring for CheckAndSave."""

    def __init__(self):
        super(CheckAndSave, self).__init__()

    def createdataset(self, para, que, ent, ans1, ans2):

        wholedata = {"para":[str(para)],"que":[[str(que)]], "entities":[ent], "ans1": [ans1], "ans2":[ans2]}

class OurModel:
    def __init__(self):
        self.getent = GetEntity()
        self.qa = QuestionAnswer()
        self.export = exportToJSON()

    def getAnswer(self, paragraph, question):

        refined_text = self.getent.preprocess_text([paragraph])
        dataEntities, numberOfPairs = self.getent.get_entity(refined_text)

        if dataEntities:
            self.export.dumpdata(dataEntities[0])
            outputAnswer = self.qa.findanswer(str(question), numberOfPairs)
            if outputAnswer == []:
                return None
            return outputAnswer
        return None

@app.route('/', methods=['GET'])
def cover():
    return render_template('cover.html')

@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/answer_me', methods=['GET', 'POST'])
def main():
    return render_template('app.html')

@app.route('/clear', methods=['GET', 'POST'])
def clear():
    return redirect(url_for('main'))

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    model2 = OurModel()
    save = CheckAndSave()
    input_paragraph = str(request.form["paragraph"])
    input_question = str(request.form["question"])
    my_answer = model2.getAnswer(input_paragraph, input_question)
    session['answer']=my_answer;

    return redirect(url_for('answer'))


@app.route('/answer', methods=['GET'])
def answer():
    return render_template('answer.html', answer=session['answer'])

@app.route('/group', methods=['GET'])
def group():
    return render_template('group.html')


if __name__ == "__main__":
    app.run(debug=True)
