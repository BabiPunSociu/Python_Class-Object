class Student:
    # Danh sach cac thuộc tính
    id = ''
    name = ''
    
    # Hàm tạo:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    # Trả về 1 chuỗi, được gọi khi dùng lệnh print() hoặc str() đối tượng
    def __str__(self):
        return f"ID: {self.id} | Name: {self.name}"
    
    # Tạo phương thức static
    @staticmethod
    def add(x, y):
        return x-y

if __name__=='__main__':
    a = Student.add(10, 2)
    print(a)
    
    sv = Student('201200059','Nguyen Van Dung')
    print(sv)

















