import csv, os, re
from string import Template
from pathlib import Path

# 1. 템플릿 불러오기
with open("template.html", "r", encoding="utf-8") as f:
    tpl = Template(f.read())

# 2. 출력 폴더 준비
output_dir = Path("site")
output_dir.mkdir(exist_ok=True)

# 3. CSV 읽기
with open("electric_certificates.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # 4. 파일 이름 만들기 (슬러그 변환)
        slug = re.sub(r'[^a-zA-Z0-9]+', '-', row['종목'])
        filename = f"{slug.lower()}.html"

        # 5. HTML 내용 채우기
        html = tpl.substitute(row)

        # 6. 저장
        with open(output_dir / filename, "w", encoding="utf-8") as out:
            out.write(html)

print("✅ 모든 자격증 페이지 생성 완료!")