import pandas as pd

def modif_column_name(file_path):
    # 원본 CSV 파일과 새 파일 경로
    output_file = 'downloaded_files/downoutput.csv'

    df = pd.read_csv(file_path, encoding='utf-8-sig')
    df.columns = ['받는사람 이름',	'받는사람 전화번호',	'받는사람 전화번호2',	'받는사람 주소',	'받는사람 상세주소',	
                        '상품 이름',	'옵션 이름',	'상품 수량',	'배송메시지',	'주문일시',	'주문번호']
    df.to_excel('downloaded_files/togle.xlsx', index=False) 


    return True
    



