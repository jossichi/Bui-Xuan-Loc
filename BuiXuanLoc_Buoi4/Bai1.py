from bs4 import BeautifulSoup

class BTTL_Bai1:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = BeautifulSoup(self.read_file(filepath), 'lxml')
        self.thong_tin_nhan_vien = self.data.find('thong_tin_nhan_vien')  # Get the root element
        self.nhanviens = self.thong_tin_nhan_vien.find_all(lambda tag: tag.name.startswith('nhanvien_'))  # Find all employee records
        print(f"Tổng nhân viên: {len(self.nhanviens)}")

    def calculate_salary(self, employee_index):
        heso_luong_element = self.nhanviens[employee_index].find('hesoluong')
        if heso_luong_element is not None:
            heso_luong = float(heso_luong_element.text)
            return heso_luong * 1210 * self.calculate_HSTD(employee_index) + 1100 + self.calculate_PC(employee_index)
        else:
            return 0  # Handle the case where 'hesoluong' is not found

    def calculate_HSTD(self, employee_index):
        chuc_vu_element = self.nhanviens[employee_index].find('chucvu')
        so_ngay_lam_viec_element = self.nhanviens[employee_index].find('songaylamviec')

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
            return 0  # Handle the case where either 'chucvu' or 'songaylamviec' is not found

    def calculate_PC(self, employee_index):
        chuc_vu = self.nhanviens[employee_index].find('chucvu').text if self.nhanviens[employee_index].find('chucvu') else None
        return 2000 if chuc_vu == 'Lanh Dao' else 0

    def print_employee_information(self, employee_index):
        nhanvien = self.nhanviens[employee_index]

        error = 'không tìm thấy'

        if nhanvien is not None:
            print(f"Thông tin nhân viên {employee_index + 1}:")

            id_element = nhanvien.find('id')
            if id_element is not None:
                print(f"Mã Nhân Viên: {id_element.text}")
            else:
                print(f"Mã Nhân Viên {error}.")

            name_element = nhanvien.find('name')
            if name_element is not None:
                print(f"Họ và tên nhân viên: {name_element.text}")
            else:
                print(f"Họ và tên nhân viên {error}.")

            phongban_element = nhanvien.find('phongban')
            if phongban_element is not None:
                print(f"Phòng ban: {phongban_element.text}")
            else:
                print(f"Phòng ban {error}.")

            chucvu_element = nhanvien.find('chucvu')
            if chucvu_element is not None:
                print(f"Chức Vụ : {chucvu_element.text}")
            else:
                print(f"Chức Vụ {error}.")

            thamnien_element = nhanvien.find('thamnien')
            if thamnien_element is not None:
                print(f"Thâm niên: {thamnien_element.text}")
            else:
                print(f"Thâm niên {error}.")

            hesoluong_element = nhanvien.find('hesoluong')
            if hesoluong_element is not None:
                print(f"Hệ số lương: {hesoluong_element.text}")
            else:
                print(f"Hệ số lương {error}.")

            songaylamviec_element = nhanvien.find('songaylamviec')
            if songaylamviec_element is not None:
                print(f"Số ngày làm việc: {songaylamviec_element.text}")
            else:
                print(f"Số ngày làm việc {error}.")

            heso_thidua = self.calculate_HSTD(employee_index)
            print(f"Hệ số thi đua: {heso_thidua}")

            phu_cap = self.calculate_PC(employee_index)
            print(f"Phụ cấp: {phu_cap}")

            luong = self.calculate_salary(employee_index)
            print(f"Lương: {luong}")
        else:
            print(f"Nhân viên {employee_index + 1} không tồn tại.")

    def read_file(self, filepath):
        with open(filepath, 'r') as file:
            data = file.read()
        return data

    def total_salary(self):
        total = 0
        for employee_index in range(len(self.nhanviens)):
            total += self.calculate_salary(employee_index)
        return total
    
    def export_employee(self, employee_index):
        heso_luong_element = self.nhanviens[employee_index].find('hesoluong')
        phong_ban_element = self.nhanviens[employee_index].find('phongban')

        if heso_luong_element is not None and phong_ban_element is not None:
            heso_luong = float(heso_luong_element.text)
            phong_ban = phong_ban_element.text

            if heso_luong > 4.34 and phong_ban == 'TAI VU':
                print(f"Thông tin nhân viên có hệ số lương lớn hơn 4.34 và làm ở phòng tài vụ:")
                self.print_employee_information(employee_index)

    def print_all_employee_information(self):
        for employee_index in range(len(self.nhanviens)):
            
            self.print_employee_information(employee_index)
            print("-" * 30)
        print(f"Tổng lương phải trả cho tất cả nhân viên: {self.total_salary()}")


def main():
    filepath = 'DATA_BAI1.xml'
    test = BTTL_Bai1(filepath)
    test.print_all_employee_information()
    for employee_index in range(len(test.nhanviens)):
        test.export_employee(employee_index)
        print("-" * 30)

if __name__ == "__main__":
    main()
