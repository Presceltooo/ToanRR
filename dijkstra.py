import sys
def dijkstra(do_thi, dinh_bat_dau):
    D = {v:float('inf') for v in do_thi} 
    for dinh in do_thi:
        for dinh_ke in do_thi[dinh]:
            D[dinh_ke] = float('inf')
    D[dinh_bat_dau] = 0 
    dinh_do_thi = list(do_thi)
    duong_di = {}

    while dinh_do_thi:
        dinh_min = None
        for dinh in dinh_do_thi: 
            if dinh_min is None:
                dinh_min = dinh
            elif D[dinh] < D[dinh_min]:
                dinh_min = dinh

        for dinh_ke, trong_so in do_thi[dinh_min].items():
            if trong_so + D[dinh_min] < D[dinh_ke]: 
                D[dinh_ke] = trong_so + D[dinh_min]
                duong_di[dinh_ke] = dinh_min
        dinh_do_thi.remove(dinh_min)

    return D, duong_di

def duong_di_ngan_nhat(do_thi, dinh_bat_dau, dinh_ket_thuc):
    D, duong_di = dijkstra(do_thi, dinh_bat_dau)

    duong_di_ngan_nhat = []
    while dinh_ket_thuc is not None:
        duong_di_ngan_nhat.append(dinh_ket_thuc)
        dinh_ket_thuc = duong_di.get(dinh_ket_thuc)

    return duong_di_ngan_nhat[::-1]

def nhap_do_thi():
    do_thi = {}
    print('''Nhập theo cú pháp: đỉnh bắt đầu 'cách' đỉnh kết thúc 'cách' trọng số
Nếu nhập hết rồi hãy ấn 'e' để đến bước tiếp theo''')
    while True:
        du_lieu = input("Nhập dữ liệu: ")
        if du_lieu == 'q':
            break
        dinh_bat_dau, dinh_ket_thuc, trong_so = du_lieu.split()
        trong_so = int(trong_so)
        if dinh_bat_dau not in do_thi:
            do_thi[dinh_bat_dau] = {}
        do_thi[dinh_bat_dau][dinh_ket_thuc] = trong_so
    return do_thi

do_thi = nhap_do_thi()
dinh_bat_dau = input("Nhập đỉnh bắt đầu: ")
dinh_ket_thuc = input("Nhập đỉnh kết thúc: ")
print("Đường đi ngắn nhất từ", dinh_bat_dau, "đến", dinh_ket_thuc, ":", duong_di_ngan_nhat(do_thi, dinh_bat_dau, dinh_ket_thuc))

