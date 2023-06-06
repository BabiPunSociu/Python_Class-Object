
# Sử dụng hai dấu gạch dưới (__) để khai báo cho mức private
# Sử dụng một dấu gạch dưới (_) để khai báo cho mức protected
# Không sử dụng dấu gạch dưới là public.

# Về Override:
  # 1. A>>B>>C: C gọi phương thức x, python tìm lần lượt x từ C -> B -> A. Khi thấy x lập tức dừng lại
  # 2. C kế thừa nhiều class: C(A,B, ...): lần lượt tìm từ C -> A -> B -> ...
class Nguoi:
    __ten=''
    __tuoi=''
    
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi=tuoi
    
    def getTen(self):
        return self.ten
    
    def setTen(self, newTen):
        self.ten = newTen
    
    # Cách viết getter setter trong python
    # getter
    @property
    def tuoi(self):
        return self.tuoi
    # setter
    @tuoi.setter
    def tuoi(self, new_tuoi):
        self.tuoi = new_tuoi

# NguoiLinh kế thừa Nguoi
class NguoiLinh(Nguoi):
    capBac=''
    donVi=''
    
    def __init__(self, ten, tuoi, capBac, donVi):
        super().__init__(ten, tuoi)
        self.capBac = capBac
        self.donVi = donVi
    
    def getCapBac(self):
        return self.capBac

if __name__=='__main__':
    a = NguoiLinh("Dũng", '20', 'Đại tướng', 'Bộ tư lệnh tác chiến hải quân')
    print(a.getTen())
    a.setTen("Nguyễn Văn Dũng")
    print(a.getTen())
    print(a.getCapBac())

