import csv
from string import Template
from pathlib import Path

# 1. 템플릿 읽기
with open("template.html", "r", encoding="utf-8") as f:
    tpl = Template(f.read())

# 2. 출력 폴더 준비 (docs)
output_dir = Path("docs")
output_dir.mkdir(exist_ok=True)

# 3. CSV 돌면서 페이지 생성
with open("electric_certificates.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        slug = row["slug"]              # ✅ CSV에서 slug 그대로 사용
        filename = f"{slug}.html"       # ✅ 파일 이름 만들기

        html = tpl.substitute(row)      # 종분류, 종목, 인정학점_전문 등 자동 치환

        (output_dir / filename).write_text(html, encoding="utf-8")

print("✅ 모든 자격증 페이지 생성 완료")
