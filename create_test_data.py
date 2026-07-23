from datetime import datetime
from pybo import create_app, db
from pybo.models import Question

app=create_app()
with app.app_context():
    print("테스트 데이터 생성 시작...")

    questions = [
        Question(
            subject=f'[테스트 데이터 입니다:{i:03d}]',
            content = '내용입니다.',
            create_date=datetime.now()
        )
        for i in range(300)
    ]

    db.session.bulk_save_objects(questions)

    db.session.commit()
    print(f"성공적으로 {len(questions)}개의 데이터가 pybo.db에 등록되었습니다.")