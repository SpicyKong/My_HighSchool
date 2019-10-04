import requests
import ast
def update_info():
    with open("question.txt", "r", encoding='UTF8') as f:
        test_text = f.read()
        question = [list(map(int,i.split(':'))) for i in test_text.split('\n')]
        N_q = len(question)
    with open("participants.txt", "r", encoding='UTF8') as f:
        test_text = f.read()
        participants1 = [i.split(':') for i in test_text.split('\n')]
        participants = {a[1].strip():a[0].strip() for a in participants1}
        N_p = len(participants)
    with open("save_board.txt", "w", encoding='UTF8') as f:
        f.write(str([[0]*(N_q+1) for _ in range(N_p)]))
def get_data():
    with open("save_board.txt", "r", encoding='UTF8') as f:
        list_A = ast.literal_eval(f.read())
        print(list_A)
update_info  ()
