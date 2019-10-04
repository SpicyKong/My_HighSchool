import requests
import ast
from bs4 import BeautifulSoup    #BeautifulSoup import
import threading
"""
def execute_func(second=1.0):
    global end
    if end:
        return
    # 할거
    pass
    threading.Timer(second, excute_func, [second]).start()
    return 0 # 혹시몰라

1000 : 100
1000 : 100
2588 : 100
1330 : 100
2753 : 100
2739 : 100
2741 : 100
2438 : 100
2747 : 100
"""
def update_info():
    global question, participants, N_p, N_q, participants1
    with open("question.txt", "r", encoding='UTF8') as f:
        test_text = f.read()
        question = [list(map(int,i.split(':'))) for i in test_text.split('\n')]
        #print("question :",question)
        N_q = len(question)
    with open("participants.txt", "r", encoding='UTF8') as f:
        test_text = f.read()
        participants1 = [i.split(':') for i in test_text.split('\n')]
        participants = {a[1].strip():a[0].strip() for a in participants1}
        participants1 = [i[1] for i in participants1]
        #print(participants1)
        N_p = len(participants)
def update_score():
    global question, participants, N_p, N_q, participants1, list_board
    
    for c, list_a in enumerate(question):
        response = requests.get('https://www.acmicpc.net/status?from_problem=1&problem_id='+str(list_a[0])).text
        soup = BeautifulSoup(response, "html.parser")#html.parser를 사용해서 soup에 넣겠다
        data_user=soup.select('#status-table > tbody > tr > td:nth-of-type(2)')#nth-of-type(1)
        data_result=soup.select('#status-table > tbody > tr > td:nth-of-type(4)')
        for n, people in enumerate(data_user):
            for q, Id in enumerate(participants1):
                if Id.strip() == people.text.strip() and data_result[n].text == '맞았습니다!!':
                    if not list_board[q][c]:
                        list_board[q][c] = 1
                        list_board[q][-1] += list_a[1]
def get_data():
    with open("save_board.txt", "r", encoding='UTF8') as f:
        list_A = ast.literal_eval(f.read())
    return list_A
def modify_data(list_board):
    with open("save_board.txt", "w", encoding='UTF8') as f:
        f.write(str(list_board))
def send_result():
    global participants, participants1, list_board, N_p
    [requests.get("http://"""자세한 링크는 가리겠습니다.""".php?name="+participants[participants1[i].strip()]+"&score="+str(list_board[i][-1])) for i in range(N_p)]


update_info()
list_board = get_data()
update_score()
modify_data(list_board)


send_result()
