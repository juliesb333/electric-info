import csv
from string import Template
from pathlib import Path

# 1. 템플릿 읽기
with open("template.html", "r", encoding="utf-8") as f:
    tpl = Template(f.read())

# 2. 출력 폴더 준비 (docs)
output_dir = Path("docs")
output_dir.mkdir(exist_ok=True)

# 3. CSV 읽어서 페이지 생성
with open("electric_certificates.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        slug = row["slug"]  # 파일 이름용 키

        # 템플릿에 넣을 데이터 매핑
        data = {
            "slug": slug,
            "name": row["종목"],
            "category": row["종분류"],
            "job_code": row["직무번호"],
            "credit_junior": row["인정학점_전문"],
            "credit_bachelor": row["인정학점_학사"],
        }

        html = tpl.substitute(data)

        # docs/slug.html 로 저장
        (output_dir / f"{slug}.html").write_text(html, encoding="utf-8")

print("✅ 모든 자격증 페이지 생성 완료")
