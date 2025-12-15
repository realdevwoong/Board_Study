text = "   안녕하세요, 테크인웅입니다.! \t\n  "
print(f"원본 문자열: '{text}'") 
# 원본 문자열: '   안녕하세요, 파이썬! 	
#  '

cleaned_text = text.strip()
print(f"strip() 결과: '{cleaned_text}'")
# strip() 결과: '안녕하세요, 파이썬!'