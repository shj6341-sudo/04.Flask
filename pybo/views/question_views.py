from flask import Blueprint, render_template
from pybo.models import Question
from datetime import datetime

bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/list/')
def _list():
    question_list = Question.query.order_by(Question.create_date.desc())

    # render_template ==> html 파일을 불러오는 역할
    return render_template('question/question_list.html', question_list=question_list, datetime=datetime)
    # import 해온 모듈(datetime 등)을 HTML 안에서 사용하려면 키워드 인자로 전달해야 함
    # question_list는 화면에 보여줄 '데이터'라서 키워드 인자로 넘겨주는 것

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question = question, datetime=datetime)