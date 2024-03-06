from bs4 import BeautifulSoup

class BTTL_Bai1:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = BeautifulSoup(self.read_file(filepath), 'lxml')
        self.nhanviens = self.data.find_all('thong_tin_nhan_vien')  # Find all employee records
                
    def calculate_salary(self, employee_index):
        heso_luong_element = self.nhanviens[employee_index].find('HeSoLuong')
        if heso_luong_element is not None:
            heso_luong = float(heso_luong_element.text)
            return heso_luong * 1210 * self.calculate_HSTD(employee_index) + 1100 + self.calculate_PC(employee_index)
        else:
            return 0  # Handle the case where 'HeSoLuong' is not found

    def calculate_HSTD(self, employee_index):
        chuc_vu_element = self.nhanviens[employee_index].find('ChucVu')
        so_ngay_lam_viec_element = self.nhanviens[employee_index].find('SoNgayLamViec')

        if chuc_vu_element is not None and so_ngay_lam_viec_element is not None:
            chuc_vu = chuc_vu_element.text
            so_ngay_lam_viec = int(so_ngay_lam_viec_element.text)

            if chuc_vu == 'Lanh Dao':
                return 1
            elif chuc_vu == 'Nhan Vien':
                if so_ngay_lam_viec < 20:
                    return 0.6
                elif so_ngay_lam_viec > 22:
                    return 1
                else:
                    return 0.8
        else:
            return 0  # Handle the case where either 'ChucVu' or 'SoNgayLamViec' is not found

    def calculate_PC(self, employee_index):
        chuc_vu = self.nhanviens[employee_index].find('ChucVu').text if self.nhanviens[employee_index].find('ChucVu') else None
        return 2000 if chuc_vu == 'Lanh Dao' else 0

    def print_employee_information(self, employee_index):
        nhanvien = self.nhanviens[employee_index]
        id_element = nhanvien.find('id')
        name_element = nhanvien.find('name')
        phongban_element = nhanvien.find('phongban')
        chucvu_element = nhanvien.find('chucvu')
        thamnien_element = nhanvien.find('thamnien')
        hesoluong_element = nhanvien.find('hesoluong')
        songaylamviec_element = nhanvien.find('songaylamviec')
        
        error = 'không tìm thấy'

        if nhanvien is not None:
            print(f"Thong tin nhan vien {employee_index + 1}:")

            id_element = nhanvien.find('ID')
            if id_element is not None:
                print(f"Mã Nhân Viên: {id_element.text}")
            else:
                print(f"Mã Nhân Viên {error}.")

            name_element = nhanvien.find('Name')
            if name_element is not None:
                print(f"Họ và tên nhân viên: {name_element.text}")
            else:
                print(f"Họ và tên nhân viên {error}.")

            phongban_element = nhanvien.find('PhongBan')
            if phongban_element is not None:
                print(f"Phòng ban: {phongban_element.text}")
            else:
                print(f"Phòng ban {error}.")

            chucvu_element = nhanvien.find('ChucVu')
            if chucvu_element is not None:
                print(f"Chức Vụ : {chucvu_element.text}")
            else:
                print(f"Chức Vụ {error}.")

            thamnien_element = nhanvien.find('ThamNien')
            if thamnien_element is not None:
                print(f"ThamNien: {thamnien_element.text}")
            else:
                print(f"ThamNien {error}.")

            hesoluong_element = nhanvien.find('HeSoLuong')
            if hesoluong_element is not None:
                print(f"HeSoLuong: {hesoluong_element.text}")
            else:
                print(f"HeSoLuong {error}.")

            songaylamviec_element = nhanvien.find('SoNgayLamViec')
            if songaylamviec_element is not None:
                print(f"SoNgayLamViec: {songaylamviec_element.text}")
            else:
                print(f"SoNgayLamViec {error}.")

            heso_thidua = self.calculate_HSTD(employee_index)
            print(f"HeSoThiDua: {heso_thidua}")

            phu_cap = self.calculate_PC(employee_index)
            print(f"PhuCap: {phu_cap}")

            luong = self.calculate_salary(employee_index)
            print(f"Luong: {luong}")
        else:
            print(f"Nhan vien {employee_index + 1} khong ton tai.")

    def read_file(self, filepath):
        with open(filepath, 'r') as file:
            data = file.read()
        return data
    
def main():
    filepath = 'DATA_BAI1.xml'
    test = BTTL_Bai1(filepath)

    for employee_index in range(len(test.nhanviens)):
        test.print_employee_information(employee_index)
        print("-" * 30)

if __name__ == "__main__":
    main()
