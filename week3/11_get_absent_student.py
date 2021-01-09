

all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

def get_absent_student(all_array, present_array):

    student_dict = {} #학생들은 담는 딕셔너리, 해쉬테이블로 사용시 {}로 표현해야함!!
    for key in all_array:
        student_dict[key] = True #키 등록

    for key in present_array:
        del student_dict[key] #출석한 학생의 키 삭제

    for key in student_dict.keys():
        return key

print(get_absent_student(all_students, present_students))