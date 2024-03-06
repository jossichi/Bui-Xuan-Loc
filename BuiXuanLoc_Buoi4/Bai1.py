from bs4 import BeautifulSoup

class BTTL_Bai1:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = BeautifulSoup(self.read_file(filepath), 'lxml')
        self.id = self.data.find_all('ID')
        self.name = self.data.find_all('Name')
        self.phongban = self.data.find_all('PhongBan')
        self.hesoluong = self.data.find_all('HeSoLuong')
        self.chucvu = self.data.find_all('ChucVu')
        self.songaylamviec = self.data.find_all('SoNgayLamViec')
        
    def calculate_salary(self):
        return float(self.hesoluong[0].text) * 1210 * self.calculate_HSTD() + 1100
    
    def calculate_HSTD(self):
        if self.chucvu[0].text == 'Lanh Dao':
            return 1
        elif self.chucvu[0].text =='NhanVien':
            if int(self.songaylamviec[0].text) < 20: 
                return 0.6
            elif int(self.songaylamviec[0].text) > 22: 
                return 1
            else: 
                return 0.8

    def read_file(self, filepath):
        with open(filepath, 'r') as file:
            data = file.read()
        return data
     
        
def main():
    filepath = 'DATA_BAI1.xml'
    test = BTTL_Bai1()
    test.read_file(filepath)