class Graph:
    def __init__(self, ma_tran):
        self.ma_tran = ma_tran
        self.so_dinh = len(ma_tran)

    def bfs(self, dinh_dau, dinh_cuoi, mang):
        check = [False]*self.so_dinh
        hang_doi = [dinh_dau]
        check[dinh_dau] = True

        while hang_doi:
            u = hang_doi.pop(0)

            for chi_so, trong_so in enumerate(self.ma_tran[u]):
                if not check[chi_so] and trong_so > 0:
                    hang_doi.append(chi_so)
                    check[chi_so] = True
                    mang[chi_so] = u

                    if chi_so == dinh_cuoi:
                        return True

        return False

    def ford_fulkerson(self, dinh_dau, dinh_cuoi):
        mang = [-1]*self.so_dinh
        luong_cuc_dai = 0

        while self.bfs(dinh_dau, dinh_cuoi, mang):
            gia_tri_luong = float("Inf")
            s = dinh_cuoi
            while s != dinh_dau:
                gia_tri_luong = min(gia_tri_luong, self.ma_tran[mang[s]][s])
                s = mang[s]

            luong_cuc_dai += gia_tri_luong
            v = dinh_cuoi
            while v != dinh_dau:
                u = mang[v]
                self.ma_tran[u][v] -= gia_tri_luong
                self.ma_tran[v][u] += gia_tri_luong
                v = mang[v]

        return luong_cuc_dai

do_thi = Graph([[0, 16, 13, 0, 0, 0],
               [0, 0, 10, 12, 0, 0],
               [0, 4, 0, 0, 14, 0],
               [0, 0, 9, 0, 0, 20],
               [0, 0, 0, 7, 0, 4],
               [0, 0, 0, 0, 0, 0]])

luong_cuc_dai = do_thi.ford_fulkerson(0, 5)
print(f"Luồng cực đại fmax = {luong_cuc_dai}")
