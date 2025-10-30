# 🧰 Hướng Dẫn Setup Môi Trường Luyện Tập Python (Cho Data Analysis & AI)

## 1️⃣ Cài đặt Python
- Tải Python mới nhất: [https://www.python.org/downloads/](https://www.python.org/downloads/) (khuyến nghị Python 3.9+)
- Khi cài, **tick chọn "Add Python to PATH"**
- Kiểm tra sau khi cài:
  ```bash
  python --version # Python 3.12.6
  pip --version # Pip version pip 25.3
  ```

---

## 2️⃣ Cài đặt công cụ làm việc (IDE)

### 🔹 Visual Studio Code (VSCode)
- Tải: [https://code.visualstudio.com](https://code.visualstudio.com)
- Extensions cần có:
  - `Python` (Microsoft)
  - `Jupyter` (chạy notebook)
  - `Pylance` (gợi ý code)
  - `Code Runner` (chạy nhanh file)

---

## 3️⃣ Tạo môi trường ảo (Virtual Environment)
Tạo môi trường riêng cho từng project để tránh xung đột thư viện.

### Tạo virtual environment:
Trong thư mục project:
```bash
python -m venv venv
```

### Kích hoạt môi trường ảo:
- **Windows (Command Prompt):**
  ```cmd
  source venv\Scripts\activate
  ```
- **Windows (Bash/Git Bash):**
  ```bash
  source venv/Scripts/activate
  ```
- **macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

### Kiểm tra kích hoạt thành công:
- Terminal sẽ hiển thị `(venv)` ở đầu dòng
- Kiểm tra Python path:
  ```bash
  which python
  ```

### Thoát khỏi virtual environment:
```bash
deactivate
```

---

## 4️⃣ Cài thư viện cần thiết
**⚠️ Lưu ý:** Đảm bảo đã kích hoạt virtual environment trước khi cài!

### Thư viện cơ bản cho Data Analysis:
```bash
pip install --upgrade pip
pip install numpy pandas matplotlib jupyter
```

### Thư viện mở rộng cho Machine Learning:
```bash
pip install seaborn scikit-learn plotly
```

### Thư viện bổ sung hữu ích:
```bash
pip install openpyxl xlrd requests beautifulsoup4
```

### Kiểm tra thư viện đã cài:
```bash
pip list
```

### Lưu danh sách thư viện (để chia sẻ):
```bash
pip freeze > requirements.txt
```

### Cài từ file requirements (khi clone project):
```bash
pip install -r requirements.txt
```

---

## 5️⃣ Dùng Jupyter Notebook để thực hành
Cài đặt (nếu chưa có):
```bash
pip install notebook
```

Chạy notebook:
```bash
jupyter notebook
```

Trình duyệt sẽ mở ra → tạo file `.ipynb` → viết code Python và chạy từng cell.

---

## 6️⃣ Tổ chức thư mục project (gợi ý)
```
learning-machine-intelligence/
├── venv/                    # Virtual environment (có thể để ở root)
├── .gitignore              # Loại trừ venv khỏi git
├── requirements.txt        # Danh sách thư viện
├── README.md
├── ai-learning/
│   └── week3-4-data-analysis/
│       ├── notebooks/
│       │   ├── pandas_intro.ipynb
│       │   └── numpy_exercise.ipynb
│       ├── data/
│       │   └── sales.csv
│       └── README.md
└── exercises/
    ├── week1-python-basics/
    └── week2-advanced-python/
```

### Tại sao để venv ở root?
- ✅ Dễ quản lý và kích hoạt
- ✅ Áp dụng cho toàn bộ project
- ✅ Không cần chuyển thư mục để activate

---

## 7️⃣ Troubleshooting & Tips

### ❌ Lỗi thường gặp:
1. **"python command not found"** → Chưa add Python vào PATH
2. **"venv\Scripts\activate không work"** → Dùng `source venv/Scripts/activate` trong bash
3. **Pip install lỗi** → Upgrade pip: `pip install --upgrade pip`

### 💡 Tips hữu ích:
- Luôn kích hoạt venv trước khi làm việc
- Dùng `pip freeze > requirements.txt` để lưu dependencies
- Thêm `venv/` vào `.gitignore`
- Kiểm tra Python path: `which python` (bash) hoặc `where python` (cmd)

---

## 8️⃣ (Tùy chọn) Môi trường Online
Nếu không muốn cài local:
- **[Kaggle Notebooks](https://www.kaggle.com/code)** — môi trường sẵn thư viện, dataset miễn phí
- **[Google Colab](https://colab.research.google.com)** — chạy Python trên cloud, GPU miễn phí
- **[Repl.it](https://replit.com)** — code online, chia sẻ dễ dàng

---

## 9️⃣ Next Steps
Sau khi setup xong:
1. ✅ Tạo file `test.py` để thử nghiệm
2. ✅ Chạy Jupyter Notebook: `jupyter notebook`
3. ✅ Thử import các thư viện: `import numpy, pandas, matplotlib`
4. ✅ Bắt đầu với notebook đầu tiên!
