import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import urllib.request
import urllib.error
import zipfile
import os

# 1. 프리텐다드 폰트 다운로드 및 압축 해제
zip_url = 'https://github.com/orioncactus/pretendard/releases/download/v1.3.9/Pretendard-1.3.9.zip'
zip_path = 'pretendard.zip'
extract_dir = 'pretendard_fonts'
font_path = None

if not os.path.exists(extract_dir):
    print("Downloading Pretendard fonts release...")
    try:
        urllib.request.urlretrieve(zip_url, zip_path)
        print("Extracting fonts...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        os.remove(zip_path) # Clean up zip
    except Exception as e:
        print(f"Error downloading or extracting: {e}")

# Find TTF/OTF Medium font file
for root, dirs, files in os.walk(extract_dir):
    for file in files:
        if 'Pretendard-Medium.ttf' in file or 'Pretendard-Medium.otf' in file:
            font_path = os.path.join(root, file)
            break
    if font_path:
        break

if not font_path:
    print("Pretendard Medium font not found!")
    exit(1)

# 2. matplotlib 폰트 추가 및 전역 적용
print(f"Using font file: {font_path}")
font_manager.fontManager.addfont(font_path)
font_prop = font_manager.FontProperties(fname=font_path)
rc('font', family=font_prop.get_name())

# Data
years = ['2023년(추정)', '2024년']
counts = [902, 1543]
colors = ['#d8bfd8', '#6a0dad']

# Plot
plt.figure(figsize=(8, 6))
bars = plt.bar(years, counts, color=colors, width=0.5)

# 타이틀 및 라벨
plt.title('관광 불편 신고 건수 증감 추이 (2023-2024)', fontsize=18, color='#4b0082', fontweight='bold', pad=20)
plt.ylabel('신고 건수 (건)', fontsize=12)

# 눈금 및 테두리 색상 보라색으로 맞춤
plt.tick_params(colors='#4b0082')
for spine in plt.gca().spines.values():
    spine.set_color('#4b0082')

# 바(Bar) 상단에 데이터 수치 텍스트 표시
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 15, f'{int(yval)}건', ha='center', va='bottom', fontsize=13, fontweight='bold', color='#4b0082')

# 주요 정보 텍스트 박스
textstr = '▶ 전년(23년) 대비 71.1% 폭증 (총 1,543건)\n▶ 주요 원인: 쇼핑 안내 및 길찾기 등\n    기본 인프라 관련 불만 급증'
props = dict(boxstyle='round,pad=0.5', facecolor='#f8f0fc', alpha=0.9, edgecolor='#6a0dad')
plt.text(0.05, 0.95, textstr, transform=plt.gca().transAxes, fontsize=12,
        verticalalignment='top', bbox=props, color='#4b0082')

plt.tight_layout()

# Save image
out_img = r'C:\Users\user\.gemini\antigravity\brain\38dbc9ad-777b-44b2-b669-206022d8c9d4\artifacts\tourist_complaints_purple.png'
plt.savefig(out_img, dpi=300)
print('Success, chart saved with Pretendard font.')
